"""Run calculator.py for real on a virtual screen, press its buttons, and save screenshots, a GIF and a report.

Used by .github/workflows/run.yml (Actions -> "Run calculator" -> Run workflow).
It needs xvfb (a virtual screen), tkinter and ImageMagick:

    xvfb-run -a -s "-screen 0 560x620x24" python3 gui_demo.py

Nothing in calculator.py is changed or copied: the script runs that file itself, takes over its window loop,
and clicks its real buttons (the same as a person would), checking what the display shows after each sum.
"""

import datetime as dt
import runpy
import shutil
import subprocess
import sys
import tkinter as tk
from pathlib import Path

OUT = Path("results")
FRAMES = OUT / "frames"
CASES = [  # (buttons pressed, what the display should show). C = Clear
    ("12+34=", "46"),
    ("C7*8=", "56"),
    ("C10/4=", "2.5"),
    ("C1.5+2.25=", "3.75"),
    ("C100+5=", "105"),
    ("C2+3=*4=", "20"),
    ("C9-10=", "-1"),
    ("C1/0=", "Not Defined"),
    ("C5+=", "Syntax Error"),
    ("C", ""),
]
results = []
gif_frames = []


def shot(win, path):
    """Screenshot of the calculator window (the virtual screen is only a little bigger than it)."""
    win.update_idletasks()
    win.update()
    w, h = win.winfo_width(), win.winfo_height()
    subprocess.run(["import", "-window", "root", "-crop", f"{w}x{h}+0+0", "+repage", str(path)], check=True)


def drive(g):
    """Called in place of window.mainloop(); g holds calculator.py's own widgets and functions."""
    win = g["window"]
    win.update()
    keys = {**{str(i): g[f"button{i}"] for i in range(10)}, "+": g["plus"], "-": g["minus"], "*": g["multiply"],
            "/": g["divide"], "=": g["equal"], ".": g["decimal"], "C": g["clear_button"]}
    n = 0
    for k, (seq, want) in enumerate(CASES, 1):
        for ch in seq:
            keys[ch].invoke()  # same as clicking the button
            win.update()
            n += 1
            frame = FRAMES / f"step_{n:03d}.png"
            shot(win, frame)
            gif_frames.append(frame)
        got = g["equation_label"].get()
        case_png = FRAMES / f"case_{k:02d}.png"
        shutil.copy(gif_frames[-1], case_png)
        results.append((seq, want, got, case_png.name))
    win.destroy()


def main() -> int:
    shutil.rmtree(OUT, ignore_errors=True)
    FRAMES.mkdir(parents=True)
    tk.Tk.mainloop = lambda self, n=0: drive(sys._getframe(1).f_globals)
    runpy.run_path("calculator.py", run_name="__main__")

    tool = ["magick"] if shutil.which("magick") else ["convert"]
    subprocess.run([*tool, "-delay", "45", "-loop", "0", *map(str, gif_frames[:]), "-layers", "Optimize",
                    str(OUT / "calculator_demo.gif")], check=True)
    for f in gif_frames:  # the single-step frames were only needed for the GIF
        f.unlink()

    bad = sum(got != want for _, want, got, _ in results)
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    shown = lambda s: s.replace("C", "Clear, ").replace("*", "×").replace("/", "÷")  # noqa: E731
    md = ["# Calculator: GUI run", "",
          f"Run {now}. `calculator.py` was started for real (its own window, on a virtual screen) and its buttons were pressed one by one.", "",
          f"**{len(results) - bad} of {len(results)} checks passed.**" if not bad else f"**{bad} of {len(results)} checks FAILED.**", "",
          "## The window, pressing 12 + 34 = and more", "",
          "![Calculator demo](calculator_demo.gif)", "",
          "## What each button sequence showed", "",
          "| Buttons pressed | Display should show | Display showed | Result | Window after |",
          "|---|---|---|---|---|"]
    for seq, want, got, png in results:
        md.append(f"| {shown(seq).strip(', ')} | {want or '(empty)'} | {got or '(empty)'} | "
                  f"{'✅ pass' if got == want else '❌ fail'} | <img src=\"frames/{png}\" width=\"150\"> |")
    md += ["", "Source: [`calculator.py`](../calculator.py) · runner: [`gui_demo.py`](../gui_demo.py) · "
           "workflow: [`run.yml`](../.github/workflows/run.yml)", ""]
    (OUT / "RESULTS.md").write_text("\n".join(md))
    for seq, want, got, _ in results:
        print("PASS" if got == want else "FAIL", f"{seq!r:14} expect {want!r:14} display {got!r}")
    print("gui_demo:", "all passed" if not bad else f"{bad} failed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

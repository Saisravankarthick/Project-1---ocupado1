# Project Occupado

A basic calculator with a window interface, written in Python with `tkinter`. It has number buttons, the four operators (`+ - * /`), a decimal point, an equals button and a clear button.

> Status: work in progress.

## Requirements

- Python 3.8 or newer
- `tkinter` (the standard Python window toolkit)
  - Windows and macOS: included with the installer from [python.org](https://www.python.org/downloads/).
  - Linux (Debian/Ubuntu): `sudo apt install python3-tk`

Check that both are in place:

```bash
python --version
python -c "import tkinter; print('tkinter OK')"
```

On macOS and Linux, use `python3` instead of `python`.

## Run it

```bash
git clone https://github.com/Saisravankarthick/Project-1---ocupado1.git
cd Project-1---ocupado1
python calculator.py
```

A window titled "Basic Calculator Program" opens. Click the buttons to build a sum, press `=` to see the answer, and use the clear button to start again.

The program needs a screen to draw its window, so it will not open on a server or other machine with no display.

## Run it on GitHub (no install needed)

1. Open the **Actions** tab.
2. Choose **Run calculator** on the left, then **Run workflow**.
3. After about a minute, open [`results/RESULTS.md`](results/RESULTS.md).

GitHub cannot show a live window in the browser, so the workflow starts the real `calculator.py` window on a virtual screen, presses its buttons, and saves an animation, screenshots and a pass/fail table to the `results/` folder.

## Click it yourself on GitHub (Codespaces)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Saisravankarthick/Project-1---ocupado1)

A Codespace is a small computer GitHub runs for you. This repo's Codespace includes a desktop you view in your browser, so the real calculator window opens there and you can click it.

1. Click the badge above (or **Code** > **Codespaces** > **Create codespace on main**). The first start takes a few minutes.
2. When it opens, click the **Ports** tab at the bottom, find port **6080** ("Desktop in the browser") and click the globe icon to open it in a new tab.
3. Click **Connect** and enter the password `vscode`. You will see an empty desktop.
4. Go back to the Codespace tab, open the **Terminal** at the bottom and run:

   ```bash
   python3 calculator.py
   ```

5. Switch to the desktop tab. The calculator window is there; click its buttons.

When you finish, stop the Codespace (**Codespaces** page > the **...** menu > **Stop**) so it doesn't use up your free monthly allowance.

## Files

| File | What it is |
|---|---|
| `calculator.py` | The calculator program |
| `gui_demo.py` | Runs `calculator.py` on a virtual screen, presses its buttons and saves screenshots |
| `.github/workflows/run.yml` | The **Run calculator** workflow (screenshots and a report) |
| `.devcontainer/devcontainer.json` | Sets up the Codespace with a browser desktop |
| `console_calculator_draft.py` | An earlier text-only draft of the calculator |

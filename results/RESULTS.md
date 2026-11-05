# Calculator: GUI run

Run 2026-11-05 12:48 UTC. `calculator.py` was started for real (its own window, on a virtual screen) and its buttons were pressed one by one.

**10 of 10 checks passed.**

## The window, pressing 12 + 34 = and more

![Calculator demo](calculator_demo.gif)

## What each button sequence showed

| Buttons pressed | Display should show | Display showed | Result | Window after |
|---|---|---|---|---|
| 12+34= | 46 | 46 | ✅ pass | <img src="frames/case_01.png" width="150"> |
| Clear, 7×8= | 56 | 56 | ✅ pass | <img src="frames/case_02.png" width="150"> |
| Clear, 10÷4= | 2.5 | 2.5 | ✅ pass | <img src="frames/case_03.png" width="150"> |
| Clear, 1.5+2.25= | 3.75 | 3.75 | ✅ pass | <img src="frames/case_04.png" width="150"> |
| Clear, 100+5= | 105 | 105 | ✅ pass | <img src="frames/case_05.png" width="150"> |
| Clear, 2+3=×4= | 20 | 20 | ✅ pass | <img src="frames/case_06.png" width="150"> |
| Clear, 9-10= | -1 | -1 | ✅ pass | <img src="frames/case_07.png" width="150"> |
| Clear, 1÷0= | Not Defined | Not Defined | ✅ pass | <img src="frames/case_08.png" width="150"> |
| Clear, 5+= | Syntax Error | Syntax Error | ✅ pass | <img src="frames/case_09.png" width="150"> |
| Clear | (empty) | (empty) | ✅ pass | <img src="frames/case_10.png" width="150"> |

Source: [`calculator.py`](../calculator.py) · runner: [`gui_demo.py`](../gui_demo.py) · workflow: [`run.yml`](../.github/workflows/run.yml)

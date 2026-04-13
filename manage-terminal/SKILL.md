---
name: manage-terminal
description: Use the tmux terminal driver to send commands to the NetOps_BAU session and read output from panes.
---

## What I do
- Route commands to tmux panes via .github/scripts/terminal_driver.py
- Support send and read actions with pane selection and line limits

## When to use me
- Any time you need to run network commands via the NetOps_BAU tmux session

## How to run (agent instructions)
Use the bash tool to call the Python driver:

Send a command to pane 2 and execute it:
```bash
python3 /home/malakak/dev_area/NetCode_v3/.github/scripts/terminal_driver.py send \
  --pane 2 \
  --command "<command>" \
  --execute
```

Read the latest output from pane 2:
```bash
python3 /home/malakak/dev_area/NetCode_v3/.github/scripts/terminal_driver.py read \
  --pane 2 \
  --lines 20
```

## Notes
- Pane indexes are visual pane numbers in the NetOps_BAU session.
- Use pane 2 for SSH/network commands, pane 1 for local notes, pane 3 for logs.
- The driver only sends Ctrl+C when a "--More--" pager prompt is detected in recent output.

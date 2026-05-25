# YouAreHacked-Python

<img width="1920" height="1080" alt="WindowsTerminal_zxpq5xVkhl" src="https://github.com/user-attachments/assets/210cefce-e307-4524-bbc8-f5014542acc4" />

A small Python script that simulates a "you've been hacked" scene on Windows. It opens Notepad and types a message, then launches a fullscreen Command Prompt with green text running a recursive directory listing, and finally shuts the machine down.

**Do not touch the keyboard or mouse while the script is running — `pyautogui` is driving input, and any interruption will desync the sequence.**

## Configuration

The shutdown is triggered at the end of the script:

```python
os.system("shutdown /s /t 1")
```

You can change the number after `/t` to delay the shutdown, or remove the line if you don't want the machine to power off at all.

## Warning

The script will shut down the computer. Don't run it with unsaved work open, and don't run it on a machine that isn't yours without the owner's consent.

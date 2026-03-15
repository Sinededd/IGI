import os
import sys


# ─────────────────────────────────────────────
#  ANSI COLOURS
# ─────────────────────────────────────────────

class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    WHITE   = "\033[97m"
    CYAN    = "\033[96m"
    YELLOW  = "\033[93m"
    GREEN   = "\033[92m"
    RED     = "\033[91m"



# ─────────────────────────────────────────────
#  RAW KEYBOARD INPUT  (cross-platform)
# ─────────────────────────────────────────────

if os.name == "nt":
    import msvcrt

    def getch() -> str:
        """
        Read a single keypress on Windows using msvcrt.

        Returns:
            str: Key identifier — 'up', 'down', 'enter', or the raw character.
        """
        ch = msvcrt.getwch()
        if ch in ("\x00", "\xe0"):
            ch2 = msvcrt.getwch()
            return {"H": "up", "P": "down"}.get(ch2, "")
        if ch in ("\r", "\n"):
            return "enter"
        return ch
else:
    import tty
    import termios

    def getch() -> str:
        """
        Read a single keypress on Unix/macOS using termios raw mode.

        Returns:
            str: Key identifier — 'up', 'down', 'enter', or the raw character.
        """
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            # print(repr(ch))
            if ch == "\x7f":
                return "backspace"
            if ch == "\x1b":
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                if ch2 == "[":
                    return {"A": "up", "B": "down"}.get(ch3, "")
            if ch in ("\r", "\n"):
                return "enter"
            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)




# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────

def clear() -> None:
    """Clear the terminal screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def pause() -> None:
    """Wait for the user to press ENTER before returning to the menu."""
    print(f"\n  {C.DIM}press enter to go back{C.RESET}", end="", flush=True)
    while True:
        if getch() == "enter":
            break
            

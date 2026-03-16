import os
import sys
from typing import Any

from settings import *



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




def render_menu(selected: int) -> None:
    """Draw the main menu, highlighting the currently selected item."""

    main_header()
    print(f"  {C.DIM}↑ ↓  navigate    enter  confirm{C.RESET}")
    print()

    for i, item in enumerate(MENU_ITEMS):
        if i == selected:
            marker = f"{C.CYAN}›{C.RESET}"
            text   = f"{C.WHITE}{C.BOLD}{item}{C.RESET}"
        else:
            marker = " "
            text   = f"{C.DIM}{item}{C.RESET}"
        print(f"  {marker}  {text}")

    print()


def main_menu() -> int:
    """Controller of the main menu."""
    selected = 0
    total    = len(MENU_ITEMS)

    while True:
        render_menu(selected)
        key = getch()

        if key == "up":
            selected = (selected - 1) % total
        elif key == "down":
            selected = (selected + 1) % total
        elif key == "enter":
            return selected


def render_task_menu(selected: int, render_header, **params) -> None:
    """
    Draw the task menu, highlighting the currently selected item.

    Args:
        selected (int): The selected item to display.
        render_header (function): A function to render the menu header.
        params (dict): Dictionary for displaying menu items.
    """

    render_header()
    print(f"  {C.DIM}↑ ↓  navigate    enter  confirm/edit{C.RESET}")
    print()

    max_length = len(max(params, key=len))

    for i, item in enumerate(params):
        item_text = f"{item.ljust(max_length)} : {params[item]}"
        if i == selected:
            marker = f"{C.CYAN}›{C.RESET}"
            text   = f"{C.WHITE}{C.BOLD}{item_text}{C.RESET}"
        else:
            marker = " "
            text   = f"{C.DIM}{item_text}{C.RESET}"
        print(f"  {marker}  {text}")

    if len(params) == selected:
        marker = f"{C.CYAN}›{C.RESET}"
        text = f"{C.WHITE}{C.BOLD}Enter{C.RESET}"
    else:
        marker = " "
        text = f"{C.DIM}Enter{C.RESET}"
    print(f"  {marker}  {text}")

    print()


def task_menu(render_header, **params : Any) -> dict:
    """
    Controller for the task menu.

    Args:
        render_header (function): A function to render the menu header.
        params (dict): Dictionary for displaying menu items.
    """
    selected = 0
    total    = len(params) + 1
    keys = list(params.keys())


    while True:
        render_task_menu(selected, render_header, **params)
        key = getch()

        if key == "up":
            selected = (selected - 1) % total
        elif key == "down":
            selected = (selected + 1) % total
        elif key == "enter":
            if selected == total - 1:
                return params
            else:
                current_key = keys[selected]
                max_length = len(max(params, key=len))
                new_value = input(f"\033[{total - selected + 1}A\033[G\033[{max_length + 8}C\033[K")
                target_type = type(params[current_key])
                try:
                    params[current_key] = target_type(new_value)
                except ValueError:
                    pass



def clear() -> None:
    """Clear the terminal screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def pause() -> None:
    """Wait for the user to press ENTER."""
    print(f"\n  {C.DIM}press enter to go back{C.RESET}", end="", flush=True)
    while True:
        if getch() == "enter":
            break


def main_header():
    """Draw the main header."""
    clear()
    print()
    print(f"  {C.DIM}{'─' * 44}{C.RESET}")
    print(f"  {C.WHITE}{C.BOLD}lab {LAB_NUMBER}{C.RESET}  {C.DIM}·  {LAB_TITLE}{C.RESET}")
    print(f"  {C.DIM}{DEVELOPER}   v{VERSION}   {DEV_DATE}{C.RESET}")
    print(f"  {C.DIM}{'─' * 44}{C.RESET}")
    print()




def task_header(number = 1, title = "Task title", description = "Task description"):
    """Draw the main header and the task header."""
    main_header()
    print(f"  {C.CYAN}TASK {number}{C.RESET}  {C.DIM}·{C.RESET}  {C.WHITE}{title}{C.RESET}")
    print(f"  {C.DIM}{description}{C.RESET}")
    print(f"  {C.DIM}{'─' * 44}{C.RESET}")
    print()

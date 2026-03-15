"""
  Brief Purpose : Laboratory work — main menu with keyboard navigation
  Lab Number    : 1
  Lab Title     : Introduction to Python Programming
  Version       : 2.0.0
  Developer     : Ivanov Ivan Ivanovich
  Date          : 2024-01-01
"""

from consolGUI import *


# ─────────────────────────────────────────────
#  CONFIG  (edit these)
# ─────────────────────────────────────────────

LAB_NUMBER  = "1"
LAB_TITLE   = "Introduction to Python Programming"
DEVELOPER   = "Grishko Denis"



# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────

def print_header() -> None:
    """
    Print the top header with lab metadata.
    Displayed on every screen (main menu and each task).
    """
    print()
    print(f"  {C.DIM}{'─' * 44}{C.RESET}")
    print(f"  {C.WHITE}{C.BOLD}lab 3{C.RESET}  {C.DIM}·  {LAB_TITLE}{C.RESET}")
    print(f"  {C.DIM}{DEVELOPER} ")
    print(f"  {C.DIM}{'─' * 44}{C.RESET}")
    print()


# ─────────────────────────────────────────────
#  MENU RENDERER
# ─────────────────────────────────────────────

MENU_ITEMS = [
    "Task 1  —  <your title>",
    "Task 2  —  <your title>",
    "Task 3  —  <your title>",
    "Task 4  —  <your title>",
    "Task 5  —  <your title>",
    "Exit",
]


def render_menu(selected: int) -> None:
    """
    Draw the main menu, highlighting the currently selected item.

    Args:
        selected (int): Index of the currently highlighted menu item.
    """
    clear()
    print_header()
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
    """
    Run the interactive main menu loop.
    Navigate with ↑ / ↓ and confirm with Enter.

    Returns:
        int: Index of the chosen menu item (0-based).
    """
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



def render_task_menu(selected: int, **params) -> None:

    clear()
    print_header()
    print(f"  {C.DIM}↑ ↓  navigate    enter  confirm/edit{C.RESET}")
    print()

    maxLength = len(max(params, key=len))

    for i, item in enumerate(params):
        itemText = f"{item.ljust(maxLength)} : {params[item]}  ({type(params[item])})"
        if i == selected:
            marker = f"{C.CYAN}›{C.RESET}"
            text   = f"{C.WHITE}{C.BOLD}{itemText}{C.RESET}"
        else:
            marker = " "
            text   = f"{C.DIM}{itemText}{C.RESET}"
        print(f"  {marker}  {text}")

    if len(params) == selected:
        marker = f"{C.CYAN}›{C.RESET}"
        text = f"{C.WHITE}{C.BOLD}Enter{C.RESET}"
    else:
        marker = " "
        text = f"{C.DIM}Enter{C.RESET}"
    print(f"  {marker}  {text}")

    print()


def task_menu(**params) -> dict:

    selected = 0
    total    = len(params) + 1
    keys = list(params.keys())


    while True:
        render_task_menu(selected, **params)
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
                maxLength = len(max(params, key=len))
                new_value = input(f"\033[{total - selected + 1}A\033[G\033[{maxLength + 8}C\033[K")
                target_type = type(params[current_key])
                try:
                    params[current_key] = target_type(new_value)
                except ValueError:
                    pass


# ─────────────────────────────────────────────
#  TASK SCREENS
# ─────────────────────────────────────────────

def task_header(number: int, title: str) -> None:
    """
    Print a minimal header for an individual task screen.

    Args:
        number (int): Task number (1-based).
        title  (str): Short descriptive title of the task.
    """
    print_header()
    print(f"  {C.CYAN}task {number}{C.RESET}  {C.DIM}·{C.RESET}  {C.WHITE}{title}{C.RESET}")
    print(f"  {C.DIM}{'─' * 44}{C.RESET}")
    print()


def run_task_1() -> None:
    """
    Task 1 entry point.
    Replace the body below with your actual task logic.
    """
    clear()
    task_header(1, "Your Task Title")

    # ── YOUR CODE BELOW ───────────────────────
    task_menu(eps=12, penis=100.3, f="hhh")
    # ── END YOUR CODE ─────────────────────────

    pause()


def run_task_2() -> None:
    """Task 2 entry point. Add your logic here."""
    clear()
    task_header(2, "Your Task Title")
    print(f"  {C.GREEN}✓{C.RESET}  task 2 is running …")
    pause()


def run_task_3() -> None:
    """Task 3 entry point. Add your logic here."""
    clear()
    task_header(3, "Your Task Title")
    print(f"  {C.GREEN}✓{C.RESET}  task 3 is running …")
    pause()


def run_task_4() -> None:
    """Task 4 entry point. Add your logic here."""
    clear()
    task_header(4, "Your Task Title")
    print(f"  {C.GREEN}✓{C.RESET}  task 4 is running …")
    pause()


def run_task_5() -> None:
    """Task 5 entry point. Add your logic here."""
    clear()
    task_header(5, "Your Task Title")
    print(f"  {C.GREEN}✓{C.RESET}  task 5 is running …")
    pause()


# ─────────────────────────────────────────────
#  ROUTING TABLE
# ─────────────────────────────────────────────

TASK_RUNNERS = {
    0: run_task_1,
    1: run_task_2,
    2: run_task_3,
    3: run_task_4,
    4: run_task_5,
}


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

def main() -> None:
    """
    Application entry point.
    Displays the main menu in a loop until the user selects Exit.
    """
    while True:
        choice = main_menu()

        if choice == len(MENU_ITEMS) - 1:   # last item = Exit
            clear()
            print()
            print(f"  {C.DIM}{'─' * 44}{C.RESET}")
            print(f"  {C.WHITE}goodbye.{C.RESET}")
            print(f"  {C.DIM}{'─' * 44}{C.RESET}")
            print()
            break

        runner = TASK_RUNNERS.get(choice)
        if runner:
            runner()


if __name__ == "__main__":
    main()
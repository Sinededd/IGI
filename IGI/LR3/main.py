from interface import *
import tasks


def run_task_1() -> None:
    """Task 1 entry point."""

    render_header = lambda: task_header(1, "Arccos", "Calculate series sum for arccos.")
    current_params = task_menu(render_header, None, x=0.5, epsilon=0.01)
    tasks.calculate_arccos(**current_params)
    pause()


def run_task_2() -> None:
    """Task 2 entry point."""
    render_header = lambda: task_header(1, "Arithmetic mean of even", "Calculate the arithmetic mean of even numbers.")

    def check_int_array(string: str):
        """Function to check if string is an integer."""
        array_string = string.strip().split()
        if not array_string:
            return None
        int_list = list(map(int, array_string))
        return int_list

    current_params = task_menu(render_header, check_int_array, array=[2, 5, -1, 4])
    tasks.calculate_sum_even(**current_params)
    # print(current_params)
    pause()



def run_task_3() -> None:
    """Task 3 entry point."""
    clear()
    task_header(3, "Your Task Title")
    print(f"  {C.GREEN}✓{C.RESET}  task 3 is running …")
    pause()


def run_task_4() -> None:
    """Task 4 entry point."""
    clear()
    task_header(4, "Your Task Title")
    print(f"  {C.GREEN}✓{C.RESET}  task 4 is running …")
    pause()


def run_task_5() -> None:
    """Task 5 entry point."""
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
    """Application entry point."""

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
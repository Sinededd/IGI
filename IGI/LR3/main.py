"""
Short description: This program is a collection of interactive business functions
designed to demonstrate Python's core capabilities, including standard data types,
collections, text analysis.

Laboratory work №: 3
Version: 1.0
Developer: Grishko Denis
Date: 2026-03-16
"""
from random import Random

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
    render_header = lambda: task_header(2, "Arithmetic mean of even", "Calculate the arithmetic mean of even numbers.")

    def check_int_array(string: str):
        """Function to check if string is an integer."""
        array_string = string.strip().split()
        if not array_string:
            return None
        int_list = list(map(int, array_string))
        return int_list

    current_params = task_menu(render_header, check_int_array, array=[2, 5, -1, 4], Random=4)
    del current_params['Random']
    tasks.calculate_sum_even(**current_params)
    pause()



def run_task_3() -> None:
    """Task 3 entry point."""
    render_header = lambda: task_header(3, "Spaces and punctuation marks", "Counts the number of spaces and punctuation marks.")
    current_params = task_menu(render_header, None, string="Тестовый текст, который нужен для проверки кода")
    tasks.count_spaces_and_punctuation(**current_params)
    pause()


def run_task_4() -> None:
    """Task 4 entry point."""
    render_header = lambda: task_header(4, "Analyzes text",
                                        "Analyzes text according to three parameters:\n"
                                        "a) number of words starting or ending with a vowel.\n"
                                        "b) frequency of each character.\n"
                                        "c) alphabetical output of words that come after commas.\n")
    current_params = task_menu(render_header, None, text="So she was "
                                                           "considering in her own mind, as "
                                                           "well as she could, for the hot day "
                                                           "made her feel very sleepy and stupid, "
                                                           "whether the pleasure of making a daisy-chain "
                                                           "would be worth the trouble of getting "
                                                           "up and picking the daisies, when "
                                                           "suddenly a White Rabbit with pink "
                                                           "eyes ran close by her.")
    tasks.analyze_text(**current_params)
    pause()


def run_task_5() -> None:
    """Task 5 entry point."""
    render_header = lambda: task_header(5, "Prod neg and sum pos", "Find product of negative numbers and sum of positive numbers up to the maximum number")

    def check_float_array(string: str):
        """Function to check if string is a float."""
        array_string = string.strip().split()
        if not array_string:
            return None
        int_list = list(map(float, array_string))
        return int_list

    current_params = task_menu(render_header, check_float_array, array=[2.6, 5.3, -1.9, 4.1])
    tasks.float_list_analyze(**current_params)
    pause()


TASK_RUNNERS = {
    0: run_task_1,
    1: run_task_2,
    2: run_task_3,
    3: run_task_4,
    4: run_task_5,
}


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
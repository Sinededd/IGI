import math


from settings import C

def calculate_arccos(x: float, epsilon: float):
    """Calculate the arccos of the given point"""

    if abs(x) > 1:
        print(f"  {C.RED}x must be between -1 and 1{C.RESET}")
        return

    max_iterations = 500
    sum_series= x
    current_term = x
    n = 0

    while abs(current_term) > epsilon:
        if n >= max_iterations:
            break

        multiplier = (x ** 2 * (2 * n + 1) ** 2) / ((2 * n + 2) * (2 * n + 3))
        current_term *= multiplier
        sum_series += current_term
        n += 1

    if n >= max_iterations:
        print(f"  {C.RED}Maximum number of iterations exceeded ({max_iterations}){C.RESET}")
    result = (math.pi / 2) - sum_series


    print(f"  {C.WHITE}Iterations:     {n}{C.RESET}")
    print(f"  {C.WHITE}Series sum:     {result:.10f}{C.RESET}")
    print(f"  {C.WHITE}Function value: {math.acos(x):.10f}{C.RESET}")



def calculate_sum_even(array: list):
    even_numbers = list(filter(lambda x: x % 2 == 0, array))
    if len(even_numbers) == 0:
        print(f"  {C.RED}No even numbers{C.RESET}")
        return
    print(f"  {C.WHITE}Arithmetic mean of even:  {sum(even_numbers) / len(even_numbers)}{C.RESET}")




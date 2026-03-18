import random
import time
from functools import wraps
from settings import C


def timer(func):
    """Decorator that prints the execution time of the function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"  {C.YELLOW}Execution time: {duration:.6f} seconds{C.RESET}")
        return result

    return wrapper


def random_int_generator(n, min_value=-100, max_value=100):
    """Generator that yields random integers"""

    for _ in range(n):
        yield random.randint(min_value, max_value)
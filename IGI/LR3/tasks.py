import math
import utils
from settings import C


@utils.timer
def calculate_arccos(x: float, epsilon: float):
    """Calculate the arccos of the given point"""

    if abs(x) > 1:
        print(f"  {C.RED}x must be between -1 and 1{C.RESET}")
        return

    max_iterations = 100000
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


def count_spaces_and_punctuation(string: str):
    spaces_count = 0
    punctuation_count = 0

    punctuation_marks = set('.,!?;:-"\'«»—…')
    for char in string:
        if char == ' ':
            spaces_count += 1
        elif char in punctuation_marks:
            punctuation_count += 1

    print(f"  Spaces count: {spaces_count}")
    print(f"  Punctuation count {punctuation_count}")


def analyze_text(text: str):
    """Analyzes text according to three parameters.

    a) number of words starting or ending with a vowel.
    b) frequency of each character.
    c) alphabetical output of words that come after commas.
    """
    vowels = set('аеёиоуыэюяaeiouy')
    text_lower = text.lower()

    temp_text = text_lower.replace(',', ' ')
    words = temp_text.split()
    vowel_words_count = 0
    for word in words:
        clean_word = word.strip('.,!?;:-"\'«»—…')
        if clean_word and (clean_word[0] in vowels or clean_word[-1] in vowels):
            vowel_words_count += 1


    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1


    words_after_comma = []
    parts = text.split(',')
    if len(parts) > 1:
        for i in range(1, len(parts)):
            part_words = parts[i].strip().split()
            words_after_comma.extend(part_words)

        words_after_comma.sort(key=lambda x: x.lower())


    print(f"a) Number of words starting or ending with a vowel: {vowel_words_count}")
    print("\nb) Character frequency:")
    for char, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True):
        display_char = char if char != ' ' else 'space'
        if char == '\n':
            display_char = 'newline'
        elif char == '\t':
            display_char = 'tab'
        print(f"  Character '{display_char}' appears {count} time(s)")

    print("\nc) Words after commas in alphabetical order:")
    if words_after_comma:
        for i, word in enumerate(words_after_comma, 1):
            print(f"  {i}. {word}")
    else:
        print("  No commas or words after commas in the text")


def float_list_analyze(array: list):
    """Find product of negative numbers and sum of positive numbers up to the maximum number."""
    max_value = max(array)
    product_negative_numbers = 1.0
    found_negative_numbers = False
    found_positive_numbers = False
    sum_positive_numbers = 0.0
    for item in array:
        if item == max_value:
            break
        if item < 0:
            found_negative_numbers = True
            product_negative_numbers *= item
        elif item > 0:
            found_positive_numbers = True
            sum_positive_numbers += item
    if not found_negative_numbers:
        print(f"  {C.RED}No negative numbers up to the maximum{C.RESET}")
    else:
        print(f"  Product of negative numbers up to the maximum: {product_negative_numbers}")
    if not found_positive_numbers:
        print(f"  {C.RED}No positive numbers up to the maximum{C.RESET}")
    else:
        print(f"  Sum of positive numbers up to the maximum: {sum_positive_numbers}")

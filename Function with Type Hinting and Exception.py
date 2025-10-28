from typing import List, Union

def safe_divide(numbers: List[Union[int, float]]) -> Union[float, str]:
    """
    Calculates the cumulative division of a list of numbers.
    Returns an error message if division by zero occurs.
    """
    if not numbers:
        return "Error: Input list is empty."

    result = numbers[0]
    
    try:
        for num in numbers[1:]:
            if num == 0:
                # Catch the specific error before ZeroDivisionError
                raise ValueError("Division by zero detected.")
            result /= num
        return result
    except ValueError as e:
        return f"Calculation Failed: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage:
print(f"Result 1 (Success): {safe_divide([100, 5, 2])}") # 100 / 5 / 2 = 10.0
print(f"Result 2 (Empty List): {safe_divide([])}")
print(f"Result 3 (Division by Zero): {safe_divide([50, 2, 0, 1])}")

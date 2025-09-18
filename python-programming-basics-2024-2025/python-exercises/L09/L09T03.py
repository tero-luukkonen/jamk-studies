from typing import Any

# Ensure the input is zero; raise TypeError if it's not a number
def is_this_zero(num: Any) -> bool:
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number.")
    return num == 0

# Safely handle is_this_zero and catch TypeError exceptions
def safe_is_this_zero(num: Any) -> tuple[bool, str | None]:
    try:
        result = is_this_zero(num)
        return (result, None)
    except TypeError as e:
        return (False, f"{e}")

# Verify multiple inputs using safe_is_this_zero and return results
def verify_is_this_zero(test_cases: list[Any]) -> list[tuple[Any, tuple[bool, str | None]]]:
    return [(case, safe_is_this_zero(case)) for case in test_cases]

# Define main
def main():
    test_results = verify_is_this_zero([0, 5, "5", None])
    for input_value, (result, error_message) in test_results:
        if error_message:
            print(f"Input: {input_value}, Result: Error - {error_message}")
        else:
            print(f"Input: {input_value}, Result: {result}")

# Start main
if __name__ == "__main__":
    main()

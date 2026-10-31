#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    """_summary_

    Args:
        temp_str (str): _description_

    Returns:
        _type_: _description_

    Raises:
        ValueError: If str cannot be converted
    """
    return int(temp_str)


def test_temperature() -> None:
    temp_str: str = "25"
    print(f"Input data is '{temp_str}'")
    temp: int = input_temperature(temp_str)
    print(f"Temperature is now {temp}°C\n")

    temp_str = "abc"
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
    except ValueError as error:
        print("Caught input_temperature error: ", end="")
        print(error)
        print("\n")


def main() -> None:
    print("=== Garden Temperature ==\n")
    test_temperature()
    print("All tests complete - program didn't crash!")


if __name__ == "__main__":
    main()

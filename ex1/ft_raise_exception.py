#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    max_temp = 40
    min_temp = 0
    temp = int(temp_str)
    if temp >= max_temp:
        msg = f"{temp}°C is too hot for plants max 40°C"
        raise ValueError(msg)
    if temp <= min_temp:
        msg = f"{temp}°C is too cold for plants (min 0°C)"
        raise ValueError(msg)
    return temp


def test_temperature() -> None:
    temp_str: str = "25"
    print(f"Input data is '{temp_str}'")
    temp: int = input_temperature(temp_str)
    print(f"Temperature is now {temp}°C\n")

    temp_str = "abc"
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    temp_str = "100"
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    temp_str = "-50"
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")


def main() -> None:
    print("=== Garden Temperature Checker ==\n")
    test_temperature()
    print("All tests complete - program didn't crash!")


if __name__ == "__main__":
    main()

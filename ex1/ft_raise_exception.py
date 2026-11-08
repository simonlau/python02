#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp >= 40:  # ruff: ignore[magic-value-comparison]
        msg = f"{temp}°C is too hot for plants max 40°C"
        raise ValueError(msg)
    if temp <= 0:
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
        print("Caught input_temperature error: ", end="")
        print(error)
        print("\n")

    temp_str = "100"
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
    except ValueError as error:
        print("Caught input_temperature error: ", end="")
        print(error)
        print("\n")

    temp_str = "-50"
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
    except ValueError as error:
        print("Caught input_temperature error: ", end="")
        print(error)
        print("\n")


def main() -> None:
    print("=== Garden Temperature Checker ==\n")
    test_temperature()
    print("All tests complete - program didn't crash!")


if __name__ == "__main__":
    main()

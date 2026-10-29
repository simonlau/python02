#!/usr/bin/env python3

def input_temperature(temp_str: str):
    """_summary_

    Args:
        temp_str (str): _description_

    Returns:
        _type_: _description_

    Raises:
        ValueError: If str cannot be converted
    """
    temp = int(temp_str)
    if temp >= 40:
        raise ValueError(f"{temp}°C is too hot for plants max 40°C")
    elif temp <= 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature():
    temp_str = '25'
    print(f"Input data is '{temp_str}'")
    temp = input_temperature(temp_str)
    print(f"Temperature is now {temp}°C\n")

    temp_str = 'abc'
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
    except ValueError as error:
        print("Caught input_temperature error: ", end="")
        print(error)
        print("\n")

    temp_str = '100'
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
    except ValueError as error:
        print("Caught input_temperature error: ", end="")
        print(error)
        print("\n")

    temp_str = '-50'
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
    except ValueError as error:
        print("Caught input_temperature error: ", end="")
        print(error)
        print("\n")


def main():
    print("=== Garden Temperature Checker ==\n")
    test_temperature()
    print("All tests complete - program didn't crash!")


if __name__ == '__main__':
    main()

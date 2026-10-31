#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            _ = int("abc")
        case 1:
            42 / 0  # pyrefly:ignore[division-by-zero]
        case 2:
            _ = open("what.txt")
        case 3:
            "42" + 42  # type: ignore[operator]
        case _:
            pass


def test_error_types(i: int) -> None:
    try:
        print(f"Testing operation {i}")
        garden_operations(i)
    except ValueError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    except ZeroDivisionError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    except FileNotFoundError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    except TypeError as error:
        print(f"Caught {error.__class__.__name__}: {error}")


def main() -> None:
    print("=== Garden Error Types Demo ==\n")
    test_error_types(0)
    test_error_types(1)
    test_error_types(2)
    test_error_types(3)
    test_error_types(4)
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()

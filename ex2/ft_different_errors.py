#!/usr/bin/env python3

def garden_operations(operation_number: int):
    match operation_number:
        case 0:
            int("abc")
        case 1:
            42 / 0  # pyrefly:ignore[division-by-zero]
        case 2:
            open("what.txt")
        case 3:
            "42" + 42  # pyrefly:ignore[unsupported-operation]


def test_error_types():
    for i in range(4):
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


def main():
    print("=== Garden Error Types Demo ==\n")
    test_error_types()
    print("All error types tested successfully!")


if __name__ == '__main__':
    main()

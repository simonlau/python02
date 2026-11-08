#!/usr/bin/env python3
# ruff: file-ignore[builtin-open, useless-expression]]
# ruff: file-ignore[open-file-with-context-handler]]

from typing import Literal, TypeAlias

OpsNum: TypeAlias = Literal[0, 1, 2, 3, 4, 5]


def garden_operations(operation_number: OpsNum) -> None:
    match operation_number:
        case 0:
            _ = int("abc")
        case 1:
            42 / 0  # pyrefly:ignore[division-by-zero]
        case 2:
            _ = open("what.txt", encoding="utf-8")
        case 3:
            # ty: ignore[unsupported-operator]
            _ = "42" + 42  # type: ignore[operator]
        case _:
            pass


def test_error_types(i: OpsNum) -> None:
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

#!/usr/bin/env python3


from typing import Literal, TypeAlias

OpsNum: TypeAlias = Literal[0, 1]


class GardenError(Exception):
    def __init__(self, msg: str = "Unknown Garden Error"):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown Plant Error"):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown Water Error"):
        super().__init__(msg)


def garden_operations(operation_number: OpsNum) -> None:
    match operation_number:
        case 0:
            msg = "The tomato plant is wilting!"
            raise PlantError(msg)
        case 1:
            msg = "Not enough water in the tank!"
            raise WaterError(msg)


def test_error_types() -> None:
    print("Testing PlantError...")
    try:
        garden_operations(0)
    except PlantError as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print()
    print("Testing WaterError...")
    try:
        garden_operations(1)
    except WaterError as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print()
    print("Testing GardenError...")
    try:
        garden_operations(0)
    except GardenError as error:
        print(f"Caught {GardenError.__name__}: {error}")
    try:
        garden_operations(1)
    except GardenError as error:
        print(f"Caught {GardenError.__name__}: {error}")


def main() -> None:
    print("=== Custom Garden Errors Demo ==\n")
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()

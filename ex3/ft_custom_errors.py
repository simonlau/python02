#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, msg: str = "Unknown Garden Error"):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown Plant Error"):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown Water Error"):
        super().__init__(msg)


def garden_operations(operation_number: int):
    match operation_number:
        case 0:
            raise PlantError("The tomato plant is wilting!")
        case 1:
            raise WaterError("Not enough water in the tank!")


def test_error_types():
    print(f"Testing PlantError...")
    try:
        garden_operations(0)
    except PlantError as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print(f"Testing WaterError...")
    try:
        garden_operations(1)
    except WaterError as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print(f"Testing GardenError...")
    try:
        garden_operations(0)
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    try:
        garden_operations(1)
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}")


def main():
    print("=== Custom Garden Errors Demo ==\n")
    test_error_types()
    print("All error types tested successfully!")


if __name__ == '__main__':
    main()

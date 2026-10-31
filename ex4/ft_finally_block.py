#!/usr/bin/env python3


from typing import TypeAlias

Plant: TypeAlias = str


class GardenError(Exception):
    def __init__(self, msg: str = "Unknown Garden Error"):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown Plant Error"):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown Water Error"):
        super().__init__(msg)


def water_plant(plant_name: Plant) -> None:
    if plant_name[0].isupper():
        print(f"Watering {plant_name}: [OK]")
        return
    raise PlantError(f"Invalid plant name to water: {plant_name}")


def test_watering_system(plants: list[Plant]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: { error }")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ==\n")
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "lettuce"])
    print("\nCleanup always happens, even with errors!")

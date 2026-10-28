# Python Exception Handling

> Sources: Garden Guardian: Data Engineering for Smart Agriculture (v3.0), 2026-10-28
> Raw: [{Garden Guardian PDF}](../../raw/python-exceptions/2026-10-28-garden-guardian-data-engineering-for-smart-agriculture.md)
> Updated: 2026-10-28

## Overview

Python's exception handling system (`try`/`except`/`finally`/`raise`) is the toolkit for building resilient data pipelines that keep running when sensors malfunction, network connections drop, or corrupted data arrives. This article distills a smart-agriculture data-engineering project that teaches exception handling through five progressive exercises: validating sensor input, raising exceptions for out-of-range readings, distinguishing built-in error types, defining custom exception classes, and guaranteeing cleanup with `finally`.

## Built-in Exception Types

Python provides distinct exception types for different failure situations, and they can be caught separately or together in a single `try` block:

- `ValueError` — bad data provided, such as passing `"abc"` to `int()`
- `ZeroDivisionError` — dividing by zero
- `FileNotFoundError` — opening a file that does not exist
- `TypeError` — mixing incompatible types, such as adding a string and a number

The built-in `Exception` class is the base class, and any built-in exception type may be used as needed. `mypy` will flag intentional faulty code that raises a `TypeError`, so such errors must be kept on purpose for testing.

> Note: Python keywords `try`, `except`, `finally`, and `raise` are fundamental language features and do not need to be listed in authorized functions.

## Data Validation with try/except

A data validation layer converts raw input (for example, a temperature string from a field sensor) into a number and filters out bad data before it corrupts analytics. Invalid input such as `"abc"` raises an error that should be caught, logged with an error message, and handled so the program keeps running instead of crashing.

## Raising Exceptions

Validation can go further than type conversion: a reading that is technically a number but unreasonable for the domain should trigger a raised exception. In the garden domain, valid plant temperatures fall between 0 and 40 degrees Celsius (limits included); values such as `100` or `-50` raise an exception with a descriptive message (e.g., `"100°C is too hot for plants (max 40°C)"`) rather than silently producing bad output.

## Custom Exception Classes

When built-in errors are not specific enough, define custom exception classes that inherit from `Exception` (or a shared base):

- `GardenError` — a basic error for garden problems
- `PlantError` — plant problems, inherits from `GardenError`
- `WaterError` — watering problems, inherits from `GardenError`

Inheritance helps organize related error types: catching `GardenError` catches all garden-related errors (`PlantError` and `WaterError` included), while each subclass can still be caught and handled specifically.

## The finally Block

The `finally` block always runs, whether or not an error occurred, making it the right place to guarantee resource cleanup — for example, closing a watering system — so cleanup happens even when errors interrupt normal flow.

## Resilient Data Pipeline Design

Robust agricultural systems are not built to avoid failures; they are designed to gracefully handle the unexpected. Key practices include validating and cleaning data streams in real time, creating domain-specific custom alerts, maintaining data integrity under real-world conditions, and never letting a pipeline crash — both normal operations and error scenarios should be demonstrated.

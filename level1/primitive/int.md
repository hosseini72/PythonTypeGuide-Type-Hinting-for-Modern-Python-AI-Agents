# Int type hint in Python

## Overview
Integer type hints in Python are used to specify that a variable should be an integer. Python's integers are unbounded, meaning they can be as large as your system's memory allows.

## Basic Usage

### Simple Integer Type Hints
```python
# Basic integer type hint
age: int = 25

# Integer in a function parameter
def calculate_square(number: int) -> int:
    return number * number

# Integer in a class attribute
class Person:
    def __init__(self, age: int) -> None:
        self.age: int = age
```

### Integer with Optional Values
```python
from typing import Optional

# Integer that can be None
nullable_age: Optional[int] = None
nullable_age = 25  # Valid assignment
```

## Common Use Cases

### Mathematical Operations
```python
def perform_calculations(a: int, b: int) -> int:
    return a + b  # Addition
    # return a - b  # Subtraction
    # return a * b  # Multiplication
    # return a // b  # Integer division
```

### Indexing and Counting
```python
def process_list(items: list[str], index: int) -> str:
    return items[index]

def count_occurrences(items: list[str], target: str) -> int:
    return items.count(target)
```

## Important Notes

1. **Integer Characteristics**:
   - Unbounded precision
   - Can be positive or negative
   - No decimal points
   - Can be used in bitwise operations

2. **Type Hint Evolution**:
   - Python 3.5+: Basic `int` type hint
   - Python 3.9+: Can be used in built-in collection types (e.g., `list[int]`)
   - Python 3.10+: Can be used in union types with `|` operator

3. **Best Practices**:
   - Use `int` for whole numbers
   - Use `Optional[int]` when the value might be None
   - Consider using `int` for array indices and counts
   - Use `int` for bitwise operations and flags

4. **Related Types**:
   - `float`: For decimal numbers
   - `bool`: For boolean values (technically a subclass of int)
   - `complex`: For complex numbers


[Back to Index](../../README.md)


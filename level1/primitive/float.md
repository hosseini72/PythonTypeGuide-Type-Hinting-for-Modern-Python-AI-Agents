# Float Type Hints in Python

## Overview
Float type hints in Python are used to specify that a variable should be a floating-point number. Floats are used for decimal numbers and are implemented using double-precision (64-bit) floating-point numbers according to the IEEE 754 standard.

## Basic Usage

### Simple Float Type Hints
```python
# Basic float type hint
pi: float = 3.14159

# Float in a function parameter
def calculate_area(radius: float) -> float:
    return pi * radius * radius

# Float in a class attribute
class Circle:
    def __init__(self, radius: float) -> None:
        self.radius: float = radius
```

### Float with Optional Values
```python
from typing import Optional

# Float that can be None
nullable_value: Optional[float] = None
nullable_value = 3.14  # Valid assignment
```

## Common Use Cases

### Mathematical Calculations
```python
def calculate_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def round_to_decimal(value: float, places: int) -> float:
    return round(value, places)
```

### Scientific Computing
```python
def convert_temperature(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def calculate_velocity(distance: float, time: float) -> float:
    """Calculate velocity in meters per second."""
    return distance / time
```

## Important Notes

1. **Float Characteristics**:
   - Double-precision (64-bit) floating-point numbers
   - Range: approximately ±1.8 × 10^308
   - Precision: about 15-17 significant digits
   - Subject to floating-point arithmetic limitations

2. **Type Hint Evolution**:
   - Python 3.5+: Basic `float` type hint
   - Python 3.9+: Can be used in built-in collection types (e.g., `list[float]`)
   - Python 3.10+: Can be used in union types with `|` operator

3. **Best Practices**:
   - Use `float` for decimal numbers
   - Use `Optional[float]` when the value might be None
   - Be aware of floating-point precision issues
   - Consider using `decimal.Decimal` for financial calculations
   - Use appropriate rounding functions when needed

4. **Related Types**:
   - `int`: For whole numbers
   - `decimal.Decimal`: For precise decimal arithmetic
   - `complex`: For complex numbers
   - `numpy.float64`: For numpy array operations


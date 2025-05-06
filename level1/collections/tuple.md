# Tuple Type Hints in Python

## Basic Usage

### Python 3.9+ (Recommended)
```python
# Tuple with specific types for each position
person: tuple[str, int, bool] = ("Bob", 42, True)

# Fixed-size tuple with specific types
point: tuple[float, float] = (10.5, 20.5)
```

### Python 3.5 to 3.8 (Legacy Style)
```python
from typing import Tuple

# Tuple with specific types for each position
person: Tuple[str, int, bool] = ("Bob", 42, True)

# Fixed-size tuple with specific types
point: Tuple[float, float] = (10.5, 20.5)
```

## Fixed-Size vs. Variable-Size Tuples

### Fixed-Size Tuples
Fixed-size tuples specify the exact number and type of elements:
```python
# A tuple with exactly three elements: string, integer, and boolean
record: tuple[str, int, bool] = ("Alice", 30, True)

# A 2D point with exactly two float coordinates
point: tuple[float, float] = (23.5, 47.2)
```

These type hints indicate that the tuple must contain the exact number of elements specified, with each element matching its corresponding type.

### Variable-Size Tuples
For variable-length tuples where all elements are the same type, use the ellipsis (...):
```python
from typing import Tuple  # Required even in Python 3.9+ for variable-length tuples

# A tuple containing any number of integers
numbers: Tuple[int, ...] = (1, 2, 3, 4, 5)

# Empty tuple of integers is also valid
empty_numbers: Tuple[int, ...] = ()
```

## Important Notes

1. **Type Hint Evolution**:
   - Python 3.9+: Use built-in types directly (e.g., `tuple[str, int, bool]`)
   - Python 3.5-3.8: Import from typing module (e.g., `Tuple[str, int, bool]`)
   - For variable-length tuples, always import `Tuple` from typing module

2. **Tuple Characteristics**:
   - Immutable ordered sequences
   - Fixed positions with specific meanings
   - Can be fixed-size or variable-size
   - Each position can have a different type

3. **Best Practices**:
   - Use fixed-size tuples when the number of elements is known
   - Use variable-size tuples with ellipsis when the number of elements varies
   - Specify types for each position in fixed-size tuples
   - Use type hints to document the meaning of each position


[Back to Index](../../README.md)

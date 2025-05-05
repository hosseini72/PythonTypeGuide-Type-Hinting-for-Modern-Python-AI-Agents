# SupportsInt Type Hints in Python

## Overview
SupportsInt type hints in Python are used to specify that a variable supports the `__int__` protocol, meaning it can be converted to an integer. This type hint is useful when you need to accept any object that can behave like an integer when explicitly converted.

## Basic Usage

### Simple SupportsInt Type Hints
```python
from typing import SupportsInt

# Basic SupportsInt type hint
number: SupportsInt = 42
number = 3.14  # Valid because float implements __int__

# SupportsInt in a function parameter
def to_integer(value: SupportsInt) -> int:
    return int(value)

# SupportsInt in a class attribute
class Measurement:
    def __init__(self, value: SupportsInt) -> None:
        self.value: int = int(value)
```

### SupportsInt with Optional Values
```python
from typing import Optional, SupportsInt

# SupportsInt that can be None
nullable_value: Optional[SupportsInt] = None
nullable_value = 42.5  # Valid assignment
```

## Common Use Cases

### Numeric Conversions
```python
def double_as_int(value: SupportsInt) -> int:
    return int(value) * 2

def format_as_hex(value: SupportsInt) -> str:
    return hex(int(value))
```

### Custom Classes with __int__
```python
class Percentage:
    def __init__(self, value: float) -> None:
        self.value = value
    
    def __int__(self) -> int:
        return int(self.value * 100)

def process_percentage(percent: SupportsInt) -> int:
    return int(percent)
```

## Important Notes

1. **SupportsInt Characteristics**:
   - Accepts any object that has an `__int__` method
   - Common types include int, float, Decimal, and custom classes
   - Always ensures that `int(obj)` is a valid operation
   - Protocol-based typing rather than inheritance-based

2. **Type Hint Evolution**:
   - Python 3.8+: `SupportsInt` from the typing module
   - Python 3.9+: Works with builtin collection types (e.g., `list[SupportsInt]`)
   - Python 3.10+: Can be used in union types with `|` operator

3. **Best Practices**:
   - Use when you need flexibility for integer conversion
   - Prefer `int` when you strictly need integers
   - Use `Optional[SupportsInt]` when the value might be None
   - Check the actual implementation of `__int__` if behavior is critical

4. **Related Types**:
   - `int`: For strict integer values
   - `SupportsFloat`: For objects supporting float conversion
   - `SupportsIndex`: For objects that can be used as sequence indices
   - `Union[int, float]`: For explicit union of common numeric types
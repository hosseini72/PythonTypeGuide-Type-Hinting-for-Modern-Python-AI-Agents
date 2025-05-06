# Boolean Type Hints in Python

## Overview
Boolean type hints in Python are used to specify that a variable should be a boolean value (True or False). In Python, booleans are a subclass of integers, where True is 1 and False is 0, but they should be used specifically for logical operations and conditions.

## Basic Usage

### Simple Boolean Type Hints
```python
# Basic boolean type hint
is_active: bool = True

# Boolean in a function parameter
def check_status(is_ready: bool) -> bool:
    return is_ready

# Boolean in a class attribute
class User:
    def __init__(self, is_verified: bool) -> None:
        self.is_verified: bool = is_verified
```

### Boolean with Optional Values
```python
from typing import Optional

# Boolean that can be None
nullable_flag: Optional[bool] = None
nullable_flag = True  # Valid assignment
```

## Common Use Cases

### Conditional Logic
```python
def process_data(is_valid: bool, data: list[int]) -> list[int]:
    if is_valid:
        return data
    return []

def check_permissions(has_access: bool, user_id: int) -> bool:
    return has_access and user_id > 0
```

### Flag Management
```python
def update_settings(enable_feature: bool, settings: dict[str, bool]) -> dict[str, bool]:
    settings['feature_enabled'] = enable_feature
    return settings
```

## Important Notes

1. **Boolean Characteristics**:
   - Only two possible values: True or False
   - Subclass of int (True = 1, False = 0)
   - Used for logical operations
   - Case-sensitive (True/False, not true/false)

2. **Type Hint Evolution**:
   - Python 3.5+: Basic `bool` type hint
   - Python 3.9+: Can be used in built-in collection types (e.g., `list[bool]`)
   - Python 3.10+: Can be used in union types with `|` operator

3. **Best Practices**:
   - Use `bool` for true/false conditions
   - Use descriptive variable names (is_, has_, can_, etc.)
   - Use `Optional[bool]` when the value might be None
   - Avoid using 1/0 instead of True/False

4. **Related Types**:
   - `int`: Parent class of bool
   - `Optional[bool]`: For nullable boolean values
   - `Union[bool, int]`: When a value could be either boolean or integer


[Back to Index](../../README.md)

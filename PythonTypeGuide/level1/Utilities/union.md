# Union Type Hints in Python

## Overview
Union type hints in Python are used when a value can be one of several different types. They allow you to express more flexible type expectations in your code. Starting with Python 3.10, you can use the pipe `|` operator instead of `Union`, which provides a more concise and readable syntax.

## Basic Usage

### Legacy Syntax (Pre-Python 3.10)
```python
from typing import Union

# Value that could be an integer or a string
id_value: Union[int, str] = "ABC123"
id_value = 42  # Also valid

# Value that could be one of three different types
data: Union[int, str, list[int]] = [1, 2, 3]

# Function accepting multiple types
def process_data(value: Union[int, str, list]) -> str:
    return str(value)
```

### Modern Syntax (Python 3.10+)
```python
# Value that could be an integer or a string
id_value: int | str = "ABC123"
id_value = 42  # Also valid

# Value that could be one of three different types
data: int | str | list[int] = [1, 2, 3]

# Function accepting multiple types
def process_data(value: int | str | list) -> str:
    return str(value)
```

## Common Use Cases

### Optional Values with None
```python
from typing import Union, Optional

# Pre-Python 3.10
maybe_name: Union[str, None] = "John"
maybe_name = None  # Also valid

# Shorthand for Union[str, None]
maybe_title: Optional[str] = "Dr."
maybe_title = None  # Also valid

# Python 3.10+
maybe_address: str | None = "123 Main St"
maybe_address = None  # Also valid
```

### Polymorphic Functions
```python
from typing import Union

# Function that handles different input types
def get_length(item: Union[str, list, tuple, dict]) -> int:
    return len(item)

# Python 3.10+ equivalent
def get_length_modern(item: str | list | tuple | dict) -> int:
    return len(item)
```

## Type Narrowing

When using Union types, you'll often need to check the type before performing operations:
```python
from typing import Union

def process_input(value: Union[int, str]) -> str:
    if isinstance(value, int):
        # Type checker knows value is int here
        return f"Received number: {value * 2}"
    else:
        # Type checker knows value is str here
        return f"Received text: {value.upper()}"
```

## Important Notes

1. **Type Hint Evolution**:
   - Python 3.5+: Use `Union` from typing module
   - Python 3.10+: Use `|` operator syntax
   - Both syntaxes are equivalent in functionality

2. **Best Practices**:
   - Use `Optional[T]` instead of `Union[T, None]` for nullable values
   - Use type narrowing with `isinstance()` for type-specific operations
   - Consider using `Literal` for specific value unions
   - Keep union types as simple as possible

3. **Related Types**:
   - `Optional[T]`: Shorthand for `Union[T, None]`
   - `Literal`: For specific value unions
   - `Any`: When any type is acceptable
   - `TypeVar`: For generic type variables

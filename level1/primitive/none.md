# None Type Hints in Python

## Overview
None type hints in Python are used to specify that a variable can be None, which represents the absence of a value. None is a singleton object in Python, meaning there is only one instance of it in the entire program. It's commonly used to represent null values, optional parameters, or uninitialized variables.

## Basic Usage

### Simple None Type Hints
```python
# Basic None type hint
value: None = None

# Function that returns None
def log_message(message: str) -> None:
    print(message)

# Class method that returns None
class Logger:
    def log(self, message: str) -> None:
        print(message)
```

### Optional Values
```python
from typing import Optional

# Variable that can be None
nullable_value: Optional[str] = None
nullable_value = "Hello"  # Valid assignment

# Function parameter that can be None
def process_data(data: Optional[list[int]]) -> None:
    if data is None:
        return
    # Process the data
```

## Common Use Cases

### Optional Parameters
```python
def create_user(name: str, age: Optional[int] = None) -> dict[str, str | int | None]:
    user = {"name": name}
    if age is not None:
        user["age"] = age
    return user
```

### Nullable Return Values
```python
def find_user(user_id: int) -> Optional[dict[str, str]]:
    # Simulate database lookup
    if user_id == 1:
        return {"name": "John", "email": "john@example.com"}
    return None
```

## Important Notes

1. **None Characteristics**:
   - Singleton object (only one instance exists)
   - Represents absence of a value
   - Evaluates to False in boolean contexts
   - Cannot be subclassed

2. **Type Hint Evolution**:
   - Python 3.5+: Basic `None` type hint
   - Python 3.9+: Can be used in built-in collection types
   - Python 3.10+: Can be used in union types with `|` operator

3. **Best Practices**:
   - Use `None` for optional values
   - Use `Optional[T]` instead of `Union[T, None]`
   - Check for None using `is` operator (not `==`)
   - Consider using `Optional` for function parameters that can be omitted
   - Use `None` as a return type for functions that don't return anything

4. **Related Types**:
   - `Optional[T]`: Union of T and None
   - `Union[T, None]`: Alternative to Optional[T]
   - `Any`: Can be None or any other type
   - `NotRequired`: For optional dictionary keys (Python 3.11+)

## Usage

## Examples

## Related Types


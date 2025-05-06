# TypedDict Type Hints in Python

## Basic Usage

### Python 3.8+ (Current)
```python
from typing import TypedDict

# Basic TypedDict definition
class User(TypedDict):
    name: str
    age: int
    is_active: bool

# Creating a TypedDict instance
user: User = {"name": "John", "age": 30, "is_active": True}
```

### Alternative Syntax (Also Python 3.8+)
```python
from typing import TypedDict

User = TypedDict("User", {
    "name": str,
    "age": int,
    "is_active": bool
})
```

## Optional Keys and TypedDict Evolution

### Optional Keys in Python 3.11+
```python
from typing import TypedDict, NotRequired

class Profile(TypedDict):
    name: str  # Required key
    age: int   # Required key
    bio: NotRequired[str]  # Optional key
```

### Optional Keys in Python 3.8-3.10
```python
from typing import TypedDict

class Profile(TypedDict, total=False):
    bio: str
    website: str

class UserProfile(Profile, total=True):
    name: str
    age: int
```

## Important Notes

1. **TypedDict Characteristics**:
   - Defines dictionaries with specific key names and value types
   - Keys must be string literals
   - Runtime behavior is identical to regular dictionaries
   - Helps static type checkers validate dictionary structure

2. **Type Hint Evolution**:
   - Python 3.8+: Basic `TypedDict` support introduced
   - Python 3.11+: Added `NotRequired` and `Required` markers for optional/required keys

3. **Best Practices**:
   - Use when you have dictionaries with consistent structure
   - Use `total=False` for dictionaries where some keys might be missing
   - Consider dataclasses for more complex data structures

4. **Future Learning**
   As you become more familiar with type hints, you'll learn how to compose TypedDict definitions through inheritance and use them with other advanced typing features like Union and Generic types.



[Back to Index](../../README.md)

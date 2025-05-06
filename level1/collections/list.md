# List Type Hints in Python

## Basic Usage

### Python 3.9+ (Recommended)
```python
# Simple list of integers
numbers: list[int] = [1, 2, 3]

# List of strings
names: list[str] = ["Alice", "Bob", "Charlie"]
```

### Python 3.5 to 3.8 (Legacy Style)
```python
from typing import List

# Simple list of integers
numbers: List[int] = [1, 2, 3]

# List of strings
names: List[str] = ["Alice", "Bob", "Charlie"]
```

## Container Types and Type Hint Evolution

### Container Types
In this category we have List, Dictionary, Set which are mutable data structure and Tuple, FrozenSet which are immutable ones. 
To use them we need to import them from the typing module. This module is built-in and there is no need to install it.

### Type Hint Evolution
As a general rule of thumb, in Python 3.9 and later, it's recommended to use the built-in list and other collection types (like dict, tuple, etc.) directly for type hinting, rather than importing them from the typing module. For example, use list[int] instead of List[int]. The capitalized forms like List are still valid in older Python versions (3.5 to 3.8), but starting with Python 3.9, using the built-in types provides a more concise and consistent approach to type hinting. This simplification is part of the efforts outlined in PEP 585 to make type annotations more intuitive and aligned with Python's dynamic nature.

```python
from typing import List, Dict, Tuple, Set, FrozenSet
# In this section we will use both of them but starting next section, we will only use Python 3.9 and later.
```

## Important Notes

1. **Type Hint Evolution**:
   - Python 3.9+: Use built-in types directly (e.g., `list[int]`)
   - Python 3.5-3.8: Import from typing module (e.g., `List[int]`)

2. **Best Practices**:
   - Be specific with types when possible
   - Use the appropriate syntax for your Python version
   - Import List from typing module if using Python 3.5-3.8

3. **Future Learning**
As you become more familiar with type hints, you'll learn how to define lists that intentionally hold multiple types, using features like Union or Tuple.

[Back to Index](../../README.md)


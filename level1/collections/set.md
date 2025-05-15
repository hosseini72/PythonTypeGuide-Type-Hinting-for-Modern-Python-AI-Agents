# Set Type Hints in Python

## Basic Usage

### Python 3.9+ (Recommended)
```python
# Set of strings
tags: set[str] = {"python", "programming", "typing"}
```

### Python 3.5 to 3.8 (Legacy Style)
```python
from typing import Set

# Set of strings
tags: Set[str] = {"python", "programming", "typing"}
```

## Set Type Hints Explained

In these examples, the set `tags` is annotated to contain strings. Type hints like `set[str]` indicate that all elements in the set are expected to be strings.

In Python, a set is an unordered collection of unique elements, and all elements in a set must be hashable. This means that each item must have a consistent hash value, which Python uses internally to manage set membership efficiently. For an object to be hashable, it must be immutable, such as a string, number, or a tuple containing only hashable elements. Mutable types like lists, dictionaries, or other sets cannot be added to a set, as their contents can change and thus make their hash unreliable. Type hints like set[str] help clarify that the set should only contain strings, improving both code readability and static type checking.

## Important Notes

1. **Set Characteristics**:
   - Unordered collection
   - Contains unique elements
   - Mutable data structure

2. **Type Hint Evolution**:
   - Python 3.9+: Use built-in types directly (e.g., `set[str]`)
   - Python 3.5-3.8: Import from typing module (e.g., `Set[str]`)

3. **Best Practices**:
   - Use type hints to specify the expected element type
   - Helps with documentation and static type checking
   - Makes code more maintainable and self-documenting

[Back to Index](../../README.md)


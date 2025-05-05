# Dictionary Type Hints in Python

## Basic Usage

### Python 3.9+ (Recommended)
```python
# Dictionary mapping strings to integers
ages: dict[str, int] = {"John": 30, "Alice": 25}
```

### Python 3.5 to 3.8 (Legacy Style)
```python
from typing import Dict

# Dictionary mapping strings to integers
ages: Dict[str, int] = {"John": 30, "Alice": 25}
```

## Dictionary Type Hints Explained

In these examples, the dictionary `ages` is annotated to map strings (names) to integers (ages). Type hints like `dict[str, int]` indicate the expected structure of the dictionary, where the keys are strings, and the values are integers.

While Python dictionaries are heterogeneous by default (can store different types without restrictions), using type hints helps convey the expected structure more clearly and can assist static analysis tools in catching type mismatches early.

## Important Notes

1. **Key Constraints**:
   - Dictionary keys in Python must be immutable objects:
     - strings
     - numbers
     - tuples of immutable objects
     - frozen sets
   - Dictionary values can be any type, either mutable or immutable

2. **Type Hint Evolution**:
   - Python 3.9+: Use built-in types directly (e.g., `dict[str, int]`)
   - Python 3.5-3.8: Import from typing module (e.g., `Dict[str, int]`)

3. **Future Learning**
As you explore more advanced type hints, you'll be able to define dictionaries with more complex key-value pairs, such as dictionaries with mixed types, using Union or TypedDict.


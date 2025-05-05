# FrozenSet Type Hints in Python

## Basic Usage

### Python 3.9+ (Recommended)
```python
# Immutable set of strings
constant_tags: frozenset[str] = frozenset({"fixed", "immutable"})

# Empty frozenset of strings
empty_constants: frozenset[str] = frozenset()

# Single element frozenset
single_constant: frozenset[str] = frozenset({"one"})

# Multiple element frozenset 
multiple_constants: frozenset[str] = frozenset({"one", "two", "three"})
```

### Python 3.5 to 3.8 (Legacy Style)
```python
from typing import FrozenSet

# Immutable set of strings
constant_tags: FrozenSet[str] = frozenset({"fixed", "immutable"})

# Empty frozenset of strings
empty_constants: FrozenSet[str] = frozenset()

# Single element frozenset
single_constant: FrozenSet[str] = frozenset({"one"})

# Multiple element frozenset 
multiple_constants: FrozenSet[str] = frozenset({"one", "two", "three"})
```

## Mixed Type Frozensets

### Python 3.9+ and Python 3.10+
```python
from typing import Union

# Python 3.9+
mixed_types: frozenset[Union[str, int]] = frozenset({"one", 2, "three", 4})

# Python 3.10+ (alternative syntax)
mixed_types: frozenset[str | int] = frozenset({"one", 2, "three", 4})
```

## FrozenSet Type Hints Explained

In these examples, the frozenset `constant_tags` is annotated to contain strings. Like other container types, these type hints specify both the container's type (frozenset) and the type of elements it contains (str).

A frozenset is an immutable version of a set in Python, meaning once it's created, it cannot be modified. This makes it suitable for use as dictionary keys or elements of another set.

## Important Notes

1. **Fixed vs. Variable Size**:
   - Unlike tuples, which can have fixed position types, both sets and frozensets are always variable-sized collections
   - All elements must be of the same type (or compatible types using Union)
   - No syntax for specifying a fixed number of elements in a frozenset or set
   - Size constraints must be enforced at runtime

2. **Type Hint Evolution**:
   - Python 3.9+: Use built-in types directly (e.g., `frozenset[str]`)
   - Python 3.5-3.8: Import from typing module (e.g., `FrozenSet[str]`)
   - Python 3.10+: Support for union syntax with `|` operator

3. **Size Validation Example**:
```python
def validate_exactly_three(fs: frozenset[str]) -> None:
    if len(fs) != 3:
        raise ValueError("Frozenset must contain exactly three elements")
        
# Example usage
three_elements: frozenset[str] = frozenset({"a", "b", "c"})
validate_exactly_three(three_elements)  # OK

one_element: frozenset[str] = frozenset({"a"})
validate_exactly_three(one_element)  # Raises ValueError
```

Unlike tuples, where the position and type of each element can be specified, frozensets (and sets) are unordered collections with no concept of positions. The type hint only specifies what types of elements can be contained, not how many.

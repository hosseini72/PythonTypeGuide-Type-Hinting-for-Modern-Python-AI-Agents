# MutableMapping Type Hint in Python

## Overview
In Python, `MutableMapping` is a generic type hint representing any mutable mapping data structure that supports modifying key-value pairs. `MutableMapping` is an abstract base class (ABC) from the `collections.abc` module that the `typing` module makes available for type hints.

The `MutableMapping` type extends `Mapping` and provides additional mutating operations like item assignment (`m[key] = value`), item deletion (`del m[key]`), and methods like `setdefault()`, `update()`, and `pop()`.

## Basic Usage
### Syntax
```python
from typing import MutableMapping

# Basic usage
def update_counters(counters: MutableMapping[str, int], key: str) -> None:
    if key in counters:
        counters[key] += 1
    else:
        counters[key] = 1

# Works with any mutable mapping type
counters_dict = {}
update_counters(counters_dict, "apple")  # dict
update_counters(counters_dict, "apple")  # Now {"apple": 2}

from collections import defaultdict
counters_default = defaultdict(int)
update_counters(counters_default, "banana")  # defaultdict
```

## Common Use Cases
### Accumulating and Updating Data
```python
from typing import MutableMapping, List

def count_word_occurrences(text: str, counts: MutableMapping[str, int]) -> None:
    """Count word occurrences in a text, updating the provided counter."""
    words = text.lower().split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

# Can use with different mutable mapping types
word_counts = {}
count_word_occurrences("the quick brown fox jumps over the lazy dog", word_counts)
print(word_counts)  # {'the': 2, 'quick': 1, 'brown': 1, ...}

# Using defaultdict
from collections import defaultdict
default_counts = defaultdict(int)
count_word_occurrences("the quick brown fox jumps over the lazy dog", default_counts)
print(default_counts)  # defaultdict(<class 'int'>, {'the': 2, 'quick': 1, ...})
```

### Building Complex Data Structures
```python
from typing import MutableMapping, List, Dict, Any

def build_index(records: List[Dict[str, Any]], key_field: str) -> MutableMapping[Any, List[Dict[str, Any]]]:
    """Build an index of records based on a specified field."""
    index: MutableMapping[Any, List[Dict[str, Any]]] = {}
    
    for record in records:
        if key_field in record:
            key = record[key_field]
            if key in index:
                index[key].append(record)
            else:
                index[key] = [record]
    
    return index

# Example usage
users = [
    {"id": 1, "name": "Alice", "department": "HR"},
    {"id": 2, "name": "Bob", "department": "IT"},
    {"id": 3, "name": "Charlie", "department": "IT"},
    {"id": 4, "name": "Diana", "department": "HR"}
]

# Create an index by department
department_index = build_index(users, "department")
print(department_index["IT"])  # [{"id": 2, "name": "Bob", ...}, {"id": 3, "name": "Charlie", ...}]
```

### Caching and Memoization
```python
from typing import MutableMapping, TypeVar, Callable, Any, Dict, Tuple
from functools import wraps

K = TypeVar('K')
V = TypeVar('V')

def memoize(cache: MutableMapping[Tuple, Any]) -> Callable:
    """Create a memoizing decorator that uses a mutable mapping as cache."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Create a hashable key from the function arguments
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper
    return decorator

# Usage
expensive_calc_cache: Dict[Tuple, int] = {}

@memoize(expensive_calc_cache)
def fibonacci(n: int) -> int:
    """Calculate fibonacci number (expensive recursive calculation)."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call calculates and caches
result1 = fibonacci(20)  # Calculates and caches results
# Second call uses cache
result2 = fibonacci(20)  # Uses cached value
```

## Advanced Usage
### MutableMapping vs. Dict and Other Mapping Types
```python
from typing import MutableMapping, Dict, DefaultDict
import collections

# Specific mapping types
def update_dict(data: Dict[str, int], key: str, value: int) -> None:
    # Only accepts dict
    data[key] = value

def update_default_dict(data: DefaultDict[str, int], key: str, value: int) -> None:
    # Only accepts defaultdict
    data[key] = value  # Won't raise KeyError even for new keys

def update_mapping(data: MutableMapping[str, int], key: str, value: int) -> None:
    # Accepts any mutable mapping type (dict, defaultdict, OrderedDict, etc.)
    data[key] = value
    
    # Can use any MutableMapping methods
    data.setdefault("counter", 0)
    data.update({"status": 1})
    old_value = data.pop("temp", None)
```

### MutableMapping vs. Mapping
```python
from typing import Mapping, MutableMapping

def analyze_data(data: Mapping[str, int]) -> int:
    """Function that only reads from a mapping."""
    return sum(data.values())

def process_data(data: MutableMapping[str, int]) -> None:
    """Function that modifies a mapping."""
    total = sum(data.values())
    data["total"] = total
    data["count"] = len(data) - 1  # -1 to exclude the "total" key we just added
    data["average"] = total / (len(data) - 1) if len(data) > 1 else 0
```

### Working with Nested MutableMappings
```python
from typing import MutableMapping, Any, List

def deep_update(
    original: MutableMapping[str, Any], 
    updates: MutableMapping[str, Any]
) -> None:
    """Recursively update a nested mapping structure."""
    for key, value in updates.items():
        if key in original and isinstance(original[key], MutableMapping) and isinstance(value, MutableMapping):
            # Recursively update nested mappings
            deep_update(original[key], value)
        else:
            # Update or add key-value pair
            original[key] = value

# Example usage
config = {
    "server": {
        "host": "localhost",
        "port": 8000,
        "settings": {
            "debug": False,
            "timeout": 30
        }
    },
    "database": {
        "url": "postgresql://localhost/db"
    }
}

updates = {
    "server": {
        "port": 9000,
        "settings": {
            "debug": True
        }
    },
    "logging": {
        "level": "INFO"
    }
}

deep_update(config, updates)
# config now has merged values with updates taking precedence
```

## Custom Implementation
### Creating Custom MutableMapping Types
```python
from typing import MutableMapping, TypeVar, Iterator, Dict, Any
from collections.abc import MutableMapping as ABCMutableMapping

K = TypeVar('K')
V = TypeVar('V')

class CaseInsensitiveDict(ABCMutableMapping):
    """A dictionary with case-insensitive string keys."""
    
    def __init__(self, data: Dict[str, V] = None):
        self._data: Dict[str, V] = {}
        if data:
            self.update(data)
    
    def __getitem__(self, key: str) -> V:
        return self._data[key.lower()]
    
    def __setitem__(self, key: str, value: V) -> None:
        self._data[key.lower()] = value
    
    def __delitem__(self, key: str) -> None:
        del self._data[key.lower()]
    
    def __iter__(self) -> Iterator[str]:
        return iter(self._data)
    
    def __len__(self) -> int:
        return len(self._data)

# Usage
headers: MutableMapping[str, str] = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
print(headers["content-type"])  # "application/json" - case insensitive access
```

### The MutableMapping Protocol
```python
from typing import MutableMapping, TypeVar, Iterator, Dict, Any, Optional
from collections.abc import MutableMapping as ABCMutableMapping

K = TypeVar('K')
V = TypeVar('V')

class TrackingDict(ABCMutableMapping):
    """A dictionary that tracks changes."""
    
    def __init__(self):
        self._data: Dict[K, V] = {}
        self.changes: int = 0
    
    # Required by MutableMapping
    def __getitem__(self, key: K) -> V:
        return self._data[key]
    
    def __setitem__(self, key: K, value: V) -> None:
        self._data[key] = value
        self.changes += 1
    
    def __delitem__(self, key: K) -> None:
        del self._data[key]
        self.changes += 1
    
    def __iter__(self) -> Iterator[K]:
        return iter(self._data)
    
    def __len__(self) -> int:
        return len(self._data)
    
    # Optional methods for better performance
    def get(self, key: K, default: Any = None) -> Any:
        return self._data.get(key, default)
    
    def clear(self) -> None:
        self._data.clear()
        self.changes += 1
    
    def pop(self, key: K, default: Any = None) -> Any:
        value = self._data.pop(key, default)
        self.changes += 1
        return value

# Usage
def process_data(data: MutableMapping[str, int]) -> None:
    data["processed"] = True

tracker = TrackingDict()
tracker["key1"] = 42
print(tracker.changes)  # 1

process_data(tracker)
print(tracker.changes)  # 2
```

## Best Practices
1. **Use `MutableMapping` when mutation is needed**: When your function needs to modify a dictionary-like object.

2. **Prefer `Mapping` when read-only access is sufficient**: This makes your intent clearer and your code safer.

3. **Use `MutableMapping` for dependency injection**: When passing containers that need to be updated.

4. **Be careful with concurrency**: Mutating shared dictionaries can lead to race conditions.

5. **Document mutation behaviors**: Make it clear in your docstrings how your function will modify the mapping.


[Back to Index](../../README.md)

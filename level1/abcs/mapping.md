# Mapping Type Hint in Python

## Overview
In Python, `Mapping` is a generic type hint representing any mapping data structure that maps keys to values. `Mapping` is an abstract base class (ABC) from the `collections.abc` module that the `typing` module makes available for type hints.

The `Mapping` type provides read-only dictionary-like behavior, supporting operations like key access (`m[key]`), key membership testing (`key in m`), iteration over keys (`for k in m`), and methods like `get()` and `items()`.

## Basic Usage
### Syntax
```python
from typing import Mapping

# Basic usage
def get_value(data: Mapping[str, int], key: str) -> int:
    return data[key]

# Works with any mapping type
get_value({"a": 1, "b": 2}, "a")  # dict
get_value(collections.ChainMap({"a": 1}, {"b": 2}), "a")  # ChainMap
```

## Common Use Cases
### Function Parameters That Accept Dictionary-like Objects
```python
from typing import Mapping, Any

def format_person(person: Mapping[str, Any]) -> str:
    """Format a person's information as a string."""
    return f"{person.get('name', 'Unknown')}, {person.get('age', 'N/A')} years old"

# Works with standard dictionaries
person_dict = {"name": "Alice", "age": 30}
print(format_person(person_dict))

# Works with other mapping types
import collections
person_default = collections.defaultdict(str)
person_default["name"] = "Bob"
print(format_person(person_default))

# Works with immutable mappings
from types import MappingProxyType
frozen_person = MappingProxyType({"name": "Charlie", "age": 25})
print(format_person(frozen_person))
```

### Configuration and Settings Management
```python
from typing import Mapping, Any

class ServiceClient:
    def __init__(self, config: Mapping[str, Any]):
        """Initialize with configuration settings.
        
        Args:
            config: Read-only mapping with configuration parameters
        """
        self.api_url = config.get("api_url", "https://api.default.com")
        self.timeout = config.get("timeout", 30)
        self.retry_count = config.get("retry_count", 3)
        
        # Store the config for reference (read-only)
        self._config = config
    
    def get_config_value(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        return self._config.get(key, default)
```

### Working with External Data Sources
```python
from typing import Mapping, List, Any

def extract_records(data_source: Mapping[str, Any], keys: List[str]) -> dict:
    """Extract specific records from a data source.
    
    Args:
        data_source: A mapping containing data records
        keys: List of keys to extract
        
    Returns:
        A dictionary containing only the requested keys
    """
    result = {}
    for key in keys:
        if key in data_source:
            result[key] = data_source[key]
    return result

# Database result proxy example
class DBResultProxy:
    def __init__(self, data):
        self._data = data
    
    def __getitem__(self, key):
        return self._data[key]
    
    def __contains__(self, key):
        return key in self._data
    
    def get(self, key, default=None):
        return self._data.get(key, default)
    
    def keys(self):
        return self._data.keys()

# Works with both dict and custom mapping type
db_result = DBResultProxy({"id": 1, "name": "John", "email": "john@example.com"})
user_data = extract_records(db_result, ["id", "name"])
```

## Advanced Usage
### Mapping vs. Dict and Other Mapping Types
```python
from typing import Mapping, Dict, DefaultDict
import collections

# Specific mapping types
def process_dict(data: Dict[str, int]) -> None:
    # Only accepts dict
    data["new_key"] = 42  # Safe to mutate

def process_default_dict(data: DefaultDict[str, int]) -> None:
    # Only accepts defaultdict
    print(data["non_existent"])  # Safe, returns default value

def process_mapping(data: Mapping[str, int]) -> None:
    # Accepts any mapping type
    # data["new_key"] = 42  # Error: might not be mutable
    # Instead, use methods all mappings support:
    for key in data:
        print(f"{key}: {data[key]}")
    
    # Check if a key exists
    if "total" in data:
        print(f"Total: {data['total']}")
    
    # Get with default
    value = data.get("count", 0)
```

### Mapping vs. MutableMapping
```python
from typing import Mapping, MutableMapping

def read_only_function(data: Mapping[str, int]) -> int:
    """Function that only reads from the mapping."""
    return sum(data.values())

def mutable_function(data: MutableMapping[str, int]) -> None:
    """Function that may modify the mapping."""
    data["sum"] = sum(data.values())
    data["count"] = len(data)
```

### Mapping vs. TypedDict
```python
from typing import Mapping, TypedDict

# TypedDict - for dictionaries with a fixed set of keys with specific types
class UserDict(TypedDict):
    name: str
    age: int

# Mapping - for any dictionary-like object
def process_user(user: Mapping[str, object]) -> None:
    if "name" in user:
        print(f"Name: {user['name']}")
    if "age" in user:
        print(f"Age: {user['age']}")

# TypedDict usage
user1: UserDict = {"name": "John", "age": 30}
process_user(user1)  # Works fine

# Regular dict usage
user2 = {"name": "Jane", "address": "123 Main St"}  # No age field
process_user(user2)  # Also works
```

### Nested Mappings
```python
from typing import Mapping, List, Any

# Complex nested structure
ConfigType = Mapping[str, Mapping[str, Any]]

def get_nested_config(config: ConfigType, section: str, key: str, default: Any = None) -> Any:
    """Get a nested configuration value."""
    if section in config:
        return config[section].get(key, default)
    return default

# Usage
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin"
    },
    "api": {
        "url": "https://api.example.com",
        "timeout": 30
    }
}

db_host = get_nested_config(config, "database", "host")  # "localhost"
api_key = get_nested_config(config, "api", "key", "default-key")  # "default-key"
```

## Custom Implementation
### Creating Custom Mapping Types
```python
from typing import Mapping, TypeVar, Iterator, Dict, Any
from collections.abc import Mapping as ABCMapping

K = TypeVar('K')
V = TypeVar('V')

class ReadOnlyDict(ABCMapping):
    """A simple read-only mapping wrapper."""
    
    def __init__(self, data: Dict[K, V]):
        self._data = dict(data)
    
    def __getitem__(self, key: K) -> V:
        return self._data[key]
    
    def __iter__(self) -> Iterator[K]:
        return iter(self._data)
    
    def __len__(self) -> int:
        return len(self._data)
    
    # Optional methods for better performance
    def get(self, key: K, default: Any = None) -> Any:
        return self._data.get(key, default)
    
    def __contains__(self, key: object) -> bool:
        return key in self._data

# Usage
def process_config(config: Mapping[str, str]) -> None:
    print(f"Host: {config.get('host', 'localhost')}")

my_config = ReadOnlyDict({"host": "example.com", "port": "8080"})
process_config(my_config)  # Works because ReadOnlyDict is a Mapping
```

## Best Practices
1. **Use `Mapping` for read-only access**: When your function only needs to read from a dictionary-like object.

2. **Use `MutableMapping` when mutation is needed**: When your function needs to modify the dictionary-like object.

3. **Prefer `Mapping` over `Dict` for parameters**: This makes your functions more flexible.

4. **Use `Mapping` for dependency injection**: When passing configuration or resources that should be read-only.

5. **Be consistent with key types**: While Python dictionaries can have mixed key types, it's better to be consistent for type safety.

```python
from typing import Mapping, Any, TypeVar, Set

K = TypeVar('K')
V = TypeVar('V')

def get_missing_keys(data: Mapping[K, V], required_keys: Set[K]) -> Set[K]:
    """Find keys that are missing from the mapping."""
    return required_keys - set(data.keys())

def merge_mappings(m1: Mapping[K, V], m2: Mapping[K, V]) -> dict[K, V]:
    """Merge two mappings, with m2 taking precedence on conflicts."""
    result = dict(m1)
    for key, value in m2.items():
        result[key] = value
    return result

def validate_structure(data: Mapping[str, Any], schema: Mapping[str, type]) -> bool:
    """Validate that a mapping follows a schema."""
    for key, expected_type in schema.items():
        if key not in data:
            return False
        if not isinstance(data[key], expected_type):
            return False
    return True
```

The `Mapping` type hint is essential when you need to work with dictionary-like objects in a read-only manner, providing flexibility to accept various mapping implementations while clearly expressing your function's requirements.

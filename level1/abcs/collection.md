# Collection Type Hint in Python

## Overview
In Python, `Collection` is a composite type hint that represents the combination of `Sized`, `Iterable`, and `Container`. It requires that objects have the `__len__`, `__iter__`, and `__contains__` methods, meaning they can:
1. Be checked for length using `len()`
2. Be iterated over using `for` loops
3. Support membership testing using the `in` operator

Most built-in Python collection types (lists, tuples, sets, dictionaries) implement this interface.

## Basic Usage
### Syntax
```python
from typing import Collection, TypeVar

T = TypeVar('T')

# Function that accepts a Collection
def process_collection(data: Collection[T]) -> int:
    """Process a collection and return its size."""
    # Can use len(), iterate over it, and check membership
    total = 0
    for item in data:
        if item in data:  # Membership check is allowed by Collection
            total += 1
    return len(data)

# Usage examples
process_collection([1, 2, 3])  # List is a Collection
process_collection((1, 2, 3))  # Tuple is a Collection
process_collection({1, 2, 3})  # Set is a Collection
process_collection({"a": 1, "b": 2})  # Dict is a Collection (for keys)
```

## Common Use Cases
### General-Purpose Collection Functions
```python
from typing import Collection, TypeVar, List, Set

T = TypeVar('T')

def count_unique_elements(collection: Collection[T]) -> int:
    """
    Count the number of unique elements in a collection.
    
    Args:
        collection: Any collection of elements
        
    Returns:
        int: Number of unique elements
    """
    return len(set(collection))

def find_duplicates(collection: Collection[T]) -> Set[T]:
    """
    Find all duplicate elements in a collection.
    
    Args:
        collection: Any collection of elements
        
    Returns:
        Set of elements that appear more than once
    """
    seen = set()
    duplicates = set()
    
    for item in collection:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return duplicates

# Usage examples
numbers = [1, 2, 3, 2, 4, 1, 5]
print(f"Unique elements: {count_unique_elements(numbers)}")  # 5
print(f"Duplicates: {find_duplicates(numbers)}")  # {1, 2}
```

### Data Processing and Validation
```python
from typing import Collection, Dict, List, TypeVar, Any

T = TypeVar('T')

def validate_collection(collection: Collection[T], 
                        min_size: int = 0,
                        max_size: int = float('inf'),
                        required_elements: Collection[T] = None) -> Dict[str, Any]:
    """
    Validate a collection against a set of criteria.
    
    Args:
        collection: The collection to validate
        min_size: Minimum acceptable size
        max_size: Maximum acceptable size
        required_elements: Elements that must be present
        
    Returns:
        Dict with validation results
    """
    results = {
        "valid": True,
        "errors": []
    }
    
    # Check size constraints
    if len(collection) < min_size:
        results["valid"] = False
        results["errors"].append(f"Collection size {len(collection)} is less than minimum {min_size}")
        
    if len(collection) > max_size:
        results["valid"] = False
        results["errors"].append(f"Collection size {len(collection)} exceeds maximum {max_size}")
    
    # Check required elements
    if required_elements:
        missing = [elem for elem in required_elements if elem not in collection]
        if missing:
            results["valid"] = False
            results["errors"].append(f"Missing required elements: {missing}")
    
    return results

# Example usage
data = ["apple", "banana", "orange"]
validation = validate_collection(
    data,
    min_size=2,
    max_size=5,
    required_elements=["apple", "banana", "grape"]
)

print(f"Validation result: {validation['valid']}")
print(f"Errors: {validation['errors']}")
```

## Custom Implementation
### Custom Collection Classes
```python
from typing import Collection, List, Set, TypeVar, Iterator, Generic

T = TypeVar('T')

class UniqueList(Collection[T], Generic[T]):
    """A list-like collection that ensures all elements are unique."""
    
    def __init__(self, items: List[T] = None):
        self._items: List[T] = []
        self._item_set: Set[T] = set()
        
        if items:
            for item in items:
                self.add(item)
    
    def add(self, item: T) -> bool:
        """
        Add an item if it's not already present.
        
        Args:
            item: The item to add
            
        Returns:
            bool: True if the item was added, False if it was already present
        """
        if item not in self._item_set:
            self._items.append(item)
            self._item_set.add(item)
            return True
        return False
    
    def __contains__(self, item: object) -> bool:
        """Check if an item is in the collection."""
        return item in self._item_set
    
    def __iter__(self) -> Iterator[T]:
        """Iterate over the items in insertion order."""
        return iter(self._items)
    
    def __len__(self) -> int:
        """Get the number of items in the collection."""
        return len(self._items)

# Usage
unique_strings = UniqueList(["apple", "banana", "apple", "cherry"])
print(f"Size: {len(unique_strings)}")  # 3
print("banana" in unique_strings)      # True
print([item for item in unique_strings])  # ["apple", "banana", "cherry"]
```

## Advanced Usage
### Collection vs Other Collection Types
```python
from typing import Sized, Iterable, Container, Collection, Sequence, Mapping
from typing import List, Dict, Set, Tuple

def compare_collection_types() -> None:
    """Compare different collection-related type hints."""
    
    # Sized: Only requires __len__
    def sized_only(obj: Sized) -> int:
        return len(obj)
    
    # Iterable: Only requires __iter__
    def iterable_only(obj: Iterable[int]) -> int:
        return sum(1 for _ in obj)
    
    # Container: Only requires __contains__
    def container_only(obj: Container[int]) -> bool:
        return 42 in obj
    
    # Collection: Requires __len__, __iter__, and __contains__
    def collection_example(obj: Collection[int]) -> int:
        # Can use all operations from Sized, Iterable, and Container
        if len(obj) == 0:
            return 0
        
        if 42 in obj:
            return 42
            
        return sum(1 for x in obj)
    
    # Sequence: Like Collection plus indexed access
    def sequence_example(obj: Sequence[int]) -> int:
        # Can also use indexing operations
        if len(obj) > 0:
            return obj[0]
        return 0
    
    # Mapping: For dict-like structures
    def mapping_example(obj: Mapping[str, int]) -> int:
        # Uses key-value access
        return obj.get("answer", 0)
    
    # Examples of types satisfying each constraint
    
    # All built-in collections are Sized
    sized_examples: List[Sized] = [[], {}, (), set(), ""]
    
    # All built-in collections are Iterable
    iterable_examples: List[Iterable] = [[], {}, (), set(), ""]
    
    # All built-in collections are Containers
    container_examples: List[Container] = [[], {}, (), set(), ""]
    
    # All built-in collections are Collections
    collection_examples: List[Collection] = [[], {}, (), set(), ""]
    
    # Not all Collections are Sequences (sets and dicts aren't)
    sequence_examples: List[Sequence] = [[], (), ""]  # Not set() or {}
    
    # Only dict-like objects are Mappings
    mapping_examples: List[Mapping] = [{}]  # Only dict in built-ins
```

### Combined Collection Types
```python
from typing import Collection, TypeVar, Callable, Protocol, Iterator

T = TypeVar('T')
U = TypeVar('U')

class SortableCollection(Protocol[T]):
    """Protocol for collections that support sorting operations."""
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[T]: ...
    def __contains__(self, item: object) -> bool: ...
    def __getitem__(self, index: int) -> T: ...

def find_largest_n(collection: Collection[T], n: int, key: Callable[[T], U] = None) -> List[T]:
    """
    Find the n largest elements in a collection.
    
    Args:
        collection: Any collection of elements
        n: Number of largest elements to return
        key: Optional key function for comparison
        
    Returns:
        List of the n largest elements
    """
    return sorted(collection, key=key, reverse=True)[:n]

# Usage
numbers = [5, 2, 8, 1, 9, 3]
largest_three = find_largest_n(numbers, 3)
print(f"Largest three numbers: {largest_three}")  # [9, 8, 5]

words = {"apple", "banana", "cherry", "date", "elderberry"}
longest_two = find_largest_n(words, 2, key=len)
print(f"Longest two words: {longest_two}")  # ["elderberry", "banana"]
```

### Mutable and Immutable Collections
```python
from typing import Collection, TypeVar, Protocol, Iterator, List

T = TypeVar('T')

class MutableCollection(Protocol[T]):
    """Protocol for mutable collections."""
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[T]: ...
    def __contains__(self, item: object) -> bool: ...
    def add(self, item: T) -> None: ...
    def remove(self, item: T) -> None: ...

class ImmutableCollection(Protocol[T]):
    """Protocol for immutable collections."""
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[T]: ...
    def __contains__(self, item: object) -> bool: ...

def safe_add_all(mutable_coll: MutableCollection[T], items: Collection[T]) -> None:
    """
    Add all items from a collection to a mutable collection.
    
    Args:
        mutable_coll: A collection that supports adding elements
        items: Items to add
    """
    for item in items:
        mutable_coll.add(item)

# Example implementation
class FrozenList(ImmutableCollection[T]):
    """An immutable list-like collection."""
    
    def __init__(self, items: List[T]):
        self._items = list(items)  # Make a copy
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self) -> Iterator[T]:
        return iter(self._items)
    
    def __contains__(self, item: object) -> bool:
        return item in self._items

# Usage
from typing import Set
mutable_set: Set[int] = {1, 2, 3}
items_to_add = FrozenList([3, 4, 5])

safe_add_all(mutable_set, items_to_add)
print(mutable_set)  # {1, 2, 3, 4, 5}
```

## Real-World Examples
### Data Processing Pipeline
```python
from typing import Collection, List, Dict, TypeVar, Callable, Optional

T = TypeVar('T')
R = TypeVar('R')

class DataPipeline:
    """A pipeline for processing collections of data."""
    
    def __init__(self, source: Collection[T]):
        self.data = list(source)
    
    def filter(self, predicate: Callable[[T], bool]) -> 'DataPipeline[T]':
        """Filter elements based on a predicate."""
        self.data = [item for item in self.data if predicate(item)]
        return self
    
    def map(self, transform: Callable[[T], R]) -> 'DataPipeline[R]':
        """Transform each element using the provided function."""
        self.data = [transform(item) for item in self.data]
        return self
    
    def group_by(self, key_func: Callable[[T], R]) -> Dict[R, List[T]]:
        """Group elements by a key function."""
        result: Dict[R, List[T]] = {}
        for item in self.data:
            key = key_func(item)
            if key not in result:
                result[key] = []
            result[key].append(item)
        return result
    
    def collect(self) -> List[T]:
        """Collect the processed data."""
        return self.data

# Usage
data = [
    {"name": "Alice", "age": 25, "department": "Engineering"},
    {"name": "Bob", "age": 30, "department": "Marketing"},
    {"name": "Charlie", "age": 35, "department": "Engineering"},
    {"name": "David", "age": 40, "department": "HR"}
]

result = (
    DataPipeline(data)
    .filter(lambda x: x["age"] > 25)
    .map(lambda x: {**x, "experience": x["age"] - 25})
    .collect()
)

grouped = (
    DataPipeline(data)
    .group_by(lambda x: x["department"])
)

print(result)
print(grouped)
```

### Configuration Validation
```python
from typing import Collection, Dict, Any, Optional, Set, List

class ConfigValidator:
    """Validator for application configuration."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.errors: List[str] = []
    
    def validate_required_keys(self, required_keys: Collection[str]) -> 'ConfigValidator':
        """
        Validate that all required keys are present in the configuration.
        
        Args:
            required_keys: Collection of keys that must exist in the config
        """
        missing_keys = [key for key in required_keys if key not in self.config]
        if missing_keys:
            self.errors.append(f"Missing required configuration keys: {', '.join(missing_keys)}")
        return self
    
    def validate_string_values(self, keys: Collection[str]) -> 'ConfigValidator':
        """
        Validate that specified keys have string values.
        
        Args:
            keys: Collection of keys that should have string values
        """
        for key in keys:
            if key in self.config and not isinstance(self.config[key], str):
                self.errors.append(f"Key '{key}' must have a string value")
        return self
    
    def validate_numeric_values(self, keys: Collection[str]) -> 'ConfigValidator':
        """
        Validate that specified keys have numeric values.
        
        Args:
            keys: Collection of keys that should have numeric values
        """
        for key in keys:
            if key in self.config and not isinstance(self.config[key], (int, float)):
                self.errors.append(f"Key '{key}' must have a numeric value")
        return self
    
    def validate_allowed_values(self, key: str, allowed_values: Collection[Any]) -> 'ConfigValidator':
        """
        Validate that a key's value is one of the allowed values.
        
        Args:
            key: The configuration key to check
            allowed_values: Collection of allowed values for the key
        """
        if key in self.config and self.config[key] not in allowed_values:
            self.errors.append(
                f"Value for '{key}' must be one of: {', '.join(str(v) for v in allowed_values)}"
            )
        return self
    
    def is_valid(self) -> bool:
        """Check if the configuration is valid."""
        return len(self.errors) == 0
    
    def get_errors(self) -> List[str]:
        """Get validation errors."""
        return self.errors

# Usage
config = {
    "app_name": "MyApp",
    "port": 8080,
    "debug": True,
    "log_level": "INFO"
}

validator = (
    ConfigValidator(config)
    .validate_required_keys(["app_name", "port", "log_level"])
    .validate_string_values(["app_name", "log_level"])
    .validate_numeric_values(["port"])
    .validate_allowed_values("log_level", ["DEBUG", "INFO", "WARNING", "ERROR"])
)

if validator.is_valid():
    print("Configuration is valid")
else:
    print("Configuration errors:")
    for error in validator.get_errors():
        print(f"- {error}")
```

## Best Practices
1. **Prefer Collection over more specific types** when you only need length, iteration, and membership testing.

2. **Use Collection for generic algorithms** that work on any collection type, regardless of underlying implementation.

3. **Document specific requirements** if your function needs more than what `Collection` provides.

4. **Consider performance implications** of the operations you're using - membership testing might be O(1) for sets but O(n) for lists.

5. **Use with type variables** to preserve the element type information and provide better type checking.

```python
from typing import Collection, TypeVar, Callable, List, Set, Dict

T = TypeVar('T')
R = TypeVar('R')

def transform_collection(collection: Collection[T], transform_func: Callable[[T], R]) -> List[R]:
    """
    Transform each element in a collection using the provided function.
    
    Args:
        collection: Any collection of elements
        transform_func: Function to apply to each element
        
    Returns:
        List of transformed elements
    """
    return [transform_func(item) for item in collection]

def collection_stats(collection: Collection[T]) -> Dict[str, any]:
    """
    Generate statistics about a collection.
    
    Args:
        collection: Any collection of elements
        
    Returns:
        Dictionary with statistics about the collection
    """
    return {
        "size": len(collection),
        "unique_count": len(set(collection)),
        "has_duplicates": len(set(collection)) < len(collection),
        "is_empty": len(collection) == 0
    }
```

[Back to Index](../../README.md)

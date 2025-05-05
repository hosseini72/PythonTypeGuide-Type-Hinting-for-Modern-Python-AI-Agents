# Container Type Hint in Python

## Overview
In Python, `Container` is a protocol type hint that represents any object that supports the `in` operator, meaning it has a `__contains__` method. This includes built-in types like strings, lists, sets, dictionaries, and any custom class that implements the `__contains__` method.

## Basic Usage
### Syntax
```python
from typing import Container, TypeVar

T = TypeVar('T')

# Function that accepts a Container
def contains_element(container: Container[T], element: T) -> bool:
    return element in container

# Usage examples
string_check = contains_element("Hello", "e")  # Strings are Containers
list_check = contains_element([1, 2, 3], 2)  # Lists are Containers
set_check = contains_element({1, 2, 3}, 4)  # Sets are Containers
dict_check = contains_element({"a": 1, "b": 2}, "a")  # Dicts are Containers (for keys)
```

## Common Use Cases
### Membership Testing Functions
```python
from typing import Container, TypeVar, List

T = TypeVar('T')

def is_missing(item: T, container: Container[T]) -> bool:
    """Check if an item is missing from a container."""
    return item not in container

def find_common_elements(container1: Container[T], container2: Container[T]) -> List[T]:
    """Find elements that are common to both containers."""
    # Note: This assumes container2 is also iterable, which Container doesn't guarantee
    return [item for item in container2 if item in container1]

# Examples
allowed_usernames = {"admin", "moderator", "editor"}
print(is_missing("guest", allowed_usernames))  # True - "guest" is not in the set

valid_codes = ["A001", "B002", "C003", "D004"]
user_codes = ["B002", "E005", "C003"]
common_codes = find_common_elements(valid_codes, user_codes)
print(common_codes)  # ["B002", "C003"]
```

### Security and Access Control
```python
from typing import Container, Dict, Any

def can_access_resource(user_id: str, resource_id: str, permissions: Container[str]) -> bool:
    """
    Check if a user has permission to access a resource.
    
    Args:
        user_id: Identifier for the user
        resource_id: Identifier for the resource
        permissions: Container of permission strings the user has
        
    Returns:
        bool: True if the user has access
    """
    required_permission = f"access:{resource_id}"
    admin_permission = "admin"
    
    return admin_permission in permissions or required_permission in permissions

# Example
user_permissions = {"edit:doc1", "view:doc2", "access:resource7", "print:all"}
can_access = can_access_resource("user123", "resource7", user_permissions)
print(f"User can access: {can_access}")  # True
```

## Custom Implementation
### Custom Container Classes
```python
from typing import Container, List, Set, TypeVar, Generic

T = TypeVar('T')

class FilteredContainer(Container[T], Generic[T]):
    """A container that filters elements based on a predicate."""
    
    def __init__(self, items: List[T], predicate):
        self._items = items
        self._predicate = predicate
    
    def __contains__(self, item: object) -> bool:
        """
        Check if the item is in the container and satisfies the predicate.
        
        Args:
            item: The item to check
            
        Returns:
            bool: True if the item is in the container and meets the filter criteria
        """
        return item in self._items and self._predicate(item)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = FilteredContainer(numbers, lambda x: x % 2 == 0)

print(2 in even_numbers)  # True
print(3 in even_numbers)  # False
```

### Implementing Container Protocol
```python
from typing import Container, Protocol, TypeVar, Set, Generic

T = TypeVar('T')

class ContainerProtocol(Protocol[T]):
    def __contains__(self, item: object) -> bool: ...

class PrefixContainer(Container[str]):
    """A container that checks if a string starts with any of the stored prefixes."""
    
    def __init__(self, prefixes: Set[str]):
        self.prefixes = prefixes
    
    def __contains__(self, item: object) -> bool:
        """
        Check if the given string starts with any of the stored prefixes.
        
        Args:
            item: The string to check
            
        Returns:
            bool: True if the string starts with any prefix
        """
        if not isinstance(item, str):
            return False
            
        return any(item.startswith(prefix) for prefix in self.prefixes)

# Usage
domains = PrefixContainer({"http://", "https://", "ftp://"})
print("https://example.com" in domains)  # True
print("example.com" in domains)          # False
```

## Advanced Usage
### Container with Bloom Filters
```python
from typing import Container, Hashable, List
import hashlib

class BloomFilter(Container[Hashable]):
    """
    Simple Bloom filter implementation as a Container.
    
    A Bloom filter is a space-efficient probabilistic data structure
    that tests whether an element is a member of a set.
    """
    
    def __init__(self, size: int = 1000, hash_functions: int = 3):
        self.size = size
        self.hash_functions = hash_functions
        self.bit_array = [False] * size
    
    def _get_hash_values(self, item: Hashable) -> List[int]:
        """Generate hash values for an item."""
        hash_values = []
        item_str = str(item).encode('utf-8')
        
        for i in range(self.hash_functions):
            # Create different hash functions by appending a salt
            salted = item_str + str(i).encode('utf-8')
            hash_value = int(hashlib.md5(salted).hexdigest(), 16) % self.size
            hash_values.append(hash_value)
        
        return hash_values
    
    def add(self, item: Hashable) -> None:
        """Add an item to the Bloom filter."""
        for index in self._get_hash_values(item):
            self.bit_array[index] = True
    
    def __contains__(self, item: object) -> bool:
        """
        Check if an item might be in the set.
        
        Note: False positives are possible, but false negatives are not.
        """
        if not isinstance(item, Hashable):
            return False
            
        return all(self.bit_array[index] for index in self._get_hash_values(item))

# Usage
bloom = BloomFilter(size=100)
bloom.add("test@example.com")
bloom.add("user@domain.com")

print("test@example.com" in bloom)  # True
print("other@example.com" in bloom)  # Likely False, but could be True (false positive)
```

### Container vs Iterable
```python
from typing import Container, Iterable, Set, TypeVar

T = TypeVar('T')

def is_in_container(item: T, container: Container[T]) -> bool:
    """Check if an item is in a container using 'in' operator."""
    return item in container  # Uses __contains__

def find_in_iterable(item: T, iterable: Iterable[T]) -> bool:
    """Find an item in an iterable by iterating through it."""
    for element in iterable:  # Uses __iter__
        if element == item:
            return True
    return False

# A set is both a Container and an Iterable
items: Set[int] = {1, 2, 3, 4}

# Container check is typically O(1) for sets
print(is_in_container(3, items))  # True, uses optimized __contains__

# Iterable check is O(n) - must check each element
print(find_in_iterable(3, items))  # True, but less efficient for large sets

# Example of a Container that's not easily iterable
class InfiniteRange(Container[int]):
    """A container representing an infinite range of integers from start."""
    
    def __init__(self, start: int):
        self.start = start
    
    def __contains__(self, item: object) -> bool:
        """Check if an integer is in the infinite range."""
        if not isinstance(item, int):
            return False
        return item >= self.start

# This is a Container but not practically iterable
numbers = InfiniteRange(10)
print(15 in numbers)  # True
print(5 in numbers)   # False
```

## Best Practices
1. **Optimize for membership testing**: If your code primarily checks for membership, `Container` is more appropriate than `Iterable`.

2. **Document containment semantics**: Clearly document what "containment" means for your custom containers.

3. **Consider performance characteristics**: When implementing `__contains__`, optimize for O(1) or O(log n) lookups when possible.

4. **Use with other collections**: Often `Container` is combined with other collection protocols like `Sized`.

5. **Type safety**: Remember that `Container[T]` guarantees `__contains__` but doesn't specify what happens with items of the wrong type.

```python
from typing import Container, Iterable, Sized, TypeVar, Protocol

T = TypeVar('T')

class SearchableCollection(Protocol[T]):
    """Protocol for collections that support membership testing and iteration."""
    def __contains__(self, item: object) -> bool: ...
    def __iter__(self) -> Iterator[T]: ...
    def __len__(self) -> int: ...

def analyze_collection(collection: SearchableCollection[T]) -> None:
    """
    Analyze a collection with containment, iteration, and size capabilities.
    
    Args:
        collection: A collection that supports containment, iteration, and size
    """
    print(f"Collection size: {len(collection)}")
    
    example_item = next(iter(collection), None)
    if example_item is not None:
        print(f"Collection contains example item: {example_item in collection}")
```


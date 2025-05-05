# Sized Type Hint in Python

## Overview
In Python, `Sized` is a protocol type hint that represents any object that has a `__len__` method, meaning it has a notion of size or length. This includes built-in types like strings, lists, tuples, dictionaries, sets, and any custom class that implements the `__len__` method.

## Basic Usage
### Syntax
```python
from typing import Sized

# Function that accepts a Sized object
def get_length(obj: Sized) -> int:
    return len(obj)

# Usage examples
string_length = get_length("Hello")  # Strings are Sized
list_length = get_length([1, 2, 3])  # Lists are Sized
tuple_length = get_length((1, 2, 3))  # Tuples are Sized
dict_length = get_length({"a": 1, "b": 2})  # Dictionaries are Sized
```

## Common Use Cases
### Generic Length Functions
```python
from typing import Sized

def is_empty(container: Sized) -> bool:
    """Check if a container is empty."""
    return len(container) == 0

def print_size_info(item: Sized) -> None:
    """Print information about the size of an object."""
    if len(item) == 0:
        print("The object is empty")
    elif len(item) == 1:
        print("The object contains 1 item")
    else:
        print(f"The object contains {len(item)} items")

# Works with any object that has a __len__ method
print_size_info("Hello")  # String
print_size_info([])  # Empty list
print_size_info({1, 2, 3})  # Set
```

### Data Container Validation
```python
from typing import Sized, TypeVar, List, Tuple, Dict, Any

T = TypeVar('T', bound=Sized)

def validate_size(obj: T, min_size: int = 0, max_size: int = float('inf')) -> bool:
    """
    Validate that an object's size is within specified bounds.
    
    Args:
        obj: Any sized object
        min_size: Minimum allowed size (inclusive)
        max_size: Maximum allowed size (inclusive)
        
    Returns:
        bool: True if the object size is within bounds
    """
    size = len(obj)
    return min_size <= size <= max_size

# Example validations
data_entries: List[Dict[str, Any]] = [{"name": "Alice"}, {"name": "Bob"}]
assert validate_size(data_entries, min_size=1)  # Must have at least one entry

username = "user123"
assert validate_size(username, min_size=3, max_size=20)  # Username length restrictions

coordinates = (10.5, 20.3)
assert validate_size(coordinates, min_size=2, max_size=2)  # Must be exactly 2D
```

## Custom Implementation
### Creating Custom Sized Types
```python
from typing import Sized, List, Iterator

class Database(Sized):
    def __init__(self):
        self.records: List[dict] = []
    
    def add_record(self, record: dict) -> None:
        self.records.append(record)
    
    def __len__(self) -> int:
        """Implement the Sized protocol."""
        return len(self.records)

# Alternative using Protocol (Python 3.8+)
from typing import Protocol

class SizedProtocol(Protocol):
    def __len__(self) -> int: ...

def get_size(obj: SizedProtocol) -> int:
    return len(obj)
```

### Custom Classes with Size
```python
from typing import Sized, List

class Playlist(Sized):
    def __init__(self, tracks: List[str]):
        self.tracks = tracks
    
    def __len__(self) -> int:
        return len(self.tracks)
    
    def add_track(self, track: str) -> None:
        self.tracks.append(track)

# Usage
playlist = Playlist(["Track 1", "Track 2"])
print(f"Playlist has {len(playlist)} tracks")

# Function accepting Sized works with our custom class
def needs_more_tracks(playlist: Sized) -> bool:
    """Determine if a playlist needs more tracks."""
    return len(playlist) < 5

if needs_more_tracks(playlist):
    print("Playlist needs more tracks!")
```

## Advanced Usage
### Combining with Other Protocols
```python
from typing import Sized, Iterable, TypeVar, List

T = TypeVar('T')

class SizedIterable(Sized, Iterable[T]):
    """Protocol for objects that have both length and can be iterated."""
    pass

def process_collection(collection: SizedIterable[T]) -> List[T]:
    """
    Process a collection that has a known size and can be iterated.
    
    Args:
        collection: An object that has both __len__ and __iter__ methods
        
    Returns:
        List of processed items
    """
    if len(collection) == 0:
        return []
    
    result = []
    for item in collection:
        # Process each item
        result.append(item)
    
    return result

# Usage
items = ["apple", "banana", "cherry"]
processed = process_collection(items)  # Lists satisfy both Sized and Iterable
```

### Complex Protocol Combinations
```python
from typing import Sized, Iterable, TypeVar, Protocol

T = TypeVar('T')

class SizedCollection(Protocol):
    """A protocol for collections that have both size and elements."""
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[T]: ...
    def __contains__(self, item: object) -> bool: ...

def analyze_collection(collection: SizedCollection[T]) -> None:
    """
    Analyze a collection with size and iteration capabilities.
    
    Args:
        collection: A collection that supports len(), iteration, and containment
    """
    print(f"Collection size: {len(collection)}")
    
    unique_items = set(collection)
    print(f"Unique items: {len(unique_items)}")
    
    if len(collection) > 0:
        first = next(iter(collection))
        print(f"First item type: {type(first).__name__}")
```

## Type Safety
### Sized vs len() Function
```python
from typing import Any, Sized

# Without type hint - less safe
def unsafe_get_length(obj: Any) -> int:
    return len(obj)  # Could fail if obj doesn't support len()

# With Sized type hint - safer
def safe_get_length(obj: Sized) -> int:
    return len(obj)  # Type checker will ensure obj supports len()

# This would pass type checking but fail at runtime
# unsafe_get_length(123)  # Error: int has no len()

# This would fail at type checking time
# safe_get_length(123)  # Type error: int is not Sized
```

## Best Practices
1. **Use it for generic functions**: When writing functions that only need to know an object's length, use `Sized` rather than specific collection types.

2. **Combine with other protocols**: Often, you'll want to combine `Sized` with other protocols like `Iterable` or `Container`.

3. **Document size semantics**: When using `Sized`, document what the size represents in your specific context.

4. **Consider runtime checks**: For functions accepting `Sized`, consider adding runtime checks for size limits if appropriate.

5. **Protocol compatibility**: Remember that `Sized` only guarantees the existence of `__len__`, not any other collection methods.

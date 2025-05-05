# Sequence Type Hint in Python

## Overview
In Python, `Sequence` is a generic type hint representing any sequence data structure that supports indexing, iteration, and has a defined length. `Sequence` is an abstract base class (ABC) from the `collections.abc` module that the `typing` module makes available for type hints.

A `Sequence` provides read-only access to its elements, allowing operations like indexing (`s[i]`), slicing (`s[i:j]`), iteration (`for x in s`), and checking membership (`x in s`).

## Basic Usage
### Syntax
```python
from typing import Sequence

# Basic usage
def process_items(items: Sequence[int]) -> int:
    return sum(items)

# Any sequence of integers is acceptable
process_items([1, 2, 3])  # List
process_items((1, 2, 3))  # Tuple
process_items(range(1, 4))  # Range
```

## Common Use Cases
### Function Parameters That Accept Multiple Sequence Types
```python
from typing import Sequence

def calculate_average(numbers: Sequence[float]) -> float:
    """Calculate the average of a sequence of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty sequence")
    return sum(numbers) / len(numbers)

# Can be called with various sequence types
calculate_average([1.5, 2.5, 3.5])  # List
calculate_average((1.5, 2.5, 3.5))  # Tuple
calculate_average(range(1, 4))  # Range
```

### API Design for Read-Only Data
```python
from typing import Sequence, Dict, Any

class DataProcessor:
    def __init__(self, data_points: Sequence[Dict[str, Any]]):
        """Initialize with a sequence of data points.
        
        Args:
            data_points: A sequence of dictionaries containing data.
                         Only read access is needed, so Sequence is used.
        """
        self.data_points = data_points
    
    def get_field_values(self, field_name: str) -> list:
        """Extract values for a specific field from all data points."""
        return [point[field_name] for point in self.data_points if field_name in point]
    
    def filter_by_value(self, field: str, value: Any) -> list:
        """Filter data points by a specific field value."""
        return [point for point in self.data_points if point.get(field) == value]
```

### Data Processing Pipelines
```python
from typing import Sequence, TypeVar, Callable

T = TypeVar('T')
R = TypeVar('R')

def map_sequence(items: Sequence[T], func: Callable[[T], R]) -> list[R]:
    """Apply a function to each item in the sequence."""
    return [func(item) for item in items]

def filter_sequence(items: Sequence[T], predicate: Callable[[T], bool]) -> list[T]:
    """Filter items in the sequence by a predicate function."""
    return [item for item in items if predicate(item)]

def pipeline(data: Sequence[T], 
             transformations: Sequence[Callable[[Sequence[Any]], Sequence[Any]]]) -> Sequence[Any]:
    """Apply a sequence of transformations to the data."""
    result = data
    for transform in transformations:
        result = transform(result)
    return result
```

## Advanced Usage
### Sequence vs. List, Tuple, and Other Sequence Types
```python
from typing import Sequence, List, Tuple

# Specific sequence types
def process_list(items: List[int]) -> None:
    # Only accepts lists
    items.append(4)  # Safe to mutate

def process_tuple(items: Tuple[int, ...]) -> None:
    # Only accepts tuples
    # items.append(4)  # Error: tuples don't have append method

def process_sequence(items: Sequence[int]) -> None:
    # Accepts any sequence type (list, tuple, range, etc.)
    # items.append(4)  # Error: might not be mutable
    # Instead, use methods all sequences support:
    for i in range(len(items)):
        print(items[i])
```

### Sequence vs. Iterable
```python
from typing import Sequence, Iterable

def process_iterable(items: Iterable[int]) -> int:
    """Process any iterable - can only iterate once."""
    total = 0
    for item in items:
        total += item
    return total

def process_sequence(items: Sequence[int]) -> int:
    """Process a sequence - supports multiple operations."""
    # Can check length
    if len(items) == 0:
        return 0
    
    # Can access by index
    first_item = items[0]
    
    # Can iterate multiple times
    total = sum(items)
    
    # Can check membership
    if 5 in items:
        total += 10
        
    return total

# Both accept a list
values = [1, 2, 3, 4]
process_iterable(values)
process_sequence(values)

# But only process_iterable accepts a generator
process_iterable(x for x in range(5))  # Works
# process_sequence(x for x in range(5))  # TypeError: 'generator' object has no attribute '__len__'
```

### Nested Sequences
```python
from typing import Sequence

# Matrix represented as a sequence of sequences
Matrix = Sequence[Sequence[float]]

def calculate_row_sums(matrix: Matrix) -> list[float]:
    """Calculate the sum of each row in a matrix."""
    return [sum(row) for row in matrix]

# Usage with different sequence types
list_matrix = [[1.0, 2.0], [3.0, 4.0]]
tuple_matrix = ((1.0, 2.0), (3.0, 4.0))

print(calculate_row_sums(list_matrix))  # [3.0, 7.0]
print(calculate_row_sums(tuple_matrix))  # [3.0, 7.0]
```

## Custom Implementation
### Creating Custom Sequence Types
```python
from typing import Sequence, TypeVar, Iterator, Any
from collections.abc import Sequence as ABCSequence

T = TypeVar('T')

class ReadOnlyList(ABCSequence):
    """A simple read-only sequence wrapper."""
    
    def __init__(self, data: Sequence[T]):
        self._data = list(data)
    
    def __getitem__(self, index: int) -> T:
        return self._data[index]
    
    def __len__(self) -> int:
        return len(self._data)
    
    # __iter__ and __contains__ are provided by ABCSequence base class

# Usage
def process_data(data: Sequence[int]) -> int:
    return sum(data)

my_data = ReadOnlyList([1, 2, 3, 4])
result = process_data(my_data)  # Works because ReadOnlyList is a Sequence
```

## Best Practices
1. **Use `Sequence` for read-only access**: When you need to guarantee that the function won't modify the input sequence.

2. **Prefer `Sequence` over specific types when possible**: This makes your functions more flexible.

3. **Use `Sequence` for API boundaries**: This allows internal implementations to change without affecting the public interface.

4. **Combine with `TypeVar` for generic functions**: This helps maintain type safety when working with generic sequence processing.

5. **Consider performance implications**: Remember that `Sequence` requires length and random access, which some iterables don't support efficiently.

```python
from typing import Sequence, TypeVar, List

T = TypeVar('T')
R = TypeVar('R')

def safe_get(sequence: Sequence[T], index: int, default: R) -> T | R:
    """Safely get an item from a sequence with a default value if index is out of range."""
    if 0 <= index < len(sequence):
        return sequence[index]
    return default

def first_or_default(sequence: Sequence[T], default: T) -> T:
    """Return the first item in the sequence or a default value if it's empty."""
    return sequence[0] if sequence else default

def to_list(sequence: Sequence[T]) -> List[T]:
    """Convert any sequence to a list."""
    return list(sequence)
```

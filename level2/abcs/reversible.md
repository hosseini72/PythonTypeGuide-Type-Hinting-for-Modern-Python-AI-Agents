# Reversible Type Hint in Python

## Syntax (All Python Versions)
```python
from typing import Reversible, List

# A list as a reversible collection
items: Reversible[int] = [1, 2, 3, 4, 5]

# A string as a reversible collection of characters
text: Reversible[str] = "hello"

# A custom reversible class
sequence: Reversible[float] = ReversibleFloats([1.1, 2.2, 3.3])
```

In Python, Reversible is a type hint used to annotate variables, arguments, or return values that are expected to be reversible collections—objects that support reversed iteration through the __reversed__() method or through the built-in reversed() function. The syntax is Reversible[item_type] where item_type is the type of items in the collection.

## When to Use Reversible

### Functions That Accept Reversible Collections
```python
from typing import Reversible, List, TypeVar

T = TypeVar('T')

def process_in_reverse_order(items: Reversible[T]) -> List[T]:
    """Process items from last to first and return a new list."""
    return list(reversed(items))

# Usage with different reversible collections
numbers = [1, 2, 3, 4, 5]
result1 = process_in_reverse_order(numbers)  # [5, 4, 3, 2, 1]

text = "hello"
result2 = process_in_reverse_order(text)     # ['o', 'l', 'l', 'e', 'h']

tuple_data = (10, 20, 30)
result3 = process_in_reverse_order(tuple_data)  # [30, 20, 10]
```

### Functions That Return Reversible Collections
```python
from typing import Reversible, List

def create_bidirectional_range(start: int, end: int) -> Reversible[int]:
    """Create a range that can be iterated in either direction."""
    return range(start, end)

# Usage
numbers = create_bidirectional_range(1, 6)
forward = list(numbers)             # [1, 2, 3, 4, 5]
backward = list(reversed(numbers))  # [5, 4, 3, 2, 1]
```

### Implementing Reversible Collections
```python
from typing import Reversible, List, Iterator, TypeVar

T = TypeVar('T')

class BidirectionalList(List[T]):
    """A list that explicitly implements reversible iteration."""
    
    def __reversed__(self) -> Iterator[T]:
        """Return an iterator that traverses the list in reverse."""
        for i in range(len(self) - 1, -1, -1):
            yield self[i]

# Function that accepts and returns a reversible collection
def filter_bidirectional(items: Reversible[T], 
                         predicate: callable) -> Reversible[T]:
    result = BidirectionalList()
    for item in items:
        if predicate(item):
            result.append(item)
    return result

# Usage
numbers = BidirectionalList([1, 2, 3, 4, 5])
evens = filter_bidirectional(numbers, lambda x: x % 2 == 0)
print(list(evens))           # [2, 4]
print(list(reversed(evens)))  # [4, 2]
```

### Creating Custom Reversible Types
You can create custom types that conform to the Reversible protocol by implementing the __reversed__ method:
```python
from typing import Reversible, Iterator, List

class NumberSequence:
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self) -> Iterator[int]:
        """Forward iteration."""
        current = self.start
        while current < self.end:
            yield current
            current += self.step
    
    def __reversed__(self) -> Iterator[int]:
        """Reverse iteration."""
        # Calculate the last value in the sequence
        steps = (self.end - self.start - 1) // self.step
        current = self.start + (steps * self.step)
        
        while current >= self.start:
            yield current
            current -= self.step

# Function that accepts a reversible collection
def sum_values(values: Reversible[int]) -> int:
    """Sum values from a reversible collection."""
    return sum(values)

# Usage with custom reversible type
seq = NumberSequence(1, 10, 2)  # Sequence: 1, 3, 5, 7, 9
forward_list = list(seq)        # [1, 3, 5, 7, 9]
reverse_list = list(reversed(seq))  # [9, 7, 5, 3, 1]
total = sum_values(seq)         # 25
```

### Reversible vs Iterable
Reversible is a more specific version of Iterable that adds the capability for reverse iteration:
```python
from typing import Reversible, Iterable, List

def requires_any_iterable(items: Iterable[int]) -> List[int]:
    """This function only needs forward iteration."""
    return [item * 2 for item in items]

def requires_reversible(items: Reversible[int]) -> List[int]:
    """This function specifically needs reverse iteration."""
    return [item * 2 for item in reversed(items)]

# A dict_keys object is Iterable but not Reversible
dict_keys = {1: 'a', 2: 'b', 3: 'c'}.keys()

# This works (only needs forward iteration)
result1 = requires_any_iterable(dict_keys)

# This would fail at runtime (dict_keys doesn't support reversed)
# result2 = requires_reversible(dict_keys)  # Runtime error!

# A list is both Iterable and Reversible
numbers = [1, 2, 3]
result3 = requires_any_iterable(numbers)  # Works
result4 = requires_reversible(numbers)    # Also works
```

## Best Practices for Using Reversible
Use when reverse iteration is required: Only use Reversible when your function actually needs to iterate through the collection in reverse.

Fall back to Iterable when possible: If your function doesn't need reverse iteration, use the more general Iterable type hint.

Implement __reversed__ efficiently: When creating custom reversible types, implement __reversed__ with the same efficiency as __iter__ when possible.

Document reverse iteration behavior: When your class implements Reversible, document how reverse iteration works, especially if it's not simply returning elements in the opposite order.

Check for reversible support: Be aware that not all iterables support reverse iteration, so validate your inputs if necessary.

```python
from typing import Reversible, TypeVar, List

T = TypeVar('T')

def last_n_elements(items: Reversible[T], n: int) -> List[T]:
    """
    Get the last n elements from a reversible collection.
    
    Args:
        items: A reversible collection of elements
        n: Number of elements to retrieve from the end
    
    Returns:
        A list containing the last n elements in their original order
    
    Note:
        This function uses reverse iteration for efficiency and
        requires a collection that supports the `reversed()` operation.
    """
    result = []
    for i, item in enumerate(reversed(items)):
        if i >= n:
            break
        result.append(item)
    return result[::-1]  # Reverse back to original order
```

The Reversible type hint is useful for functions that specifically need to work with collections that can be iterated in reverse order, providing clear intent and enabling type checkers to verify that appropriate collections are passed to such functions.



[Back to Index](../../README.md)

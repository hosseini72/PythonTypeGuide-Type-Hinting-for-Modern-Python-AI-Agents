# Iterable Type Hint in Python

## Overview
In Python, `Iterable` is a protocol type hint that represents any object that can be iterated over, meaning it has an `__iter__` method that returns an iterator. This includes all built-in collections (lists, tuples, dictionaries, sets), strings, generators, and any custom class that implements the `__iter__` method.

## Basic Usage
### Syntax
```python
from typing import Iterable, TypeVar

T = TypeVar('T')

# Function that accepts an Iterable
def process_items(items: Iterable[T]) -> int:
    """Process items from an iterable and return count."""
    count = 0
    for item in items:
        # Process each item
        count += 1
    return count

# Usage examples
process_items([1, 2, 3])  # Lists are Iterable
process_items((1, 2, 3))  # Tuples are Iterable
process_items({1, 2, 3})  # Sets are Iterable
process_items({"a": 1, "b": 2})  # Dictionaries are Iterable (keys)
process_items("abc")  # Strings are Iterable
process_items(range(10))  # Range objects are Iterable
```

## Common Use Cases
### Processing Sequential Data
```python
from typing import Iterable, List, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def map_values(items: Iterable[T], func: callable) -> List[R]:
    """
    Apply a function to each item in the iterable.
    
    Args:
        items: Any iterable of elements
        func: Function to apply to each element
        
    Returns:
        List of transformed elements
    """
    return [func(item) for item in items]

def filter_values(items: Iterable[T], predicate: callable) -> List[T]:
    """
    Filter items based on a predicate function.
    
    Args:
        items: Any iterable of elements
        predicate: Function that returns True for items to keep
        
    Returns:
        List of filtered elements
    """
    return [item for item in items if predicate(item)]

# Usage examples
numbers = range(1, 11)
doubled = map_values(numbers, lambda x: x * 2)
print(doubled)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

evens = filter_values(numbers, lambda x: x % 2 == 0)
print(evens)  # [2, 4, 6, 8, 10]
```

### Data Aggregation and Reduction
```python
from typing import Iterable, TypeVar, Optional
import statistics

T = TypeVar('T', int, float)

def calculate_statistics(values: Iterable[T]) -> dict:
    """
    Calculate various statistics for a collection of numerical values.
    
    Args:
        values: Iterable of numerical values
        
    Returns:
        Dictionary with statistical measures
    """
    # Convert to list to avoid multiple iterations
    value_list = list(values)
    
    if not value_list:
        return {
            "count": 0,
            "sum": 0,
            "mean": None,
            "median": None,
            "min": None,
            "max": None
        }
    
    return {
        "count": len(value_list),
        "sum": sum(value_list),
        "mean": statistics.mean(value_list),
        "median": statistics.median(value_list),
        "min": min(value_list),
        "max": max(value_list)
    }

# Example usage
data_points = [12.5, 10.2, 15.1, 9.8, 17.3, 11.5]
stats = calculate_statistics(data_points)
print(f"Statistics: {stats}")

# Works with any numeric iterable
more_stats = calculate_statistics(range(1, 101))
print(f"Mean of 1-100: {more_stats['mean']}")
```

### Stream Processing
```python
from typing import Iterable, Iterator, TypeVar, Generator

T = TypeVar('T')

def chunk_data(data: Iterable[T], chunk_size: int) -> Iterator[list[T]]:
    """
    Split an iterable into chunks of specified size.
    
    Args:
        data: Any iterable of elements
        chunk_size: Number of elements per chunk
        
    Yields:
        Lists containing chunks of data
    """
    chunk = []
    for item in data:
        chunk.append(item)
        if len(chunk) >= chunk_size:
            yield chunk
            chunk = []
    
    if chunk:  # Don't forget the last partial chunk
        yield chunk

def moving_average(data: Iterable[float], window_size: int) -> Generator[float, None, None]:
    """
    Calculate moving average over an iterable.
    
    Args:
        data: Iterable of numeric values
        window_size: Size of the moving window
        
    Yields:
        Moving averages
    """
    window = []
    for value in data:
        window.append(value)
        if len(window) > window_size:
            window.pop(0)
        if len(window) == window_size:
            yield sum(window) / window_size

# Example usage
sensor_data = [10.2, 11.5, 10.9, 12.1, 11.8, 13.2, 12.7, 13.5]

# Process in chunks of 3
for chunk in chunk_data(sensor_data, 3):
    print(f"Processing chunk: {chunk}")

# Calculate 3-point moving average
averages = list(moving_average(sensor_data, 3))
print(f"Moving averages: {averages}")
```

## Custom Implementation
### Creating Custom Iterables
```python
from typing import Iterable, Iterator, TypeVar, Generator
import math

T = TypeVar('T')

class Fibonacci(Iterable[int]):
    """Class representing the Fibonacci sequence up to n terms."""
    
    def __init__(self, n: int):
        """Initialize with number of terms to generate."""
        self.n = n
    
    def __iter__(self) -> Iterator[int]:
        """Return an iterator for the sequence."""
        a, b = 0, 1
        for _ in range(self.n):
            yield a
            a, b = b, a + b

class PrimeNumbers(Iterable[int]):
    """Class generating prime numbers up to a limit."""
    
    def __init__(self, limit: int):
        """Initialize with upper limit."""
        self.limit = limit
    
    def __iter__(self) -> Iterator[int]:
        """Return an iterator for prime numbers."""
        if self.limit < 2:
            return
        
        yield 2  # First prime
        
        # Check odd numbers only
        for num in range(3, self.limit + 1, 2):
            is_prime = True
            # Check divisibility up to sqrt(num)
            for divisor in range(3, int(math.sqrt(num)) + 1, 2):
                if num % divisor == 0:
                    is_prime = False
                    break
            
            if is_prime:
                yield num

# Usage examples
fib = Fibonacci(10)
print(f"First 10 Fibonacci numbers: {list(fib)}")

primes = PrimeNumbers(50)
print(f"Prime numbers up to 50: {list(primes)}")

# Combining custom iterables
def first_n_common(iterable1: Iterable[T], iterable2: Iterable[T], n: int) -> list[T]:
    """Find first n common elements between two iterables."""
    common = []
    set2 = set(iterable2)  # Convert second iterable to set for O(1) lookups
    
    for item in iterable1:
        if item in set2:
            common.append(item)
            if len(common) >= n:
                break
    
    return common

# Find common numbers between Fibonacci and primes up to 5
common = first_n_common(Fibonacci(20), PrimeNumbers(100), 5)
print(f"First 5 numbers in both sequences: {common}")  # [2, 3, 5, 13, 89]
```

## Advanced Usage
### Infinite Iterables
```python
from typing import Iterable, Iterator, TypeVar, Optional
import itertools
import time

T = TypeVar('T')

def take(n: int, iterable: Iterable[T]) -> list[T]:
    """Take first n items from an iterable."""
    return list(itertools.islice(iterable, n))

class InfiniteCounter(Iterable[int]):
    """An infinite sequence of integers."""
    
    def __init__(self, start: int = 0, step: int = 1):
        self.start = start
        self.step = step
    
    def __iter__(self) -> Iterator[int]:
        value = self.start
        while True:  # Never stops
            yield value
            value += self.step

def sensor_simulator() -> Iterator[float]:
    """Simulate an infinite stream of sensor readings."""
    while True:
        # Simulate some time-based value with noise
        yield 20 + 5 * math.sin(time.time() / 10) + random.random()
        time.sleep(0.1)  # Simulate reading delay

# Usage with take() to avoid infinite loops
counter = InfiniteCounter(10, 5)
print(f"First 5 numbers: {take(5, counter)}")  # [10, 15, 20, 25, 30]

# Using with more advanced itertools
from itertools import cycle, repeat, count

# Cycling through a finite sequence infinitely
days = cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
print(f"Next 10 days: {take(10, days)}")

# Repeated values
warnings = repeat("Warning: System overheating", 3)
for warning in warnings:
    print(warning)

# Counting with a start and step
even_numbers = count(start=0, step=2)
print(f"First 5 even numbers: {take(5, even_numbers)}")  # [0, 2, 4, 6, 8]
```

### Lazy Evaluation and Memory Efficiency
```python
from typing import Iterable, Iterator, TypeVar
import sys

T = TypeVar('T')

def get_large_range() -> range:
    """Return a memory-efficient range object."""
    return range(10**8)  # 100 million numbers

def process_large_data(data: Iterable[T]) -> int:
    """
    Process large amounts of data efficiently.
    
    Args:
        data: Iterable that may contain a large number of elements
        
    Returns:
        Count of processed elements
    """
    count = 0
    for item in data:
        # Process each item without loading everything into memory
        count += 1
        if count % 10000000 == 0:  # Every 10 million
            print(f"Processed {count} items...")
    return count

# Memory comparison
def memory_comparison():
    # Memory-inefficient approach (loads everything into memory)
    large_list = list(range(10**7))  # 10 million numbers
    list_size = sys.getsizeof(large_list) + sum(sys.getsizeof(i) for i in large_list[:5]) * len(large_list) // 5
    
    # Memory-efficient iterable
    large_range = range(10**7)  # Same 10 million numbers
    range_size = sys.getsizeof(large_range)
    
    print(f"List size: {list_size / 1024 / 1024:.2f} MB")
    print(f"Range size: {range_size / 1024:.2f} KB")
    
    # Efficient file processing
    with open("large_file.txt", "w") as f:
        for i in range(1000):
            f.write(f"Line {i}\n")
    
    def line_count(filename: str) -> int:
        """Count lines in a file efficiently."""
        count = 0
        with open(filename, "r") as f:
            for _ in f:  # Efficient file iterator
                count += 1
        return count
    
    print(f"File has {line_count('large_file.txt')} lines")

# Generator expressions for memory efficiency
def sum_of_squares(n: int) -> int:
    """Calculate sum of squares using generator expression."""
    return sum(x**2 for x in range(n))  # Generator expression

# List comprehension loads everything into memory
squares_list = [x**2 for x in range(1000000)]

# Generator expression is lazy and more memory-efficient
squares_gen = (x**2 for x in range(1000000))

print(f"Sum of first million squares: {sum_of_squares(1000000)}")
```

### Iterable vs Iterator
```python
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

def demonstrate_difference():
    # An iterable can be used multiple times
    numbers = [1, 2, 3, 4, 5]  # This is an Iterable
    
    print("First iteration:")
    for n in numbers:
        print(n, end=' ')
    print()
    
    print("Second iteration:")
    for n in numbers:
        print(n, end=' ')
    print()
    
    # An iterator is consumed as you use it
    numbers_iter = iter(numbers)  # This is an Iterator
    
    print("First iteration of iterator:")
    for n in numbers_iter:
        print(n, end=' ')
    print()
    
    print("Second iteration of iterator:")
    for n in numbers_iter:  # This won't print anything - iterator is consumed
        print(n, end=' ')
    print(" (nothing - iterator is exhausted)")

# Custom class that is both Iterable and Iterator
class CountDown(Iterable[int], Iterator[int]):
    """A countdown that is both an iterable and its own iterator."""
    
    def __init__(self, start: int):
        self.current = start
    
    def __iter__(self) -> Iterator[int]:
        """Return self as the iterator."""
        return self
    
    def __next__(self) -> int:
        """Get next value or raise StopIteration."""
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Usage
countdown = CountDown(5)
print(list(countdown))  # [5, 4, 3, 2, 1]
print(list(countdown))  # [] (iterator is exhausted)

# A more proper Iterable-only implementation
class ProperCountDown(Iterable[int]):
    """A countdown that creates fresh iterators."""
    
    def __init__(self, start: int):
        self.start = start
    
    def __iter__(self) -> Iterator[int]:
        """Return a new iterator each time."""
        current = self.start
        while current > 0:
            yield current
            current -= 1

# Usage
proper_countdown = ProperCountDown(5)
print(list(proper_countdown))  # [5, 4, 3, 2, 1]
print(list(proper_countdown))  # [5, 4, 3, 2, 1] (works again!)
```

## Best Practices
1. **Use Iterable for function parameters** when you only need to iterate over the input once.

2. **Create lazy iterables with generators** to improve memory efficiency for large datasets.

3. **Convert to a concrete collection** (like list) when you need to:
   - Use the data multiple times
   - Know the length
   - Access elements by index
   - Use methods specific to that collection type

4. **Compose iterables with itertools** to build complex data processing pipelines without intermediate collections.

5. **Remember consumption behavior**: Be aware that some iterables (like generators and iterators) can only be consumed once.

```python
from typing import Iterable, TypeVar, Iterator
import itertools

T = TypeVar('T')

def process_data_stream(data: Iterable[T]) -> Iterator[T]:
    """
    Process a data stream efficiently using composition of iterables.
    
    Args:
        data: Source iterable
        
    Returns:
        Iterator of processed results
    """
    # Chain of operations, all lazy
    return itertools.islice(  # Take only first 1000
        (x for x in data if isinstance(x, (int, float))),  # Filter numeric
        1000
    )

# Flattening nested iterables
def flatten(nested: Iterable[Iterable[T]]) -> Iterator[T]:
    """Flatten a nested iterable structure."""
    for inner in nested:
        for item in inner:
            yield item

# Alternative using itertools.chain
def flatten_alt(nested: Iterable[Iterable[T]]) -> Iterator[T]:
    """Flatten a nested iterable using itertools."""
    return itertools.chain.from_iterable(nested)

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = list(flatten(matrix))
print(f"Flattened: {flat}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The `Iterable` type hint is fundamental to Python's collection system, representing objects that can be iterated over. Using this type hint improves code flexibility, enabling functions to work with a wide variety of sequence types while maintaining good type safety.


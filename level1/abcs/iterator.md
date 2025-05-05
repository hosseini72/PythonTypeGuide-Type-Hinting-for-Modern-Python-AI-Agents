# Iterator Type Hint in Python

## Overview
In Python, `Iterator` is a protocol type hint that represents objects that implement both `__iter__` and `__next__` methods. Unlike general iterables, iterators maintain state and are consumed as they are iterated over. Once an iterator is exhausted, it cannot be reused without creating a new iterator.

## Basic Usage
### Syntax
```python
from typing import Iterator, TypeVar

T = TypeVar('T')

# Function that accepts an Iterator
def consume_iterator(iterator: Iterator[T]) -> None:
    """Consume all elements from an iterator."""
    for item in iterator:
        print(f"Processing: {item}")

# Usage examples
consume_iterator(iter([1, 2, 3]))  # Convert list to iterator
consume_iterator(iter("abc"))  # Convert string to iterator
consume_iterator((x for x in range(5)))  # Generator expression is an Iterator
```

## Common Use Cases
### Stream Processing
```python
from typing import Iterator, TypeVar, List, Optional
import csv
from io import StringIO

T = TypeVar('T')

def process_csv_rows(csv_data: str) -> Iterator[dict]:
    """
    Process CSV data row by row.
    
    Args:
        csv_data: String containing CSV data
        
    Yields:
        Each row as a dictionary
    """
    csv_file = StringIO(csv_data)
    reader = csv.DictReader(csv_file)
    for row in reader:
        # Process and yield one row at a time
        yield row

def filter_iterator(iterator: Iterator[T], predicate: callable) -> Iterator[T]:
    """
    Filter elements from an iterator based on a predicate.
    
    Args:
        iterator: Source iterator
        predicate: Function returning True for elements to keep
        
    Yields:
        Filtered elements
    """
    for item in iterator:
        if predicate(item):
            yield item

# Example usage
csv_content = """
name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
David,40,Boston
"""

# Process CSV row by row
rows = process_csv_rows(csv_content.strip())

# Filter rows where age > 30
filtered_rows = filter_iterator(rows, lambda row: int(row['age']) > 30)

# Print filtered rows
for row in filtered_rows:
    print(f"{row['name']} from {row['city']}, age {row['age']}")
```

### Data Transformation Pipelines
```python
from typing import Iterator, TypeVar, Callable, Any, Dict, List

T = TypeVar('T')
U = TypeVar('U')

def map_iterator(iterator: Iterator[T], transform: Callable[[T], U]) -> Iterator[U]:
    """
    Apply a transformation to each element in an iterator.
    
    Args:
        iterator: Source iterator
        transform: Function to apply to each element
        
    Yields:
        Transformed elements
    """
    for item in iterator:
        yield transform(item)

def batch_iterator(iterator: Iterator[T], batch_size: int) -> Iterator[List[T]]:
    """
    Batch elements from an iterator.
    
    Args:
        iterator: Source iterator
        batch_size: Number of elements per batch
        
    Yields:
        Lists containing batches of elements
    """
    batch = []
    for item in iterator:
        batch.append(item)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    
    if batch:  # Don't forget the last partial batch
        yield batch

# Example usage
def process_log_entries(log_file: str) -> Iterator[Dict[str, Any]]:
    """Process log entries line by line."""
    with open(log_file, 'r') as f:
        for line in f:
            # Parse log entry (simplified)
            if line.strip():
                parts = line.strip().split(' - ')
                if len(parts) >= 3:
                    yield {
                        'timestamp': parts[0],
                        'level': parts[1],
                        'message': parts[2]
                    }

# Example log file:
# 2023-05-01 12:00:00 - INFO - User logged in
# 2023-05-01 12:01:30 - WARNING - High memory usage
# 2023-05-01 12:02:15 - ERROR - Database connection failed

# Pipeline for processing logs
def process_logs_pipeline(log_file: str):
    # Step 1: Parse log entries
    entries = process_log_entries(log_file)
    
    # Step 2: Filter for errors and warnings
    important_entries = filter_iterator(
        entries,
        lambda entry: entry['level'] in ('ERROR', 'WARNING')
    )
    
    # Step 3: Transform entries to include severity level
    enhanced_entries = map_iterator(
        important_entries,
        lambda entry: {
            **entry,
            'severity': 'HIGH' if entry['level'] == 'ERROR' else 'MEDIUM'
        }
    )
    
    # Step 4: Batch entries for processing
    batches = batch_iterator(enhanced_entries, 10)
    
    # Process each batch
    for i, batch in enumerate(batches):
        print(f"Processing batch {i+1} with {len(batch)} entries")
        for entry in batch:
            print(f"{entry['timestamp']} - {entry['level']} ({entry['severity']}): {entry['message']}")
```

### Memory-Efficient Processing
```python
from typing import Iterator, List, Dict, Any
import json

def read_large_json_file(file_path: str) -> Iterator[Dict[str, Any]]:
    """
    Read a large JSON file containing an array of objects line by line.
    
    Args:
        file_path: Path to the JSON file
        
    Yields:
        Each JSON object parsed as a dictionary
    """
    with open(file_path, 'r') as f:
        # Skip the opening bracket
        first_line = f.readline().strip()
        if not first_line.startswith('['):
            raise ValueError("Expected JSON array")
        
        # Process each line as a separate JSON object
        for line in f:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
                
            # Remove trailing comma if present
            if line.endswith(','):
                line = line[:-1]
                
            # Skip the closing bracket
            if line == ']':
                break
                
            try:
                yield json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")

def find_matching_records(records: Iterator[Dict[str, Any]], criteria: Dict[str, Any]) -> Iterator[Dict[str, Any]]:
    """
    Find records that match all criteria.
    
    Args:
        records: Iterator of record dictionaries
        criteria: Dictionary of field-value pairs to match
        
    Yields:
        Records that match all criteria
    """
    for record in records:
        if all(record.get(field) == value for field, value in criteria.items()):
            yield record

# Example usage for a hypothetical large data file
def analyze_large_data(file_path: str, output_path: str):
    """Analyze a large dataset without loading it all into memory."""
    # Read data as an iterator
    data_iterator = read_large_json_file(file_path)
    
    # Filter for relevant records
    active_users = find_matching_records(data_iterator, {'status': 'active'})
    
    # Process records in batches to avoid memory issues
    with open(output_path, 'w') as out_file:
        for batch in batch_iterator(active_users, 1000):
            # Process batch
            for user in batch:
                # Write processed data
                out_file.write(f"{user['id']},{user['name']},{user['last_login']}\n")
```

## Custom Implementation
### Creating Custom Iterators
```python
from typing import Iterator, TypeVar, List, Optional, Generic

T = TypeVar('T')

class ReverseIterator(Iterator[T]):
    """Iterator that yields elements from a sequence in reverse order."""
    
    def __init__(self, sequence: List[T]):
        self.sequence = sequence
        self.index = len(sequence)
    
    def __iter__(self) -> Iterator[T]:
        """Return self as the iterator."""
        return self
    
    def __next__(self) -> T:
        """Get the next element or raise StopIteration."""
        if self.index <= 0:
            raise StopIteration
        
        self.index -= 1
        return self.sequence[self.index]

class PeekableIterator(Iterator[T], Generic[T]):
    """An iterator that allows peeking at the next element without consuming it."""
    
    def __init__(self, iterator: Iterator[T]):
        self.iterator = iterator
        self._peek: Optional[T] = None
        self._has_peek = False
    
    def __iter__(self) -> Iterator[T]:
        """Return self as the iterator."""
        return self
    
    def __next__(self) -> T:
        """Get the next element or raise StopIteration."""
        if self._has_peek:
            value = self._peek
            self._peek = None
            self._has_peek = False
            return value
        else:
            return next(self.iterator)
    
    def peek(self) -> Optional[T]:
        """
        Peek at the next element without consuming it.
        
        Returns:
            The next element or None if iterator is exhausted
        """
        if not self._has_peek:
            try:
                self._peek = next(self.iterator)
                self._has_peek = True
            except StopIteration:
                return None
        
        return self._peek

# Usage examples
numbers = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(numbers)
print(list(reverse_iter))  # [5, 4, 3, 2, 1]

# Using PeekableIterator
def parse_tokens(tokens: Iterator[str]) -> List[str]:
    """Parse tokens with lookahead."""
    peekable = PeekableIterator(tokens)
    result = []
    
    while True:
        current = peekable.peek()
        if current is None:
            break
        
        if current == '(':
            # Consume '('
            next(peekable)
            # Process until matching ')'
            group = []
            while peekable.peek() != ')':
                if peekable.peek() is None:
                    raise ValueError("Unclosed parenthesis")
                group.append(next(peekable))
            # Consume ')'
            next(peekable)
            result.append(f"({' '.join(group)})")
        else:
            result.append(next(peekable))
    
    return result

# Example parsing
tokens = iter(['a', 'b', '(', 'c', 'd', ')', 'e'])
parsed = parse_tokens(tokens)
print(parsed)  # ['a', 'b', '(c d)', 'e']
```

## Advanced Usage
### Iterator State and Consumption
```python
from typing import Iterator, TypeVar, List, Iterable

T = TypeVar('T')

def demonstrate_consumption():
    # Create an iterator
    numbers = [1, 2, 3, 4, 5]
    iterator = iter(numbers)
    
    # Use the iterator partially
    print(next(iterator))  # 1
    print(next(iterator))  # 2
    
    # Remaining elements
    remaining = list(iterator)
    print(remaining)  # [3, 4, 5]
    
    # Iterator is now exhausted
    try:
        print(next(iterator))
    except StopIteration:
        print("Iterator is exhausted")

def clone_iterator(iterator: Iterator[T], n: int = 2) -> List[Iterator[T]]:
    """
    Clone an iterator into multiple copies.
    Note: This consumes the original iterator.
    
    Args:
        iterator: Source iterator
        n: Number of clones to create
        
    Returns:
        List of n iterators, each yielding the same elements
    """
    # Consume the iterator into a list
    items = list(iterator)
    
    # Create n new iterators
    return [iter(items) for _ in range(n)]

def safe_next(iterator: Iterator[T], default: T = None) -> T:
    """
    Safely get the next element from an iterator with a default value.
    
    Args:
        iterator: Source iterator
        default: Value to return if iterator is exhausted
        
    Returns:
        Next element or default value
    """
    try:
        return next(iterator)
    except StopIteration:
        return default

# Example usage
def compare_iterators_and_iterables():
    # Creating a list (Iterable)
    numbers_list = [1, 2, 3]
    
    # Creating an iterator from the list
    numbers_iter = iter(numbers_list)
    
    # You can iterate over a list multiple times
    print("First list iteration:")
    for n in numbers_list:
        print(n, end=' ')
```


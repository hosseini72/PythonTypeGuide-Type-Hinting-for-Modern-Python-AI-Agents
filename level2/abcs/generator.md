# Generator Type Hints in Python

## Overview
Generator type hints in Python are used to specify functions or objects that generate a sequence of values lazily using the `yield` statement. Generators are iterators that can only be iterated once, producing values on-demand rather than computing the entire sequence at once, making them memory-efficient for large data processing.

## Basic Usage

### Simple Generator Type Hints
```python
from typing import Generator

# Basic Generator type hint
def count_up(limit: int) -> Generator[int, None, None]:
    for i in range(limit):
        yield i

counter: Generator[int, None, None] = count_up(5)

# Generator in a function parameter
def process_numbers(numbers: Generator[int, None, None]) -> int:
    return sum(numbers)

# Generator in a class attribute
class DataProcessor:
    def __init__(self, data_source: Generator[str, None, None]) -> None:
        self.data_source: Generator[str, None, None] = data_source
```

### Generator with Optional Values
```python
from typing import Optional, Generator

# Generator that can be None
nullable_gen: Optional[Generator[float, None, None]] = None
def generate_floats() -> Generator[float, None, None]:
    for i in range(5):
        yield i / 2.0
nullable_gen = generate_floats()  # Valid assignment
```

## Common Use Cases

### Data Processing Pipelines
```python
from typing import Generator, List, TypeVar, Any

T = TypeVar('T')
U = TypeVar('U')

def map_values(func: callable[[T], U], values: Generator[T, None, None]) -> Generator[U, None, None]:
    for value in values:
        yield func(value)

def filter_values(pred: callable[[T], bool], values: Generator[T, None, None]) -> Generator[T, None, None]:
    for value in values:
        if pred(value):
            yield value

def process_data() -> Generator[dict, None, None]:
    data = read_large_file()  # Returns a generator of lines
    parsed = map_values(parse_line, data)
    filtered = filter_values(is_valid_record, parsed)
    for record in filtered:
        # Process each record
        yield {"processed": record}
```

### Generators with Send and Return Types
```python
from typing import Generator

# Generator that can receive values and return a result
def echo_generator() -> Generator[str, str, int]:
    count = 0
    msg = yield "Ready"  # Initial yield
    while msg != "stop":
        count += 1
        msg = yield f"Echo: {msg}"
    return count

# Using the generator
def use_echo() -> None:
    gen: Generator[str, str, int] = echo_generator()
    print(next(gen))  # Prints "Ready" and pauses at first yield
    print(gen.send("Hello"))  # Sends "Hello", prints "Echo: Hello"
    print(gen.send("World"))  # Sends "World", prints "Echo: World"
    try:
        gen.send("stop")  # This will raise StopIteration with return value
    except StopIteration as e:
        print(f"Generator returned: {e.value}")  # Prints the count
```

## Important Notes

1. **Generator Characteristics**:
   - Created using functions with `yield` statements
   - Parameterized as `Generator[YieldType, SendType, ReturnType]`
   - YieldType: Type of values yielded by the generator
   - SendType: Type of values that can be sent to the generator via .send()
   - ReturnType: Type returned when generator completes (from return statement)
   - Common pattern is `Generator[T, None, None]` for simple generators
   - Lazily evaluated, generating values on-demand
   - Can only be iterated once

2. **Type Hint Evolution**:
   - Python 3.5+: Basic `Generator` type hint
   - Python 3.6.1+: Full support for variable annotations
   - Python 3.9+: Can be used in built-in collection types (e.g., `list[Generator[int, None, None]]`)
   - Python 3.10+: Can be used in union types with `|` operator

3. **Best Practices**:
   - Use `Generator[YieldType, None, None]` for simple yield-only generators
   - Use `Iterator[T]` when you only care about the iteration aspect
   - Specify SendType when using `.send()` to communicate with the generator
   - Specify ReturnType when the generator has a meaningful return value
   - Close generators explicitly if they need cleanup using `.close()`

4. **Related Types**:
   - `Iterator`: More general type for any iterator
   - `Iterable`: For objects that can produce iterators
   - `AsyncGenerator`: For asynchronous generators using `async def` with `yield`
   - `collections.abc.Generator`: Runtime checkable version (Python 3.9+)
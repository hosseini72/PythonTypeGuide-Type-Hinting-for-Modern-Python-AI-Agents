# AsyncIterable Type Hints in Python

## Overview
AsyncIterable type hints in Python are used to specify objects that implement the `__aiter__` method, which returns an AsyncIterator. These objects can be used in `async for` loops and represent asynchronous streams of data. AsyncIterable is a more general type than AsyncIterator, capturing any object that can produce an asynchronous iterator.

## Basic Usage

### Simple AsyncIterable Type Hints
```python
from typing import AsyncIterable

# Basic AsyncIterable type hint
async def generate_data(limit: int) -> AsyncIterable[int]:
    for i in range(limit):
        yield i
        await asyncio.sleep(0.1)

data_source: AsyncIterable[int] = generate_data(5)

# AsyncIterable in a function parameter
async def sum_values(values: AsyncIterable[int]) -> int:
    total = 0
    async for value in values:
        total += value
    return total

# AsyncIterable in a class attribute
class DataAnalyzer:
    def __init__(self, data_stream: AsyncIterable[float]) -> None:
        self.data_stream: AsyncIterable[float] = data_stream
```

### AsyncIterable with Optional Values
```python
from typing import Optional, AsyncIterable

# AsyncIterable that can be None
nullable_stream: Optional[AsyncIterable[str]] = None
async def generate_strings() -> AsyncIterable[str]:
    words = ["async", "programming", "python"]
    for word in words:
        yield word
        await asyncio.sleep(0.1)
nullable_stream = generate_strings()  # Valid assignment
```

## Common Use Cases

### Processing Data Streams
```python
import asyncio
from typing import AsyncIterable, List, TypeVar

T = TypeVar('T')

async def collect_to_list(iterable: AsyncIterable[T]) -> List[T]:
    result = []
    async for item in iterable:
        result.append(item)
    return result

async def process_in_batches(iterable: AsyncIterable[T], batch_size: int = 10) -> AsyncIterable[List[T]]:
    batch = []
    async for item in iterable:
        batch.append(item)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    if batch:  # Don't forget the last partial batch
        yield batch
```

### Custom AsyncIterable Classes
```python
from typing import AsyncIterable, AsyncIterator, Any
import asyncio

class AsyncRange:
    def __init__(self, stop: int, delay: float = 0.1) -> None:
        self.stop = stop
        self.delay = delay
    
    def __aiter__(self) -> AsyncIterator[int]:
        async def iterator() -> AsyncIterator[int]:
            for i in range(self.stop):
                await asyncio.sleep(self.delay)
                yield i
        return iterator()

class AsyncEventEmitter:
    def __init__(self) -> None:
        self.events = []
    
    def add_event(self, event: Any) -> None:
        self.events.append(event)
    
    def get_events(self) -> AsyncIterable[Any]:
        async def event_generator() -> AsyncIterator[Any]:
            for event in self.events:
                yield event
                await asyncio.sleep(0.01)
        return event_generator()
```

## Important Notes

1. **AsyncIterable Characteristics**:
   - Implements only the `__aiter__` method that returns an AsyncIterator
   - Can be used directly in `async for` loops
   - AsyncIterable objects can be iterated multiple times
   - More general than AsyncIterator (which is both iterable and iterator)
   - Common in representing sources of asynchronous data streams

2. **Type Hint Evolution**:
   - Python 3.5+: Basic `AsyncIterable` type hint
   - Python 3.6+: Support for async generators (`async def` with `yield`)
   - Python 3.9+: Can be used in built-in collection types (e.g., `list[AsyncIterable[int]]`)
   - Python 3.10+: Can be used in union types with `|` operator

3. **Best Practices**:
   - Use `AsyncIterable[T]` for parameters accepting any async iterable object
   - Use `AsyncIterator[T]` when you need to directly access the iterator methods
   - Prefer async generator functions for simple AsyncIterable implementations
   - Remember that AsyncIterable objects can be iterated multiple times
   - Consider resource management (like async context managers) for cleanup

4. **Related Types**:
   - `AsyncIterator`: For objects that are both async iterable and iterators
   - `Iterable`: The synchronous equivalent of AsyncIterable
   - `AsyncGenerator`: Specific type for async generator functions
   - `Awaitable`: For objects that can be awaited once
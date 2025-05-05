# AsyncIterator Type Hints in Python

## Overview
AsyncIterator type hints in Python are used to specify objects that implement the asynchronous iterator protocol (`__aiter__` and `__anext__` methods). These objects allow asynchronous iteration, enabling retrieval of values with `async for` loops, and are fundamental to Python's asynchronous programming model for handling streams of data.

## Basic Usage

### Simple AsyncIterator Type Hints
```python
from typing import AsyncIterator

# Basic AsyncIterator type hint
async def async_count(limit: int) -> AsyncIterator[int]:
    for i in range(limit):
        yield i
        await asyncio.sleep(0.1)

counter: AsyncIterator[int] = async_count(5)

# AsyncIterator in a function parameter
async def process_items(items: AsyncIterator[str]) -> list[str]:
    result = []
    async for item in items:
        result.append(item.upper())
    return result

# AsyncIterator in a class attribute
class DataProcessor:
    def __init__(self, data_stream: AsyncIterator[bytes]) -> None:
        self.data_stream: AsyncIterator[bytes] = data_stream
```

### AsyncIterator with Optional Values
```python
from typing import Optional, AsyncIterator

# AsyncIterator that can be None
nullable_stream: Optional[AsyncIterator[float]] = None
async def generate_floats() -> AsyncIterator[float]:
    for i in range(5):
        yield float(i) / 2
        await asyncio.sleep(0.1)
nullable_stream = generate_floats()  # Valid assignment
```

## Common Use Cases

### Stream Processing
```python
import asyncio
from typing import AsyncIterator, TypeVar

T = TypeVar('T')

async def filter_async(
    predicate: callable[[T], bool], 
    iterator: AsyncIterator[T]
) -> AsyncIterator[T]:
    async for item in iterator:
        if predicate(item):
            yield item

async def map_async(
    func: callable[[T], T], 
    iterator: AsyncIterator[T]
) -> AsyncIterator[T]:
    async for item in iterator:
        yield func(item)
```

### Custom AsyncIterator Classes
```python
from typing import AsyncIterator, Any, Optional

class AsyncQueue:
    def __init__(self) -> None:
        self.items = []
        
    def add_item(self, item: Any) -> None:
        self.items.append(item)
        
    def __aiter__(self) -> 'AsyncQueue':
        return self
        
    async def __anext__(self) -> Any:
        if not self.items:
            raise StopAsyncIteration
        return self.items.pop(0)

async def process_queue(queue: AsyncIterator[str]) -> None:
    async for item in queue:
        print(f"Processing {item}")
```

## Important Notes

1. **AsyncIterator Characteristics**:
   - Implements `__aiter__` and `__anext__` methods
   - `__anext__` returns an awaitable that resolves to the next value
   - Used with `async for` loops
   - Can be created using async generator functions (`async def` with `yield`)
   - Raises `StopAsyncIteration` when iteration is complete

2. **Type Hint Evolution**:
   - Python 3.5+: Basic `AsyncIterator` type hint
   - Python 3.9+: Can be used in built-in collection types (e.g., `list[AsyncIterator[int]]`)
   - Python 3.10+: Can be used in union types with `|` operator

3. **Best Practices**:
   - Use `AsyncIterator[T]` for objects that will be used in `async for` loops
   - Use `AsyncIterable[T]` for objects that implement only `__aiter__`
   - Consider using async generator functions for simpler implementations
   - Close iterators explicitly if needed using `aclose()`

4. **Related Types**:
   - `AsyncIterable`: For objects that return `AsyncIterator` objects
   - `AsyncGenerator`: More specific type for async generator functions
   - `Iterator`: For synchronous iteration
   - `Awaitable`: For objects that can be awaited once
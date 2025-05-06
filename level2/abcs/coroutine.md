# Coroutine Type Hints in Python

## Overview
Coroutine type hints in Python are used to specify objects created by `async def` functions. Coroutines are a specialized form of awaitable objects that represent asynchronous operations and can be awaited using the `await` keyword. The Coroutine type hint is more specific than Awaitable and is used to indicate native Python coroutines.

## Basic Usage

### Simple Coroutine Type Hints
```python
from typing import Coroutine

# Basic Coroutine type hint
async def fetch_data() -> str:
    # Some async operation
    return "Data"

result: Coroutine[None, None, str] = fetch_data()

# Coroutine in a function parameter
def schedule_coroutine(coro: Coroutine[None, None, str]) -> None:
    # Schedule the coroutine for execution
    import asyncio
    asyncio.create_task(coro)

# Coroutine in a class attribute
class TaskScheduler:
    def __init__(self, startup_task: Coroutine[None, None, None]) -> None:
        self.startup_task: Coroutine[None, None, None] = startup_task
```

### Coroutine with Optional Values
```python
from typing import Optional, Coroutine

# Coroutine that can be None
nullable_task: Optional[Coroutine[None, None, int]] = None
async def get_count() -> int:
    return 42
nullable_task = get_count()  # Valid assignment
```

## Common Use Cases

### Function Returning Coroutines
```python
from typing import Coroutine, Any

def create_fetcher(url: str) -> Coroutine[None, None, str]:
    async def fetch() -> str:
        # Simulate fetching data from URL
        return f"Data from {url}"
    
    return fetch()

async def process_urls(urls: list[str]) -> list[str]:
    results = []
    for url in urls:
        coro: Coroutine[None, None, str] = create_fetcher(url)
        results.append(await coro)
    return results
```

### Coroutines with Send/Yield Types
```python
from typing import Coroutine

# Coroutine that yields int values and can receive str values
async def data_processor() -> int:
    received = yield 1
    if isinstance(received, str):
        return len(received)
    return 0

# Type hint specifying yield and send types
processor: Coroutine[str, int, int] = data_processor()
```

## Important Notes

1. **Coroutine Characteristics**:
   - Created by `async def` functions
   - Parameterized as `Coroutine[YieldType, SendType, ReturnType]`
   - YieldType: Type of values yielded by coroutine
   - SendType: Type of values that can be sent to coroutine
   - ReturnType: Type returned by coroutine
   - Common pattern is `Coroutine[None, None, T]` for simple async functions

2. **Type Hint Evolution**:
   - Python 3.5+: Basic `Coroutine` type hint
   - Python 3.9+: Can be used in built-in collection types (e.g., `list[Coroutine[None, None, str]]`)
   - Python 3.10+: Can be used in union types with `|` operator

3. **Best Practices**:
   - Use `Coroutine[None, None, T]` for standard async functions
   - Use `Awaitable[T]` when you want to accept any awaitable object
   - Remember to await coroutines to get their return values
   - Avoid passing raw coroutines around; consider using Tasks

4. **Related Types**:
   - `Awaitable`: More general type for any awaitable object
   - `AsyncGenerator`: For async generators (using `async def` with `yield`)
   - `Generator`: For synchronous generators
   - `asyncio.Task`: Concrete scheduled coroutine from the asyncio module


[Back to Index](../../README.md)

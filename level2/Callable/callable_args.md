# Callable Type Hints in Python

## Overview
Callable type hints in Python are used to specify functions, methods, or any callable objects. The `Callable[[Arg1Type, Arg2Type, ...], ReturnType]` syntax indicates that a variable is expected to be callable with specific argument types and return type. This is especially useful for higher-order functions, callbacks, and dependency injection patterns.

## Basic Usage

### Simple Callable Type Hints
```python
from typing import Callable

# Basic Callable type hint
def greet(name: str) -> str:
    return f"Hello, {name}!"

greeter: Callable[[str], str] = greet

# Callable with multiple parameters
def add(a: int, b: int) -> int:
    return a + b

adder: Callable[[int, int], int] = add

# Callable in a function parameter
def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

# Callable in a class attribute
class MathOperations:
    def __init__(self, operation: Callable[[float, float], float]) -> None:
        self.operation: Callable[[float, float], float] = operation
```

### Callable with Optional Values
```python
from typing import Optional, Callable

# Callable that can be None
nullable_func: Optional[Callable[[str], int]] = None

def string_length(s: str) -> int:
    return len(s)

nullable_func = string_length  # Valid assignment
```

## Common Use Cases

### Higher-Order Functions
```python
from typing import Callable, List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def map_items(func: Callable[[T], U], items: List[T]) -> List[U]:
    return [func(item) for item in items]

def filter_items(predicate: Callable[[T], bool], items: List[T]) -> List[T]:
    return [item for item in items if predicate(item)]

def compose(f: Callable[[T], U], g: Callable[[U], T]) -> Callable[[T], T]:
    return lambda x: g(f(x))
```

### Callback Patterns
```python
from typing import Callable, Any, Dict, Optional

# Event handler pattern
class EventEmitter:
    def __init__(self) -> None:
        self.listeners: Dict[str, List[Callable[..., None]]] = {}
        
    def on(self, event: str, callback: Callable[..., None]) -> None:
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(callback)
        
    def emit(self, event: str, *args: Any, **kwargs: Any) -> None:
        if event in self.listeners:
            for callback in self.listeners[event]:
                callback(*args, **kwargs)

# Strategy pattern
class Validator:
    def __init__(self, validation_strategy: Callable[[str], bool]) -> None:
        self.validate: Callable[[str], bool] = validation_strategy
        
    def is_valid(self, value: str) -> bool:
        return self.validate(value)

# Using functions as validators
def email_validator(value: str) -> bool:
    return "@" in value and "." in value

def length_validator(min_length: int) -> Callable[[str], bool]:
    def validate(value: str) -> bool:
        return len(value) >= min_length
    return validate
```

## Important Notes

1. **Callable Characteristics**:
   - Represents any callable object (functions, methods, lambdas, classes)
   - First bracket contains argument types in order
   - Second element is the return type
   - Empty first bracket `Callable[[], ReturnType]` represents no arguments
   - `Callable[..., ReturnType]` represents any argument list with specified return type
   - Can be used with `TypeVar` for generic callbacks

2. **Type Hint Evolution**:
   - Python 3.5+: Basic `Callable` type hint
   - Python 3.9+: Can be used in built-in collection types (e.g., `list[Callable[[int], str]]`)
   - Python 3.10+: Can be used in union types with `|` operator
   - Python 3.10+: `ParamSpec` and `Concatenate` for more advanced callable typing

3. **Best Practices**:
   - Use `Callable[[Arg1, Arg2], Return]` for specific function signatures
   - Use `Callable[..., Return]` when only the return type matters
   - For callbacks that modify state but don't return values, use `Callable[[Args], None]`
   - Consider using `Protocol` for more complex callable behaviors
   - Use `TypeVar` for generic function types

4. **Related Types**:
   - `Protocol`: For more complex callable interfaces
   - `ParamSpec`: For preserving parameter types in higher-order functions (Python 3.10+)
   - `Concatenate`: For adding parameters to existing callable types (Python 3.10+)
   - `collections.abc.Callable`: Runtime checkable version (Python 3.9+)


[Back to Index](../../README.md)

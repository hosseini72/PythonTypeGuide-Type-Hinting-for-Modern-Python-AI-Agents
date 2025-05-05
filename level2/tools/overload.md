# Overload Type Hints in Python

## Overview
The `@overload` decorator in Python is used to specify multiple type signatures for a single function. This enables static type checkers to choose the correct return type based on the argument types provided. While Python doesn't support function overloading at runtime, `@overload` provides a mechanism for static type checkers to understand functions that behave differently depending on their input types.

## Basic Usage

### Simple Overload Type Hints
```python
from typing import overload, Union, List

# Basic overload type hints
@overload
def process(value: int) -> int: ...

@overload
def process(value: str) -> str: ...

# Implementation (not annotated with @overload)
def process(value: Union[int, str]) -> Union[int, str]:
    if isinstance(value, int):
        return value * 2
    elif isinstance(value, str):
        return value.upper()
    raise TypeError("Expected int or str")

# Type checker understands these correctly
result1: int = process(42)  # Type checker knows result is int
result2: str = process("hello")  # Type checker knows result is str
```

### Overload with Multiple Parameters
```python
from typing import overload, List, Dict, Optional

@overload
def fetch_data(id: int) -> Dict[str, str]: ...

@overload
def fetch_data(ids: List[int]) -> List[Dict[str, str]]: ...

@overload
def fetch_data(id: None = None) -> List[Dict[str, str]]: ...

# Actual implementation
def fetch_data(id: Optional[Union[int, List[int]]] = None) -> Union[Dict[str, str], List[Dict[str, str]]]:
    if id is None:
        # Return all records
        return [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}]
    elif isinstance(id, int):
        # Return single record
        return {"id": str(id), "name": f"Item {id}"}
    else:
        # Return multiple specific records
        return [{"id": str(i), "name": f"Item {i}"} for i in id]
```

## Common Use Cases

### Polymorphic Functions
```python
from typing import overload, Union, List, Tuple

@overload
def join_items(items: List[str], separator: str = " ") -> str: ...

@overload
def join_items(items: Tuple[str, ...], separator: str = " ") -> str: ...

def join_items(items: Union[List[str], Tuple[str, ...]], separator: str = " ") -> str:
    return separator.join(items)

# Type checker understands return type
result1 = join_items(["a", "b", "c"], "-")  # Type: str
result2 = join_items(("a", "b", "c"))       # Type: str
```

### Factory Functions
```python
from typing import overload, Type, TypeVar, Dict, Any

T = TypeVar('T')
U = TypeVar('U')

class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

@overload
def create_object(obj_type: Type[User], data: Dict[str, Any]) -> User: ...

@overload
def create_object(obj_type: Type[Product], data: Dict[str, Any]) -> Product: ...

@overload
def create_object(obj_type: Type[T], data: Dict[str, Any]) -> T: ...

def create_object(obj_type, data):
    return obj_type(**data)

# Type checker knows the correct return type
user = create_object(User, {"name": "John", "age": 30})  # Type: User
product = create_object(Product, {"name": "Laptop", "price": 999.99})  # Type: Product
```

## Important Notes

1. **Overload Characteristics**:
   - Only affects static type checking, not runtime behavior
   - Requires all overloaded signatures to be annotated with `@overload`
   - Requires an actual implementation function (without `@overload`)
   - Implementation function typically uses `Union` types for parameters and return type
   - Overload signatures end with `...` (ellipsis)
   - Must be imported from the `typing` module

2. **Type Hint Evolution**:
   - Python 3.5+: `@overload` introduced
   - Python 3.8+: Improved overload capabilities and checking in tools like mypy
   - Python 3.9+: Compatible with built-in collection types (e.g., `list[int]`)
   - Python 3.10+: Compatible with union types using the `|` operator

3. **Best Practices**:
   - Use when a function can accept multiple distinct types and return different types
   - List the most specific overloads first, followed by more general ones
   - Make sure implementation function covers all overloaded cases
   - Use for "either-or" scenarios rather than optional parameters
   - Document each overload signature if behaviors differ significantly
   - The implementation function should handle all cases defined in the overloads

4. **Related Types**:
   - `Union`: Alternative for simpler cases where return type doesn't depend on input type
   - `TypeVar`: Used for generic functions where type relationships need to be preserved
   - `@singledispatch`: For runtime function dispatching based on argument type
   - `Protocol`: For defining interfaces based on behavior rather than inheritance
# TypeGuard Type Hints in Python

## Overview
TypeGuard type hints in Python are used to create user-defined type narrowing functions. Introduced in Python 3.10, TypeGuard allows for custom type checking functions that narrow down the type of a variable within a conditional scope. This is particularly useful when you need to perform runtime type checking and want the type checker to understand that a condition narrows down the type of a variable.

## Basic Usage

### Simple TypeGuard Type Hints
```python
from typing import TypeGuard, List, Any

# Basic TypeGuard type hint
def is_string_list(val: List[Any]) -> TypeGuard[List[str]]:
    return all(isinstance(x, str) for x in val)

# Using TypeGuard in code
def process_strings(values: List[Any]) -> None:
    if is_string_list(values):
        # Here, type checker knows values is List[str]
        for s in values:
            print(s.upper())  # Safe to call string methods

# TypeGuard in a function parameter
def handle_data(type_checker: Callable[[Any], TypeGuard[List[int]]], data: Any) -> None:
    if type_checker(data):
        # Here, type checker knows data is List[int]
        total = sum(data)  # Safe to use as integers
```

### TypeGuard for Custom Types
```python
from typing import TypeGuard, Dict, Any, Union

class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

def is_user(obj: Any) -> TypeGuard[User]:
    return isinstance(obj, User)

def is_user_dict(obj: Dict[str, Any]) -> TypeGuard[Dict[str, Union[str, int]]]:
    return (
        isinstance(obj, dict) and
        "name" in obj and isinstance(obj["name"], str) and
        "age" in obj and isinstance(obj["age"], int)
    )

# Using TypeGuard
def process_user(data: Any) -> None:
    if is_user(data):
        # Type checker knows data is User here
        print(f"User: {data.name}, Age: {data.age}")
    elif is_user_dict(data):
        # Type checker knows data is a dict with name and age
        print(f"User: {data['name']}, Age: {data['age']}")
```

## Common Use Cases

### Type Narrowing in Collections
```python
from typing import TypeGuard, List, Any, Union, Dict

def is_int_list(val: List[Any]) -> TypeGuard[List[int]]:
    return all(isinstance(x, int) for x in val)

def is_str_dict(val: Dict[Any, Any]) -> TypeGuard[Dict[str, str]]:
    return (
        all(isinstance(k, str) for k in val.keys()) and
        all(isinstance(v, str) for v in val.values())
    )

def sum_if_ints(data: List[Any]) -> int:
    if is_int_list(data):
        # Safe to sum as we've narrowed the type
        return sum(data)
    return 0

def join_if_str_dict(data: Dict[Any, Any]) -> str:
    if is_str_dict(data):
        # Safe to join as we've narrowed the type
        return ", ".join(f"{k}={v}" for k, v in data.items())
    return ""
```

### Complex Type Validation
```python
from typing import TypeGuard, Dict, Any, List, Union

# Complex JSON structure validation
JsonPrimitive = Union[str, int, float, bool, None]
JsonValue = Union[JsonPrimitive, List['JsonValue'], Dict[str, 'JsonValue']]

def is_json_object(obj: Any) -> TypeGuard[Dict[str, JsonValue]]:
    if not isinstance(obj, dict):
        return False
    
    return all(
        isinstance(k, str) and is_json_value(v)
        for k, v in obj.items()
    )

def is_json_array(obj: Any) -> TypeGuard[List[JsonValue]]:
    if not isinstance(obj, list):
        return False
    
    return all(is_json_value(v) for v in obj)

def is_json_primitive(obj: Any) -> TypeGuard[JsonPrimitive]:
    return obj is None or isinstance(obj, (str, int, float, bool))

def is_json_value(obj: Any) -> TypeGuard[JsonValue]:
    return (
        is_json_primitive(obj) or
        is_json_array(obj) or
        is_json_object(obj)
    )

# Using the type guards
def process_json(data: Any) -> None:
    if is_json_value(data):
        # Type checker knows data is a valid JSON value
        print("Valid JSON")
    else:
        print("Invalid JSON")
```

## Important Notes

1. **TypeGuard Characteristics**:
   - Introduced in Python 3.10
   - Used for custom type narrowing functions
   - Return value is `TypeGuard[SomeType]` not the actual boolean
   - Function implementation should return a boolean
   - Helps static type checkers understand dynamic type checks
   - Only narrows the type of a specific variable used in the check

2. **Type Hint Evolution**:
   - Python 3.10+: Introduction of `TypeGuard`
   - Before `TypeGuard`, similar functionality was approximated with `cast()`
   - Works well with `Union` types for conditional branching

3. **Best Practices**:
   - Use for runtime type checking when static typing isn't sufficient
   - Keep implementation strictly about type checking (avoid side effects)
   - Return `TypeGuard[T]` only when you've verified the object is truly of type T
   - TypeGuard functions should be pure (same input = same output)
   - Use descriptive function names that indicate what type is being guarded

4. **Related Types**:
   - `isinstance()` and `issubclass()`: Built-in type checking functions
   - `Union`: For types that could be one of several possibilities
   - `cast()`: For telling the type checker about a type without checking
   - `Protocol`: For structural subtyping
   - `Any`: The dynamic type that TypeGuard helps to narrow
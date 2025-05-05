# Callable Type Hint in Python

## Syntax (All Python Versions)
```python
from typing import Callable, List

# Function that takes two ints and returns a string
handler: Callable[[int, int], str] = lambda x, y: str(x + y)

# Function that takes no arguments and returns a float
generator: Callable[[], float] = lambda: 3.14

# Function with any number of arguments returning a boolean
validator: Callable[..., bool] = lambda *args: len(args) > 0
```

In Python, Callable is a type hint used to annotate variables, arguments, or return values that are expected to be callable objects (functions, methods, or classes). The syntax is Callable[[arg1_type, arg2_type, ...], return_type] where the first element is a list of argument types and the second element is the return type.

## When to Use Callable

### Function Parameters That Accept Functions
```python
from typing import Callable, List

# Higher-order function that applies a function to each element
def map_values(values: List[int], mapper: Callable[[int], str]) -> List[str]:
    return [mapper(x) for x in values]

# Use with a lambda
results = map_values([1, 2, 3], lambda x: f"Value: {x}")

# Use with a regular function
def format_number(num: int) -> str:
    return f"Number #{num}"

results = map_values([1, 2, 3], format_number)
```

### Callback Functions
```python
from typing import Callable

# Event handler with callback
def register_callback(event_name: str, 
                     callback: Callable[[str, dict], None]) -> None:
    # Register the callback to be called when event occurs
    pass

# Usage
def on_user_login(user_id: str, user_data: dict) -> None:
    print(f"User {user_id} logged in")

register_callback("login", on_user_login)
```

### Function Factories
```python
from typing import Callable, TypeVar

T = TypeVar('T')
U = TypeVar('U')

# A function that returns another function
def create_processor(prefix: str) -> Callable[[T], U]:
    def process(value: T) -> U:
        # Process the value with the prefix
        return f"{prefix}: {value}"  # type: ignore
    
    return process

# Usage
string_processor = create_processor("STRING")
result = string_processor("hello")  # Returns "STRING: hello"
```

### Variable Arguments with Callable
For functions with complex signatures, you can use ellipsis (...) to represent any number of arguments:
```python
from typing import Callable, Any

# A function that takes any arguments and returns any value
processor: Callable[..., Any] = lambda *args, **kwargs: sum(args)

# More specific: a function taking any args but returning string
formatter: Callable[..., str] = lambda *args: ", ".join(str(arg) for arg in args)
```

### Type Variables with Callable
You can use type variables to create generic callable types:
```python
from typing import Callable, TypeVar, List

T = TypeVar('T')
U = TypeVar('U')

# A function that transforms a list of one type to another type
def transform_list(items: List[T], transformer: Callable[[T], U]) -> List[U]:
    return [transformer(item) for item in items]

# Usage
numbers = [1, 2, 3]
strings = transform_list(numbers, lambda x: str(x))  # List of strings
doubles = transform_list(numbers, lambda x: x * 2)   # List of integers
```

## Best Practices for Using Callable
Be specific about argument types: Whenever possible, specify the exact argument types rather than using ....

Consider Protocol for complex signatures: For functions with complex signatures (optional arguments, keyword arguments), consider using Protocol instead.

Use type variables for generic functions: When the function operates on generic types, combine Callable with type variables.

Document expected behavior: Since the type hint only specifies the signature, add docstrings to explain the expected behavior of the callable.

Type check your functions: Ensure that functions you pass actually match the expected signature.

```python
from typing import Callable, List, TypeVar

T = TypeVar('T')

def apply_to_each(items: List[T], func: Callable[[T], str]) -> List[str]:
    """
    Apply the given function to each item in the list.
    
    Args:
        items: A list of items of any type T
        func: A function that converts an item of type T to a string
              The function must not modify the original item.
    
    Returns:
        A list of strings resulting from applying func to each item
    """
    return [func(item) for item in items]
```

The Callable type hint is essential for typing higher-order functions and callback patterns, enabling type checkers to verify that functions are used with correct argument and return types.


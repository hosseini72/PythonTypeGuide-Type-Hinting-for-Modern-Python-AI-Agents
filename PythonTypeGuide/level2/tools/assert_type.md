# assert_type in Python

## Basic Usage

### Python 3.11+ (Current)
```python
from typing import assert_type

# Basic usage with simple types
x = "hello"
assert_type(x, str)  # Passes type checking

# With more complex types
numbers = [1, 2, 3]
assert_type(numbers, list[int])  # Passes type checking
```

### With Generic Types
```python
from typing import assert_type, TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

container = Container(42)
assert_type(container, Container[int])  # Passes type checking
assert_type(container.value, int)       # Passes type checking
```

## Common Use Cases

### Verifying Type Inference
```python
from typing import assert_type

# Verify type inference in complex expressions
result = [x * 2 for x in [1, 2, 3]]
assert_type(result, list[int])  # Confirms result is list[int]

# Verify function return types
def get_user_id() -> int:
    return 42

user_id = get_user_id()
assert_type(user_id, int)  # Validates return type
```

## Important Notes

1. **assert_type Characteristics**:
   - Development-time checking tool only
   - No runtime effect (becomes a no-op in runtime code)
   - Only useful with static type checkers like mypy or pyright
   - Helps verify type checker is inferring expected types

2. **Type Hint Evolution**:
   - Python 3.11+: Introduced in the typing module
   - Requires a type checker to be useful

3. **Best Practices**:
   - Use during development to validate type checker behavior
   - Useful for complex or non-obvious type inference cases
   - Can serve as documentation of expected types
   - Remove in production code if desired

4. **Future Learning**
   As you become more familiar with type hints, you'll learn how to use assert_type with more complex typing constructs like Unions, TypeVars, and conditional types.
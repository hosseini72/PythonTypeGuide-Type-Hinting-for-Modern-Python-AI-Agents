# assert_never in Python

## Basic Usage

### Python 3.11+ (Current)
```python
from typing import assert_never, Union, Literal

# With Union types to ensure exhaustive handling
def process_shape(shape: Union[Literal["circle"], Literal["square"]]) -> str:
    if shape == "circle":
        return "Processing circle"
    elif shape == "square":
        return "Processing square"
    else:
        assert_never(shape)  # Type checker will ensure all cases are handled
```

### With Enums
```python
from typing import assert_never
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

def describe_color(color: Color) -> str:
    if color is Color.RED:
        return "Vibrant red"
    elif color is Color.GREEN:
        return "Fresh green"
    elif color is Color.BLUE:
        return "Deep blue"
    else:
        assert_never(color)  # Type checker will catch if new enum values are added
```

## Common Use Cases

### Exhaustiveness Checking
```python
from typing import assert_never, Union

# Ensure all cases in a union are handled
def get_type_name(value: Union[str, int, float, list]) -> str:
    if isinstance(value, str):
        return "string"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, list):
        return "list"
    else:
        assert_never(value)  # Type checker will catch if Union changes
```

## Important Notes

1. **assert_never Characteristics**:
   - Ensures exhaustive handling of all possible types
   - Takes a value that should have type 'Never' (impossible type)
   - Raises an exception at runtime if actually called
   - Most useful with type checkers to enforce exhaustiveness

2. **Type Hint Evolution**:
   - Python 3.11+: Introduced in the typing module
   - Requires a type checker to provide full benefits

3. **Best Practices**:
   - Use in exhaustive pattern matching scenarios
   - Helps maintain code when adding new variants to unions or enums
   - Serves as both type checking aid and runtime safeguard
   - Particularly useful with discriminated unions

4. **Future Learning**
   As you become more familiar with type hints, you'll see how assert_never combines with pattern matching (Python 3.10+) to create powerful and type-safe code that handles all possible cases.
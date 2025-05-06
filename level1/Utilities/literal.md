# Literal Type Hint in Python

## Syntax (Python 3.8+)
```python
from typing import Literal
# Variable that can only be specific literal values
status_code: Literal[200, 404, 500] = 200
status_code = 404  # No type error
status_code = 500  # No type error
status_code = 403  # Type error! Only 200, 404, or 500 allowed

# Function that accepts only specific literal values
def process_http_status(code: Literal[200, 404, 500]) -> str:
    if code == 200:
        return "OK"
    elif code == 404:
        return "Not Found"
    else:  # code == 500
        return "Server Error"
```

For Python 3.7 and below, you need to install and import from typing_extensions:
```python
from typing_extensions import Literal

# Same usage as above
status: Literal["on", "off"] = "on"
```

In Python, Literal is a type hint that restricts a value to one of a specific set of literal values. It allows you to be extremely precise about what values are allowed in a particular context.

## When to Use Literal

### Enum-like Constants Without Creating Enums
```python
from typing import Literal

# Instead of creating an enum for simple cases
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def log(message: str, level: LogLevel) -> None:
    print(f"[{level}] {message}")

log("System starting", "INFO")     # Valid
log("Error occurred", "ERROR")     # Valid
log("Unknown problem", "PROBLEM")  # Type error! Not a valid log level
```

### Function Parameters with Fixed Options
```python
from typing import Literal

# HTTP methods are a fixed set of strings
def make_request(url: str, method: Literal["GET", "POST", "PUT", "DELETE"]) -> None:
    # Implementation
    pass

make_request("https://api.example.com", "GET")    # Valid
make_request("https://api.example.com", "PATCH")  # Type error! PATCH not in allowed values
```

### Return Values with Specific Meanings
```python
from typing import Literal

# Function that returns specific status codes
def check_availability(resource: str) -> Literal[0, 1, -1]:
    """
    Check if a resource is available.
    Returns:
        0: Resource is available
        1: Resource exists but is locked
        -1: Resource doesn't exist
    """
    # Implementation...
    return 0

status = check_availability("data.txt")
if status == 0:
    # Resource is available
    pass
```

## Combining Literal with Other Types
You can combine Literal with other type hints using Union:
```python
from typing import Literal, Union

# A result that can be either successful with a value, or a specific error code
Result = Union[str, Literal["NOT_FOUND", "PERMISSION_DENIED"]]

def get_resource(name: str) -> Result:
    if not resource_exists(name):
        return "NOT_FOUND"
    elif not has_permission(name):
        return "PERMISSION_DENIED"
    else:
        return f"Content of {name}"
```

## Literal with Boolean and Numeric Types
Literal works with any literal value, not just strings:
```python
from typing import Literal

# Boolean literals
def set_feature(name: str, enabled: Literal[True]) -> None:
    """Enable a feature (cannot be used to disable)."""
    # Implementation that only allows enabling features
    pass

# Numeric literals
def allocate_resources(cpu_count: Literal[1, 2, 4, 8]) -> None:
    """Allocate resources with specific CPU counts only."""
    # Implementation that only works with specific CPU counts
    pass
```

## Literal vs Enum
While Enum provides similar functionality for restricting values, Literal is simpler for cases when you just need to restrict to specific literal values:
```python
from enum import Enum
from typing import Literal

# Using Enum
class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

def process_color_enum(color: Color) -> None:
    pass

# Using Literal
ColorLiteral = Literal["red", "green", "blue"]

def process_color_literal(color: ColorLiteral) -> None:
    pass

# Enum requires creating the instance
process_color_enum(Color.RED)

# Literal uses the direct values
process_color_literal("red")
```

## Best Practices for Using Literal
Use for small, fixed sets of values: Literal is ideal when you have a small number of specific values that are meaningful in your program.

Consider Enum for complex cases: If you need additional behavior beyond just type checking, or if the set of values is large, consider using Enum instead.

Document the meaning of literals: Add comments or docstrings explaining what each literal value represents, especially for numeric literals.

Use for precise API contracts: Literal helps create very precise API contracts about exactly what values are accepted or returned.

Combine with Union for flexibility: Use Union[Literal[...], Literal[...]] or Union[Literal[...], OtherType] when you need more complex type specifications.

```python
from typing import Literal, Union

# Response can be a specific error code or a dictionary of results
Response = Union[Literal["TIMEOUT", "SERVER_ERROR"], dict]

def fetch_data() -> Response:
    # Implementation
    if timeout_occurred():
        return "TIMEOUT"
    elif server_error_occurred():
        return "SERVER_ERROR"
    else:
        return {"status": "success", "data": [...]}
```

The Literal type hint is a powerful tool for making your type annotations more precise and expressive, particularly when dealing with a fixed set of possible values for a variable, parameter, or return value.


[Back to Index](../../README.md)

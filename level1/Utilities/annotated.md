# Annotated Type Hint in Python

## Syntax (Python 3.9+)
```python
from typing import Annotated

# Basic usage with a simple string annotation
user_id: Annotated[int, "User ID must be positive"] = 123

# Multiple metadata annotations
coordinate: Annotated[float, "Range: 0-100", "Represents percentage"] = 75.5

# Function parameters with annotations
def process_payment(
    amount: Annotated[float, "Must be positive"],
    currency: Annotated[str, "3-letter ISO currency code"]
) -> None:
    pass
```

For Python 3.7-3.8, you need to use typing_extensions:
```python
from typing_extensions import Annotated

# Same usage as above
value: Annotated[int, "Required metadata"] = 42
```

In Python, Annotated is a special type hint that wraps another type and adds metadata annotations without affecting the runtime type. It allows you to attach additional information to type hints that can be used by third-party tools, libraries, and frameworks.

## When to Use Annotated

### Additional Validation Requirements
```python
from typing import Annotated
from pydantic import Field  # Third-party validation library

# Using Annotated with Pydantic for validation
UserID = Annotated[int, Field(gt=0, lt=1000)]
Username = Annotated[str, Field(min_length=3, max_length=20)]

def create_user(user_id: UserID, username: Username) -> None:
    # Implementation
    pass

# A type checker still sees these as int and str
# But Pydantic can use the metadata for validation
```

### Documentation in Type Hints
```python
from typing import Annotated, List

# Adding documentation to complex types
Matrix = Annotated[List[List[float]], "2D matrix of floating point values"]

def calculate_determinant(matrix: Matrix) -> float:
    # Implementation
    return 0.0

# The type is still List[List[float]], but with added documentation
```

### Framework-Specific Metadata
```python
from typing import Annotated
from fastapi import Path, Query  # Third-party framework

# FastAPI uses Annotated for parameter metadata
def get_item(
    item_id: Annotated[int, Path(title="Item ID", ge=1)],
    q: Annotated[str, Query(max_length=50)] = None
):
    # Implementation
    return {"item_id": item_id, "q": q}
```

### Multiple Metadata Annotations
Annotated can include multiple metadata objects:
```python
from typing import Annotated
from dataclasses import dataclass

# Custom metadata classes
@dataclass
class Size:
    min_value: int
    max_value: int

@dataclass
class DatabaseInfo:
    column_name: str
    nullable: bool

# Usage with multiple metadata items
UserId = Annotated[int, 
                  Size(min_value=1, max_value=1000),
                  DatabaseInfo(column_name="user_id", nullable=False),
                  "Primary key for the users table"]

def process_user(user_id: UserId) -> None:
    # The type is still int, but with three metadata items
    pass
```

### Retrieving Annotations
You can retrieve annotations using the get_type_hints function with the include_extras parameter:
```python
from typing import Annotated, get_type_hints

def process_value(value: Annotated[int, "Must be positive"]) -> None:
    pass

# Get the annotations with metadata
hints = get_type_hints(process_value, include_extras=True)
# hints = {'value': typing.Annotated[int, 'Must be positive']}

# Get just the underlying types
simple_hints = get_type_hints(process_value)
# simple_hints = {'value': int}
```

### Combining Annotated with Other Type Hints
Annotated can be combined with any other type hint:
```python
from typing import Annotated, List, Optional, Union

# Complex type with annotation
OptionalIDs = Annotated[Optional[List[int]], "List of optional user IDs"]

# Union with annotation
Result = Annotated[Union[str, int], "Success (str) or error code (int)"]

# Nested Annotated (though this can get confusing)
PositiveInt = Annotated[int, "Must be positive"]
UserID = Annotated[PositiveInt, "User identifier"]
```

## Best Practices for Using Annotated
Use for framework integration: Annotated is particularly useful when integrating with frameworks that need additional metadata beyond the type.

Keep runtime-relevant validation separate: While you can use Annotated for validation hints, remember that it doesn't enforce anything at runtime by itself.

Don't overuse: Only add metadata that will actually be used by tools or is critical for documentation.

Be consistent: If you use Annotated for one parameter in a function, consider using it for all parameters that need similar metadata.

Document metadata expectations: If you're creating a framework that processes annotations, document what metadata you expect and in what format.

```python
from typing import Annotated, Any, Dict

# Clear documentation of expected metadata
def register_endpoint(
    path: str,
    handler: Annotated[
        callable,
        "Must accept request object and return dict or None"
    ],
    metadata: Annotated[
        Dict[str, Any],
        "Optional endpoint configuration"
    ] = None
) -> None:
    """
    Register an API endpoint.
    
    The handler function must accept a request object and return a dict or None.
    Metadata can include: authentication, rate_limit, cache_ttl.
    """
    # Implementation
    pass
```

The Annotated type hint is a powerful way to extend Python's type system with additional metadata that can be used by tools, frameworks, and documentation generators without affecting the runtime behavior of your code.


[Back to Index](../../README.md)

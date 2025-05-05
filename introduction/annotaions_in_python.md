# Annotations in Python

Writing annotations and mentioning types of variables in Python is quite straightforward. It just needs a colon (:) followed by the type. As any function or method has a return value (even if it's None), it should be mentioned after -> (dash followed by greater-than sign).

## Basic Syntax

```python
def function(arg1: str, arg2: int) -> str:
    return f"{arg1} {arg2}"

class MyClass:
    class_var_1: str
    class_var_2: int
```

## Type Aliases

Before we dive deeper into the taxonomy of types in Python, it's better we get familiar with type aliases.

Type aliases allow us to create alternative names for existing types, which can improve code readability and maintainability. For example:

```python
Name = str
Age = int
Result = str

def function(arg1: Name, arg2: Age) -> Result:
    return f"{arg1} is {arg2} years old"
```

This kind of annotation may make the code more clear, especially in domain-specific applications, but it adds some overhead in reviewing the code as developers need to track these aliases.

## Variable Annotations

Python 3.6 introduced variable annotations (PEP 526), allowing us to annotate variables directly:

```python
name: str = "John"
age: int = 30
is_active: bool = True

# Even without initialization:
user_id: int  # To be assigned later
```

## Benefits of Type Aliases

Type aliases become particularly powerful when working with complex types:

```python
from typing import Dict, List, Tuple

# Without type aliases
def process_user_data(users: Dict[str, Tuple[str, int, List[str]]]) -> List[str]:
    pass

# With type aliases
UserId = str
Name = str
Age = int
Interests = List[str]
UserInfo = Tuple[Name, Age, Interests]
UserDatabase = Dict[UserId, UserInfo]
UserNames = List[str]

def process_user_data(users: UserDatabase) -> UserNames:
    pass
```

The second version with aliases is much clearer about what each component represents, making the code more self-documenting.

## Self-Documenting Code

Self-documenting code refers to code that inherently communicates its purpose, behavior, and expectations to developers without requiring extensive additional documentation. When code is self-documenting, its functionality becomes evident through clear naming and structure, reducing the need for separate documentation and making implicit assumptions explicit.

Type hints excel at creating self-documenting code by:
- Clarifying function signatures
- Making complex data structures more readable
- Setting clear expectations for interfaces
- Eliminating the guesswork typically required to understand valid inputs

This means developers can understand how to use functions and methods correctly simply by reading their signatures, without having to dive into implementation details or rely on external documentation. The type information serves as built-in documentation that remains synchronized with the code itself, making the entire codebase more accessible and maintainable.

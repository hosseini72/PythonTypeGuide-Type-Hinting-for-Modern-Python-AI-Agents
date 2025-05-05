# ClassVar Type Hint in Python

## Syntax (All Python Versions)
```python
from typing import ClassVar

class Counter:
    # Class variable (shared among all instances)
    count: ClassVar[int] = 0
  
    def __init__(self, value: int = 0):
        self.value = value
        Counter.count += 1
```

In Python, ClassVar is a special type hint that indicates a variable is intended to be a class variable rather than an instance variable. It helps distinguish between variables that belong to the class itself versus those that belong to instances of the class. ClassVar is used exclusively within class definitions.

## When to Use ClassVar

### Documenting Class Variables
```python
from typing import ClassVar, Dict, List

class User:
    # Class variables - shared across all instances
    _registry: ClassVar[Dict[int, "User"]] = {}
    active_count: ClassVar[int] = 0
    
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        User._registry[user_id] = self
        User.active_count += 1
```

### Class-level Constants
```python
from typing import ClassVar, List

class HttpStatusCodes:
    # Class constants (although Final might be more appropriate here)
    OK: ClassVar[int] = 200
    NOT_FOUND: ClassVar[int] = 404
    SERVER_ERROR: ClassVar[int] = 500
    
    # List of all defined status codes
    ALL_CODES: ClassVar[List[int]] = [200, 404, 500]
```

### Cached Class Properties
```python
from typing import ClassVar, Dict, Type
import weakref

class Service:
    # Class-level cache of instantiated services
    _instances: ClassVar[Dict[str, "Service"]] = {}
    
    # Instance attributes
    name: str
    
    def __init__(self, name: str):
        self.name = name
    
    @classmethod
    def get_instance(cls: Type["Service"], name: str) -> "Service":
        if name not in cls._instances:
            cls._instances[name] = cls(name)
        return cls._instances[name]
```

### ClassVar in Dataclasses
ClassVar is particularly useful with dataclasses to exclude class variables from the generated __init__ method:
```python
from dataclasses import dataclass
from typing import ClassVar, List

@dataclass
class Product:
    # Class variables - not included in __init__
    catalog: ClassVar[List["Product"]] = []
    next_id: ClassVar[int] = 1
    
    # Instance variables - included in __init__
    name: str
    price: float
    product_id: int = 0
    
    def __post_init__(self):
        if self.product_id == 0:
            self.product_id = Product.next_id
            Product.next_id += 1
        Product.catalog.append(self)
```

### ClassVar vs Regular Class Variables
While ClassVar doesn't change runtime behavior, it provides clarity and enables type checking:
```python
from typing import ClassVar

class WithoutClassVar:
    count = 0  # Class variable by convention
    
    def __init__(self):
        self.count += 1  # Oops! Creates an instance variable shadowing the class variable

class WithClassVar:
    count: ClassVar[int] = 0  # Clearly marked as class variable
    
    def __init__(self):
        self.count += 1  # Type error! Cannot create instance variable with same name
```

## Best Practices for Using ClassVar
Use for true class variables: Only use ClassVar for variables that are genuinely shared across all instances.

Be explicit about types: Always specify the type parameter, e.g., ClassVar[int] rather than just ClassVar.

Combine with Final when appropriate: For class constants, consider using Final[ClassVar[type]] to indicate they shouldn't be reassigned.

Use in dataclasses: ClassVar is particularly useful in dataclasses to exclude variables from __init__.

Document the purpose: Explain why a variable is class-level, especially for counters, registries, or caches.

```python
from typing import ClassVar, Dict, Final
from dataclasses import dataclass

@dataclass
class ConfigurationManager:
    # Class constants that should never change
    DEFAULT_TIMEOUT: Final[ClassVar[int]] = 30
    
    # Class-level registry
    _configs: ClassVar[Dict[str, "ConfigurationManager"]] = {}
    
    # Instance variables
    name: str
    settings: Dict[str, str]
    
    def __post_init__(self):
        # Register this instance
        ConfigurationManager._configs[self.name] = self
```

The ClassVar type hint is a useful tool for clearly documenting class variables and preventing common mistakes where instance variables unintentionally shadow class variables. While it doesn't change runtime behavior, it provides valuable information to both developers and type checkers.



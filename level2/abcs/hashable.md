# Hashable Type Hint in Python

## Syntax (All Python Versions)
```python
from typing import Hashable, Dict, Set

# Integer as a hashable type
key1: Hashable = 42

# String as a hashable type
key2: Hashable = "username"

# Tuple of hashable items (immutable)
key3: Hashable = (1, "user", True)

# Dictionary using hashable keys
lookup: Dict[Hashable, str] = {
    42: "answer",
    "username": "admin",
    (1, "user", True): "composite key"
}
```

In Python, Hashable is a type hint used to annotate variables, arguments, or return values that are expected to be hashable objects—objects that have a hash value which doesn't change during their lifetime and can be compared to other objects. The syntax is simply Hashable without type parameters.

## When to Use Hashable

### Function Parameters That Require Hashable Objects
```python
from typing import Hashable, Set, Dict, Any

def add_to_set(items: Set[Hashable], new_item: Hashable) -> Set[Hashable]:
    """Add a hashable item to a set and return the updated set."""
    items.add(new_item)
    return items

# Usage with different hashable types
numbers = {1, 2, 3}
result1 = add_to_set(numbers, 4)         # {1, 2, 3, 4}
result2 = add_to_set(result1, "string")  # {1, 2, 3, 4, "string"}
result3 = add_to_set(result2, (1, 2))    # {1, 2, 3, 4, "string", (1, 2)}

# This would fail at runtime
# add_to_set(result3, [1, 2])  # TypeError: unhashable type: 'list'
```

### Dictionary and Set Key Types
```python
from typing import Dict, Set, Hashable, TypeVar, Any

T = TypeVar('T')

def create_lookup_table(keys: Set[Hashable], 
                       value_func: callable) -> Dict[Hashable, Any]:
    """Create a dictionary from hashable keys and a value function."""
    return {key: value_func(key) for key in keys}

# Usage
keys = {1, "user", (True, False)}
result = create_lookup_table(keys, lambda k: f"Value for {k}")
# Result: {1: "Value for 1", "user": "Value for user", (True, False): "Value for (True, False)"}
```

### Cache Keys
```python
from typing import Hashable, Dict, Any, TypeVar, Callable
from functools import lru_cache

K = TypeVar('K', bound=Hashable)
V = TypeVar('V')

# A simple cache implementation using Hashable keys
class SimpleCache(Dict[K, V]):
    def get_or_compute(self, key: K, compute_func: Callable[[K], V]) -> V:
        """Get value for key or compute it if not found."""
        if key not in self:
            self[key] = compute_func(key)
        return self[key]

# Usage
cache: SimpleCache[Hashable, int] = SimpleCache()
result1 = cache.get_or_compute("key1", lambda k: len(k) * 10)  # 40
result2 = cache.get_or_compute((1, 2, 3), lambda k: sum(k))    # 6
```

### Hashable and Function Caching
The Hashable type hint is especially useful for function caching, where keys need to be hashable:
```python
from typing import Hashable, TypeVar, Dict, Any, Tuple
from functools import lru_cache

T = TypeVar('T')

# Function that caches results using hashable arguments
@lru_cache(maxsize=100)
def expensive_computation(key: Hashable, factor: int = 1) -> float:
    """Perform an expensive computation with caching."""
    print(f"Computing for {key} with factor {factor}")
    if isinstance(key, str):
        return len(key) * factor
    elif isinstance(key, (int, float)):
        return key * factor
    elif isinstance(key, tuple):
        return sum(key) * factor
    return 0

# Usage with different hashable types
result1 = expensive_computation(42)         # Computes and caches
result2 = expensive_computation(42)         # Uses cached result
result3 = expensive_computation("hello")    # Computes and caches
result4 = expensive_computation((1, 2, 3))  # Computes and caches
```

### Making Custom Types Hashable
You can create custom types that satisfy the Hashable protocol by implementing the __hash__ and __eq__ methods:
```python
from typing import Hashable, Dict, Set, Any

class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
    
    def __hash__(self) -> int:
        """Return a hash based on immutable attributes."""
        return hash((self.user_id, self.username))
    
    def __eq__(self, other: Any) -> bool:
        """Define equality based on the same attributes used for hashing."""
        if not isinstance(other, User):
            return False
        return (self.user_id, self.username) == (other.user_id, other.username)

# Function that accepts hashable objects
def add_to_registry(registry: Set[Hashable], item: Hashable) -> None:
    """Add an item to a registry set."""
    registry.add(item)

# Usage with custom hashable type
users: Set[User] = set()
user1 = User(1, "alice")
user2 = User(2, "bob")
user3 = User(1, "alice")  # Same values as user1

add_to_registry(users, user1)
add_to_registry(users, user2)
add_to_registry(users, user3)  # Won't be added because it equals user1

print(len(users))  # 2 (user3 wasn't added because it's equal to user1)
```

### Limitations and Cautions with Hashable
Be cautious about which objects are truly hashable:
```python
from typing import Hashable, Dict, Any

def safely_use_as_key(value: Any) -> bool:
    """Determine if a value can be safely used as a dictionary key."""
    try:
        hash(value)
        return True
    except TypeError:
        return False

# Built-in immutable types
print(safely_use_as_key(42))       # True (int)
print(safely_use_as_key("hello"))  # True (str)
print(safely_use_as_key((1, 2)))   # True (tuple of hashable items)

# Mutable types
print(safely_use_as_key([1, 2]))   # False (list)
print(safely_use_as_key({1, 2}))   # False (set)
print(safely_use_as_key({"a": 1})) # False (dict)

# Tuple containing mutable items
print(safely_use_as_key((1, [2, 3])))  # False (tuple containing a list)
```

## Best Practices for Using Hashable
Use for dictionary and set keys: Use Hashable for parameters that will be used as keys in dictionaries or elements in sets.

Ensure both __hash__ and __eq__ are implemented: When creating custom hashable types, always implement both methods consistently.

Base hash on immutable attributes: Only use immutable attributes in the hash calculation to ensure hash values don't change.

Consider using a frozen dataclass: For simple data classes that need to be hashable, use @dataclasses.dataclass(frozen=True).

Be cautious with mutable attributes: If your class has mutable attributes, consider carefully whether it should be hashable at all.

```python
from typing import Hashable, Dict, Set
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePoint:
    """A hashable immutable point class."""
    x: int
    y: int
    # Being a frozen dataclass automatically makes this hashable

def process_unique_points(points: Set[ImmutablePoint]) -> Dict[ImmutablePoint, float]:
    """
    Process a set of unique points and return a mapping of points to values.
    
    Args:
        points: A set of hashable points
    
    Returns:
        A dictionary mapping each point to its distance from origin
    """
    return {
        point: (point.x ** 2 + point.y ** 2) ** 0.5
        for point in points
    }
```

The Hashable type hint is essential for functions that use objects as dictionary keys or set elements, enabling type checkers to verify that only hashable objects are used in contexts that require them. This helps catch potential runtime errors early in the development process.



[Back to Index](../../README.md)

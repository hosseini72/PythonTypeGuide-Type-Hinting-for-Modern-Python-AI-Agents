# NewType Type Hints in Python

## Overview
NewType in Python is used to create distinct types that are treated as separate from their base type by static type checkers, while remaining identical to the base type at runtime. This allows developers to create domain-specific types for improved type safety, preventing logical errors without incurring any runtime overhead. NewType is particularly useful for creating meaningful type distinctions for primitive types like strings and integers.

## Basic Usage

### Simple NewType Type Hints
```python
from typing import NewType

# Basic NewType definitions
UserId = NewType('UserId', int)
EmailAddress = NewType('EmailAddress', str)
PostalCode = NewType('PostalCode', str)

# Creating values of the new type
user_id: UserId = UserId(42)
email: EmailAddress = EmailAddress("user@example.com")
zip_code: PostalCode = PostalCode("90210")

# NewType in a function parameter
def get_user_data(user_id: UserId) -> dict:
    return {"id": user_id, "name": "John Doe"}

# NewType in a class attribute
class User:
    def __init__(self, id: UserId, email: EmailAddress) -> None:
        self.id: UserId = id
        self.email: EmailAddress = email
```

### NewType with Collections
```python
from typing import NewType, List, Dict

# NewType with collections
ProductId = NewType('ProductId', int)
Quantity = NewType('Quantity', int)

# Usage in collections
product_ids: List[ProductId] = [ProductId(1), ProductId(2), ProductId(3)]
inventory: Dict[ProductId, Quantity] = {
    ProductId(1): Quantity(10),
    ProductId(2): Quantity(5)
}
```

## Common Use Cases

### Domain-Specific Types
```python
from typing import NewType, Dict

# Money-related types
DollarsUSD = NewType('DollarsUSD', int)
EurosCent = NewType('EurosCent', int)

def convert_usd_to_eur(amount: DollarsUSD) -> EurosCent:
    # Conversion rate: 1 USD = 0.85 EUR
    return EurosCent(int(amount * 85))

# Prevents logical errors like this:
# regular_dollars = 100
# get_user_data(regular_dollars)  # Type error: expected UserId, got int

def process_payment(amount: DollarsUSD) -> None:
    print(f"Processing payment of ${amount/100:.2f}")

# These are different types to the type checker
price: DollarsUSD = DollarsUSD(500)  # $5.00
euro_amount: EurosCent = EurosCent(500)  # €5.00

# This would raise a type error during static checking
# process_payment(euro_amount)  # Error: Expected DollarsUSD, got EurosCent
```

### Type-Safe Identifiers
```python
from typing import NewType, Dict, List

# Different ID types
UserId = NewType('UserId', int)
GroupId = NewType('GroupId', int)
PostId = NewType('PostId', int)

# Database functions
def get_user(user_id: UserId) -> Dict[str, str]:
    # Fetch user from database
    return {"name": "Jane Doe"}

def get_group(group_id: GroupId) -> Dict[str, str]:
    # Fetch group from database
    return {"name": "Developers"}

def get_post(post_id: PostId) -> Dict[str, str]:
    # Fetch post from database
    return {"title": "Hello World"}

# Type safety in action
user_id = UserId(42)
group_id = GroupId(42)

# These are considered different types by the type checker
user = get_user(user_id)  # OK
# group = get_user(group_id)  # Type error: expected UserId, got GroupId

def get_user_groups(user_id: UserId) -> List[GroupId]:
    # Get groups for a user
    return [GroupId(1), GroupId(2)]
```

## Important Notes

1. **NewType Characteristics**:
   - Creates a separate type for static type checking
   - At runtime, the new type is identical to the original
   - No runtime overhead or performance impact
   - Cannot be subclassed or instantiated (use as a function instead)
   - Only works with a single underlying type (no generics)
   - New types made from the same base type are distinct from each other

2. **Type Hint Evolution**:
   - Python 3.5.2+: Introduction of `NewType`
   - Python 3.9+: Can be used in built-in collection types (e.g., `list[UserId]`)
   - Python 3.10+: Can be used in union types with `|` operator

3. **Best Practices**:
   - Use for creating domain-specific types from primitives
   - Use for distinguishing between semantically different identifiers
   - Name the types clearly to indicate their purpose
   - Don't use for complex validation (consider Pydantic or dataclasses)
   - Remember there's no runtime type checking with NewType
   - Consider using static type checkers like mypy to enforce type safety

4. **Related Types**:
   - `TypeVar`: For generic type parameters
   - `Literal`: For a finite set of allowed values
   - `Enum`: For enumerated values with runtime validation
   - `NamedTuple`: For structured data with named fields
   - `Protocol`: For structural subtyping



[Back to Index](../../README.md)

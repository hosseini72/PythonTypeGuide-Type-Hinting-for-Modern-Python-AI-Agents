# NamedTuple Type Hint in Python

## Syntax (All Python Versions)
```python
from typing import NamedTuple

# Class-based syntax
class Point(NamedTuple):
    x: float
    y: float
    label: str = ""  # Optional field with default value

# Usage
p = Point(1.0, 2.0, "Origin")
print(p.x, p.y, p.label)  # Access via attribute names
print(p[0], p[1], p[2])   # Access via indices (tuple-like)
```

Alternative function-style syntax (older style, but still works):
```python
from typing import NamedTuple

# Function-style syntax
Point = NamedTuple('Point', [
    ('x', float),
    ('y', float),
    ('label', str)
])
```

In Python, NamedTuple from the typing module is an enhanced version of collections.namedtuple that adds type annotations. It creates tuple-like immutable objects with named fields and type information. NamedTuple combines the memory efficiency and immutability of tuples with the readability of attribute access.

## When to Use NamedTuple

### Lightweight Data Objects
```python
from typing import NamedTuple, Optional

class User(NamedTuple):
    id: int
    name: str
    email: str
    active: bool = True
    department: Optional[str] = None

# Create instances
admin = User(1, "Admin", "admin@example.com")
guest = User(2, "Guest", "guest@example.com", False)
employee = User(3, "John Smith", "john@example.com", department="Engineering")

# Access attributes
print(f"User {admin.name} has email {admin.email}")

# Unpacking works like regular tuples
user_id, name, *rest = employee
```

### Return Values with Multiple Components
```python
from typing import NamedTuple, List

class StatisticsResult(NamedTuple):
    mean: float
    median: float
    std_dev: float
    min_value: float
    max_value: float

def calculate_statistics(data: List[float]) -> StatisticsResult:
    # Calculate various statistics...
    return StatisticsResult(
        mean=sum(data) / len(data),
        median=sorted(data)[len(data) // 2],
        std_dev=calculate_std_dev(data),
        min_value=min(data),
        max_value=max(data)
    )

# Usage
stats = calculate_statistics([1.0, 2.0, 3.0, 4.0, 5.0])
print(f"Mean: {stats.mean}, Median: {stats.median}")

# Selective unpacking
mean, median, *_ = stats
```

### Fixed Data Structures
```python
from typing import NamedTuple, List
from datetime import datetime

class LogEntry(NamedTuple):
    timestamp: datetime
    level: str
    message: str
    details: dict = {}

# Creating a log entry
entry = LogEntry(
    timestamp=datetime.now(),
    level="ERROR",
    message="Database connection failed"
)

# Log entries are immutable
try:
    entry.level = "WARNING"  # This will raise an AttributeError
except AttributeError:
    print("Cannot modify a NamedTuple!")
```

### NamedTuple Methods and Properties
NamedTuple inherits all tuple methods and adds some extras:
```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

p1 = Point(1.0, 2.0)

# Convert to dictionary
point_dict = p1._asdict()  # {'x': 1.0, 'y': 2.0}

# Create a new instance with updated values
p2 = p1._replace(y=3.0)  # Point(x=1.0, y=3.0)

# Field names and defaults
print(Point._fields)  # ('x', 'y')
print(Point._field_defaults)  # {} (no defaults in this example)
```

### NamedTuple with Inheritance and Methods
Unlike collections.namedtuple, typing NamedTuple supports adding methods and class variables:
```python
from typing import NamedTuple
import math

class Point(NamedTuple):
    x: float
    y: float
    
    # Class variable
    dimensions: int = 2
    
    # Instance method
    def distance_to_origin(self) -> float:
        """Calculate distance from the point to the origin."""
        return math.sqrt(self.x**2 + self.y**2)
    
    # Class method
    @classmethod
    def from_polar(cls, radius: float, angle_rad: float) -> 'Point':
        """Create a Point from polar coordinates."""
        return cls(
            x=radius * math.cos(angle_rad),
            y=radius * math.sin(angle_rad)
        )

# Using the methods
p1 = Point(3.0, 4.0)
print(p1.distance_to_origin())  # 5.0

# Using the class method
p2 = Point.from_polar(5.0, math.pi/4)
print(p2)  # Point(x≈3.54, y≈3.54)
```

### NamedTuple vs Dataclass vs TypedDict
Each serves different purposes:
```python
from typing import NamedTuple, TypedDict
from dataclasses import dataclass

# NamedTuple - immutable, tuple-like
class PointTuple(NamedTuple):
    x: float
    y: float

# Dataclass - mutable by default, class-like
@dataclass
class PointClass:
    x: float
    y: float

# TypedDict - dictionary with specific keys
class PointDict(TypedDict):
    x: float
    y: float

# Usage differences
pt = PointTuple(1.0, 2.0)
pc = PointClass(1.0, 2.0)
pd: PointDict = {"x": 1.0, "y": 2.0}

# Access differences
print(pt.x, pt[0])  # Both work for NamedTuple
print(pc.x)         # Only attribute access for dataclass
print(pd["x"])      # Only key access for TypedDict

# Mutability differences
# pt.x = 2.0        # Error! NamedTuples are immutable
pc.x = 2.0          # Works - dataclasses are mutable by default
pd["x"] = 2.0       # Works - dictionaries are mutable
```

## Best Practices for Using NamedTuple
Use for immutable data: Choose NamedTuple when data shouldn't change after creation.

Prefer for small records: NamedTuples are ideal for small data objects with a fixed set of fields.

Add helpful methods: Enhance NamedTuples with methods that operate on their data.

Document fields: Add clear type hints and docstrings to explain the purpose of each field.

Use default values: For optional fields, provide default values rather than using Optional when appropriate.

```python
from typing import NamedTuple, Optional
from datetime import datetime

class Transaction(NamedTuple):
    """Represents a financial transaction."""
    transaction_id: str
    amount: float
    timestamp: datetime
    description: str = ""
    category: Optional[str] = None
    
    def is_recent(self, within_days: int = 7) -> bool:
        """Check if the transaction occurred within the specified number of days."""
        time_delta = datetime.now() - self.timestamp
        return time_delta.days <= within_days
    
    def formatted_amount(self, currency: str = "$") -> str:
        """Return a formatted string representation of the amount."""
        return f"{currency}{abs(self.amount):.2f}"
```

The NamedTuple type hint provides a clean, efficient, and type-safe way to create lightweight immutable data objects in Python. It combines the benefits of tuples (immutability, efficiency) with those of classes (named attributes, methods) while adding strong typing for better code quality and IDE support.



[Back to Index](../../README.md)

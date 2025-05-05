# ContextManager Type Hint in Python

## Syntax (All Python Versions)
```python
from typing import ContextManager, List

# A context manager for a file
file_cm: ContextManager[file] = open('example.txt', 'r')

# A context manager that yields a string
string_cm: ContextManager[str] = open('example.txt', 'r')

# A context manager for a custom object
db_cm: ContextManager[Database] = connect_to_database()
```

In Python, ContextManager is a type hint used to annotate variables, arguments, or return values that are expected to work as context managers (objects that can be used with the with statement). The syntax is ContextManager[yield_type] where yield_type is the type yielded by the context manager when entering the with block.

## When to Use ContextManager

### Functions That Return Context Managers
```python
from typing import ContextManager, TextIO

def get_file_handler(filename: str) -> ContextManager[TextIO]:
    """Return a context manager that yields a file object."""
    return open(filename, 'r')

# Usage
with get_file_handler('data.txt') as file:
    content = file.read()
```

### Custom Context Managers
```python
from typing import ContextManager
from contextlib import contextmanager

@contextmanager
def temp_directory() -> ContextManager[str]:
    """Create a temporary directory and yield its path."""
    import tempfile
    import shutil
    
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)

# Usage
with temp_directory() as dir_path:
    print(f"Working in {dir_path}")
    # Files created here will be cleaned up after the block
```

### Resource Management
```python
from typing import ContextManager
from contextlib import contextmanager

class DatabaseConnection:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
    
    def execute(self, query: str) -> list:
        # Execute the query
        return []
    
    def close(self) -> None:
        # Close the connection
        pass

@contextmanager
def db_transaction(conn_string: str) -> ContextManager[DatabaseConnection]:
    """Create a database connection and handle transaction management."""
    connection = DatabaseConnection(conn_string)
    try:
        yield connection
        # Auto-commit at the end if no exceptions
    except Exception:
        # Auto-rollback on exceptions
        raise
    finally:
        connection.close()

# Usage
with db_transaction("postgresql://localhost/mydb") as conn:
    results = conn.execute("SELECT * FROM users")
```

### Creating Classes That Implement Context Managers
You can create classes that implement the context manager protocol by defining __enter__ and __exit__ methods:
```python
from typing import ContextManager, TypeVar, Generic

T = TypeVar('T')

class SimpleContextManager(Generic[T]):
    def __init__(self, value: T):
        self.value = value
    
    def __enter__(self) -> T:
        print("Entering context")
        return self.value
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print("Exiting context")
        # Return True to suppress exceptions
        return False

# Function that returns a typed context manager
def create_context(value: T) -> ContextManager[T]:
    return SimpleContextManager(value)

# Usage
with create_context("Hello World") as text:
    print(text)  # Will be a string
```

### Using contextlib for Simple Context Managers
The contextlib module makes it easy to create context managers with a generator function:
```python
from typing import ContextManager, Any
from contextlib import contextmanager

@contextmanager
def measure_time() -> ContextManager[float]:
    """Context manager that measures execution time."""
    import time
    start_time = time.time()
    try:
        yield start_time  # The yielded value is available in the with block
    finally:
        end_time = time.time()
        print(f"Execution took {end_time - start_time:.3f} seconds")

# Usage
with measure_time() as start:
    # Perform some time-consuming operations
    import time
    time.sleep(1)
```

## Best Practices for Using ContextManager
Be specific about the yielded type: Specify what type the context manager yields when entering the context.

Use contextlib for simple cases: For simple context managers, use the @contextmanager decorator from the contextlib module.

Always handle cleanup: Ensure that resource cleanup happens in the __exit__ method or in the finally block of a @contextmanager decorated function.

Document the context: Add docstrings explaining what happens when entering and exiting the context.

Return appropriate values from __exit__: Return True from __exit__ only if you want to suppress exceptions.

```python
from typing import ContextManager, TextIO
from contextlib import contextmanager

@contextmanager
def safe_open(file_path: str, mode: str = 'r') -> ContextManager[TextIO]:
    """
    Safely open a file and ensure it's closed after use.
    
    Args:
        file_path: Path to the file to open
        mode: Mode to open the file in ('r', 'w', etc.)
    
    Yields:
        The opened file object
    
    Raises:
        FileNotFoundError: If the file doesn't exist in read mode
    """
    file = None
    try:
        file = open(file_path, mode)
        yield file
    finally:
        if file is not None:
            file.close()
```

The ContextManager type hint is valuable for indicating functions or variables that follow the context manager protocol, enhancing code readability and enabling more precise type checking for resources that require setup and cleanup operations.

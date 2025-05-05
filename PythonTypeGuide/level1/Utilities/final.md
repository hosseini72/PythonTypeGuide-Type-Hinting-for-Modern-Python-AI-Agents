# Final Type Hint in Python

## Syntax (Python 3.8+)
```python
from typing import Final

# Basic usage - a constant that cannot be reassigned
MAX_CONNECTIONS: Final = 100
MAX_CONNECTIONS = 200  # Type error! Cannot assign to a variable annotated with Final

# With explicit type
API_KEY: Final[str] = "abc123"
TIMEOUT_SECONDS: Final[float] = 30.0

# In a class
class Configuration:
    DEBUG: Final = False
    MAX_RETRIES: Final[int] = 3
```

For Python 3.7 and below, you need to use typing_extensions:
```python
from typing_extensions import Final

# Same usage as above
VERSION: Final = "1.0.0"
```

In Python, Final is a special type hint that indicates a variable or attribute should not be reassigned or overridden. It helps enforce immutability at the variable level and is primarily intended for use with type checkers rather than imposing runtime constraints.

## When to Use Final

### Constants and Configuration Values
```python
from typing import Final, Dict, Any

# Application constants
APP_NAME: Final = "MyApp"
VERSION: Final = "1.0.0"
DEFAULT_SETTINGS: Final[Dict[str, Any]] = {
    "timeout": 30,
    "retries": 3,
    "debug": False
}

# These constants can be imported and used elsewhere,
# but cannot be reassigned
```

### Class Constants
```python
from typing import Final, ClassVar

class PaymentProcessor:
    # Class-level constants that apply to all instances
    SUPPORTED_CURRENCIES: Final[list[str]] = ["USD", "EUR", "GBP"]
    MAX_AMOUNT: Final = 10000
    
    # Instance attributes that cannot be reassigned
    def __init__(self, merchant_id: str):
        self.merchant_id: Final[str] = merchant_id
```

### Preventing Method Overrides
```python
from typing import Final

class BaseAuthenticator:
    def authenticate(self, username: str, password: str) -> bool:
        # Base implementation
        result = self._check_credentials(username, password)
        self._log_attempt(username, result)
        return result
    
    def _check_credentials(self, username: str, password: str) -> bool:
        # Implementation
        return True
    
    # This method should not be overridden by subclasses
    def _log_attempt(self, username: str, success: bool) -> None:
        """Log authentication attempts - security critical, do not override."""
        # Implementation that should not be changed
        pass
    
    # Using Final to prevent override in type checkers
    def verify_token(self, token: str) -> bool:
        """Final method that should not be overridden."""
        # Implementation
        return len(token) > 0
    
    # Explicit notation for methods that should not be overridden
    # (Python 3.8+)
    def revoke_access(self, user_id: str) -> None:
        """Revokes all access for a user."""
        # Implementation
        pass

class CustomAuthenticator(BaseAuthenticator):
    def _check_credentials(self, username: str, password: str) -> bool:
        # This is fine, _check_credentials is not final
        return custom_check(username, password)
    
    def verify_token(self, token: str) -> bool:
        # Type error! Cannot override a method marked Final
        return custom_verify(token)
    
    def revoke_access(self, user_id: str) -> None:
        # Type error! Cannot override a method marked Final
        pass
```

### Final Methods and Classes
In Python 3.8+, you can use Final to prevent method overrides or class inheritance:
```python
from typing import final

# Prevent method override
class Base:
    @final
    def do_something(self) -> None:
        pass

# Prevent class inheritance
@final
class Utility:
    def helper_method(self) -> None:
        pass

class Derived(Utility):  # Type error! Cannot inherit from final class
    pass
```

### Final vs. Constant Naming Conventions
While Python traditionally uses uppercase names for constants, Final provides additional type checking benefits:
```python
# Traditional constant (only a convention)
MAX_RETRIES = 3
MAX_RETRIES = 5  # No error, just violates convention

# Final constant (enforced by type checkers)
from typing import Final
MAX_CONNECTIONS: Final = 100
MAX_CONNECTIONS = 200  # Type error!
```

## Best Practices for Using Final
Use for true constants: Apply Final to values that should never change after initialization.

Be explicit about types: While Final can infer the type, it's clearer to use Final[type] for better readability.

Don't overuse: Reserve Final for values where reassignment would be a genuine mistake, not for all read-only data.

Document the reason: Explain why a value is marked as Final, especially for API or implementation details that might otherwise be expected to change.

Consider Final for security-critical methods: Use @final to prevent overriding methods that are security-sensitive.

```python
from typing import Final, Dict, final

class SecurityManager:
    # Clearly documented Final constant
    TOKEN_EXPIRY_SECONDS: Final[int] = 3600  # 1 hour
    
    def __init__(self, config: Dict[str, str]):
        # Final instance attribute
        self.api_key: Final[str] = config["api_key"]
    
    @final
    def validate_signature(self, data: str, signature: str) -> bool:
        """
        Validates a cryptographic signature - security critical method
        that should not be overridden by subclasses.
        """
        # Implementation
        return True
```

The Final type hint is a valuable tool for documenting and enforcing that certain values should not be reassigned, enhancing code quality and preventing certain classes of bugs. Unlike some other type hints, Final provides clear guidance to both developers and type checkers about the intended immutability of a value.



# LiteralString Type Hint in Python

## Syntax (Python 3.11+)
```python
from typing import LiteralString

# Variable that can only be a string literal or derived from other literal strings
safe_sql_input: LiteralString = "SELECT * FROM users"

# Function that requires a literal string
def execute_query(query: LiteralString) -> None:
    # Implementation knowing the query is safe
    pass
```

For Python 3.10 and below, you need to use typing_extensions:
```python
from typing_extensions import LiteralString

# Same usage as above
safe_identifier: LiteralString = "user_table"
```

In Python, LiteralString is a special type hint introduced in Python 3.11 specifically to address security concerns in applications. It represents string values that are either string literals or derived from other literal strings through operations like concatenation, formatting, or f-strings. Its primary purpose is to prevent SQL injection, command injection, and other security vulnerabilities by ensuring a string doesn't contain user-controlled input.

## When to Use LiteralString

### Preventing SQL Injection
```python
from typing import LiteralString

def execute_sql(query: LiteralString) -> None:
    """
    Execute a SQL query safely.
    
    The query must be a literal string or derived from literals,
    which ensures it cannot contain user input that might lead
    to SQL injection.
    """
    # Safe to execute directly
    db.execute(query)

# Safe usage
execute_sql("SELECT * FROM users WHERE active = TRUE")

# String concatenation of literals is still considered a LiteralString
table: LiteralString = "users"
execute_sql(f"SELECT * FROM {table} WHERE id = 1")

# This would be rejected by type checkers
user_input = input("Enter a value: ")
execute_sql(f"SELECT * FROM users WHERE name = '{user_input}'")  # Type error!
```

### Preventing Command Injection
```python
from typing import LiteralString
import subprocess

def run_command(command: LiteralString) -> None:
    """
    Run a shell command safely.
    
    The command must be a literal string, preventing command injection.
    """
    subprocess.run(command, shell=True)

# Safe usage
run_command("ls -la")

# Dynamic but still safe
options: LiteralString = "-la"
run_command(f"ls {options}")

# This would be rejected by type checkers
user_input = input("Enter a directory: ")
run_command(f"ls {user_input}")  # Type error!
```

### Safe Template Generation
```python
from typing import LiteralString, List

def create_html_template(title: LiteralString, sections: List[LiteralString]) -> str:
    """
    Create an HTML template with safe content.
    
    Both the title and section content must be literal strings,
    preventing XSS vulnerabilities.
    """
    html = f"<html><head><title>{title}</title></head><body>"
    for section in sections:
        html += f"<div>{section}</div>"
    html += "</body></html>"
    return html

# Safe usage
template = create_html_template(
    "Welcome Page",
    ["<h1>Welcome</h1>", "<p>This is a safe template.</p>"]
)

# This would be rejected by type checkers
user_input = input("Enter a title: ")
template = create_html_template(user_input, ["<h1>Welcome</h1>"])  # Type error!
```

### LiteralString vs Regular Strings
LiteralString is more specific than str:
```python
from typing import LiteralString

# Regular string function
def process_any_string(s: str) -> None:
    print(s)

# LiteralString function
def process_safe_string(s: LiteralString) -> None:
    print(s)

# Usage examples
process_any_string("Hello")  # Works
process_any_string(input())  # Works

process_safe_string("Hello")  # Works
process_safe_string(input())  # Type error!
```

## Best Practices for Using LiteralString

1. Use for security-critical functions: Apply LiteralString to functions that need to ensure string safety.

2. Document security implications: Clearly document why LiteralString is used in your code.

3. Consider backward compatibility: Use typing_extensions for Python versions before 3.11.

4. Combine with other security measures: Don't rely solely on LiteralString for security.

5. Use for template systems: Apply LiteralString to template engines and string formatting functions.

The LiteralString type hint is a powerful tool for preventing security vulnerabilities in Python applications. By ensuring that certain strings can only be literal values or derived from literals, it helps prevent common security issues like SQL injection and command injection.




[Back to Index](../../README.md)

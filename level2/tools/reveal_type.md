# reveal_type in Python

## Basic Usage

### With Static Type Checkers (mypy, pyright, etc.)
```python
# Not an actual import! This is a special form recognized by type checkers
# Uncomment the next line only when using type checkers that need it
# from typing import reveal_type  # Only needed for some type checkers

x = "hello"
reveal_type(x)  # Type checker will report: "Revealed type is 'str'"

numbers = [1, 2, 3]
reveal_type(numbers)  # Type checker will report: "Revealed type is 'list[int]'"
```

### With Complex Types
```python
from typing import Dict, List, Optional

# With nested types
data: Dict[str, List[int]] = {"values": [1, 2, 3]}
reveal_type(data)  # Type checker: "Revealed type is 'Dict[str, List[int]]'"
reveal_type(data["values"])  # Type checker: "Revealed type is 'List[int]'"

# With Optional types
maybe_name: Optional[str] = "John"
reveal_type(maybe_name)  # Type checker: "Revealed type is 'Optional[str]'"
```

## Common Use Cases

### Debugging Type Inference
```python
# Check inferred types in complex expressions
result = [x.strip() for x in ["a ", " b", "c "]]
reveal_type(result)  # Type checker: "Revealed type is 'List[str]'"

# Check type inference with lambdas and higher-order functions
mapped = map(lambda x: x * 2, [1, 2, 3])
reveal_type(mapped)  # Type checker: "Revealed type is 'map[int]'"
reveal_type(list(mapped))  # Type checker: "Revealed type is 'List[int]'"
```

## Important Notes

1. **reveal_type Characteristics**:
   - Development-time debugging tool only
   - Not a standard Python function (recognized only by type checkers)
   - No effect at runtime (raises NameError if not imported)
   - Shows the inferred type as reported by the type checker

2. **Type Checker Support**:
   - Supported by major type checkers (mypy, pyright, pytype)
   - Different type checkers may have slightly different output formats
   - Some type checkers may require importing it from typing (Python 3.11+)

3. **Best Practices**:
   - Use during development to understand type inference
   - Remove before committing code or shipping to production
   - Helpful for debugging complex type issues
   - Use with type checker in strict mode for best results

4. **Future Learning**
   As you become more familiar with type hints, you'll use reveal_type to understand how type checkers handle more advanced features like TypeVar, Protocol, and conditional typing.
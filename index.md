# Python Type Hints Guide

Welcome to the comprehensive guide to Python type hints. This documentation is organized into three levels of complexity, from foundational to advanced usage.

## Introduction

Before diving into the type hints, we recommend starting with our introduction materials:

- [Introduction to Python Type Hints](introduction/readme.md) - A comprehensive overview of type hints in Python
- [Why Use Type Hints?](introduction/why_type_hints.md) - Understanding the benefits and use cases
- [Annotations in Python](introduction/annotation_in_python.md) - How Python handles type annotations
- [Type Hint Taxonomy](introduction/type_hint_taxonomy.md) - Our three-level organization system

These documents provide:
- A clear understanding of type hints and their importance
- The benefits and use cases for type hints
- How Python implements type annotations
- A structured approach to learning type hints
- Best practices for type hint usage

## Documentation Structure

### Level 1: Foundational & Frequent Use
The most commonly used types — ideal for application developers, readable, and easily understood without advanced typing knowledge.

- [Primitive & Built-in Types](level1/primitive/int.md) (`int`, `float`, `str`, etc.)
- [Collections](level1/collections/list.md) (`List`, `Dict`, `Tuple`, etc.)
- [Basic Utilities](level1/utilities/optional.md) (`Optional`, `Union`, `Any`, etc.)
- [Common ABCs & Interfaces](level1/abcs/iterable.md) (`Iterable`, `Sequence`, etc.)

📌 **Audience**: All developers, especially those new to type hinting.

### Level 2: Intermediate Use
Used when building reusable components, APIs, or maintaining mid/large-scale codebases.

- [Structured Data](level2/structured/typeddict.md) (`TypedDict`, `NamedTuple`, etc.)
- [More ABCs & Utilities](level2/abcs/contextmanager.md) (`ContextManager`, `AsyncContextManager`, etc.)
- [Advanced Callable Types](level2/callable/callable_args.md) (`Callable[[Arg1, Arg2], Return]`, etc.)
- [Development Tools](level2/tools/overload.md) (`overload`, `cast`, etc.)

📌 **Audience**: Intermediate developers, library consumers, API designers.

### Level 3: Advanced & Metaprogramming
Powerful but complex tools for advanced typing, generic libraries, or static analysis tooling.

- [Generics and Metatypes](level3/generics/generic.md) (`Generic`, `TypeVar`, etc.)
- [Protocols and Structural Typing](level3/protocols/protocol.md) (`Protocol`, `runtime_checkable`, etc.)
- [Type System Internals](level3/internals/forwardref.md) (`ForwardRef`, `get_args`, etc.)
- [ABC-Heavy & Domain-Specific](level3/domain/binaryio.md) (`BinaryIO`, `IO`, etc.)
- [Decorators and Annotations](level3/decorators/dataclass_transform.md) (`dataclass_transform`, `final`, etc.)

📌 **Audience**: Library authors, power users, and those working on complex type systems.

## Getting Started

1. Start with the [Introduction to Python Type Hints](introduction/readme.md)
2. Understand [Why Type Hints Matter](introduction/why_type_hints.md)
3. Learn about [Annotations in Python](introduction/annotation_in_python.md)
4. Explore the [Type Hint Taxonomy](introduction/type_hint_taxonomy.md)
5. Begin with Level 1 type hints for everyday usage
6. Progress to Level 2 for more complex scenarios
7. Use Level 3 for advanced use cases and metaprogramming

## Contributing

This documentation is open for contributions. Please feel free to submit pull requests or open issues for any improvements or corrections. 
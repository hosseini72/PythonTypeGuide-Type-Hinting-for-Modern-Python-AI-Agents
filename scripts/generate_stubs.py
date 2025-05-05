import os
from pathlib import Path


def create_stub_file(path: str, title: str):
    """Create an empty stub file with a title."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write("## Overview\n\n")
        f.write("## Usage\n\n")
        f.write("## Examples\n\n")
        f.write("## Related Types\n\n")


def main():
    base_dir = Path("PythonTypeGuide")
    
    # Level 1: Foundational & Frequent Use
    level1_types = {
        "primitive": ["int", "float", "str", "bool", "bytes", "complex", "None"],
        "collections": ["List", "Dict", "Tuple", "Set", "FrozenSet"],
        "utilities": [
            "Optional", "Union", "Any", "Literal", "Callable",
            "Annotated", "Final", "ClassVar", "Type"
        ],
        "abcs": [
            "Iterable", "Iterator", "Sequence", "Mapping",
            "MutableMapping", "Sized", "Container", "Collection"
        ]
    }
    
    # Level 2: Intermediate Use
    level2_types = {
        "structured": ["TypedDict", "NamedTuple", "TypeAlias", "LiteralString"],
        "abcs": [
            "ContextManager", "AsyncContextManager", "Reversible",
            "Hashable", "SupportsInt"
        ],
        "async": [
            "Awaitable", "Coroutine", "AsyncIterator",
            "AsyncIterable", "Generator"
        ],
        "callable": ["Callable_Args", "TypeGuard", "NewType"],
        "tools": [
            "overload", "cast", "reveal_type", "assert_type",
            "assert_never"
        ]
    }
    
    # Level 3: Advanced & Metaprogramming
    level3_types = {
        "generics": [
            "Generic", "TypeVar", "TypeVarTuple", "ParamSpec",
            "Concatenate", "Unpack", "Self"
        ],
        "protocols": [
            "Protocol", "runtime_checkable", "is_protocol",
            "get_protocol_members"
        ],
        "internals": [
            "ForwardRef", "get_args", "get_origin", "get_type_hints",
            "TypeAliasType", "NoReturn", "Never", "NoDefault"
        ],
        "domain": ["BinaryIO", "IO", "TextIO", "Match", "Pattern", "AnyStr"],
        "decorators": [
            "dataclass_transform", "final", "override",
            "no_type_check", "no_type_check_decorator",
            "ReadOnly", "Required", "NotRequired"
        ]
    }
    
    # Generate Level 1 files
    for category, types in level1_types.items():
        for type_name in types:
            path = base_dir / "level1" / category / f"{type_name.lower()}.md"
            create_stub_file(str(path), type_name)
    
    # Generate Level 2 files
    for category, types in level2_types.items():
        for type_name in types:
            path = base_dir / "level2" / category / f"{type_name.lower()}.md"
            create_stub_file(str(path), type_name)
    
    # Generate Level 3 files
    for category, types in level3_types.items():
        for type_name in types:
            path = base_dir / "level3" / category / f"{type_name.lower()}.md"
            create_stub_file(str(path), type_name)


if __name__ == "__main__":
    main() 
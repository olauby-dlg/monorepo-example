# Example of Python Monorepository

## Motivation

Trying to solve the problem:

    In a python mono-repository,
    How to make auto-imports of objects from editable libraries work ?


## Setup

2 projects:

```
.
├── app
│   ├── .venv
│   ├── app
│   │   └── main.py
│   └── pyproject.toml
└── mylib
    ├── .venv
    ├── mylib
    │   └── __init__.py
    │   └── module.py
    └── pyproject.toml
```

Using **VSCode** with **Pylance** lsp.

VSCode **Workspace** mode:
- [monorepo.code-workspace](monorepo.code-workspace)
- Enable python-interpreter / LSP switching
- Enable vscode tests exploration (not in this project)


## Conclusion

Work in Progress. See [issues](ISSUES.md).

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
    └── pyproject.toml
```

Using **poetry** (2.1.3) as dependency manager.

Using **VSCode** with extensions:

- Python
- Python Environments
- **Pylance** (LSP based on **pyright**)
- Ruff - useless here but force of habbit

Using VSCode **Workspace** mode:

- [monorepo.code-workspace](monorepo.code-workspace)
- Enable python-interpreter / LSP switching
- Enable vscode tests exploration (not in this project)


## About

- `myapp` has a dependency to `numpy`: just for the sake of testing auto-import from a third party library (working)
- `app` has a editable-dependency to `myapp`: auto-imports of myapp objects in app do not work

## Conclusion

Feels like Pylance is just not good for mono-repositories.

I removed it and it works fine.

See [issues](ISSUES.md).

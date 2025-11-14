# Issues

## Open issues

### Broken auto-import

In VSCode, when typing the name of an object (e.g. `bar`) from [mylib](mylib/mylib/__init__.py) in [app](app/app/main.py), no auto-import is suggested.


Observations:

- Auto-import does not work when app is open individually
- When restarting the python server, and immediatly writting bar in app I get the auto import suggestion. But when doing it a few seconds later I don't have it:
    - Auto import works while LSP is restarting
    - Auto import stop working when LSP has restarted

Solution ?

Adding `include=["../mylib"]` to pyright config seems to fix the issue


### Poetry generates egg-info folder

When running `poetry install/update/sync` in [app][app/], it generates a folder `mylib.egg-info` in [mylib](mylib/).


## Resolved issues

### Editable Libaray vs Pyright

Editable libraries break pyright path finding:
- When a dependency is installed as editable with PEP660, you get `Import "..." could not be resolved`
- See pyright issue: https://github.com/microsoft/pyright/issues/3846
- Solution is to add path to library to [pyright extraPaths](app/pyproject.toml)

This is not an issue you encouter with legacy installation of editable libraries, as it was creating simlinks in site-packages.

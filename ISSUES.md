# Issues

## Open issues

### Broken auto-import

In VSCode, when typing the name of an object (e.g. `bar`) from [mylib](mylib/mylib/__init__.py) in [app](app/app/main.py), no auto-import is suggested.


Observations:

- Auto-import does not work when app is open individually
- When restarting the python server, and immediatly writting bar in app I get the auto import suggestion. But when doing it a few seconds later I don't have it:
    - Auto import works while LSP is restarting
    - Auto import stop working when LSP has restarted


#### Option A: use include

Adding `include=["../mylib"]` to pyright config seems to fix the issue:

- Re-exports are not suggested:
    - Mentionned here: https://github.com/microsoft/pylance-release/issues/5654
    - Supposed to be fixed: https://github.com/microsoft/pylance-release/issues/4065

- The option includeAliasesFromUserFiles breaks the import paths:
    - `"python.analysis.includeAliasesFromUserFiles": true`
    - the issue persist even after removing the option...

- Sometimes I get suggestions to import `baz`/`bar` from `myapp.myapp` instead of from `myapp.myapp`
    - includeAliasesFromUserFiles triggered it a few time
    - probably because of app workspace been inside root workspace
    - but very unsure of what is going on

#### Option B: Remove Pylance

Uninstall Pylance.
Install Pyright extension from microsoft.
Switch lsp to Jedi.


### Poetry generates egg-info folder

When running `poetry install/update/sync` in [app][app/], it generates a folder `mylib.egg-info` in [mylib](mylib/).


## Resolved issues

### Editable Libaray vs Pyright

Editable libraries break pyright path finding:
- When a dependency is installed as editable with PEP660, you get `Import "..." could not be resolved`
- See pyright issue: https://github.com/microsoft/pyright/issues/3846

This is not an issue you encouter with legacy installation of editable libraries, as it was creating simlinks in site-packages.

**Solution**: add path to library to [pyright extraPaths](app/pyproject.toml)


### Ruff

```
2025-11-14 14:44:46.219552000  WARN Ignoring request because snapshot for path `Url { scheme: "file", cannot_be_a_base: false, username: "", password: None, host: None, port: None, path: ".../app/app/main.py", query: None, fragment: None }` doesn't exist.
```

Claude AI assumes it is because ruff doesn't know what pyproject.toml configuration it should use.

**Solution**: add "ruff.configuration": "${workspaceFolder}/pyproject.toml", to [workspace settings](monorepo.code-workspace)

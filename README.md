# public-repo-github-app-spike
I'm testing using GitHub Apps instead of a PAT. This is a public repo that needs access to a private repo. 

## Technical documentation

Install [uv](https://docs.astral.sh/uv/) to get started.

### Dependencies

Run `uv sync` to install dependencies.  

### Development tasks

Run `uv run pytest` to run tests.  
Run `uv run ruff format` to format the code.  
Run `uv run ruff check .` to lint code base.  
Run `uv run pyright` to validate the type hints.

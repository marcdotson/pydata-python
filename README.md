# Python Orientation


Python is a big tent. Follow along for a brief orientation to “the
second best language for everything.”

## Project Organization

- `/code` Scripts with prefixes (e.g., `01_import-data.py`,
  `02_clean-data.py`) and functions in `/code/src`.
- `/data` Simulated and real data, the latter not pushed.
- `/figures` PNG images and plots.
- `/presentations` Presentation slides.
- `/private` A catch-all folder for miscellaneous files, not pushed.
- `/.quarto` Hidden Quarto project library, not pushed.
- `/.venv` Hidden Python project library, not pushed.
- `.gitignore` Hidden Git instructions file.
- `.python-version` Hidden Python version file.
- `LICENSE` MIT License for “as is” permission.
- `README.md` GitHub-flavored markdown README rendered from
  `README.qmd`.
- `README.qmd` Quarto markdown README to edit and render into
  `README.md`.
- `_quarto.yml` Quarto project configuration file.
- `pyproject.toml` Python project environment configuration file.
- `uv.lock` Python project environment lockfile.

## Project Environment

After cloning this repository, go to the project’s terminal in Positron
and run `uv run` to create the `/.venv` project library and install the
specified Python and library versions.

For more details on using Positron, Python, Quarto, and GitHub see the
[data stack](https://github.com/marcdotson/data-stack) repository.

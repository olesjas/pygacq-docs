# PyGacq documentation

User documentation for PyGacq, built with [Sphinx](https://www.sphinx-doc.org/)
and published on [Read the Docs](https://readthedocs.org/).

Pages live in `docs/` and can be written in Markdown (`.md`, via
[MyST](https://myst-parser.readthedocs.io/)) or reStructuredText (`.rst`).
New pages have to be added to a `toctree` (see `docs/index.md` and
`docs/tutorial/index.md`) to show up in the navigation.

## Building locally

One-time setup:

```bash
python3 -m venv .venv
.venv/bin/pip install -r docs/requirements.txt
```

Build and open:

```bash
.venv/bin/sphinx-build -b html docs docs/_build/html
open docs/_build/html/index.html
```

(or `make -C docs html SPHINXBUILD=../.venv/bin/sphinx-build`)

## Publishing on Read the Docs

1. Push this repository to a **public** GitHub repository.
2. Sign in at https://readthedocs.org with that GitHub account and choose
   **Import a Project**, then pick the repository.
3. Read the Docs builds from `.readthedocs.yaml` on every push.

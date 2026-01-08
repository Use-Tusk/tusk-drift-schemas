# Tusk Drift Schemas

This repo holds schemas defined as protobuf files used by Tusk Drift. We use Buf to generate code for each language we support (currently TypeScript, Golang, and Python).

## Prerequisites

Before generating schemas, install the following:

1. Install the [Buf CLI](https://buf.build/docs/cli/installation/).
2. Python `betterproto` (for Python code generation):

   ```bash
   pip install "betterproto[compiler]>=2.0.0b7"
   # Or using the requirements file:
   pip install -r requirements.txt
   ```

## Generating Schemas

After modifying `.proto` files, regenerate the code:

```bash
npm run generate
```

> [!NOTE]
> You may see "duplicate generated file name" warnings from betterproto. These are harmless and can be ignored — they occur because multiple proto packages share the same Python namespace (`tusk.drift`).

Then build the TypeScript package:

```bash
npm run build
```

## Usage

### Installing schemas in TypeScript projects

```bash
npm install @use-tusk/drift-schemas
```

Developing locally:

- In this repo, run `npm link` to create a symlink to the local package.
- In your project, run `npm link @use-tusk/drift-schemas` to use the local package.
- After updating the schemas, run `npm run build` to rebuild the package.
- Run `npm unlink @use-tusk/drift-schemas` to remove the local package.

### Installing schemas in Golang projects

```text
go get github.com/Use-Tusk/tusk-drift-schemas
```

When developing locally, add this to `go.mod` in your project:

```text
replace github.com/Use-Tusk/tusk-drift-schemas => ../tusk-drift-schemas
```

Run `go mod tidy` to update the dependencies.
Remember to remove this before pushing.

### Installing schemas in Python projects

```bash
pip install tusk-drift-schemas
```

Then you can import as

```python
# Core schemas
from tusk.drift.core.v1 import *

# Backend schemas
from tusk.drift.backend.v1 import *
```

---

## Releasing

Use the release script to create a new release:

```bash
# Patch release (0.1.22 → 0.1.23)
./scripts/release.sh

# Minor release (0.1.22 → 0.2.0)
./scripts/release.sh minor
```

The script will:

1. Run preflight checks (on main, up to date, no uncommitted changes)
2. Run `generate` and `build` to verify everything works
3. Update version in both `package.json` and `pyproject.toml`
4. Commit, tag, and push to GitHub
5. Create a GitHub Release (which triggers the NPM & PyPI publish workflows)

> [!NOTE]
> If a broken release occurs, or you just want to test some stuff, you can supply an optional version override to the GH actions manually, like `0.1.23.dev1`.

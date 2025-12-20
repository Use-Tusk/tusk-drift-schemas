# Tusk Drift Schemas 

This repo holds schemas defined as protobuf files used by Tusk Drift. We use Buf to generate code for each language we support (currently TypeScript and Golang).

Install Buf [here](https://buf.build/docs/cli/installation/).

## TypeScript

### Installing schemas in TypeScript projects

```
npm install @use-tusk/drift-schemas
```

### Developing locally

In this repo, run `npm link` to create a symlink to the local package.
In your project, run `npm link @use-tusk/drift-schemas` to use the local package.
After updating the schemas, run `npm run build` to rebuild the package.
Run `npm unlink @use-tusk/drift-schemas` to remove the local package.

## Golang

### Installing schemas in Golang projects

```
go get github.com/Use-Tusk/tusk-drift-schemas
```

### Developing locally

In your project, add this to `go.mod`:
```
replace github.com/Use-Tusk/tusk-drift-schemas => ../tusk-drift-schemas
```
Run `go mod tidy` to update the dependencies.
Remember to remove this before pushing.

## Python

### Installing schemas in Python projects

```
pip install tusk-drift-schemas
```
Then you can import as
```
# Core schemas
from tusk.drift.core.v1 import *

# Backend schemas
from tusk.drift.backend.v1 import *
```

# Building

## Releasing

1. Checkout a new branch with the new version number (e.g. `git checkout -b v0.1.1`)
2. Increment the patch version (e.g. 0.1.0 → 0.1.1), using `npm version patch`. This creates a commit and a tag.
3. Push the branch and the tag to GitHub.
4. Create a new release on GitHub with the new version number.
5. The release will trigger a GitHub Actions workflow to publish the package to NPM an PyPi. Golang just pulls from GitHub so no need for publishing.

Note: if a broken release occurs, or you just want to test some stuff, you can
supply an optional version override to the GH actions manually, like 0.1.1.dev1.

# rust-codegen

Internal code generator for Rust protobuf schemas in this repository.

## Purpose

This crate runs `prost-build` against `../proto` and writes checked-in Rust
generated files to:

- `../rust/src/generated`

The publishable Rust crate (`../rust`) then includes these files directly.

## Usage

Preferred (repo-wide generation):

```bash
npm run generate
```

Rust-only generation:

```bash
cargo run -p tusk-drift-schemas-rust-codegen
```

## Notes

- This crate is tooling-only and is not published (`publish = false`).
- Keep generated files committed so schema changes are visible in PR diffs.

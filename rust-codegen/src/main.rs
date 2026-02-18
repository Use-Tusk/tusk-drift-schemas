use std::fs;
use std::path::Path;
use std::path::PathBuf;

fn main() {
    let repo_root = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("codegen crate should live under repo root")
        .to_path_buf();

    let proto_root = repo_root.join("proto");
    let crate_out_dir = repo_root.join("rust/src/generated");

    let inputs = [
        proto_root.join("core/communication.proto"),
        proto_root.join("core/json_schema.proto"),
        proto_root.join("core/span.proto"),
        proto_root.join("backend/common.proto"),
        proto_root.join("backend/client_service.proto"),
        proto_root.join("backend/span_export_service.proto"),
        proto_root.join("backend/test_run_service.proto"),
        proto_root.join("postgresql/postgresql.proto"),
    ];

    let input_refs = inputs.iter().map(|p| p.as_path()).collect::<Vec<_>>();

    compile_to(&crate_out_dir, &input_refs, proto_root.as_path());
    println!("Generated Rust schemas in {}", crate_out_dir.display());
}

fn compile_to(out_dir: &Path, input_refs: &[&Path], proto_root: &Path) {
    fs::create_dir_all(out_dir).expect("failed to create output dir");

    prost_build::Config::new()
        .out_dir(out_dir)
        .compile_protos(input_refs, &[proto_root])
        .expect("failed to compile protobuf schemas");

    // Remove stale files that might linger when schema packages are renamed.
    // Keep this conservative to avoid deleting unrelated checked-in files.
    let expected = [
        "tusk.drift.core.v1.rs",
        "tusk.drift.backend.v1.rs",
        "tusk.drift.instrumentation.postgresql.v1.rs",
    ];
    for entry in fs::read_dir(out_dir).expect("failed to read output dir") {
        let entry = entry.expect("failed to read output dir entry");
        let name = entry.file_name();
        let name = name.to_string_lossy();
        if name.ends_with(".rs") && !expected.iter().any(|v| *v == name) {
            fs::remove_file(entry.path()).expect("failed to remove stale generated file");
        }
    }
}

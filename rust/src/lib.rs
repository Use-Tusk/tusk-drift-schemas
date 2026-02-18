pub mod tusk {
    pub mod drift {
        pub mod core {
            pub mod v1 {
                include!(concat!(
                    env!("CARGO_MANIFEST_DIR"),
                    "/src/generated/tusk.drift.core.v1.rs"
                ));
            }
        }
        pub mod backend {
            pub mod v1 {
                include!(concat!(
                    env!("CARGO_MANIFEST_DIR"),
                    "/src/generated/tusk.drift.backend.v1.rs"
                ));
            }
        }
        pub mod instrumentation {
            pub mod postgresql {
                pub mod v1 {
                    include!(concat!(
                        env!("CARGO_MANIFEST_DIR"),
                        "/src/generated/tusk.drift.instrumentation.postgresql.v1.rs"
                    ));
                }
            }
        }
    }
}

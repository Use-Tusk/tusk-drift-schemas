# Tusk Drift Schema Design

## Context and Problem

Tusk Drift is a CLI application that replays traces in services instrumented with SDKs. The system works by having SDKs intercept outbound requests (PostgreSQL, HTTP, etc.) and request mocks from the CLI server via Unix socket communication. The CLI returns stored mock responses that patch the outbound calls during replay.

The core challenge was determining how to share type definitions between the CLI (written in Go) and multiple language SDKs (Node.js/TypeScript, with future support for Python, Ruby, etc.) while maintaining type safety and allowing independent evolution.

## Architectural Decisions

### Schema Distribution Strategy: Protocol Buffers with Modular Packaging

We decided on Protocol Buffers over alternatives like JSON Schema or OpenAPI because:
- Provides both compile-time and runtime type safety across languages
- Offers excellent schema evolution capabilities with backward/forward compatibility
- Has mature tooling and code generation for all target languages
- More efficient than JSON for network communication
- Self-documenting schemas

The distribution strategy uses separate packages per schema type, published to each language's native package manager (NPM for TypeScript, Go modules, PyPI for Python, etc.).

### Communication vs. Instrumentation Schemas

A critical decision was to separate concerns into two schema layers:

**Communication Layer (CLI ↔ SDK Interface):**
- Generic, stable protocol for CLI-SDK communication
- Uses opaque JSON-like data structures (protobuf Struct types)
- CLI treats instrumentation-specific data as black boxes
- Enables CLI to remain instrumentation-agnostic
- Hash-based matching for exact mock retrieval without semantic understanding

**Instrumentation Layer (SDK Internal):**
- Type-safe, instrumentation-specific schemas (HTTP, PostgreSQL, MySQL, etc.)
- Used only within individual instrumentation libraries
- Can evolve independently without affecting CLI
- Provides rich type safety for SDK development

This decoupling prevents the CLI from needing updates when new instrumentation types are added and allows instrumentation schemas to evolve at their own pace.

### Repository Structure

```
tusk-drift-schemas/
├── proto/
│   ├── core/
│   │   ├── span.proto              # Generic span structure
│   │   └── communication.proto     # CLI ↔ SDK protocol
│   ├── http/
│   │   └── http.proto              # HTTP instrumentation types
│   ├── postgresql/
│   │   └── postgresql.proto        # PostgreSQL instrumentation types
│   └── mysql/
│       └── mysql.proto             # MySQL instrumentation types
├── generated/                      # Generated code (gitignored)
├── scripts/                        # Code generation scripts
└── templates/                      # Code generation templates
```

Each schema gets published as separate packages (e.g., `@tusk/drift-schemas-core`, `@tusk/drift-schemas-postgresql`) allowing instrumentation libraries to depend only on what they need.

## Schema Design Details

### Core Schemas

**span.proto:** Contains a universal span structure that works for all instrumentation types. Key features:
- Generic input/output data as protobuf Struct (JSON-like)
- Hash fields for fast mock matching
- OpenTelemetry-compatible span kinds and status codes
- Legacy timing fields to maintain backward compatibility with current `[seconds, nanoseconds]` format
- Modern timing fields using standard protobuf Duration/Timestamp types

**communication.proto:** Defines the generic CLI-SDK protocol with:
- Mock request/response messages using opaque data structures
- SDK connection handshake with version negotiation
- Hash-based matching fields for exact mock retrieval
- No instrumentation-specific knowledge required

### Instrumentation-Specific Schemas

**postgresql.proto:** Rich PostgreSQL-specific types including:
- Query structures with SQL text, parameters, and connection context
- Result structures matching our actual trace data format
- PostgreSQL-specific field definitions with OIDs and type information
- Error handling with detailed PostgreSQL error codes and context
- Advanced features like prepared statements, transactions, and batch operations

The design ensures each instrumentation library gets precise type safety while keeping the CLI completely generic.

## Version Management Strategy

The approach handles schema evolution through:
- Semantic versioning for each schema package
- Version negotiation during SDK-CLI connection
- Backward compatibility support in the CLI for multiple schema versions
- Independent evolution of instrumentation schemas without breaking changes to the communication layer

## Implementation Progress

### Completed
-  **Schema Design:** Full protobuf definitions for core communication and PostgreSQL instrumentation
-  **Code Generation:** Working scripts that generate packages with proper dependencies (implemented for TypeScript, Go)
-  **Repository Structure:** Established the modular schema organization
-  **Build Infrastructure:** Scripts for code generation with proper package.json, tsconfig.json, and dependency management

### Not Yet Implemented
-  **Other Language Support:** Python, Ruby, Java code generation
-  **CI/CD Pipeline:** Automated publishing to package managers
-  **SDK Migration:** Updating existing Node.js SDK to use the new typed schemas
-  **Mock Matching Updates:** CLI mock matching logic needs to be updated for hash-based generic matching
-  **Additional Instrumentation Schemas:** HTTP, MySQL, Redis schemas still need to be defined
-  **Version Negotiation:** Implementation of the version negotiation protocol during SDK initialization and connection

This design provides a solid foundation for a multi-language SDK ecosystem with strong type safety, independent evolution, and clean separation of concerns between communication and instrumentation logic.

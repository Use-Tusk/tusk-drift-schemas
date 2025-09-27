# System Dependency & Versioning

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                            TUSK DRIFT ECOSYSTEM                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                              SCHEMA LAYER                                    │
├──────────────────────────────────────────────────────────────────────────────┤
│  tusk-drift-schemas Repository                                               │
│  ┌─────────────────────┐  ┌─────────────────────────────────────────────────┐│
│  │   Communication     │  │         Instrumentation Schemas                 ││
│  │     Schemas         │  │                                                 ││
│  │                     │  │  ┌──────────┐ ┌──────────┐ ┌──────────┐         ││
│  │ base/               │  │  │   http/  │ │    pg/   │ │  mysql/  │   ...   ││
│  │ ├─ span.proto       │  │  │ http.    │ │ postgres │ │ mysql.   │         ││
│  │ └─ communication.   │  │  │ proto    │ │ ql.proto │ │ proto    │         ││
│  │    proto            │  │  └──────────┘ └──────────┘ └──────────┘         ││
│  └─────────────────────┘  └─────────────────────────────────────────────────┘│
└──────────────────────────────────────────────────────────────────────────────┘
                │                               │
                │ generates                     │ generates
                ▼                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          GENERATED PACKAGES                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Go Modules:                   NPM Packages:                                │
│  github.com/tusk/schemas/      @tusk/drift-schemas-base                     │
│  ├─ go/base                    @tusk/drift-schemas-http                     │
│  ├─ go/http                    @tusk/drift-schemas-postgresql               │
│  ├─ go/postgresql              @tusk/drift-schemas-mysql                    │
│  └─ go/mysql                   ...                                          │
│                                                                             │
│  Python Packages:              Ruby Gems:                                   │
│  tusk-drift-schemas-base       tusk-drift-schemas-base                      │
│  tusk-drift-schemas-http       tusk-drift-schemas-http                      │
│  tusk-drift-schemas-postgresql tusk-drift-schemas-postgresql                │
│  ...                          ...                                           │
└─────────────────────────────────────────────────────────────────────────────┘
                │                               │
                │ consumed by                   │ consumed by
                ▼                               ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                          APPLICATION LAYER                                   │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────┐              ┌─────────────────────────────────┐│
│  │         CLI             │              │           SDK ECOSYSTEM         ││
│  │   (tusk-drift-cli)      │              │                                 ││
│  │                         │              │  ┌─────────────────────────────┐││
│  │ Dependencies:           │              │  │        SDK Core             │││
│  │ • go/base               │◄─────────────┤  │  (@tusk/drift-sdk-base)     │││
│  │   (communication only)  │ Unix Socket  │  │                             │││
│  │                         │              │  │ Dependencies:               │││
│  │ Does NOT depend on:     │              │  │ • @tusk/schemas-base        │││
│  │ • go/http               │              │  │   (communication)           │││
│  │ • go/postgresql         │              │  └─────────────────────────────┘││
│  │ • go/mysql              │              │                 │               ││
│  │ (instrumentation        │              │                 │ used by       ││
│  │  agnostic)              │              │                 ▼               ││
│  └─────────────────────────┘              │  ┌─────────────────────────────┐││
│                                           │  │   Instrumentation Libraries │││
│                                           │  │                             │││
│                                           │  │ @tusk/drift-instr-http:     │││
│                                           │  │ • @tusk/schemas-base        │││
│                                           │  │ • @tusk/schemas-http        │││
│                                           │  │                             │││
│                                           │  │ @tusk/drift-instr-pg:       │││
│                                           │  │ • @tusk/schemas-base        │││
│                                           │  │ • @tusk/schemas-postgresql  │││
│                                           │  │                             │││
│                                           │  │ @tusk/drift-instr-mysql:    │││
│                                           │  │ • @tusk/schemas-base        │││
│                                           │  │ • @tusk/schemas-mysql       │││
│                                           │  └─────────────────────────────┘││
│                                           └─────────────────────────────────┘│
└──────────────────────────────────────────────────────────────────────────────┘
                                                          │
                                                          │ installed by
                                                          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            USER APPLICATIONS                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  User's Node.js App:                    User's Python App:                  │
│                                                                             │
│  package.json:                          requirements.txt:                   │
│  {                                       tusk-drift-sdk-base                │
│    "dependencies": {                     tusk-drift-instr-postgresql        │
│      "@tusk/drift-sdk-base": "^1.0.0",  tusk-drift-instr-redis              │
│      "@tusk/drift-instr-pg": "^1.0.0",                                      │
│      "@tusk/drift-instr-redis": "^1.0.0"                                    │
│    }                                                                        │
│  }                                                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Version Progagation

### Scenario 1: Communication schema change (wide impact)

```
Step 1: Schema Update
├─ Developer updates base/communication.proto (v1.0.0 → v1.1.0)
├─ Breaking change: adds required field to MockRequest
└─ CI/CD generates and publishes @tusk/schemas-base v1.1.0

Step 2: CLI Update (required)
├─ CLI must update to support new communication schema
├─ Update go.mod: go/base v1.0.0 → v1.1.0
├─ Implement new communication protocol features
├─ Release CLI v1.2.0
└─ CLI now supports both v1.0.0 and v1.1.0 communication schemas

Step 3: SDK Core Update (required)
├─ SDK core updates: @tusk/schemas-base v1.0.0 → v1.1.0
├─ Implement new communication features
├─ Release @tusk/drift-sdk-base v1.1.0
└─ SDK negotiates schema version with CLI during connection

Step 4: Instrumentation Libraries (no change required)
├─ @tusk/drift-instr-http: No update needed
├─ @tusk/drift-instr-pg: No update needed
├─ @tusk/drift-instr-mysql: No update needed
└─ They only depend on SDK core, not communication schemas directly

Step 5: User Impact
├─ Users must update CLI to v1.2.0
├─ Users must update SDK core to @tusk/drift-sdk-base v1.1.0
└─ Instrumentation libraries continue working without updates
```

### Scenario 2: Instrumentation schema change (narrow impact)

```
Step 1: Schema Update
├─ Developer updates postgresql/postgresql.proto (v1.0.0 → v1.1.0)
├─ Adds new optional fields for query performance metrics
└─ CI/CD generates and publishes @tusk/schemas-postgresql v1.1.0

Step 2: CLI Update (not required)
├─ CLI continues to treat PostgreSQL data as opaque JSON
├─ Hash-based matching still works regardless of schema version
├─ No CLI changes needed
└─ CLI remains instrumentation-agnostic

Step 3: PostgreSQL Instrumentation Update (required)
├─ Update @tusk/drift-instr-pg:
│  └─ @tusk/schemas-postgresql v1.0.0 → v1.1.0
├─ Implement new performance metrics collection
├─ Release @tusk/drift-instr-pg v1.1.0
└─ Backward compatible with all CLI versions

Step 4: User Impact
├─ Users optionally update @tusk/drift-instr-pg to v1.1.0
├─ No CLI update required
├─ No breaking changes
└─ True incremental adoption
```

### Scenario 3: New instrumentation type addition

```
Step 1: Schema Creation
├─ Developer creates redis/redis.proto v1.0.0
├─ CI/CD generates and publishes @tusk/schemas-redis v1.0.0
└─ New schema, no breaking changes to existing schemas

Step 2: CLI Update (optional enhancement)
├─ CLI can optionally add redis-specific optimizations
├─ CLI already supports generic instrumentation via communication schema
├─ Release CLI v1.1.2 with Redis optimizations
└─ Older CLI versions still work with Redis (generic handling)

Step 3: Redis Instrumentation Creation
├─ Create new @tusk/drift-instr-redis package:
│  ├─ @tusk/schemas-base v1.1.0
│  └─ @tusk/schemas-redis v1.0.0
├─ Release @tusk/drift-instr-redis v1.0.0
└─ Independent development and release

Step 4: Other Components (no change required)
├─ SDK Core: No changes needed
├─ All existing instrumentation libraries: No changes needed
└─ Existing user applications: No changes needed

Step 5: User Impact
├─ Users can optionally install @tusk/drift-instr-redis
├─ No breaking changes to existing functionality
├─ Redis support works with existing CLI versions
└─ Additive enhancement only
```

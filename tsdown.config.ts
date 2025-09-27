import { defineConfig } from "tsdown";

export default defineConfig({
  entry: [
    "generated/ts/core/*.ts",
    "generated/ts/backend/*.ts",
    "generated/ts/google/protobuf/*.ts",
    "generated/ts/postgresql/*.ts",
  ],
  format: ["cjs", "esm"],
  dts: {
    sourcemap: true,
  },
  exports: true,
  sourcemap: true,
  clean: true,
  target: "es2020",
  platform: "node",
  external: ["@protobuf-ts/runtime", "@protobuf-ts/runtime-rpc"],
});

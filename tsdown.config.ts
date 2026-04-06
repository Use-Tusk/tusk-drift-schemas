const commonConfig = {
  format: ["cjs", "esm"] as const,
  dts: {
    sourcemap: true,
  },
  sourcemap: true,
  target: "es2020",
  platform: "node",
  external: ["@protobuf-ts/runtime", "@protobuf-ts/runtime-rpc"],
};

export default [
  {
    ...commonConfig,
    entry: [
      "generated/ts/core/*.ts",
      "generated/ts/backend/*.ts",
      "generated/ts/query/*.ts",
      "generated/ts/google/protobuf/*.ts",
      "generated/ts/postgresql/*.ts",
    ],
    clean: true,
    outDir: "dist",
  },
  {
    ...commonConfig,
    entry: ["src/query/*.ts"],
    clean: false,
    outDir: "dist/query",
  },
] as const;

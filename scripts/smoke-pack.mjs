import { mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";

function run(command, args, options = {}) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, {
      stdio: "inherit",
      ...options,
    });

    child.on("error", reject);
    child.on("exit", (code) => {
      if (code === 0) {
        resolve();
        return;
      }
      reject(new Error(`${command} ${args.join(" ")} exited with code ${code ?? "unknown"}`));
    });
  });
}

const packageRoot = fileURLToPath(new URL("../", import.meta.url));

const ESM_CHECK = `\
await import("@use-tusk/drift-schemas/query/span_query");
await import("@use-tusk/drift-schemas/query/span_query_helpers");
await import("@use-tusk/drift-schemas/core/span");
await import("@use-tusk/drift-schemas/backend/client_service");
await import("@use-tusk/drift-schemas/google/protobuf/struct");
await import("@use-tusk/drift-schemas/postgresql/postgresql");
console.log("esm smoke check passed");
`;

const CJS_CHECK = `\
require("@use-tusk/drift-schemas/query/span_query");
require("@use-tusk/drift-schemas/query/span_query_helpers");
require("@use-tusk/drift-schemas/core/span");
require("@use-tusk/drift-schemas/backend/client_service");
require("@use-tusk/drift-schemas/google/protobuf/struct");
require("@use-tusk/drift-schemas/postgresql/postgresql");
console.log("cjs smoke check passed");
`;

async function main() {
  const packageJson = JSON.parse(await readFile(join(packageRoot, "package.json"), "utf8"));
  const tarballName = `${String(packageJson.name).replace(/^@/, "").replace("/", "-")}-${packageJson.version}.tgz`;
  const tempRoot = await mkdtemp(join(tmpdir(), "drift-schemas-pack-"));
  const consumerDir = join(tempRoot, "consumer");

  try {
    await run("npm", ["pack", "--quiet", "--pack-destination", tempRoot], {
      cwd: packageRoot,
    });

    await mkdir(consumerDir, { recursive: true });
    await writeFile(
      join(consumerDir, "package.json"),
      JSON.stringify(
        {
          name: "drift-schemas-pack-smoke",
          private: true,
          type: "module",
        },
        null,
        2,
      ) + "\n",
    );
    await writeFile(join(consumerDir, "esm-check.mjs"), ESM_CHECK);
    await writeFile(join(consumerDir, "cjs-check.cjs"), CJS_CHECK);

    await run("npm", ["install", "--no-package-lock", join(tempRoot, tarballName)], {
      cwd: consumerDir,
    });
    await run("node", ["esm-check.mjs"], { cwd: consumerDir });
    await run("node", ["cjs-check.cjs"], { cwd: consumerDir });
  } finally {
    await rm(tempRoot, { recursive: true, force: true });
  }
}

await main();

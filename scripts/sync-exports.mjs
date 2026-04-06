import { readdir, readFile, writeFile } from "node:fs/promises";

// Maintainers only need to update ENTRY_GROUPS when introducing a new top-level
// TypeScript export root (for example, another generated/ts/* group or a new
// hand-authored source directory). Adding or removing files within one of these
// directories does not require manual package.json export edits; sync:exports
// discovers those entrypoints automatically.
const ENTRY_GROUPS = [
  { sourceDir: "generated/ts/backend", exportPrefix: "backend" },
  { sourceDir: "generated/ts/core", exportPrefix: "core" },
  { sourceDir: "generated/ts/google/protobuf", exportPrefix: "google/protobuf" },
  { sourceDir: "generated/ts/postgresql", exportPrefix: "postgresql" },
  { sourceDir: "generated/ts/query", exportPrefix: "query" },
  { sourceDir: "src/query", exportPrefix: "query" },
];

const STATIC_EXPORTS = {
  "./package.json": "./package.json",
};

function getPackageJsonPath() {
  return new URL("../package.json", import.meta.url);
}

async function listEntryNames(sourceDir) {
  const directoryUrl = new URL(`../${sourceDir}/`, import.meta.url);
  const entries = await readdir(directoryUrl, { withFileTypes: true });

  return entries
    .filter((entry) => entry.isFile() && entry.name.endsWith(".ts") && !entry.name.endsWith(".d.ts"))
    .map((entry) => entry.name.slice(0, -3))
    .sort((left, right) => left.localeCompare(right));
}

function createExportTarget(subpath) {
  return {
    import: `./dist/${subpath}.js`,
    require: `./dist/${subpath}.cjs`,
  };
}

async function buildExports() {
  const exportsMap = {};

  for (const group of ENTRY_GROUPS) {
    const entryNames = await listEntryNames(group.sourceDir);
    for (const entryName of entryNames) {
      const subpath = `${group.exportPrefix}/${entryName}`;
      const exportKey = `./${subpath}`;
      if (exportKey in exportsMap) {
        throw new Error(`Duplicate export detected for ${exportKey}`);
      }
      exportsMap[exportKey] = createExportTarget(subpath);
    }
  }

  return {
    ...exportsMap,
    ...STATIC_EXPORTS,
  };
}

async function main() {
  const packageJsonPath = getPackageJsonPath();
  const packageJsonContents = await readFile(packageJsonPath, "utf8");
  const packageJson = JSON.parse(packageJsonContents);
  const nextExports = await buildExports();

  if (JSON.stringify(packageJson.exports) === JSON.stringify(nextExports)) {
    console.log("package.json exports already up to date");
    return;
  }

  packageJson.exports = nextExports;
  await writeFile(packageJsonPath, `${JSON.stringify(packageJson, null, 2)}\n`);
  console.log("updated package.json exports");
}

await main();

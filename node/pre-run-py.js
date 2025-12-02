import fs from "node:fs";
import path, { extname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawn, exec } from "node:child_process";
// import "./keyboard.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const pythonScript = path.join(__dirname, "deploy.py");

console.log("当前工作目录:", process.cwd());
console.log("脚本所在目录:", __dirname);
console.log("pythonScript", pythonScript);

function readFileContent(filePath) {
  const raw = fs.readFileSync(path.resolve(__dirname, filePath), "utf-8");
  if (extname(filePath) === ".json") {
    return JSON.parse(raw);
  }
  return raw;
}



function openBrowser(url) {
  const command =
    process.platform === "darwin"
      ? `open "${url}"`
      : process.platform === "win32"
      ? `start "" "${url}"`
      : `xdg-open "${url}"`;

  exec(command);
}
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function runPython(index, hasDesc) {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn(
      "python",
      [pythonScript, `--index=${index}`, hasDesc && "--hasDesc"].filter(
        Boolean
      ),
      {
        stdio: "inherit",
      }
    );

    pythonProcess.on("close", (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(new Error(`Python 进程退出,错误码: ${code}`));
      }
    });

    pythonProcess.on("error", (err) => {
      reject(err);
    });
  });
}

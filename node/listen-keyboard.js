import { GlobalKeyboardListener } from "node-global-key-listener";

const v = new GlobalKeyboardListener();

v.addListener((e, down) => {
  // console.log(`${e.name} ${e.state}`);

  // 检测特定按键
  if (e.name === "ESCAPE" && e.state === "DOWN") {
    console.log("ESC 被按下");
    v.kill();
    process.exit(0);
  }

  // 检测组合键
  if (e.state === "DOWN" && e.name === "C" && down["LEFT CTRL"]) {
    console.log("Ctrl+C 被按下");
    v.kill();
    process.exit(0);
  }
});

// 优雅退出
process.on("SIGINT", () => {
  v.kill();
  process.exit(0);
});

import pyautogui
import time
import sys
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
from pynput.keyboard import Key, Controller

import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="部署脚本")

# 添加参数
parser.add_argument("--hasDesc", action="store_true", help="是否包含描述")
parser.add_argument("--index", type=int, default=1, help="索引")

# 解析参数
args = parser.parse_args()

# 使用参数
if args.hasDesc:
    print("包含描述")
else:
    print("不包含描述")

print(f"index: {args.index}")

# 全局变量控制程序是否继续运行
should_exit = False


def on_press(key: Key | KeyCode | None) -> None:
    """键盘按键监听回调函数"""
    global should_exit
    global coun
    global break_loop
    global running

    try:
        print(f"按下键: {key}")
        # 检测是否按下ESC键
        if key == Key.esc:
            should_exit = True
            listener.stop()
            print("\n检测到ESC键，准备退出程序...")
            sys.exit(0)

    except AttributeError:
        pass


# 启动键盘监听器（在后台线程运行）
listener = keyboard.Listener(on_press=on_press)
listener.start()


DESC_HEIGHT = 20

HEIGHT = 0 if args.hasDesc else -DESC_HEIGHT
print(f"HEIGHT: {HEIGHT}")

点击a = [1, 2 + HEIGHT]
点击b = [77, 37 + HEIGHT] 


def check_exit() -> None:
    """检查是否需要退出"""
    if should_exit:
        print("程序已终止")
        sys.exit(0)


def move_click(position: list[int]) -> None:
    """移动鼠标并点击"""
    check_exit()
    time.sleep(0.1)
    pyautogui.moveTo(*position, duration=0.1)
    pyautogui.click()
    time.sleep(0.1)
    check_exit()


def main() -> None:
    global should_exit

    if should_exit:
        print("程序已终止")
        listener.stop()
        sys.exit(0)

    print("程序已启动，按ESC键可随时退出...")
    time.sleep(1)

    try: 
        move_click(点击部署a)
        move_click(点击配置模板) 
        time.sleep(0.6)
        pyautogui.scroll(-3000)
        time.sleep(0.1)
        move_click(点击部署b)
        print("程序执行完成！")
        time.sleep(1)

    finally:
        listener.stop()
        should_exit = True


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
        print("\n程序已退出")
    except Exception as e:
        print(f"\n程序执行出错: {e}")
        sys.exit(1)

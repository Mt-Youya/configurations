import os
import rarfile
import shutil


# 首先安装rarfile库: pip install rarfile
# 还需要安装unrar工具
rarfile.UNRAR_TOOL = "C:/Program Files/WinRAR/UnRAR.exe"
def extract_all_rars(base_dir):
    # 遍历基础目录下的所有子目录
    for root, dirs, files in os.walk(base_dir):
        # 查找每个目录中的RAR文件
        rar_files = [f for f in files if f.lower().endswith('.rar')]

        for rar_file in rar_files:
            rar_path = os.path.join(root, rar_file)
            # 创建临时解压目录
            temp_extract_dir = os.path.join(root, "temp_extract")
            os.makedirs(temp_extract_dir, exist_ok=True)

            print(f"解压文件: {rar_path}")

            try:
                # 使用rarfile库解压
                with rarfile.RarFile(rar_path) as rf:
                    rf.extractall(temp_extract_dir)

                # 将解压后的内容移动到基础目录
                extracted_items = os.listdir(temp_extract_dir)
                for item in extracted_items:
                    item_path = os.path.join(temp_extract_dir, item)
                    dest_path = os.path.join(base_dir, item)

                    # 处理文件名冲突
                    if os.path.exists(dest_path):
                        print(f"警告: {dest_path} 已存在，正在重命名...")
                        base, ext = os.path.splitext(item)
                        i = 1
                        while os.path.exists(os.path.join(base_dir, f"{base}_{i}{ext}")):
                            i += 1
                        dest_path = os.path.join(base_dir, f"{base}_{i}{ext}")

                    # 移动文件或目录
                    shutil.move(item_path, dest_path)
                    print(f"已移动: {item} 到 {dest_path}")

                # 清理临时目录
                shutil.rmtree(temp_extract_dir)

            except Exception as e:
                print(f"处理 {rar_path} 时出错: {str(e)}")


if __name__ == "__main__":
    base_folder = input("请输入要处理的基础文件夹路径: ")

    if os.path.isdir(base_folder):
        extract_all_rars(base_folder)
        print("处理完成!")
    else:
        print("指定的路径不是有效的文件夹!")

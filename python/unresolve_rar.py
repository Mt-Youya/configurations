import os
import rarfile

def extract_rars_to_parent(root_dir):
    """
    遍历 root_dir 目录及其所有子目录，
    对每个 .rar 文件解压到它所在目录的父目录中。
    """
    # os.walk 默认是自上而下遍历
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.rar'):
                rar_path = os.path.join(subdir, file)
                # 获取当前文件所在的上一级目录（即父目录）
                parent_dir = os.path.abspath(os.path.join(subdir, os.pardir))
                print(f'正在解压 {rar_path} 到 {parent_dir} ...')
                try:
                    # 打开 .rar 文件
                    with rarfile.RarFile(rar_path) as rf:
                        # 解压所有内容到父目录
                        rf.extractall(path=parent_dir)
                    print(f'解压成功：{rar_path}')
                except Exception as e:
                    print(f'解压失败：{rar_path}，错误信息：{e}')

if __name__ == '__main__':
    # 指定文件夹 A 的路径，例如 "C:\path\to\A"
    folder_A = r'D:\GameLauncher\folders'
    extract_rars_to_parent(folder_A)

import os
import tkinter as tk
from tkinter import filedialog, messagebox


def rename_files():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 打开文件选择对话框，让用户选择文件
    file_paths = filedialog.askopenfilenames(title="选择文件", filetypes=[("All Files", "*.*")])
    if not file_paths:
        return

    for file_path in file_paths:
        try:
            # 获取不带扩展名的文件名
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            # 创建新的 jpg 文件名
            new_file = base_name + '.jpg'
            # 构建完整的路径
            new_file_path = os.path.join(os.path.dirname(file_path), new_file)

            # 重命名文件
            os.rename(file_path, new_file_path)
            messagebox.showinfo("成功", f"已将文件 {file_path} 重命名为 {new_file}")
        except Exception as e:
            messagebox.showerror("错误", f"无法重命名文件 {file_path}: {e}")

    root.destroy()  # 销毁主窗口


if __name__ == "__main__":
    rename_files()

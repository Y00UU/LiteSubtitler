import os
import subprocess
import sys


def convert_ui_to_py(gui_folder: str = os.path.abspath(__file__), ui_filename: str = "all") -> None:
    """将ui文件转换成.py文件

    Args:
        gui_folder (str, optional): gui目录路径. 默认为当前.py文件所在目录.
        ui_filename (str, optional): ui文件名. "all"默认为gui文件夹下全部.ui文件.
    """
    if ui_filename == "all":
        for filename in os.listdir(gui_folder):
            if filename.endswith(".ui"):
                ui_file = os.path.join(gui_folder, filename)
                py_file = os.path.splitext(ui_file)[0] + ".py"
                command = f'pyuic6 "{ui_file}" -o "{py_file}"'
                print(f"Converting {ui_file} to {py_file}...")
                subprocess.run(command, shell=True)
    else:
        directory, _ = os.path.split(ui_filename)
        if os.path.exists(path=ui_filename):
            ui_filename_without_suffix, _ = os.path.splitext(os.path.basename(ui_filename))
            py_filename = os.path.join(directory, f"{ui_filename_without_suffix}.py")
            command = f'pyuic6 "{ui_filename}" -o "{py_filename}"'
            print(f"Converting {ui_filename} to py_filename...")
            subprocess.run(command, shell=True)


if __name__ == "__main__":
    gui_folder = os.path.abspath(__file__)
    if len(sys.argv) == 1:
        convert_ui_to_py()
    else:
        for i, arg in enumerate(sys.argv):
            if i == 0 and len(arg):
                gui_folder = os.path.abspath(arg)
            elif i == 1 and len(arg):
                convert_ui_to_py(gui_folder, arg)

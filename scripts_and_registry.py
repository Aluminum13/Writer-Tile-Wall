import os
import winreg as reg
import sys


# 检查是否支持 reconfigure 方法
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="GBK")
else:
    # 对于更老的 Python 版本，使用 io.TextIOWrapper
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='GBK')


def create_paint_bat(bat_path):
    # 创建 .bat 文件内容
    bat_content = f'@echo off\n' \
                  f'taskkill /F /IM pythonw.exe\n' \
                  f'echo Running {paint_path} at %date% %time% >> "{log_path}"\n' \
                  f'pythonw.exe "{paint_path}" >> "{log_path}" 2>&1\n' \
                  f'echo Running {scan_path} at %date% %time% >> "{log_path}"\n' \
                  f'start "" pythonw.exe "{scan_path}" >> "{log_path}" 2>&1'

    try:
        # 写入 .bat 文件
        with open(bat_path, 'w', encoding='gbk') as bat_file:
            bat_file.write(bat_content)
        print(f"'{bat_path}' 创建成功")
    except Exception as e:
        print(f"创建 .bat 文件时发生错误: {e}")


def create_scan_bat(bat_path):
    # 创建 .bat 文件内容
    bat_content = f'@echo off\n' \
                  f'taskkill /F /IM pythonw.exe\n' \
                  f'echo Running {scan_path} at %date% %time% >> "{log_path}"\n' \
                  f'start "" pythonw.exe "{scan_path}" >> "{log_path}" 2>&1'

    try:
        # 写入 .bat 文件
        with open(bat_path, 'w', encoding='gbk') as bat_file:
            bat_file.write(bat_content)
        print(f"'{bat_path}' 创建成功")
    except Exception as e:
        print(f"创建 .bat 文件时发生错误: {e}")


def add_to_startup(bat_path):
    # 获取 bat 文件的绝对路径
    bat_path = os.path.abspath(bat_path)

    # 注册表路径
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        # 打开注册表键（如果没有则创建）
        registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_WRITE)

        # 添加自启项
        reg.SetValueEx(registry_key, "ScanProgram", 0, reg.REG_SZ, f'"{bat_path}"')
        reg.CloseKey(registry_key)
        print(f"'{bat_path}' 已成功添加到开机自启项")

    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    scan_path = os.path.abspath("scan.py")
    paint_path = os.path.abspath("paint.py")
    log_path = os.path.abspath("log.txt")
    scan_bat_path = "open_scan.bat"
    paint_bat_path = "open_paint.bat"

    create_scan_bat(scan_bat_path)
    create_paint_bat(paint_bat_path)
    add_to_startup(os.path.abspath(scan_bat_path))

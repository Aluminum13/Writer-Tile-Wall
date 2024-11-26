import subprocess
import sys

# 定义需要安装的库
required_libraries = [
    "python-docx",  # docx
    "numpy",        # np
    "pandas",       # pd
    "matplotlib",   # plt
    "seaborn",      # sns
    "chardet"       # chardet
]

# 检查并安装缺少的库
def install_libraries():
    for library in required_libraries:
        if library == "python-docx":
            try:
                __import__(library.split('==')[0][7:])  # 尝试导入库
                print(f"{library} 已安装")
            except ImportError:
                print(f"{library} 未安装，正在安装...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", library])
                print(f"{library} 安装完成")
        else:
            try:
                __import__(library.split('==')[0])  # 尝试导入库
                print(f"{library} 已安装")
            except ImportError:
                print(f"{library} 未安装，正在安装...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", library])
                print(f"{library} 安装完成")

if __name__ == "__main__":
    install_libraries()
import os
import time
import json
import chardet
from tkinter import filedialog
import tkinter as tk
from datetime import datetime
from docx import Document


# 统计文本文件的字符数
def count_txt_length(file_path):
    with open(file_path, 'rb') as f:  # 以二进制模式打开文件
        raw_data = f.read()  # 读取文件的原始字节
        result = chardet.detect(raw_data)  # 使用chardet来检测编码
        encoding = result['encoding']  # 获取推测的编码类型

    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return len(f.read())  # 返回文件的字符数
    except UnicodeDecodeError:
        print(f"无法解码文件 {file_path}，可能是编码问题")
        return 0


# 统计 Word 文件的字符数
def count_word_length(file_path):
    doc = Document(file_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return len(text)


# 扫描目录并统计文件的总长度
def scan_directory(directory):
    total_length = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                if filename.endswith('.txt'):
                    file_length = count_txt_length(file_path)
                    print(f"已统计文件：{file_path}，字数{file_length}")
                    total_length += file_length
                elif (filename.endswith('.docx') or filename.endswith('.doc')) and not filename.startswith('~'):
                    try:
                        file_length = count_word_length(file_path)
                        print(f"已统计文件：{file_path}，字数{file_length}")
                        total_length += file_length
                    except Exception as e:
                        print(f"统计文件：{file_path}时发生错误：{e}")
    return total_length


# 记录数据到指定文件，格式：YYYY-MM-DD HH:MM:SS
def record_data(file_path, character_length):
    # 获取当前日期，格式为 YYYY-MM-DD HH:MM:SS
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 打开文件，追加数据
    with open(file_path, 'a', encoding='gbk') as f:
        f.write(f"{current_date} {character_length}\n")


def schedule_task():
    # 程序启动先进行一次扫描
    total_length = scan_directory(directory)
    print(f"总字数: {total_length}")
    record_data(file_path, total_length)

    while True:
        now = datetime.now()
        # 每天00:00执行扫描
        if now.hour == 0 and now.minute == 0:
            total_length = scan_directory(directory)
            print(f"总字数: {total_length}")
            record_data(file_path, total_length)
            time.sleep(80)  # 延迟以确保在分钟级别的时间点捕捉到

        time.sleep(20)  # 每20秒钟检查一次时间


def get_directory():
    # 设置路径文件
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'path_config.json')

    # 如果路径配置文件已存在，读取配置中的路径
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
            return config.get('directory', None)

    # 如果路径配置文件不存在，弹出文件对话框让用户选择路径
    else:
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        selected_path = filedialog.askdirectory(title="请选择一个目录")

        # 如果选择了目录，则保存路径
        if selected_path:
            config = {'directory': selected_path}
            with open(config_file, 'w') as f:
                json.dump(config, f)

        return selected_path


# 启动程序
if __name__ == "__main__":
    directory = get_directory()
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.dat")

    schedule_task()

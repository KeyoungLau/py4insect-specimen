# @author   :Keyoung
# @software :Pycharm
# @mtime    :2020-03-10
# @platform :WinNT
from checkFile import check_file
from countCard import count_card
from drawGrid import draw_grid
from tkinter import *

def main():
    # 检查读写文件
    read_file, save_file = check_file(".\\input-file\\昆虫86015后2019724_测试.csv", ".\\output-file\\test4.xlsx")
    # 计算需要多少卡片
    page = count_card(read_file)
    # 画卡片和处理数据
    draw_grid(page, read_file, save_file)

if __name__ == '__main__':
    main()



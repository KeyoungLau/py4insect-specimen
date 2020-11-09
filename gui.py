# 建立空白窗口，窗口默认的名称是tk
import sys
from tkinter import *
from tkinter.filedialog import askopenfilename
from checkFile import check_file
from countCard import count_card
from drawGrid import draw_grid
from pkg import gl

def start_work():
    # 检查读写文件
    read_file, save_file = check_file(file_in.get(), "123456.xlsx")
    # 计算需要多少卡片
    page = count_card(read_file)
    # 画卡片和处理数据
    draw_grid(page, read_file, save_file)


def get_file_path():
    # 获取输入文件名
    file_path = askopenfilename(title='选择CSV文件',
                                filetypes=[('*.csv', '*.CSV'), ('All Files', '*')], initialdir=r'C:\Users\Keyou\PycharmProjects\InsectSample')
    path.set(file_path)
    return file_path



root = Tk()
root.title("昆虫标本卡片制作工具v0.1")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 400
h = 300
x = int((screenWidth - w) / 2)  # 必须指定为整数，不然下面的geometry方法会报错
y = int((screenHeight - h) / 2)
root.geometry(f"{w}x{h}+{x}+{y}")
#root.configure(bg="lightgreen")  # 窗口背景颜色
root.resizable(False,False)  # 禁止调整窗口大小
root.iconbitmap("insect.ico")  # 更改图标
label = Label(root, text="输入文件\n请选择经过预处理的CSV格式文件",height=4,width=30,relief="groove",  bg="lightgreen")
#label.pack(anchor=N, side=LEFT, padx=10, pady=10)


btn = Button(root, text="开始运行", command=lambda : start_work())
#btn.pack()
btn.grid(row=1, column=0)

btn_choose_file = Button(root, text="选择文件", command=get_file_path)
btn_choose_file.grid(row=0, column=0)


path = StringVar()
file_in = Entry(root, text="输入文件：", textvariable=path)
#file_in.pack()
file_in.grid(row=0, column=1)


output_text = Text(root)
output_text.grid(row=2, column=0)
# 滚动条
yscrollbar = Scrollbar(root)
yscrollbar.grid(row=2, column=2, sticky=W)
yscrollbar.config(command=output_text.yview)
output_text.config(yscrollcommand=yscrollbar.set)


# 插入输入内容
print(gl.output_str)
#output_text.insert(END, gl.output_str)
output_text.see(END)
output_text.update()

def redirector(inputStr):
    output_text.insert(INSERT, inputStr)

sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.


import sys
from tkinter import *
from tkinter.filedialog import askopenfilename
from checkFile import check_file, generate_time_stamp
from countCard import count_card
from drawGrid import draw_grid
from tkinter import messagebox



# 定义函数
def start_work():
    # 检查读写文件
    read_file, save_file = check_file(file_in.get(), "数据处理" + generate_time_stamp()+".xlsx")
    # 计算需要多少卡片
    page = count_card(read_file)
    # 画卡片和处理数据
    draw_grid(page, read_file, save_file)
    messagebox.showinfo("Message Box", "数据处理完成")

def get_file_path():
    # 获取输入文件名
    file_path = askopenfilename(title='选择CSV文件',
                                filetypes=[('*.csv', '*.CSV'), ('All Files', '*')], initialdir=r'C:\Users\Keyou\PycharmProjects\InsectSample')
    path.set(file_path)
    return file_path

# 定义一个重定向输出函数
def redirector(inputStr):
    output_text.insert(INSERT, inputStr)

sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.

root = Tk()
# root是Tk类的实例化
root.title("昆虫标本卡片制作程序")
# 设置一些长宽
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 400
h = 300
x = int((screenWidth - w) / 2)  # 必须指定为整数，不然下面的geometry方法会报错
y = int((screenHeight - h) / 2)
root.geometry(f"{w}x{h}+{x}+{y}")
root.resizable(False, False)  # 禁止调整窗口大小
root.iconbitmap(r".\static\insect.ico")  # 更改图标

# 定义一个要用到的变量
path = StringVar()


# 实例化两个按钮
btn_start_work = Button(root, text="开始运行", font="Times 10 bold", fg="white", bg="blue", command=lambda : start_work())
btn_choose_file = Button(root, text="选择文件",font="Times 10 bold",fg="white", bg="red", command=get_file_path)
#btn_start_work.pack(anchor=NW, side=LEFT, pady=10, padx=10)
btn_start_work.place(x=10, y=10)
btn_choose_file.place(x=105, y=10)

#btn_choose_file.pack(anchor=NW,side=LEFT, pady=10)


# 定义一个输入文本框
file_in = Entry(root, text="输入文件：", textvariable=path, relief="groove")
file_in.place(x=200, y=15)


# 定义一个输出文本框
output_text = Text(root, width=31, height=9, font="微软雅黑", bg="lightgreen", fg="blue")
output_text.place(x=10, y=60)
output_text.see(END)
output_text.update()



if __name__ == '__main__':
    root.mainloop()
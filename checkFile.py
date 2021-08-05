# 文件检查模块，主要用于检查目录下是否存同名文件

def generate_time_stamp():
    """
    生成一个统一的时间戳，用于文件命名
    :return:
    """
    from datetime import datetime
    nowTime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return nowTime




def check_file(read_filename: str, save_filename: str):
    # 文件检查函数，检查目录下是否存同名文件，若存在，则视情况删除
    import os
    path = os.getcwd()
    print(f"读取文件<{read_filename}>\n保存文件名为<{save_filename}>\n保存路径为<{path}>")
    # 检查文件类型
    if read_filename[-3:].lower() != "csv":
        output_str = "传入文件不是csv文件......"
        print(output_str)

    try:
        if os.path.exists(save_filename):
            os.remove(save_filename)
            print("该目录下存在同名文件<{}>。".format(save_filename))
            #prompt = "是否要删除文件<{}>，请输入y/n ".format(save_filename)
            #sign = input(prompt)
            # if sign.lower() == "y":
            #     os.remove(save_filename)
            #     print("<{}>已经删除。".format(save_filename))
            # else:
            #     print("程序退出。")
            #     exit()
        else:
            print("该目录下无同名文件<{}>。".format(save_filename))
    except PermissionError:
        print("另一个程序正在使用<{}>文件，请关闭该文件后重试。".format(save_filename))
        exit()
    # 返回要读取的文件名
    return read_filename, save_filename


if __name__ == '__main__':
    a, b = check_file("昆虫86015后2019724_测试.csv", "文件名称2.xlsx")
    print(a)
    print(b)

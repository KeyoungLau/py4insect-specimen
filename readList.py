# 读取csv文件形成一个列表
def read_csv_to_list(readfile):
    import csv
    lst = []
    with open(readfile, 'r', encoding='UTF-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            lst.append(line)
    return list(reversed(lst))


if __name__ == '__main__':
    lst = read_csv_to_list("昆虫86015后2019724_测试.csv")
    while lst:
        a = lst.pop()
        print(a)
    print(lst)
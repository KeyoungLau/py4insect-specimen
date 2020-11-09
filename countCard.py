# 计算传入的CSV文件需要多少张卡片


def count_card(file):
    """
    该函数用于计算需要多少张卡片
    :return:
    """
    import csv
    import math
    fobj = open(file, 'r', encoding='UTF-8-sig')
    print("读取<{}>文件\n计算所需卡片数量中...".format(file))
    reader = csv.reader(fobj)
    lst = [item[7] for item in reader]  # 7表示用学名来对比
    # print(lst)
    need_card = None

    # 只有一个物种的特殊情况
    if len(set(lst)) == 1:
        need_card += math.ceil(len(lst) / 10)
        print("<{}>文件需要画{}张卡片。".format(file, need_card))
        return need_card

    # 至少有两种物种的情况
    need_card = 0
    inner_card_count = 1
    tmp_item = lst.pop(0)
    while lst:
        if tmp_item == lst[0]:
            inner_card_count += 1
            # print(inner_card_count)
            tmp_item = lst.pop(0)
        else:
            # print(inner_card_count)
            need_card += math.ceil(inner_card_count / 10)
            tmp_item = lst.pop(0)
            inner_card_count = 1

    # 这里最后还要算一次，因为最后的inner_card_count不会计算到就跳出循环了
    need_card += math.ceil(inner_card_count / 10)
    print("<{}>文件需要画{}张卡片。".format(file, need_card))
    return need_card


if __name__ == '__main__':
    # a = count_card("昆虫86015后2019724_测试.csv")
    count_card("昆虫86015后2019724_测试.csv")
    # print(a)

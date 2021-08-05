# -*- coding:utf-8 -*-
# author：keyoung
# email：keyoung.lau@qq.com
# date：2019-10-11
def draw_grid(amount_card, read_file, savefile_name):
    from readList import read_csv_to_list
    import xlsxwriter

    workbook = xlsxwriter.Workbook(savefile_name)     # 新建excel表
    worksheet = workbook.add_worksheet('sheet1')       # 新建sheet（sheet的名称为"sheet1"）

    # 设置右对齐格式
    align_right = workbook.add_format()
    align_right.set_align("right")
    align_right.set_bottom(1)
    align_right.set_bottom_color("black")

    # 设置单元格格式1
    border1 = workbook.add_format()
    border1.set_bottom(1)
    border1.set_bottom_color("black")

    # 设置单元格格式2
    border2 = workbook.add_format()
    border2.set_left(2)
    border2.set_left_color("black")
    border2.set_right(2)
    border2.set_right_color("black")
    border2.set_top(2)
    border2.set_top_color("black")
    border2.set_bottom(1)
    border2.set_bottom_color("black")
    border2.set_valign("vcenter")
    border2.set_align("center")

    # 设置单元格格式3
    border3 = workbook.add_format()
    border3.set_left(1)
    border3.set_left_color("black")
    border3.set_right(1)
    border3.set_right_color("black")
    border3.set_top(1)
    border3.set_top_color("black")
    border3.set_bottom(1)
    border3.set_bottom_color("black")

    # 设置一个9号字体
    border3_with_smaller_font = workbook.add_format()
    border3_with_smaller_font.set_left(1)
    border3_with_smaller_font.set_left_color("black")
    border3_with_smaller_font.set_right(1)
    border3_with_smaller_font.set_right_color("black")
    border3_with_smaller_font.set_top(1)
    border3_with_smaller_font.set_top_color("black")
    border3_with_smaller_font.set_bottom(1)
    border3_with_smaller_font.set_bottom_color("black")
    border3_with_smaller_font.set_font_size(9)

    # 设置一个8号字体
    border3_with_very_smaller_font = workbook.add_format()
    border3_with_very_smaller_font.set_left(1)
    border3_with_very_smaller_font.set_left_color("black")
    border3_with_very_smaller_font.set_right(1)
    border3_with_very_smaller_font.set_right_color("black")
    border3_with_very_smaller_font.set_top(1)
    border3_with_very_smaller_font.set_top_color("black")
    border3_with_very_smaller_font.set_bottom(1)
    border3_with_very_smaller_font.set_bottom_color("black")
    border3_with_very_smaller_font.set_font_size(8)

    # 设置一个居中格式
    border3_with_center = workbook.add_format()
    border3_with_center.set_left(1)
    border3_with_center.set_left_color("black")
    border3_with_center.set_right(1)
    border3_with_center.set_right_color("black")
    border3_with_center.set_top(1)
    border3_with_center.set_top_color("black")
    border3_with_center.set_bottom(1)
    border3_with_center.set_bottom_color("black")
    border3_with_center.set_align("center")

    # rewrite drawGrid
    rownum = 0
    colnum = 0
    print("绘制卡片中......")

    # 这里稍微处理一下amount_card，使得画卡片的时候永远是偶数张卡片，方便打印控制，而且不会使处理数据的时候混乱
    if amount_card % 2 == 0:
        draw_card_amount = amount_card
    else:
        draw_card_amount = amount_card + 1

    for page in range(draw_card_amount):
        if rownum >= (amount_card * 18) / 2:  # 一个格子需要18行
            # 这是控制换列
            colnum = 5
            rownum = 0
        # 写前三行
        worksheet.write(rownum, colnum, "科  名")
        worksheet.write(rownum + 1, colnum, "学  名")
        worksheet.write(rownum + 2, colnum, "中  名")

        worksheet.write(rownum, colnum + 1, None, border1)
        worksheet.write(rownum + 1, colnum + 1, None, border1)
        worksheet.write(rownum + 2, colnum + 1, None, border1)

        worksheet.write(rownum + 4, colnum, "登记号", border2)
        worksheet.write(rownum + 4, colnum + 1, "采集地点", border2)
        worksheet.write(rownum + 4, colnum + 2, "采集日期", border2)
        worksheet.write(rownum + 4, colnum + 3, "标本概况", border2)

        worksheet.write(rownum + 9, colnum, "登记号", border2)
        worksheet.write(rownum + 9, colnum + 1, "采集地点", border2)
        worksheet.write(rownum + 9, colnum + 2, "采集日期", border2)
        worksheet.write(rownum + 9, colnum + 3, "标本概况", border2)

        # 写个编号吧，如果不需要可以用随时注释掉
        worksheet.write(rownum, colnum + 3, "第{}张".format(page + 1), align_right)

        # 设置样式
        worksheet.set_column(0, 0, 7.22)  # 设置A列宽度
        worksheet.set_column(5, 5, 7.22)  # 设置F列宽度
        worksheet.set_column(2, 2, 11.22)  # 设置C列宽度
        worksheet.set_column(7, 7, 11.22)  # 设置H列宽度
        worksheet.set_column(1, 1, 14.22)  # 设置B列宽度
        worksheet.set_column(6, 6, 14.22)  # 设置G列宽度
        worksheet.set_column(3, 3, 25.22)  # 设置D列宽度
        worksheet.set_column(8, 8, 25.22)  # 设置I列宽度
        worksheet.set_column(4, 4, 5.11)  # 设置E列宽度,为了裁纸的时候舒服一点

        # 调整行高
        worksheet.set_row(rownum, 25.0, None)
        worksheet.set_row(rownum + 1, 25.0, None)
        worksheet.set_row(rownum + 2, 25.0, None)
        worksheet.set_row(rownum + 4, 20.6, None)
        worksheet.set_row(rownum + 5, 20.6, None)
        worksheet.set_row(rownum + 6, 20.6, None)
        worksheet.set_row(rownum + 7, 20.6, None)

        worksheet.set_row(rownum + 9, 20.6, None)
        worksheet.set_row(rownum + 10, 20.6, None)
        worksheet.set_row(rownum + 11, 20.6, None)
        worksheet.set_row(rownum + 12, 20.6, None)
        worksheet.set_row(rownum + 13, 20.6, None)
        worksheet.set_row(rownum + 14, 20.6, None)
        worksheet.set_row(rownum + 15, 20.6, None)
        worksheet.set_row(rownum + 16, 20.6, None)
        worksheet.set_row(rownum + 17, 118.7, None)

        worksheet.write_blank(rownum, colnum + 2, "", border1)
        worksheet.write_blank(rownum + 1, colnum + 2, "", border1)
        worksheet.write_blank(rownum + 1, colnum + 3, "", border1)
        worksheet.write_blank(rownum + 2, colnum + 2, "", border1)
        worksheet.write_blank(rownum + 2, colnum + 3, "", border1)

        for j in range(5, 8):
            for q in range(0, 4):
                worksheet.write_blank(rownum + j, colnum + q, "", border3)

        for j in range(10, 17):
            for q in range(0, 4):
                worksheet.write_blank(rownum + j, colnum + q, "", border3)
        rownum = rownum + 18

    # 这里定义一个内部函数，用来把学名的种名属名（specific_generic_name）和作者（author）分离出来
    def split_scientific_name(scientific_name: str):
        import re
        global specific_generic_name, author_name
        specific_generic_name = re.findall("(^[A-Z].*? .*?) .*", scientific_name)
        if specific_generic_name:
            specific_generic_name = specific_generic_name[0]
            author_name = scientific_name[len(specific_generic_name) + 1:]
        if len(author_name) == 0:
            author_name = " "
        return specific_generic_name, author_name

    # rewrite handleListDate(重写老版的handleListDate)
    print("处理数据中......")
    lst = read_csv_to_list(read_file)
    amount_of_lst = len(lst)
    current_row = lst.pop()  # 抽出数据

    italic = workbook.add_format({'italic': True})
    rownum = 0  # 行号
    colnum = 0  # 列号

    # 这里可以选者两种对比方式，7是选择学名,感觉科学一点
    check_name = current_row[7]
    # 先把第一个给填了，等会再来对比分析

    generic_name, author = split_scientific_name(current_row[7])

    worksheet.write(rownum, colnum + 1, current_row[2], border1)  # 写科名
    worksheet.write_rich_string(rownum + 1, colnum + 1,  italic, f"{generic_name} ", f"{author}", border1)  # 写学名
    worksheet.write(rownum + 2, colnum + 1, current_row[1], border1)  # 写中文名

    worksheet.write(rownum + 5, colnum, current_row[0], border3)  # 写登记号
    if len(current_row[10]) < 8:
        worksheet.write(rownum + 5, colnum + 1, current_row[10], border3)  # 写采集地点
    else:
        worksheet.write(rownum + 5, colnum + 1, current_row[10], border3_with_smaller_font)  # 写采集地点
    worksheet.write(rownum + 5, colnum + 2, current_row[13], border3_with_center)  # 写采集日期
    if len(current_row[11] + "采集 " + current_row[12]) < 17:
        worksheet.write(rownum + 5, colnum + 3, current_row[11] + "采集 " + current_row[12], border3)  # 写标本概况
    elif 17 <= len(current_row[11] + "采集 " + current_row[12]) < 24:
        worksheet.write(rownum + 5, colnum + 3, current_row[11] + "采集 " + current_row[12], border3_with_smaller_font)  # 写标本概况
    else:
        worksheet.write(rownum + 5, colnum + 3, current_row[11] + "采集 " + current_row[12],
                        border3_with_very_smaller_font)  # 写标本概况

    # 第一条数据录完之后就要对比分析了
    row_counter = 1  # 设置一个行计数器

    while lst:  # 当列表lst不为空，就不断抽取数据
        if rownum > (amount_card * 18) / 2:  # 这个是控制换到另一边
            colnum = 5
            rownum = 0
        current_row = lst.pop()  # 又抽取一条数据
        if current_row[7] == check_name:
            if row_counter == 3:
                # 因为要空一行，所以要多加一个判断
                row_counter = 5
            if row_counter > 11:
                # 大于这么多就准备换页了
                row_counter = 0
                rownum = rownum + 18
                if rownum >= (page * 9) + 1:  # 这个数字应该还要计算一下,天灵灵地灵灵，保佑不出错
                    rownum = 0
                    colnum = 5
            generic_name, author = split_scientific_name(current_row[7])
            worksheet.write(rownum, colnum + 1, current_row[2], border1)  # 写科名
            worksheet.write_rich_string(rownum + 1, colnum + 1, italic, f"{generic_name} ", f"{author}", border1)  # 写学名
            worksheet.write(rownum + 2, colnum + 1, current_row[1], border1)  # 写中文名
            # 如果相等，意思就是同一种标本
            # 同一种标本就不用再写科名，学名和中文名了
            worksheet.write(rownum + 5 + row_counter, colnum, current_row[0], border3)  # 写登记号
            if len(current_row[10]) < 8:
                worksheet.write(rownum + 5 + row_counter, colnum + 1, current_row[10], border3)  # 写采集地点
            else:
                worksheet.write(rownum + 5 + row_counter, colnum + 1, current_row[10], border3_with_smaller_font)  # 写采集地点
            worksheet.write(rownum + 5 + row_counter, colnum + 2, current_row[13], border3_with_center)  # 写采集日期
            if len(current_row[11] + "采集 " + current_row[12]) < 17:
                worksheet.write(rownum + 5 + row_counter, colnum + 3, current_row[11] + "采集 " + current_row[12], border3)  # 写标本概况
            elif 17 <= len(current_row[11] + "采集 " + current_row[12]) < 24:
                worksheet.write(rownum + 5 + row_counter, colnum + 3, current_row[11] + "采集 " + current_row[12],
                                border3_with_smaller_font)  # 写标本概况
            else:
                worksheet.write(rownum + 5 + row_counter, colnum + 3, current_row[11] + "采集 " + current_row[12],
                                border3_with_very_smaller_font)  # 写标本概况

            row_counter = row_counter + 1
        else:
            # 这是不等于的情况，意思就是不是同一种标本
            # 就要跳到下一页去了
            rownum = rownum + 18
            # 在前后不同的情况下也要考虑换列的情况
            if rownum >= (page * 9) + 1:
                rownum = 0
                colnum = 5

            generic_name, author = split_scientific_name(current_row[7])
            worksheet.write(rownum, colnum + 1, current_row[2], border1)  # 写科名
            worksheet.write_rich_string(rownum + 1, colnum + 1, italic, f"{generic_name} ", f"{author}", border1)  # 写学名
            worksheet.write(rownum + 2, colnum + 1, current_row[1], border1)  # 写中文名

            worksheet.write(rownum + 5, colnum, current_row[0], border3)  # 写登记号
            if len(current_row[10]):
                worksheet.write(rownum + 5, colnum + 1, current_row[10], border3)  # 写采集地点
            else:
                worksheet.write(rownum + 5, colnum + 1, current_row[10], border3_with_smaller_font)  # 写采集地点
            worksheet.write(rownum + 5, colnum + 2, current_row[13], border3_with_center)  # 写采集日期
            if len(current_row[11] + "采集 " + current_row[12]) < 17:
                worksheet.write(rownum + 5, colnum + 3, current_row[11] + "采集 " + current_row[12], border3)  # 写标本概况
            elif 17 <= len(current_row[11] + "采集 " + current_row[12]) < 24:
                worksheet.write(rownum + 5, colnum + 3, current_row[11] + "采集 " + current_row[12], border3_with_smaller_font)  # 写标本概况
            else:
                worksheet.write(rownum + 5, colnum + 3, current_row[11] + "采集 " + current_row[12],
                                border3_with_very_smaller_font)

            # 再把check_name重新赋值一下
            check_name = current_row[7]
            row_counter = 1

    workbook.close()
    print(f"数据处理完成，一共处理{amount_of_lst}条数据。")
    print(f"保存文件<{savefile_name}>。")
    print("-"*46)
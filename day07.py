from turtle import st

import numpy as np
import xlrd

# 拿到工作簿
wb = xlrd.open_workbook(filename=r"C:\Users\微软微软\Desktop\python学习新\day7\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("1月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服一月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤一月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣一月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草一月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血一月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫一月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣一月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤一月销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲一月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装一月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣一月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣一月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤一月销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)

# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("2月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服二月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤二月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣二月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草二月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血二月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫二月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣二月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤二月销总售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲二月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装二月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣二月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣二月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲二月裤销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)

# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("3月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服三月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤三月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣三月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草三月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血三月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫三月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣三月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤三月销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲三月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装三月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣三月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣三月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤三月销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)

# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("4月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服四月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤四月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣四月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草四月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血四月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫四月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣四月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤四月销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲四月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装四月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣四月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣四月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤四月销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)

# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("5月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服五月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤五月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣五月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草五月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血五月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫五月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣五月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤五月销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲五月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装五月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣五月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣五月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤五月销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)

# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("6月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服六月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤六月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣六月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草六月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血六月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫六月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣六月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤六月销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲六月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装六月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣六月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣六月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤六月销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)

# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("7月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服7月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤7月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣7月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草7月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血7月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫7月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣7月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤7月销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲7月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装7月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣7月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣7月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤7月销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)
# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("8月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服8月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤8月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣8月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草8月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血8月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫8月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣8月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤8月销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲8月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装8月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣8月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣8月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤8月销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)
# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("9月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服9月销总售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤9月销总售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣9月销总售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草9月销总售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血9月销总售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫9月销总售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣9月销总售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤9月销总售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲9月销总售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装9月销总售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣9月销总售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣9月销总售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤9月销总售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)


# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("10月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服10月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤10月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣10月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草10月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血10月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫10月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣10月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤10月销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲10月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装10月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣10月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣10月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤10月销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)

# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("11月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服11月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤11月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣11月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草11月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血11月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫11月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣11月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤11月销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲11月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装11月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣11月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣11月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤11月销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)
# # 选择一个选项卡
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
st1 = wb.sheet_by_name("12月")
rows1 = st1.nrows #获取有多少行
sal_sum1 = 0
for j in range(1,rows1):
    data = st1.row_values(j)
    if data[1] == str("羽绒服"):
        num_sum1=num_sum1+data[4]
    elif data[1] == str("牛仔裤"):
        num_sum2=num_sum2+data[4]
    elif data[1] == str("风衣"):
        num_sum3 = num_sum3 + data[4]
    elif data[1] == str("皮草"):
        num_sum4 = num_sum4 + data[4]
    elif data[1] == str("T血"):
        num_sum5 = num_sum5 + data[4]
    elif data[1] == str("衬衫"):
        num_sum6 = num_sum6 + data[4]
    elif data[1] == str("卫衣"):
        num_sum7 = num_sum7 + data[4]
    elif data[1] == str("铅笔裤"):
        num_sum8 = num_sum8 + data[4]
    elif data[1] == str("马甲"):
        num_sum9 = num_sum9 + data[4]
    elif data[1] == str("小西装"):
        num_sum10 = num_sum10 + data[4]
    elif data[1] == str("棉衣"):
        num_sum11 = num_sum11 + data[4]
    elif data[1] == str("皮衣"):
        num_sum12 = num_sum12 + data[4]
    elif data[1] == str("休闲裤"):
        num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服12月销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤12月销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣12月销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草12月销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血12月销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫12月销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣12月销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤12月销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲12月销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装12月销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣12月销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣12月销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤12月销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)


#####全年销售总额
wb_len=len(wb.sheets())
sal_sum = 0
for i in range(wb_len):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    for j in range(1,rows):
        data = st.row_values(j)
        a = data[2]*data[4]
        sal_sum=sal_sum +a
print("全年总销售额为：",sal_sum)


#####每件衣服的销售（件数）占比
wb_len=len(wb.sheets())
num_sum1 = 0
num_sum2 = 0
num_sum3 = 0
num_sum4 = 0
num_sum5 = 0
num_sum6 = 0
num_sum7 = 0
num_sum8 = 0
num_sum9 = 0
num_sum10 = 0
num_sum11 = 0
num_sum12 = 0
num_sum13 = 0
for i in range(wb_len):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    for j in range(1,rows):
        data = st.row_values(j)
        if data[1] == str("羽绒服"):
            num_sum1=num_sum1+data[4]
        elif data[1] == str("牛仔裤"):
            num_sum2=num_sum2+data[4]
        elif data[1] == str("风衣"):
            num_sum3 = num_sum3 + data[4]
        elif data[1] == str("皮草"):
            num_sum4 = num_sum4 + data[4]
        elif data[1] == str("T血"):
            num_sum5 = num_sum5 + data[4]
        elif data[1] == str("衬衫"):
            num_sum6 = num_sum6 + data[4]
        elif data[1] == str("卫衣"):
            num_sum7 = num_sum7 + data[4]
        elif data[1] == str("铅笔裤"):
            num_sum8 = num_sum8 + data[4]
        elif data[1] == str("马甲"):
            num_sum9 = num_sum9 + data[4]
        elif data[1] == str("小西装"):
            num_sum10 = num_sum10 + data[4]
        elif data[1] == str("棉衣"):
            num_sum11 = num_sum11 + data[4]
        elif data[1] == str("皮衣"):
            num_sum12 = num_sum12 + data[4]
        elif data[1] == str("休闲裤"):
            num_sum13 = num_sum13 + data[4]
sum_num=num_sum1+num_sum2+num_sum3+num_sum4+num_sum5+num_sum6+num_sum7+num_sum8+num_sum9+num_sum10+num_sum11+num_sum12+num_sum13
print("羽绒服全年总销售件数为：",num_sum1,"销售件数占比为:",num_sum1/sum_num)
print("牛仔裤全年总销售件数为：",num_sum2,"销售件数占比为:",num_sum2/sum_num)
print("风衣全年总销售件数为：",num_sum3,"销售件数占比为:",num_sum3/sum_num)
print("皮草全年总销售件数为：",num_sum4,"销售件数占比为:",num_sum4/sum_num)
print("T血全年总销售件数为：",num_sum5,"销售件数占比为:",num_sum5/sum_num)
print("衬衫全年总销售件数为：",num_sum6,"销售件数占比为:",num_sum6/sum_num)
print("卫衣全年总销售件数为：",num_sum7,"销售件数占比为:",num_sum7/sum_num)
print("铅笔裤全年总销售件数为：",num_sum8,"销售件数占比为:",num_sum8/sum_num)
print("马甲全年总销售件数为：",num_sum9,"销售件数占比为:",num_sum9/sum_num)
print("小西装全年总销售件数为：",num_sum10,"销售件数占比为:",num_sum10/sum_num)
print("棉衣全年总销售件数为：",num_sum11,"销售件数占比为:",num_sum11/sum_num)
print("皮衣全年总销售件数为：",num_sum12,"销售件数占比为:",num_sum12/sum_num)
print("休闲裤全年总销售件数为：",num_sum13,"销售件数占比为:",num_sum13/sum_num)


nums= ["羽绒服",num_sum1,"牛仔裤",num_sum2,"风衣",num_sum3,"皮草",num_sum4,"T血",num_sum5,"衬衫",num_sum6,"卫衣",num_sum7,"铅笔裤",num_sum8,"马甲",num_sum9,"小西装",num_sum10,"棉衣",num_sum11,"皮衣",num_sum12,"休闲裤",num_sum13]
nums2= [["羽绒服",num_sum1],["牛仔裤",num_sum2],["风衣",num_sum3],["皮草",num_sum4],["T血",num_sum5],["衬衫",num_sum6],["卫衣",num_sum7],["铅笔裤",num_sum8],["马甲",num_sum9],["小西装",num_sum10],["棉衣",num_sum11],["皮衣",num_sum12],["休闲裤",num_sum13]]

########最畅销的衣服是那种
a=int(0)
for index, value in enumerate(nums):
    if isinstance(value, str):
        a=a
    else:
        if a>=value:
            a=a
        if a<value:
            a=value
x = [i for i in nums2 if a in i]
print("最畅销的衣服是:",x,"件")


#######全年销量最低的衣服
b=int(9999999999999)
for index, value in enumerate(nums):
    if isinstance(value, str):
        b=b
    else:
        if b>=value:
            b=value
        if b<value:
            b=b
y = [i for i in nums2 if b in i]
print("全年销量最低的衣服是",y,"件")










#####总销售额占比
wb_len=len(wb.sheets())
sal_sum1 = 0
sal_sum2 = 0
sal_sum3 = 0
sal_sum4 = 0
sal_sum5 = 0
sal_sum6 = 0
sal_sum7 = 0
sal_sum8 = 0
sal_sum9 = 0
sal_sum10 = 0
sal_sum11 = 0
sal_sum12 = 0
sal_sum13 = 0

for i in range(wb_len):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    for j in range(1,rows):
        data = st.row_values(j)
        if data[1]==str("羽绒服"):
            a = data[2]*data[4]
            sal_sum1=sal_sum1+a
        elif data[1] == str("牛仔裤"):
            a = data[2] * data[4]
            sal_sum2 = sal_sum2 + a
        elif data[1] == str("风衣"):
            a = data[2] * data[4]
            sal_sum3 = sal_sum3 + a
        elif data[1] == str("皮草"):
            a = data[2] * data[4]
            sal_sum4 = sal_sum4 + a
        elif data[1] == str("T血"):
            a = data[2] * data[4]
            sal_sum5 = sal_sum5 + a
        elif data[1] == str("衬衫"):
            a = data[2] * data[4]
            sal_sum6 = sal_sum6 + a
        elif data[1] == str("卫衣"):
            a = data[2] * data[4]
            sal_sum7 = sal_sum7 + a
        elif data[1] == str("铅笔裤"):
            a = data[2] * data[4]
            sal_sum8 = sal_sum8 + a
        elif data[1] == str("马甲"):
            a = data[2] * data[4]
            sal_sum9 = sal_sum9 + a
        elif data[1] == str("小西装"):
            a = data[2] * data[4]
            sal_sum10 = sal_sum10 + a
        elif data[1] == str("棉衣"):
            a = data[2] * data[4]
            sal_sum11 = sal_sum11 + a
        elif data[1] == str("皮衣"):
            a = data[2] * data[4]
            sal_sum12 = sal_sum12 + a
        elif data[1] == str("休闲裤"):
            a = data[2] * data[4]
            sal_sum13 = sal_sum13 + a
sum_sal =sal_sum1+sal_sum2+sal_sum3+sal_sum4+sal_sum5+sal_sum6+sal_sum7+sal_sum8+sal_sum9+sal_sum10+sal_sum11+sal_sum12+sal_sum13
print("羽绒服全年总销售额为：",sal_sum1,"销售额占比为：",sal_sum1/sum_sal)
print("牛仔裤全年总销售额为：",sal_sum2,"销售额占比为：",sal_sum2/sum_sal)
print("风衣全年总销售额为：",sal_sum3,"销售额占比为：",sal_sum3/sum_sal)
print("皮草全年总销售额为：",sal_sum4,"销售额占比为：",sal_sum4/sum_sal)
print("T血全年总销售额为：",sal_sum5,"销售额占比为：",sal_sum5/sum_sal)
print("衬衫全年总销售额为：",sal_sum6,"销售额占比为：",sal_sum6/sum_sal)
print("卫衣全年总销售额为：",sal_sum7,"销售额占比为：",sal_sum7/sum_sal)
print("铅笔裤全年总销售额为：",sal_sum8,"销售额占比为：",sal_sum8/sum_sal)
print("马甲全年总销售额为：",sal_sum9,"销售额占比为：",sal_sum9/sum_sal)
print("小西装全年总销售额为：",sal_sum10,"销售额占比为：",sal_sum10/sum_sal)
print("棉衣全年总销售额为：",sal_sum11,"销售额占比为：",sal_sum11/sum_sal)
print("皮衣全年总销售额为：",sal_sum12,"销售额占比为：",sal_sum12/sum_sal)
print("休闲裤全年总销售额为：",sal_sum13,"销售额占比为：",sal_sum13/sum_sal)
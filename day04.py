# num = int(input("请输入一个数字："))
# while num != 0:
#     print(num % 10)
#     num = num // 10
# 运行结果
# 请输入一个数字：12345
# 5
# 4
# 3
# 2
# 1
#
# 进程已结束，退出代码为 0





# print('姓名  年龄  性别  编号   任职公司   薪资   部门编号')
# names = [
#     ["曹操", "56", "男", "106", "IBM", 500, "50"],
#     ["大乔", "19", "女", "230", "微软", 501, "60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700, "10"]]
#
# num = []
# count =0
# for i in range(len(names)):
#     print(names[i])
#     num.append(names[i][5])
#     count +=1
# print(num)
# print("count =",count)
######## 1.统计每个人的平均薪资
# total = sum(num)
# print(total)
# avg = total/count
# print("平均薪资：", int(avg))
#
########## 2.统计每个人的平均年龄
# num1 = []
# count =0
# for k in range(len(names)):
#     num1.append(int(names[k][1]))
#     count +=1
# avg = sum(num1)/count
# print("平均年龄：", int(avg))
#
###########3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
# names.append(['刘备', '45', '男', '220,', 'alibaba', 500, '30'])
# for i in range(len(names)):
#     print(names[i])
#
#########4.统计公司男女人数
# count = count1 = 0
# for i in names:
#     if i[2] == '男':
#         count += 1
#     else:
#         count1 += 1
# print('公司男：', count, '人', '\t', '公司女：', count1, '人')
####5.每个部门的人数








# names = {
#        "罗恩":[23,35,44],
#        "哈利":[60,77,68,88,90],
#        "赫敏":[97,99,89,91,95,90],
#        "马尔福":[100,85,90]
# }
# for key in names:
#     print(key, "总成绩:",sum(names[key]))













# a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
# print(a)
# a.sort()
# print(a)


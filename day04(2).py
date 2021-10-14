######1、请循环遍历出所有的key
######2、请循环遍历出所有的value
######3、请在字典中增加一个键值对,"k4":"v4"


# dict={
#       "k1":"v1",
#       "k2":"v2",
#       "k3":"v3"
#      }
# for key,value in dict.items():
#     print(key)
# for key, value in dict.items():
#     print(value)
# dict2 ={"k4":"v4"}
# dict.update(dict2)
# print(dict)






###########小明去超市购买水果，账单如下
##########请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
##########用水果名称做key，金额做value，创建一个字典
# info = {
#     "苹果":32.8,
#     "香蕉": 22,
#     "葡萄": 15.5
# }
# name =str(input("输入水果名"))
# for key,value in info.items():
#     if key == str(name):
#         print(value)
#     else:
#         print("没有这种水果")






###########小明，小刚去超市里购买水果
###########小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
###########以姓名做key，value仍然是字典

# Fruits = {
# 	  "苹果":12.3,
# 	  "草莓":4.5,
#       "香蕉":6.3,
#       "葡萄":5.8,
#       "橘子":6.4,
#       "樱桃":15.8
# }
# info = {
#     "小明": {
#         "fruits": {"苹果":4, "草莓":13, "香蕉":10},
#         "money":"a"
#     },
#     "小刚": {
#         "fruits": {"葡萄":19, "橘子":12, "樱桃":30},
#         "money":"b"
#     }
# }
# name =str(input("输入水果名"))
# for key1,value1 in Fruits.items():
#     if key1 == str(name):
#         print(key1,"单价为:",value1)
#         price =value1
# for key2, value2 in info["小明"]["fruits"].items():
#     if key2 == str(name):
#         print(name,"购买数量为:",value2)
#         qua1 =value2
#         a=price*qua1
# dict={name:a}
# print(dict)
# for key3, value3 in info["小刚"]["fruits"].items():
#     if key3 == str(name):
#         print(name,"购买数量为:",value3)
#         qua2 =value3
#         b=price*qua2
#     dict={name:b}
#     print(dict)





##################有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# names = {"姓名":{"刘备":{"年龄":"56","性别":"男","编号":"106","任职公司":"IBM","薪资":500,"部门编号":"50"},
#                 "大乔":{"年龄":"19","性别":"女","编号":"230","任职公司":"微软","薪资":501,"部门编号":"60"},
#                 "小乔":{"年龄":"19","性别":"女","编号":"210","任职公司":"Oracle","薪资":600,"部门编号":"60"},
#                 "张飞":{"年龄":"45","性别":"男","编号":"230","任职公司":"Tencent","薪资":700,"部门编号":"10"}}
# }
# for key,value in names.items():
#     print(key)
# for key, value in names.items():
#     print(value)





# Friuts = {
#     '苹果': 12.3,  # 水果和单价
#     '草莓': 4.5,
#     '香蕉': 6.3,
#     '葡萄': 5.8,
#     '橘子': 6.4,
#     '樱桃': 15.8
# }
#
# info = {
#     '小明': {
#         'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
#         'money': Friuts['苹果'] * 4 + Friuts['草莓'] * 13 + Friuts['香蕉'] * 10
#     },
#     '小刚': {
#         'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
#         'money': Friuts['葡萄'] * 19 + Friuts['橘子'] * 12 + Friuts['樱桃'] * 30
#     }
# }
# print(info)





############编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
# def add(num):
#     num3 = dict()
#     for i in num:
#         if num.count(i) not in num3:
#             num3[i] = num.count(i)
#     return num3
#
# lii = [21, 21, 21, 56, 10, 10, 56, 10, 56, 56, 56, 56, 56, 56, 56]
# print(add(lii))








# Friuts = {
#     "苹果": 12.3,
#     "草莓": 4.5,
#     "香蕉": 6.3,
#     "葡萄": 5.8,
#     "橘子": 6.4,
#     "樱桃": 15.8
# }
# info = {
#     "小明": {
#         "fruits": {
#             "苹果": 4, "草莓": 13, "香蕉": 10
#         },
#     },
#     "小刚": {
#         "fruits": {
#             "葡萄": 19, "橘子": 12, "樱桃": 30
#         }
#     }
# }
# for i in info.keys():
#     totalPrice = 0
#     for j in info[i]["fruits"]:
#         price = info[i]["fruits"][j] * (Friuts[j])
#         totalPrice += price
#     print(i, "的总价为：", totalPrice)
#     info[i]["money"] = totalPrice
# print(info)
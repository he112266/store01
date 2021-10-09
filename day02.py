######判断数字是否在范围内
# num=int(input("请输入一个数字："))
# if num >=10 and num <=90:
#     print("ok")
# else:
#     print("no")




######随机一个数字
# import random
# ran=random.randint(20,70)
# print(ran)




######华氏温度转换为摄氏温度
# F=int(input("请输入华氏温度:",))
# C=(F - 32)/1.8
# print("转换成摄氏温度为：",C)




######输入圆的半径计算计算周长和面积
# r=int(input("请输入圆的半径："))
# L=2*3.1415926*r
# S=3.1415926*r*r
# print("该圆的周长为：",L)
# print("该圆的面积为：",S)




######输入年份判断是不是闰年
# Y=int(input("请输入年份："))
# if Y % 4 == 0 and Y % 100 != 0 :
#     print("该年是闰年")
# elif Y % 400 == 0 :
#     print("该年是闰年")
# else:
#     print("该年不是闰年")




######英制单位英寸与公制单位厘米互换
# L=int(input("请输入长度："))
# Unit=str(input("请输入单位："))
# a=2.54*L
# b=L/2.54
# if Unit == 'inch':
#     print("转换后长度为",a,"cm")
# elif Unit == 'cm':
#     print("转换后长度为",b,"inch")




######百分制成绩转换为等级制成绩
# score=int(input("输入的成绩是："))
# if score >=90:
#     print("A")
# elif score>=80 and score<90:
#     print("B")
# elif score>=70 and score<80:
#     print("C")
# elif score>=60 and score<70:
#     print("D")
# elif score>=0 and score<60:
#     print("E")
# else:
#     print("别瞎弄")



######输入三条边长，如果能构成三角形就计算周长和面积
# len1=int(input("请输入第一条边长为："))
# len2=int(input("请输入第二条边长为："))
# len3=int(input("请输入第三条边长为："))
# C=len1 + len2 + len3
# p=C/2
# S=(p*(p-len1)*(p-len2)*(p-len3))**0.5
# if len1 + len2 > len3 and len2 + len3 >len1 and len1 + len3 > len2:
#     print("这三条边组成的三角形周长为:",C)
#     print("这三条边组成的三角形面积为:",S)
# else :
#     print("这三条边不能组成三角形")




######10-90这个范围里面
######如果猜大了打印”猜大了“ 猜小了
######最多猜3次 暂停5秒
# import random
# import time
# randint=random.randint(10,90)
# print("一共3次机会")
# num1=randint
# count=int(3)
# while True:
#     num=int(input("猜猜随机数是多少"))
#     count=count-1
#     if num == num1 :
#         print("猜对了")
#         break
#     else:
#         if count==0 :
#             print("猜测失败，5秒后重新开始")
#             time.sleep(5)
#             print("请重新开始")
#             break
#         else:
#             if num > num1:
#                 print("%s,还有%d次机会"%('猜大了',count))
#             else:
#                 print("%s,还有%d次机会"%('猜小了',count))


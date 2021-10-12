######实现输入10个数字，并打印10个数的求和结果
# sum = 0
# for num in range(10):
#     number = int(input("请输入一个数字："))
#     sum += number
# print(sum)



#######从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
# list = []
# sum = 0
# max = 0
# for num in range(10):
#     number = int(input("请输入一个数:"))
#     list.append(number)
#     sum += number
#     for count in range(len(list)):
#         if list[count] > max :
#             max = list[count]
#         elif list[count] < max:
#             max = max
#         elif list[count] == max:
#             max = list[count]
# average = sum/10
#
# print("输入10个数之和为:",sum)
# print("输入的10个数中最大的值为:", max)
# print("输入的10个数的平均值为:",average)



######使用random模块，如何产生 50~150之间的数
# import random
# ran=random.randint(50,150)
# print(ran)



######编程实现下列图形的打印
# for i in range(8):
#     for j in range(0, 8- i):
#         print(end=" ")
#     for k in range(8 - i, 8):
#         print("^", end=" ")
#
#     print("")



#######使用while循环实现99乘法表的打印
# for i in range(1,10):
#      for j in  range(1,i+1):
#         print("%d*%d=%2d"%(j,i,j*i),end=' ')
#      print("")


# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print("%d*%d=%2d"%(j,i,j*i),end=' ')
#         j+=1
#     print("")
#     i+=1



#######编程实现99乘法表的倒叙打印
# for i in range(9,0,-1):
#     for j in range(1,i+1):
#          print("%d*%d=%2d"%(j,i,j*i),end=' ')
#     print("")


# i=9
# while i>=1:
#     k=9
#     while k>i:
#         print(end='       ')
#         k-=1
#     j = 1
#     while j<=i:
#         print("%d*%d=%2d"%(j,i,j*i),end=' ')
#         j+=1
#     print("")
#     i-=1



######从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# a=int(input("第一条边长："))
# b=int(input("第二条边长："))
# c=int(input("第三条边长："))
# if a+b>c and b+c>a and a+c>b:
#     print("可以构成三角形")
#     if a==b==c :
#         print("可以构成等边三角形")
#     elif a==b!=c or a==c!=b or b==c!=a:
#         print("可以构成等腰三角形")
#     elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
#         print("可以构成直角三角形")
#     else:
#          print("可以构成普通三角形")
# else:
#     print("不能构成三角形")



######使用+，-号实现两个数的调换
# a = eval(input("请输入一个数a:"))
# b = eval(input("请输入一个数b:"))
# print("交换前的两个数是：{},{}".format(a,b))
# a,b = b,a
# print("交换后的两个数是：{},{}".format(a,b))



#######用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# def  recursion(n):
#     if n==1:
#         return 1
#     else:
#         return  n*recursion(n-1)
# Sum = 0
# for  i  in range(1,21):
#     Sum +=recursion(i)
# print(Sum)



######一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出
# a=int(input("井的高度为："))
# b=int(input("每天往上爬的高度为："))
# c=int(input("每天下滑的高度为："))
# d=(a-b)/(b-c)+1
# e=int(d)
# if d==e:
#     print("青蛙能在第",e,"天出来")
# else:
#     print("青蛙能在第",e+1,"天出来")


# jing=-23
# up=4
# down=-2
# num=1
# while jing<0:
# 	print ('day ',num,end="   ")
# 	jing+=up
# 	print('up',jing,end="   ")
# 	if jing>=0:
# 		break
# 	jing+=down
# 	print('down',jing)
# 	if jing>=0:
# 		break
# 	num+=1



#######实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# name = 'root'
# passwd = 'admin'
# lock_usr = []
# for i in range(0, 3):
# 	usr_name = input("用户名：")
# 	usr_passwd = input("密码：")
# 	if usr_name == name and usr_passwd == passwd:
# 		print("玩命加载中...")
# 		break
# 	elif name != usr_name or passwd != usr_passwd:
# 		if i < 2:
# 			print("用户名密码错误，请重新输入！")
# 		else:
# 			lock_usr.append(usr_name)
# 			print("对不起！机会只有三次，您的账号密码被锁定")
# 	elif usr_name in lock_usr:
# 		print("该账号已锁定，请解锁后登陆")




# 继续完成上午的猜数字游戏的需求功能。
# 1.添加计数打印功能
# 2.添加次数金币功能和锁定系统功能。
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





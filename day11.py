# 要求：
# 1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
# 2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
# 3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
# 4、使用新手机对象调用手机介绍的方法；
# 5、使用新手机对象调用打电话的方法；
# import time
# class OldPhone:
#     __phone_number = ""
#
#     def setPhone_number(self, phone_number):
#         self.__phone_number = phone_number
#     def getPhone_number(self):
#         return self.__phone_number
#
#     def call(self, number):
#         print(self.__phone_number, "正在给", number, "打电话")
#
#         # for i in range(8):
#         #     print(".",end="")
#         #     time.sleep(1)
#         print("对方已接通！")
#
# class NewPhone(OldPhone):
#     __brand = ""
#
#     def setBrand(self, brand):
#         self.__brand = brand
#     def getBrand(self):
#         return self.__brand
#
#     def call(self, number):
#         # 老代码照样使用old-phone运行
#         super().call(number)
#
#         # 新的三项功能，自己来显示
#         print("品牌为:", self.__brand, "的手机很好用")
#
#
# phone = NewPhone()
# phone.setPhone_number("13552648187")
# phone.setBrand("诺基亚")
# phone.call("1831564056")

# 要求：
# 1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
# 2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
# 3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
# 4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
# 5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；

class Oldcook:
    __name = ""
    __age = 0

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        if age < 0 or age > 120:
            print("年龄非法！")
        else:
            self.__age = age

    def getAge(self):
        return self.__age

    def steamrice(self):
        print("厨师",self.__name,"正在蒸饭")


class Youngcook(Oldcook):

    def stirfry(self):
        print("厨师",self.getName(),"正在炒菜")

class Littlecook(Youngcook,Oldcook):

    def cooking(self):
        print("厨师", self.getName(), "正在蒸饭,炒菜")

cook = Littlecook()
cook.setName("小王")
cook.setAge(12)
cook.cooking()


# 请编程
# i.人：年龄，性别，姓名。
# ii.现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
# iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。

# class person:
#     __age = 0
#     __sex = ""
#     __name = ""
#
#     def setAge(self,age):
#         if age < 0 or age > 120:
#             print("年龄非法！")
#         else:
#             self.__age = age
#
#     def setSex(self,sex):
#         if sex == "男" or sex == "女":
#             self.__sex = sex
#         else:
#             print("性别非法")
#
#     def getSex(self):
#         return self.__sex
#
#     def setName(self,name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
# class worker(person):
#
#     def work(self):
#         print(self.getName(),"正在工作")
#
# class student(person):
#
#     def study(self):
#         print(self.getName(),"刚学习完")
#     def sing(self):
#         print("一会儿要去唱歌")
# st = student()
# st.setName("丹吉尔")
# st.study()
# st.sing()

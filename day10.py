# class Water_cup:
#     __high = 0.0
#     __volume = 0.0
#     __color = ""
#     __material = ""
#
#
#     def setHigh(self,high):
#         if high < 0  or high > 30:
#             print("高度非法，这是水杯吗？")
#         else:
#             self.__high = high
#     def getHigh(self):
#         return self.__high
#
#
#     def setVolume(self,volume):
#         if volume < 0  or volume > 2000:
#             print("容积非法！")
#         else:
#             self.__volume = volume
#     def getVolume(self):
#         return self.__volume
#
#
#     def setColor(self,color):
#         if color == "":
#             print("颜色非法，别瞎弄！")
#         else:
#             self.__color  =  color
#     def getColor(self):
#         return self.__color
#
#     def setMaterial(self,material):
#         if material == "":
#             print("材料非法！")
#         else:
#             self.__material = material
#     def getVolume(self):
#         return self.__material
#
#
#     def put(self,liquidName):
#         print(self.__material,"材料的杯子可以放",liquidName,"类型的液体")
#
#
#     def showMe(self):
#         print("水杯高度为",self.__high,"cm,"
#               ,"容量为",self.__volume,"ml,"
#               ,"材料是由",self.__material,"组成的,"
#               ,"它的颜色是",self.__color,"的")
#
#
# Water_cup = Water_cup()
#
# Water_cup.setHigh(30)
# Water_cup.setVolume(800)
# Water_cup.setMaterial("vf")
# Water_cup.setColor("透明")
# Water_cup.put("可乐")
# Water_cup.showMe()
# print("#########################################################################################")






# class laptop:
#     __brand = ""
#     __screen_size = 0
#     __price = 0
#     __cputype = ""
#     __memory_size = 0
#     __standby_time = 0
#
#     def setBrand (self,brand ):
#         self.__brand  = brand
#     def getBrand (self):
#         return self.__brand
#
#
#     def setScreen_size(self,screen_size):
#         if screen_size < 0  or screen_size > 21:
#             print("屏幕大小非法")
#         else:
#             self.__screen_size = screen_size
#     def getScreen_size(self):
#         return self.__screen_size
#
#
#     def setPrice (self,price ):
#         if price  < 0  or price  > 10000000:
#             print("价格非法！")
#         else:
#             self.__price  = price
#     def getPrice (self):
#         return self.__price
#
#
#     def setCputype(self,cputype):
#         self.__cputype = cputype
#     def getCputype(self):
#         return self.__cputype
#
#
#     def setMemory_size(self,memory_size):
#         if memory_size< 0  or memory_size > 32:
#             print("内存大小非法！")
#         else:
#             self.__memory_size = memory_size
#     def getMemory_size(self):
#         return self.__memory_size
#
#
#     def setStandby_time(self,standby_time):
#         if standby_time< 0  or standby_time > 10:
#             print("待机时长非法！")
#         else:
#             self.__standby_time = standby_time
#     def getStandby_time(self):
#         return self.__standby_time
#
#
#
#     def typewriting(self,words):
#         print(self.__brand,"品牌的笔记本电脑正打字练习文章",words)
#     def playgame(self,game):
#         print(self.__brand,"品牌的笔记本电脑正在进行",game,"游戏")
#     def watchvideo(self,video):
#         print(self.__brand,"品牌的笔记本电脑正在播放视频",video)
#
#
#     def showMe(self):
#         print("这台笔记本电脑是",self.__brand,"品牌的,"
#               ,"屏幕大小为",self.__screen_size,"寸,"
#               ,"价格大概",self.__price,"元左右,"
#               ,"它的cpu型号是",self.__cputype,"的,"
#               ,"内存大小有", self.__memory_size, "个G,"
#               ,"可以待机将近", self.__standby_time, "个小时" )
#
#
# laptop = laptop()
#
# laptop.setBrand("联想")
# laptop.setScreen_size(15)
# laptop.setPrice(6666)
# laptop.setCputype("酷睿i5")
# laptop.setMemory_size(16)
# laptop.setStandby_time(6)
# laptop.typewriting("I have a dream")
# laptop.playgame("吃鸡")
# laptop.watchvideo("葫芦娃")
# laptop.showMe()
# print("#################################################################################")





# 定义一个空调类和对应的测试类
# 要求：
# 1、空调有品牌和价格两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
# 2、提供一个无返回值的无参数的开机的方法，内容打印一句话：“空调开机了...”；
# 3、提供一个无返回值的带1个int类型参数的定时关机的方法,(int类型的参数表示设定的分钟数)，内容打印一句话：“空调将在xxx分钟后自动关闭...”；
# 4、在测试类中创建出空调对象，并给空调的品牌和价格赋任意值；
# 5、使用空调对象获取空调的品牌和价格并打印到控制台上；
# 6、使用空调对象调用开机方法；
# 7、使用空调对象调用定时关机方法，并传递具体数据值，在控制台上可以看到的效果为：空调将在xxx分钟后自动关闭...
# 其中语句中的“xxx”是调用方法时传递的具体数据值；



class air_conditioner:
    __brand = ""
    __price = 0

    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def setPrice (self,price ):
        if price  < 0  or price  > 1000000:
            print("价格非法！")
        else:
            self.__price  = price
    def getPrice (self):
        return self.__price


    def powerup(self,on):
        print("空调开机了",on)
    def poweroff(self,minute):
        print("空调将在",minute,"分钟后关机")

    def showMe(self):
        print("这是一台",self.__brand,"品牌的空调,售价大约",self.__price,"元")

air = air_conditioner()

air.setBrand("格力")
air.setPrice(2500)
air.poweroff(5)
air.showMe()













# class User:
#     __username = ""
#     __age = 0
#     __high = 0.0
#     __weight = 0
#     __sex = ""
#     __phoneNumber = ""
#
#
#     def setPhoneNumber(self,phone):
#         # 12  11  10
#         if phone.startswith("12") or  phone.startswith("10") or phone.startswith("11"):
#             print("手机号非法！你是政府官员？")
#         elif len(phone) != 11:
#             print("手机号码不正确！请输入11位手机号码！")
#         elif not phone.startswith("1"):
#             print("手机号必须是1开头！别瞎弄!")
#         else:
#             self.__phoneNumber = phone
#
#     def getPhoneNumber(self):
#         return self.__phoneNumber
#
#
#     def setUsername(self,username):
#         if username == "":
#             print("姓名非法，别瞎弄！")
#         else:
#            self.__username = username
#
#     def getUsername(self):
#         return self.__username
#
#     def setAge(self,age):
#         if age < 0 or age > 120:
#             print("年龄非法！")
#         else:
#             self.__age = age
#
#     def getAge(self):
#         return self.__age
#
#
#
#     def setHigh(self,high):
#         if high < 0  or high > 2.5:
#             print("身高非法，你比长颈鹿还猛？？？")
#         else:
#             self.__high = high
#
#     def getHigh(self):
#         return self.__high
#
#
#     def setSex(self,sex):
#         if sex  != "男"  and sex != "女":
#             print("性别非法！你去过泰国？")
#         else:
#             self.__sex = sex
#     def getSex(self):
#         return self.__sex
#
#
#     def setWeight(self,weight):
#         if weight < 0  or weight > 200:
#             print("你是^(*￣(oo)￣)^吗？非法了！别瞎弄！")
#         else:
#             self.__weight  =  weight
#
#     def getWeight(self):
#         return self.__weight
#
#
#     def eat(self,eatName):
#         print(self.__username,"正在吃",eatName)
#
#     def sleep(self,hour):
#         print(self.__username,"正在睡觉，已经睡了",hour,"小时！")
#
#     def playGame(self,gameName):
#         print(self.__username,"喜欢打",gameName,"，已经是废铁的级别！")
#
#     def study(self,subject,hour):
#         print(self.__username,"正在研究",subject,"，已经研究了",hour,"个小时！")
#
#     def showMe(self):
#         print("我叫",self.__username
#               ,",我今年",self.__age
#               ,"岁，身高："
#               ,self.__high
#               ,"米，我是"
#               ,self.__sex
#               ,"性别！我的手机号码:"
#               ,self.__phoneNumber)
#
# user = User()
#
# user.setUsername("jason jia")
# # user.username = "旺财"
# user.setAge(25)
# # user.high = 2.3
# user.setHigh(2.3)
# # user.sex = "male"
# user.setSex("男")
# # user.age = -25
# user.setWeight(70)
# user.setPhoneNumber("13552648187")
#
# user.eat("汉堡")
# user.sleep(18)
# user.study("科学",10)
# user.playGame("英雄联盟")
# user.showMe()
# print("######################################################################")


# 要求：
# 1、学生有姓名和年龄两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
# 2、提供一个无返回值的无参数的自我介绍的方法，内容打印一句话：
# “大家好，我叫xxx，今年xxx岁了！”
# 3、提供一个返回值为String类型，参数为学生类型的比较年龄差值的方法，如果当前对象的年龄比参数中的学生的年龄大，则返回：“我比同桌大xxx岁！”；如果当前对象的年龄比参数中的学生的年龄小，则返回：“我比同桌小xxx岁！”；如果当前对象的年龄和参数中的学生的年龄一样大，则返回：“我和同桌一样大！”
# 4、在测试类中分别创建你和你同桌两个人的对象，并分别给你和你同桌的姓名和年龄属性赋上对应的值；
# 5、调用你自己的对象的自我介绍的方法，展示出你自己的姓名和年龄；
# 6、用你自己的对象调用比较年龄差值的方法，把你同桌作为参数使用，并打印方法返回的字符串的内容；


# class Student:
#     __username = None
#     __age =  None
#
#     def setUsername(self,username):
#         self.__username =  username
#
#     def getUsername(self):
#         return self.__username
#
#     def setAge(self,age):
#         if age > 120 or age < 0:
#             print("您年龄输入非法！")
#         else:
#             self.__age = age
#
#     def getAge(self):
#         return self.__age
#
#     def showMe(self):
#         print("大家好，我叫",self.__username,"，今年",self.__age,"岁了！")
#
#     def compare(self,student):# self代表我自己    student代表另一个人
#         if self.__age > student.getAge():
#             print("我比同桌大",(self.__age - student.getAge()),"岁！")
#         elif self.__age < student.getAge():
#             print("我比同桌小", ( student.getAge()- self.__age),"岁！")
#         else:
#             print("我俩一样大！")
#
# s = Student()
# s.setUsername("旺财")
# s.setAge(55)
#
# s1 = Student()
# s1.setUsername("李四")
# s1.setAge(56)
#
# s.compare(s1) # 旺财要和李四比较
# s1.compare(s)
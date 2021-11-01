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






class User:
    __username = ""
    __age = 0
    __high = 0.0
    __weight = 0
    __sex = ""
    __phoneNumber = ""


    def setPhoneNumber(self,phone):
        # 12  11  10
        if phone.startswith("12") or  phone.startswith("10") or phone.startswith("11"):
            print("手机号非法！你是政府官员？")
        elif len(phone) != 11:
            print("手机号码不正确！请输入11位手机号码！")
        elif not phone.startswith("1"):
            print("手机号必须是1开头！别瞎弄!")
        else:
            self.__phoneNumber = phone

    def getPhoneNumber(self):
        return self.__phoneNumber


    def setUsername(self,username):
        if username == "":
            print("姓名非法，别瞎弄！")
        else:
           self.__username = username

    def getUsername(self):
        return self.__username

    def setAge(self,age):
        if age < 0 or age > 120:
            print("年龄非法！")
        else:
            self.__age = age

    def getAge(self):
        return self.__age



    def setHigh(self,high):
        if high < 0  or high > 2.5:
            print("身高非法，你比长颈鹿还猛？？？")
        else:
            self.__high = high

    def getHigh(self):
        return self.__high


    def setSex(self,sex):
        if sex  != "男"  and sex != "女":
            print("性别非法！你去过泰国？")
        else:
            self.__sex = sex
    def getSex(self):
        return self.__sex


    def setWeight(self,weight):
        if weight < 0  or weight > 200:
            print("你是^(*￣(oo)￣)^吗？非法了！别瞎弄！")
        else:
            self.__weight  =  weight

    def getWeight(self):
        return self.__weight


    def eat(self,eatName):
        print(self.__username,"正在吃",eatName)

    def sleep(self,hour):
        print(self.__username,"正在睡觉，已经睡了",hour,"小时！")

    def playGame(self,gameName):
        print(self.__username,"喜欢打",gameName,"，已经是废铁的级别！")

    def study(self,subject,hour):
        print(self.__username,"正在研究",subject,"，已经研究了",hour,"个小时！")

    def showMe(self):
        print("我叫",self.__username
              ,",我今年",self.__age
              ,"岁，身高："
              ,self.__high
              ,"米，我是"
              ,self.__sex
              ,"性别！我的手机号码:"
              ,self.__phoneNumber)

user = User()

user.setUsername("jason jia")
# user.username = "旺财"
user.setAge(25)
# user.high = 2.3
user.setHigh(2.3)
# user.sex = "male"
user.setSex("男")
# user.age = -25
user.setWeight(70)
user.setPhoneNumber("13552648187")

user.eat("汉堡")
user.sleep(18)
user.study("科学",10)
user.playGame("英雄联盟")
user.showMe()

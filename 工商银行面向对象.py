from Utils import Utils

class Bank():
    # 个人信息模板
    myinfo = '''
    \033[0;32;40m
    ------------账户信息------------
    账号：{account}
    姓名：{username}
    密码：{password}
    地址：
        国家：{country}
        省份：{province}
        街道：{street}
        门牌号：{door}
    账户余额：{money}
    注册银行名：{bank_name}
    -------------------------------
    \033[0m
    '''
    bank = {}  # 银行数据库

    __bank_name = "中国工商银行昌平支行"  # 银行名称

    bank_choose = {"1": "开户", "2": "存钱", "3": "取钱", "4": "转账", "5": "查询", "6": "Bye!"}  # 银行业务选项

    # 银行的名称是建立时就定下来的，不存在用户来设置其名称
    __bank_name = None
    def getBankName(self):
        return self.__bank_name

    # 判断是否在某个范围之内
    def isExists(self,chose, data):
        if chose in data:
            return True
        return False

    # 银行开户逻辑
    def bank_addUser(self,username, password, country, province, street, door,
                     money):

        if len(self.bank) >= 100:
            return 3
        elif username in self.bank:
            return 2
        else:
            self.bank[username] = {"account": Utils().getRandom(),
                              "password": password,
                              "country": country,
                              "province": province,
                              "street": street,
                              "door": door,
                              "money": money,
                              "bank_name": self.__bank_name}
            return 1

    # 银行存钱逻辑
    def bank_saveMoney(self,account="0", saveMoney=0):
        # 获取所有账号
        values = self.bank.values()
        for i in values:
            if account in i.values():
                i["money"] = i["money"] + saveMoney
                return True
        return False

    # 银行取钱逻辑
    def bank_money(self,account="0", money=0):
        # 获取所有账户
        values = self.bank.values()
        for i in values:
            if account in i.values():
                if money < i["money"]:
                    i["money"] = i["money"] - money
                    return True
        return False

# 用户类
class User():
    __userID=None
    __username=None
    __password=None
    __address=None
    __money=None
    __registertime=None
    __khh=None
    def setUserID(self,userID):
        self.__userID=userID
    def getUserID(self):
        return self.__userID
    def setUsername(self,username):
        self.__username=username
    def getUsername(self):
        return self.__username
    def setPassword(self,password):
        self.__password=password
    def getPassword(self):
        return self.__password
    def setAddress(self,address):
        self.__address=address
    def getAddress(self):
        return self.__address
    def setMoney(self,money):
        self.__money=money
    def getMoney(self):
        return self.__money
    def setRegistertime(self,registertime):
        self.__registertime=registertime
    def getRegistertime(self):
        return self.__registertime
    def setKhh(self,khh):
        self.__khh=khh
    def getKhh(self):
        return self.__khh

# 地址类
class Address():
    __country=None
    __province=None
    __street=None
    __door=None
    def setCountry(self,country):
        self.__country=country
    def getCountry(self):
        return self.__country
    def setProvince(self,province):
        self.__province=province
    def getProvince(self):
        return self.__province
    def setStreet(self,street):
        self.__street=street
    def getStreet(self):
        return self.__street
    def setDoor(self,door):
        self.__door=door
    def getDoor(self):
        return self.__door
from Bank import Bank
welcome = '''\033[0;32;40m
*******************************
*    中国工商银行账户管理系统    *
*******************************
*           选项              *\033[0m
'''
welcome_item ='''\033[0;32;40m*           {0}.{1}           *\033[0m'''
# 欢迎类
class Welcome:

    def print_welcome(self):
        print(welcome)
        keys = Bank.bank_choose.keys()
        for key in keys:
            print(welcome_item.format(key,Bank.bank_choose.get(key)))
        print("\033[0;32;40m******************************\033[0m")

# 初始化必要对象
welcome =  Welcome()
utils = Utils()
address = Address()
user = User()
bank = Bank()


# 必要的初始化方法
# 开户方法
def addUser():
    username = utils.inputHelp("用户名")
    password = utils.inputHelp("密码")
    country = utils.inputHelp("居住地址，1.国家：")
    province = utils.inputHelp("省份")
    street = utils.inputHelp("街道")
    door = utils.inputHelp("门牌号")
    money = int(input("银行卡存款余额"))

    n = bank.bank_addUser(username, password, country, province, street, door, money)

    if n == 2:
        print("该用户已存在！")
    elif n == 3:
        print("用户库已满！请携带证件到其他地方办理！谢谢！")
    elif n == 1:
        print("注册成功！以下是您的开户信息：")
        user = bank.bank[username]
        print(bank.myinfo.format(account=user["account"],
                            username=username,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]
        ))

def saveMoney(self):
    account = self.inputHelp("账号")
    saveMoney = self.inputHelp("存储金额")
    while True:
        if saveMoney.isdigit():
            saveMoney = int(saveMoney)
            break
        else:
            print("余额输入错误，请重新输入！")
    flag = self.bank_saveMoney(account, saveMoney)
    if flag:
        print("存储成功!")

def takeMoney(self):
    # 取钱由你们自己来开发
    account = self.inputHelp("账号")
    money = self.inputHelp("要取金额")
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入要取金额有误，请重新输入！")
    flag = self.bank_money(account, money)
    if flag:
        print("取钱成功！")
    else:
        print("取钱失败！")

    # pass

def transMoney(self):
    # 转账由你们自己来开发了
    account = self.inputHelp("账号")
    money = self.inputHelp("要转账金额")
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入要取金额有误，请重新输入！")
    flag = self.bank_money(account, money)
    account = self.inputHelp("账号")
    flag1 = self.bank_saveMoney(account, money)
    if flag and flag1:
        print("转账成功！")
    else:
        print("转账失败！")


def selectUser(self):
    username = self.inputHelp("用户名")
    if username in bank:
        user = bank[username]
        print(bank.myinfo.format(account=user["account"],
                            username=username,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]))
while True:
    # 欢迎页面
    welcome.print_welcome()

    #用户选择:程序入口
    chose = utils.inputHelp("选项")
    if bank.isExists(chose,bank.bank_choose):
        if chose == "1":
            addUser()
        elif chose == "2":
            saveMoney()
        elif chose == "3":
            takeMoney()
        elif chose == "4":
            transMoney()
        elif chose  == "5":
            selectUser()
        elif chose == "6":
            print("Bye!欢迎下次光临！")
            break
    else:
        print("不存在改选项，被瞎弄！")
from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import time
import xlrd
from xlutils import copy

wb = xlrd.open_workbook(filename=r"D:\Users\PycharmProjects\pythonProject2\自动化\HKR.xlsx", encoding_override=True)
st = wb.sheet_by_name("LOGIN")
wb_copy = copy.copy(wb)
rows = st.nrows
da = []
for i in range(1, rows):
    date = st.row_values(i)
    da.append([date[0], date[1], date[2], i])
print(da)
time.sleep(3)


class LoginOpera:
    # 保证driver使用全局同一个
    def __init__(self, driver):
        self.driver = driver
    # 登陆

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//*[@id='loginname']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

    # # 获取登陆成功的实际结果
    # def getLoginSuccessResult(self):
    #     return self.driver.title

    # 获取失败的结果数据
    def getLoginErrorResult(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text


@ddt
class TestHkr(TestCase):
    global wb_copy

    @data(*da)
    @unpack
    def testLogin(self, a, b, c, d):
        login = LoginOpera(self.driver)
        login.login(a, b)
        # result = login.getLoginSuccessResult()
        result2 = login.getLoginErrorResult()
        if result2 == c:
            print("不通过")
            wb_copy.get_sheet(0).write(d, 3, "通过！")
            wb_copy.save('HKR.xlsx')
        else:
            print("通过")
            wb_copy.get_sheet(0).write(d, 3, "不通过")
            wb_copy.save('HKR.xlsx')
            # login = LoginOpera(self.driver)
            # # 执行登陆的三项惭怍
            # login.login(username, password)
            #
            # # 获取实际结果
            # result = login.getLoginSuccessResult()
        time.sleep(3)

        # 断言
        self.assertEqual(c, result2)

    # 在所有用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()

    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()


def send_email(name):
    sender = '1004515171@qq.com'
    passwd = "apnhvzzmsgjpbdbj"
    receivers = '1004515171@qq.com'
    subject = '登录系统测试'

    # 构造邮件对象
    message = MIMEMultipart()
    message['From'] = Header("cc", 'utf-8')
    message['To'] = Header("ll", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message_content = "附件为测试结果"
    message.attach(MIMEText(message_content, 'plain', 'utf-8'))

    # 添加附件
    with open(name, mode='rb') as f:
        att_file = f.read()
    att1 = MIMEApplication(att_file)
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="%s"' % name
    message.attach(att1)

    # 发送邮件
    try:
        smtpobj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpobj.login(sender, passwd)
        smtpobj.sendmail(sender, receivers, message.as_string())
        smtpobj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as cause:
        print("无法发送邮件", cause)


send_email("HKR.xls")

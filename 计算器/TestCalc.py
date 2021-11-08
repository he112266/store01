'''

    unittest:单元测试框架

    1.子类继承TestCase
    2.写测试用例:testXxxxx
    任务1：
        使用邮件发送测试报告
        温馨提示：用户名，密码（smtp授权码开通即可。）
    任务2：执行减法，乘法，除法，测试用例。并生成测试报告。
'''

from Calc import Calc
from unittest import TestCase


class TestCalc(TestCase):
    def testAdd1(self):
        #
        a = 6
        b = 5
        s = 11

        calc = Calc()
        sum = calc.add(a, b)

        self.assertEqual(s, sum)

    def testAdd2(self):
        #
        a = -6
        b = -5
        s = -11

        calc = Calc()
        sum = calc.add(a, b)

        self.assertEqual(s, sum)

    def testAdd3(self):
        #
        a = -6
        b = 5
        s = -1

        calc = Calc()
        sum = calc.add(a, b)

        self.assertEqual(s, sum)

    def testAdd4(self):
        #
        a = 6
        b = -5
        s = 1

        calc = Calc()
        sum = calc.add(a, b)

        self.assertEqual(s, sum)

    def testminus1(self):
        #
        a = 6
        b = 5
        d = 1

        calc = Calc()
        differ = calc.minus(a, b)

        self.assertEqual(d, differ)

    def testminus2(self):
        #
        a = -6
        b = -5
        d = -1

        calc = Calc()
        differ = calc.minus(a, b)

        self.assertEqual(d, differ)

    def testminus3(self):
        #
        a = -6
        b = 5
        d = -11

        calc = Calc()
        differ = calc.minus(a, b)

        self.assertEqual(d, differ)

    def testminus4(self):
        #
        a = 6
        b = -5
        d = 11

        calc = Calc()
        differ = calc.minus(a, b)

        self.assertEqual(d, differ)

    def testmulti1(self):
        #
        a = 6
        b = 5
        m = 30

        calc = Calc()
        product = calc.multi(a, b)

        self.assertEqual(m, product)

    def testmulti2(self):
        #
        a = -6
        b = -5
        m = 30

        calc = Calc()
        product = calc.multi(a, b)

        self.assertEqual(m, product)

    def testmulti3(self):
        #
        a = -6
        b = 5
        m = -30

        calc = Calc()
        product = calc.multi(a, b)

        self.assertEqual(m, product)

    def testmulti4(self):
        #
        a = 6
        b = -5
        m = -30

        calc = Calc()
        product = calc.multi(a, b)

        self.assertEqual(m, product)

    def testdevision1(self):
        #
        a = 20
        b = 5
        v = 4

        calc = Calc()
        quotient = calc.devision(a, b)

        self.assertEqual(v, quotient)

    def testdevision2(self):
        #
        a = -20
        b = -5
        v = 4

        calc = Calc()
        quotient = calc.devision(a, b)

        self.assertEqual(v, quotient)

    def testdevision3(self):
        #
        a = -20
        b = 5
        v = -4

        calc = Calc()
        quotient = calc.devision(a, b)

        self.assertEqual(v, quotient)

    def testdevision4(self):
        #
        a = 20
        b = -5
        v = -4

        calc = Calc()
        quotient = calc.devision(a, b)

        self.assertEqual(v, quotient)

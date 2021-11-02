import unittest
import importlib

module_loaded = importlib.import_module('fraction.Fraction')
assert module_loaded.__name__ == 'fraction.Fraction'
Fraction = getattr(module_loaded, 'Fraction')
FractionException = getattr(module_loaded, 'FractionException')
assert Fraction.__name__ == 'Fraction'
assert FractionException.__name__ == 'FractionException'


class FractionTests(unittest.TestCase):
    def test1(self):
        f1 = Fraction()
        self.assertEqual(str(f1), '0/1')

    def test2(self):
        f1 = Fraction(1)
        f2 = Fraction(-2)
        self.assertEqual(str(f1), '1/1')
        self.assertEqual(str(f2), '-2/1')

    def test3(self):
        f1 = Fraction(denominator=2)
        self.assertEqual(str(f1), '0/1')
        f2 = Fraction(denominator=-3)
        self.assertEqual(str(f2), '0/1')

    def test4(self):
        f1 = Fraction(1, 3)
        f2 = Fraction(3, 6)
        f3 = Fraction(7, 9)

        self.assertEqual(str(f1), '1/3')
        self.assertEqual(str(f2), '1/2')
        self.assertEqual(str(f3), '7/9')

    def test5(self):
        f1 = Fraction(-2, 4)
        f2 = Fraction(3, -9)
        f3 = Fraction(-4, -8)
        self.assertEqual(str(f1), '-1/2')
        self.assertEqual(str(f2), '-1/3')
        self.assertEqual(str(f3), '1/2')

    def test6(self):
        f1 = Fraction(0.0)
        f2 = Fraction(1.1)
        f3 = Fraction(1.2)
        f4 = Fraction(-1.4)
        self.assertEqual(str(f1), '0/1')
        self.assertEqual(str(f2), '11/10')
        self.assertEqual(str(f3), '6/5')
        self.assertEqual(str(f4), '-7/5')

    def test7(self):
        f1 = Fraction(0.0, 7)
        f2 = Fraction(1.1, 7)
        f3 = Fraction(1.2, 8)
        try:
            f4 = Fraction(9.1, 0.0)
        except Exception as fe:
            self.assertEqual(fe.__class__.__name__, 'FractionException')
        self.assertEqual(str(f1), '0/1')
        self.assertEqual(str(f2), '11/70')
        self.assertEqual(str(f3), '3/20')

    def test8(self):
        f1 = Fraction(2, 1.1)
        f2 = Fraction(8, 1.6)
        f3 = Fraction(0, 5.6)
        self.assertEqual(str(f1), '20/11')
        self.assertEqual(str(f2), '5/1')
        self.assertEqual(str(f3), '0/1')

    def test9(self):
        f1 = Fraction(-2, 7.8)
        f2 = Fraction(1.1, -110)
        f3 = Fraction(4.7, 9.4)
        f4 = Fraction(-8.9, -26.7)
        self.assertEqual(str(f1), '-10/39')
        self.assertEqual(str(f2), '-1/100')
        self.assertEqual(str(f3), '1/2')
        self.assertEqual(str(f4), '1/3')

    def test10(self):
        f1 = Fraction('1')
        f2 = Fraction('-2')
        self.assertEqual(str(f1), '1/1')
        self.assertEqual(str(f2), '-2/1')

    def test11(self):
        f1 = Fraction(denominator='2')
        self.assertEqual(str(f1), '0/1')
        f2 = Fraction(denominator='-3')
        self.assertEqual(str(f2), '0/1')

    def test12(self):
        f1 = Fraction('1', '3')
        f2 = Fraction('3', '6')
        f3 = Fraction('7', '9')
        self.assertEqual(str(f1), '1/3')
        self.assertEqual(str(f2), '1/2')
        self.assertEqual(str(f3), '7/9')

    def test13(self):
        f1 = Fraction('-2', '4')
        f2 = Fraction('3', '-9')
        f3 = Fraction('-4', '-8')
        self.assertEqual(str(f1), '-1/2')
        self.assertEqual(str(f2), '-1/3')
        self.assertEqual(str(f3), '1/2')

    def test14(self):
        f1 = Fraction('0.0')
        f2 = Fraction('1.1')
        f3 = Fraction('1.2')
        f4 = Fraction('-1.4')
        self.assertEqual(str(f1), '0/1')
        self.assertEqual(str(f2), '11/10')
        self.assertEqual(str(f3), '6/5')
        self.assertEqual(str(f4), '-7/5')

    def test15(self):
        f1 = Fraction('0.0', '7')
        f2 = Fraction('1.1', 7)
        f3 = Fraction(1.2, '8')
        try:
            f4 = Fraction(9.1, 0.0)
        except Exception as fe:
            self.assertEqual(fe.__class__.__name__, 'FractionException')
        self.assertEqual(str(f1), '0/1')
        self.assertEqual(str(f2), '11/70')
        self.assertEqual(str(f3), '3/20')

    def test16(self):
        f1 = Fraction('2', '1.1')
        f2 = Fraction(8, '1.6')
        f3 = Fraction('0', 5.6)
        self.assertEqual(str(f1), '20/11')
        self.assertEqual(str(f2), '5/1')
        self.assertEqual(str(f3), '0/1')

    def test17(self):
        f1 = Fraction('-2', '7.8')
        f2 = Fraction(1.1, '-110')
        f3 = Fraction('4.7', 9.4)
        f4 = Fraction('-8.9', '-26.7')
        self.assertEqual(str(f1), '-10/39')
        self.assertEqual(str(f2), '-1/100')
        self.assertEqual(str(f3), '1/2')
        self.assertEqual(str(f4), '1/3')

    def test18(self):
        f1 = Fraction('0/2')
        f2 = Fraction('0/-3')
        self.assertEqual(str(f1), '0/1')
        self.assertEqual(str(f2), '0/1')

    def test19(self):
        f1 = Fraction('1/3')
        f2 = Fraction('3/6')
        f3 = Fraction('7/9')
        self.assertEqual(str(f1), '1/3')
        self.assertEqual(str(f2), '1/2')
        self.assertEqual(str(f3), '7/9')

    def test20(self):
        f1 = Fraction('-2/4')
        f2 = Fraction('3/-9')
        f3 = Fraction('-4/-8')
        self.assertEqual(str(f1), '-1/2')
        self.assertEqual(str(f2), '-1/3')
        self.assertEqual(str(f3), '1/2')

    def test21(self):
        f1 = Fraction('0.0')
        f2 = Fraction('1.1')
        f3 = Fraction('1.2')
        f4 = Fraction('-1.4')
        self.assertEqual(str(f1), '0/1')
        self.assertEqual(str(f2), '11/10')
        self.assertEqual(str(f3), '6/5')
        self.assertEqual(str(f4), '-7/5')

    def test22(self):
        f1 = Fraction('0.0/7')
        f2 = Fraction('1.1/7')
        f3 = Fraction('1.2/8')
        try:
            f4 = Fraction(9.1, 0.0)
        except Exception as fe:
            self.assertEqual(fe.__class__.__name__, 'FractionException')
        self.assertEqual(str(f1), '0/1')
        self.assertEqual(str(f2), '11/70')
        self.assertEqual(str(f3), '3/20')

    def test23(self):
        f1 = Fraction('2/1.1')
        f2 = Fraction('8/1.6')
        f3 = Fraction('0/5.6')
        self.assertEqual(str(f1), '20/11')
        self.assertEqual(str(f2), '5/1')
        self.assertEqual(str(f3), '0/1')

    def test24(self):
        f1 = Fraction('-2/7.8')
        f2 = Fraction('1.1/-110')
        f3 = Fraction('4.7/9.4')
        f4 = Fraction('-8.9/-26.7')
        self.assertEqual(str(f1), '-10/39')
        self.assertEqual(str(f2), '-1/100')
        self.assertEqual(str(f3), '1/2')
        self.assertEqual(str(f4), '1/3')

    def test25(self):
        try:
            f1 = Fraction('0/2', '0/-3')
        except Exception as fe:
            self.assertEqual(fe.__class__.__name__, 'FractionException')

    def test26(self):
        f1 = Fraction('3', '0.1/3')
        f2 = Fraction('0.2/7', '4.1')
        self.assertEqual(str(f1), '90/1')
        self.assertEqual(str(f2), '2/287')

    def test27(self):
        f1 = Fraction('0.7/4', '-9.23')
        f2 = Fraction("-5.44", "-33.2")
        self.assertEqual(str(f1), '-35/1846')
        self.assertEqual(str(f2), '68/415')

    def test28(self):
        f1 = Fraction.fromdecimal(1.2)
        f2 = Fraction.fromdecimal(1.22)
        f3 = Fraction.fromdecimal(1.222)
        f4 = Fraction.fromdecimal(12.2222)
        f5 = Fraction.fromdecimal(122.22222)
        self.assertEqual(str(f1), '6/5')
        self.assertEqual(str(f2), '61/50')
        self.assertEqual(str(f3), '611/500')
        self.assertEqual(str(f4), '61111/5000')
        self.assertEqual(str(f5), '6111111/50000')
    
    def test29(self):
        f1 = Fraction.fromdecimal(0x4f)
        self.assertEqual(str(f1), '79/1')

    def test30(self):
        try:
            f1 = Fraction.fromdecimal(0.1, 3)
        except Exception as fe:
            self.assertEqual(fe.__class__.__name__, 'FractionException')

    def test31(self):
        try:
            f1 = Fraction.fromdecimal(0.1, '.1')
        except Exception as fe:
            self.assertEqual(fe.__class__.__name__, 'FractionException')
    
    def test32(self):
        try:
            f1 = Fraction.fromdecimal(0.1, '%')
        except Exception as fe:
            self.assertEqual(fe.__class__.__name__, 'FractionException')

    def test33(self):
        try:
            f1 = Fraction.fromdecimal(0.1, '2')
        except Exception as fe:
            self.assertEqual(fe.__class__.__name__, 'FractionException')

    def test34(self):
        try:
            f1 = Fraction.fromdecimal(0.2, '23')
        except Exception as fe:
            self.assertEqual(fe.__class__.__name__, 'FractionException')

    def test35(self):
        f1 = Fraction.fromdecimal(1056.901379, rec='79')
        self.assertEqual(str(f1), '523166183/495000')
    
    def test36(self):
        f1 = Fraction.fromdecimal(24.5067, rec='067')
        self.assertEqual(str(f1), '122411/4995')


if __name__ == "__main__":
    unittest.main()

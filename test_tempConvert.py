from tempConvert import fahr_cel, cel_fahr
import unittest
import random

class TestClass(unittest.TestCase):

    def setResult(cls, amount, errors, failures, skipped):
        cls.amount, cls.errors, cls.failures, cls.skipped=amount, errors, failures, skipped

    def test_init(self):
        print("Init unit testing temperature conversion:\n")

        print("Fahrenheit to Celsius:\n")

        for f in range(0,50):
            c = ((f - 32) * 5/9)+random.randint(0,1)
            with self.subTest(str(f)+" F to C is "+str(c)):
                self.assertEqual(fahr_cel(f), c)



        for c in range(0,50):
            f = ((c * 9/5) + 32)+random.randint(0,1)
            with self.subTest(str(c)+" C to F is "+str(f)):
                self.assertEqual(cel_fahr(c), f)


# tests=TestClass()
# tests.test_init()
res=unittest.main(verbosity=2)
# print(res)

from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):

    def test_sub_function(self):
        res = calc.subtract(21, 13)

        self.assertEqual(res, 8)
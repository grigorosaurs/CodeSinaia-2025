import unittest
from roman_converter import roman_converter

class TestInvalidInput(unittest.TestCase):
    # ======== Step 1 ======== no input, return None
    def test_no_input(self):
        self.assertEqual(roman_converter(None), None)
    def test_sti(self):
        self.assertEqual(roman_converter("shaorma"),None)
    def test_dec(self):
        self.assertEqual(roman_converter(3.14),None)
    def test_min(self):
        self.assertEqual(roman_converter(0),None)
    def test_max(self):
        self.assertEqual(roman_converter(4000),None)
    def test_one(self):
        self.assertEqual(roman_converter(1),"I")
    def test_four(self):
        self.assertEqual(roman_converter(4), "IV")
    def test_five(self):
        self.assertEqual(roman_converter(5),"V")
    def test_nine(self):
        self.assertEqual(roman_converter(9),"IX")
    def test_ten(self):
        self.assertEqual(roman_converter(10),"X")
    def test_forty(self):
        self.assertEqual(roman_converter(40), "XL")
    def test_fifty(self):
        self.assertEqual(roman_converter(50),"L")
    def test_ninety(self):
        self.assertEqual(roman_converter(90), "XC")
    def test_hundred(self):
        self.assertEqual(roman_converter(100), "C")
    def test_fourhundred(self):
        self.assertEqual(roman_converter(400), "CD")
    def test_fivehundred(self):
        self.assertEqual(roman_converter(500),"D")
    def test_ninehundred(self):
        self.assertEqual(roman_converter(900), "CM")
    def test_thousand(self):
        self.assertEqual(roman_converter(1000), "M")
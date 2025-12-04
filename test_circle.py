import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_normal(self):
        """Тест площади круга с нормальным значением радиуса"""
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25, places=5)

    def test_area_zero(self):
        """Тест площади круга с нулевым радиусом"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        """Тест площади круга с радиусом 1"""
        res = area(1)
        self.assertAlmostEqual(res, math.pi, places=5)

    def test_area_float(self):
        """Тест площади круга с дробным радиусом"""
        res = area(2.5)
        self.assertAlmostEqual(res, math.pi * 6.25, places=5)

    def test_perimeter_normal(self):
        """Тест периметра круга с нормальным значением радиуса"""
        res = perimeter(5)
        self.assertAlmostEqual(res, 2 * math.pi * 5, places=5)

    def test_perimeter_zero(self):
        """Тест периметра круга с нулевым радиусом"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        """Тест периметра круга с радиусом 1"""
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi, places=5)

    def test_perimeter_float(self):
        """Тест периметра круга с дробным радиусом"""
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 2 * math.pi * 2.5, places=5)


import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        """Тест площади квадрата с нормальным значением стороны"""
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_zero(self):
        """Тест площади квадрата с нулевой стороной"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        """Тест площади квадрата со стороной 1"""
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_float(self):
        """Тест площади квадрата с дробной стороной"""
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_perimeter_normal(self):
        """Тест периметра квадрата с нормальным значением стороны"""
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_zero(self):
        """Тест периметра квадрата с нулевой стороной"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        """Тест периметра квадрата со стороной 1"""
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_float(self):
        """Тест периметра квадрата с дробной стороной"""
        res = perimeter(2.5)
        self.assertEqual(res, 10.0)


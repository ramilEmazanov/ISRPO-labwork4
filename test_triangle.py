import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        """Тест площади треугольника с нормальными значениями"""
        res = area(5, 10)
        self.assertEqual(res, 25)

    def test_area_zero_base(self):
        """Тест площади треугольника с нулевым основанием"""
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_zero_height(self):
        """Тест площади треугольника с нулевой высотой"""
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        """Тест площади треугольника с дробными значениями"""
        res = area(2.5, 4.0)
        self.assertEqual(res, 5.0)

    def test_perimeter_normal(self):
        """Тест периметра треугольника с нормальными значениями"""
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_equilateral(self):
        """Тест периметра равностороннего треугольника"""
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)

    def test_perimeter_zero_side(self):
        """Тест периметра треугольника с нулевой стороной"""
        res = perimeter(0, 4, 5)
        self.assertEqual(res, 9)

    def test_perimeter_float(self):
        """Тест периметра треугольника с дробными значениями"""
        res = perimeter(2.5, 3.5, 4.0)
        self.assertEqual(res, 10.0)

    def test_perimeter_isosceles(self):
        """Тест периметра равнобедренного треугольника"""
        res = perimeter(5, 5, 8)
        self.assertEqual(res, 18)


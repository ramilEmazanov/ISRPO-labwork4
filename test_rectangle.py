import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        """Тест площади прямоугольника с нормальными значениями"""
        res = area(5, 10)
        self.assertEqual(res, 50)

    def test_area_zero_width(self):
        """Тест площади прямоугольника с нулевой шириной"""
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_zero_height(self):
        """Тест площади прямоугольника с нулевой высотой"""
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_square(self):
        """Тест площади квадрата (прямоугольник с равными сторонами)"""
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_float(self):
        """Тест площади прямоугольника с дробными значениями"""
        res = area(2.5, 4.0)
        self.assertEqual(res, 10.0)

    def test_perimeter_normal(self):
        """Тест периметра прямоугольника с нормальными значениями"""
        res = perimeter(5, 10)
        self.assertEqual(res, 30)

    def test_perimeter_zero_width(self):
        """Тест периметра прямоугольника с нулевой шириной"""
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_perimeter_zero_height(self):
        """Тест периметра прямоугольника с нулевой высотой"""
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_square(self):
        """Тест периметра квадрата"""
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_float(self):
        """Тест периметра прямоугольника с дробными значениями"""
        res = perimeter(2.5, 4.0)
        self.assertEqual(res, 13.0)

    def test_area_negative_width(self):
        """Тест площади прямоугольника с отрицательной шириной"""
        with self.assertRaises(ValueError):
            area(-5, 10)

    def test_area_negative_height(self):
        """Тест площади прямоугольника с отрицательной высотой"""
        with self.assertRaises(ValueError):
            area(5, -10)

    def test_area_negative_both(self):
        """Тест площади прямоугольника с отрицательными обеими сторонами"""
        with self.assertRaises(ValueError):
            area(-5, -10)

    def test_perimeter_negative_width(self):
        """Тест периметра прямоугольника с отрицательной шириной"""
        with self.assertRaises(ValueError):
            perimeter(-5, 10)

    def test_perimeter_negative_height(self):
        """Тест периметра прямоугольника с отрицательной высотой"""
        with self.assertRaises(ValueError):
            perimeter(5, -10)

    def test_perimeter_negative_both(self):
        """Тест периметра прямоугольника с отрицательными обеими сторонами"""
        with self.assertRaises(ValueError):
            perimeter(-5, -10)


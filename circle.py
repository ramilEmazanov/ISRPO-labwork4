import math


def area(r):
    """
    Вычисляет площадь круга.
    
    Args:
        r (float): Радиус круга (должен быть неотрицательным)
    
    Returns:
        float: Площадь круга
    
    Raises:
        ValueError: Если радиус отрицательный
    """
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр круга.
    
    Args:
        r (float): Радиус круга (должен быть неотрицательным)
    
    Returns:
        float: Периметр круга
    
    Raises:
        ValueError: Если радиус отрицательный
    """
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r


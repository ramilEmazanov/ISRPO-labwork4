def area(a):
    """
    Вычисляет площадь квадрата.
    
    Args:
        a (float): Сторона квадрата (должна быть неотрицательной)
    
    Returns:
        float: Площадь квадрата
    
    Raises:
        ValueError: Если сторона отрицательная
    """
    if a < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной")
    return a * a


def perimeter(a):
    """
    Вычисляет периметр квадрата.
    
    Args:
        a (float): Сторона квадрата (должна быть неотрицательной)
    
    Returns:
        float: Периметр квадрата
    
    Raises:
        ValueError: Если сторона отрицательная
    """
    if a < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной")
    return 4 * a

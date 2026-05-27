#----------------------------------------------Task_#1------------------------------------------------------------------
#-------------------------------------------Фигуры и площади------------------------------------------------------------

#Создайте абстрактный класс Shape.
#В классе должен быть метод area(), который возвращает площадь фигуры.
#Реализуйте два класса:
#Circle, который принимает радиус.
#Rectangle, который принимает ширину и высоту.

# Пример использования
#shapes = [Circle(3), Rectangle(4, 5)]

#for shape in shapes:

#    print(f"Area: {shape.area():.2f}")

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     """
#         Abstract base class for geometric shapes.
#
#         Methods:
#             area():
#                 Returns the area of the shape.
#         """
#
#     @abstractmethod
#     def area(self):
#       pass
#
# class Circle(Shape):
#     """
#         Represents a circle.
#
#         Attributes:
#             radius (float): Radius of the circle.
#
#         Methods:
#             area():
#                 Returns the area of the circle.
#         """
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# class Rectangle(Shape):
#     """
#         Represents a rectangle.
#
#         Attributes:
#             width (float): Rectangle width.
#             height (float): Rectangle height.
#
#         Methods:
#             area():
#                 Returns the area of the rectangle.
#         """
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# shapes = [Circle(1), Rectangle(4, 5)]
#
# for shape in shapes:
#
#     print(f"Area: {shape.area():.2f}")

#---------------------------------------Task_#2-------------------------------------------------------------------------
#--------------------------------Проверка размеров фигур----------------------------------------------------------------
# Доработайте фигуры:
#
# Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
# Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение InvalidSizeError.

from abc import ABC, abstractmethod

class InvalidSizeError(Exception):
    """Raised when shape dimensions are invalid."""
    pass

class Shape(ABC):
    """
        Abstract base class for geometric shapes.

        Methods:
            area():
                Returns the area of the shape.
        """

    @abstractmethod
    def area(self):
        """Calculate and return shape area."""
    pass

class Circle(Shape):
    """
        Represents a circle.

        Attributes:
            radius (float): Radius of the circle.

        Methods:
            area():
                Returns the area of the circle.
        """
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError(
                "Radius must be greater than zero."
            )
        self.radius = radius


    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    """
        Represents a rectangle.

        Attributes:
            width (float): Rectangle width.
            height (float): Rectangle height.

        Methods:
            area():
                Returns the area of the rectangle.
        """
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError(
                "Width and height must be greater than zero."
            )

        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height

try:
    shapes = [Circle(1), Rectangle(4, 5)]

    for shape in shapes:

        print(f"Area: {shape.area():.2f}")

except InvalidSizeError as error:
    print(error)

#-----------------------------------------------------------------------------------------------------------------------
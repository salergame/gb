import argparse
import logging

logging.basicConfig(filename='rectangle_operations.log', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height is not None else width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
        new_width = abs(self.width - other.width)
        new_height = abs(self.height - other.height)
        return Rectangle(new_width, new_height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

def rectangle_operations(width1, height1, width2, height2):
    rect1 = Rectangle(width1, height1)
    rect2 = Rectangle(width2, height2)

    logger.info(f"Прямоугольник 1: {rect1}")
    logger.info(f"Прямоугольник 2: {rect2}")
    logger.info(f"Периметр прямоугольника 1: {rect1.perimeter()}")
    logger.info(f"Площадь прямоугольника 1: {rect1.area()}")
    logger.info(f"Периметр прямоугольника 2: {rect2.perimeter()}")
    logger.info(f"Площадь прямоугольника 2: {rect2.area()}")

    rect_sum = rect1 + rect2
    rect_diff = rect1 - rect2

    logger.info(f"Сумма прямоугольников: {rect_sum}")
    logger.info(f"Разность прямоугольников: {rect_diff}")
    logger.info(f"Прямоугольник 1 меньше прямоугольника 2: {rect1 < rect2}")
    logger.info(f"Прямоугольники равны: {rect1 == rect2}")
    logger.info(f"Прямоугольник 1 меньше или равен прямоугольнику 2: {rect1 <= rect2}")

def main():
    parser = argparse.ArgumentParser(description='Операции с прямоугольниками', prog='rectangle_operations.py')
    parser.add_argument('width1', type=int, help='Ширина прямоугольника 1')
    parser.add_argument('height1', type=int, nargs='?', default=None, help='Высота прямоугольника 1 (если не указана, считается равной ширине)')
    parser.add_argument('width2', type=int, help='Ширина прямоугольника 2')
    parser.add_argument('height2', type=int, nargs='?', default=None, help='Высота прямоугольника 2 (если не указана, считается равной ширине)')
    args = parser.parse_args()

    rectangle_operations(args.width1, args.height1, args.width2, args.height2)

rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 3)

print(rect1)
print(rect2)

print(rect1.perimeter())
print(rect1.area())
print(rect2.perimeter())
print(rect2.area())

rect_sum = rect1 + rect2
rect_diff = rect1 - rect2

print(rect_sum)
print(rect_diff)

print(rect1 < rect2)
print(rect1 == rect2)
print(rect1 <= rect2)

print(repr(rect1))
print(repr(rect2))


if __name__ == '__main__':
    main()

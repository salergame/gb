import argparse
import logging
from pathlib import Path
from collections import namedtuple

logging.basicConfig(filename='animal_factory.log', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', 'name, extension, dir, parent')

class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        try:
            return self.wingspan / 2
        except ZeroDivisionError as e:
            logger.error(f"Error calculating wing length for {self.name}: {e}")
            return None

class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        try:
            if self.max_depth < 10:
                return "Мелководная рыба"
            elif self.max_depth > 100:
                return "Глубоководная рыба"
            else:
                return "Средневодная рыба"
        except Exception as e:
            logger.error(f"Error determining depth for {self.name}: {e}")
            return None

class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        try:
            if self.weight < 1:
                return "Малявка"
            elif self.weight > 200:
                return "Гигант"
            else:
                return "Обычный"
        except Exception as e:
            logger.error(f"Error determining category for {self.name}: {e}")
            return None

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        try:
            if animal_type == 'Bird':
                return Bird(*args)
            elif animal_type == 'Fish':
                return Fish(*args)
            elif animal_type == 'Mammal':
                return Mammal(*args)
            else:
                raise ValueError('Недопустимый тип животного')
        except Exception as e:
            logger.error(f"Error creating animal of type {animal_type}: {e}")
            return None

def read_dir(path: Path) -> None:
    for file in path.iterdir():
        obj = File(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(obj)
        if obj.dir:
            read_dir(Path(obj.parent)/obj.name)

def walker():
    parser = argparse.ArgumentParser(
        description='Сохраняем данные о каталоге в файл',
        prog='task_1.py'
    )
    parser.add_argument('-p', '--path', type=Path, required=True, help='Введите путь: ')
    args = parser.parse_args()
    return read_dir(args.path)

animal1 = AnimalFactory.create_animal('Bird', 'Eagle', 200)
print(animal1.wing_length())

if __name__ == '__main__':
    walker()

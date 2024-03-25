from datetime import datetime
import argparse
import logging

logging.basicConfig(filename='mystr.log', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

class MyStr(str):
    def __new__(cls, value, author):
        obj = super().__new__(cls, value)
        obj.author = author
        obj.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return obj

    def __str__(self):
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {self.time})"

    def __repr__(self):
        return f"MyStr({super().__repr__()}, '{self.author}')"

def create_my_str(text, author):
    my_string = MyStr(text, author)
    logger.info(my_string)
    return my_string

def main():
    parser = argparse.ArgumentParser(
        description='Создаем объект MyStr с указанным текстом и автором',
        prog='task_2.py'
    )
    parser.add_argument('-t', '--text', type=str, required=True, help='Текст для создания объекта MyStr')
    parser.add_argument('-a', '--author', type=str, required=True, help='Автор текста')
    args = parser.parse_args()

    my_string = create_my_str(args.text, args.author)
    print(my_string)

if __name__ == '__main__':
    main()

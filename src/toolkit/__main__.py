import argparse
import sys

from .calculator import calculate
from .converter import convert
from .errors import WholeErrors, MissingArgumentError, ExtraArgumentError


def main():
    # Кастомный вывод ошибок
    try:
        # Создание парсера аргументов
        parser = argparse.ArgumentParser(description='Парсер')
        parser.add_argument('command', help='Выберите команду: calc или convert', nargs='?', default=None)
        parser.add_argument('expression', help='Введите выражение', nargs='*')
        # Добавление аргументов для convert, с учетом того, что есть зарезервированные слова from, to
        parser.add_argument('--from', dest='fromU', help='Введите единицы, из которых надо переводить')
        parser.add_argument('--to', dest='toU', help='Введите единицы, в которые надо переводить')

        # Чтение переданных аргументов
        args = parser.parse_args()

        # Обработка возможных ошибок argparse

        if args.command is None:
            raise MissingArgumentError('Не передана команда (calc/convert)')
        if len(args.expression) == 0:
            raise MissingArgumentError('Не передано выражение')
        if len(args.expression) > 1:
            raise ExtraArgumentError('Слишком много аргументов')
        if args.command == 'calc':
            # Результат калькулятора
            res = calculate(args.expression[0])
        elif args.command == 'convert':
            if args.fromU is None or args.toU is None:
                raise MissingArgumentError('нужно указать --from и --to')
            # Результат конвертера
            res = convert(args.expression[0], args.fromU.lower(), args.toU.lower())

        print(res)

        # Если ошибок не найдено - возвращаем код 0
        return 0
    except WholeErrors as error:
        print(f'Ошибка: {error}', file=sys.stderr)
        # Если есть ошибка - возвращаем код 2
        return 2


# Быстрый выход из программы при возникновении ошибок
sys.exit(main())
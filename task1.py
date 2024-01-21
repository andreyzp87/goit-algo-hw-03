# Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).
# Рекурсивне читання директорій:
# Має бути написана функція, яка приймає шлях до директорії як аргумент.
# Функція має перебирати всі елементи у директорії.
# Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він має бути доступним для копіювання.
# Копіювання файлів:
# Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
# Файл з відповідним типом має бути скопійований у відповідну піддиректорію.
# Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.

import argparse
import shutil
from pathlib import Path


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=Path, default=Path('source'))
    parser.add_argument('-o', '--output', type=Path, default=Path('output'))
    return parser.parse_args()


def copy_files(source: Path, output: Path):
    for path in source.iterdir():
        if path.is_dir():
            copy_files(path, output)
        else:
            ext = path.suffix.replace('.', '')
            out = output / ext
            out.mkdir(parents=True, exist_ok=True)
            shutil.copy(path, out / path.name)


def main():
    args = get_arguments()
    copy_files(args.source, args.output)


if __name__ == '__main__':
    main()

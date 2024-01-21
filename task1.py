import argparse
import shutil
from pathlib import Path


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=Path, default=Path('source'))
    parser.add_argument('-d', '--dist', type=Path, default=Path('dist'))
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
    copy_files(args.source, args.dist)


if __name__ == '__main__':
    main()

import sys


def txt_importer(path_file):
    if not path_file.lower().endswith('.txt'):
        print("Formato inválido", file=sys.stderr)
        return []
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

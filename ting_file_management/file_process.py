from ting_file_management.file_management import txt_importer


def process(path_file, instance):

    lines = txt_importer(path_file)
    if not lines:
        return
    for item in instance.items:
        if item['nome_do_arquivo'] == path_file:
            return
    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    instance.enqueue(file_data)
    print(file_data)


def remove(instance):
    if instance.is_empty():
        print("Não há elementos")
        return
    file_data = instance.dequeue()
    print(f"Arquivo {file_data['nome_do_arquivo']} removido com sucesso")
    if not instance.is_empty():
        instance.dequeue()


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        raise IndexError("Índice Inválido ou Inexistente")

    return instance.items[position]

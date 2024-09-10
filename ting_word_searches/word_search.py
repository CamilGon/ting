def exists_word(word, instance):
    results = []
    word_lower = word.lower()
    for file_info in instance.items:
        lines = file_info.get("linhas_do_arquivo", [])
        ocorrencias = []
        for index, line in enumerate(lines):
            if word_lower in line.lower():
                ocorrencias.append({"linha": index + 1})
        if ocorrencias:
            results.append({
                "palavra": word,
                "arquivo": file_info.get("nome_do_arquivo"),
                "ocorrencias": ocorrencias
            })
    return results


def search_by_word(word, instance):
    results = []
    word_lower = word.lower()
    for file_info in instance.items:
        lines = file_info.get("linhas_do_arquivo", [])
        ocorrencias = []
        for index, line in enumerate(lines):
            if word_lower in line.lower():
                ocorrencias.append({
                    "linha": index + 1,
                    "conteudo": line
                })
        if ocorrencias:
            results.append({
                "palavra": word,
                "arquivo": file_info.get("nome_do_arquivo"),
                "ocorrencias": ocorrencias
            })
    return results

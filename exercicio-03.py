# Informações de um livro

# Cadastrando os livros

lista_livros: list = []
while True:
    livro_info: dict = {}
    titulo: str = input("Qual o nome do livro? ").strip().capitalize()
    livro_info["titulo"] = titulo
    autor: str = input("Qual o autor do livro? ").strip().capitalize()
    livro_info["autor"] = autor
    ano: str = input("Qual o ano de publicação do livro? ").strip()
    while True:
        if ano.isdigit() and len(ano) == 4:
            ano = int(ano)
            livro_info["ano"] = ano
            break
    
        ano: str = input("O ano deve estar no formato AAAA. Ex: 2026 ")

    lista_livros.append(livro_info)

    while True:
        pergunta: str = input("Deseja cadastrar outro livro? [S/N] ").upper()

        if pergunta in ("S", "N"):
            break
    
        print(f"Atenção! Digite apenas 'S' ou 'N'.")

    if pergunta == "N":
        break

print(lista_livros)


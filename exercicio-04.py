# Preço total da lista de compras

lista_items: list = []


while True:
    try:

        item_info: dict = {}

        item: str = input("Qual item deseja adicionar? ").strip().capitalize()
        item_info["item"] = item

        while True:
            quantidade: str = input("Qual a quantidade? ")
            if "," in quantidade:
                print("Utilize '.' como separador decimal.")
                continue
            elif not quantidade.replace(".", "", 1).isnumeric():
                print("Informe um número decimal. Ex: 1.5")
                continue

            break
        quantidade = float(quantidade) 

        while True:
            preco: str = input("Qual o preço unitário do produto? ")
            if "," in preco:
                print("Utilize '.' como separador decimal.")
                continue
            elif not preco.replace(".", "", 1).isnumeric():
                print("Informe um número decimal. Ex: 1.5")
                continue

            break
        
        preco = float(preco)
        item_info["preco"] = quantidade * preco

        lista_items.append(item_info)

        while True:
            pergunta = input("Deseja adicionar outro intem? [S / N] ").upper()

            if pergunta in ("S", "N"):
                break

        if pergunta == "N":
            break
        
           
    except ValueError as err:
        print(f"Atenção! {err}")

valor_total = sum(i["preco"] for i in lista_items)

print(f"O valor total da compra foi de R$ {valor_total:.2f}.")
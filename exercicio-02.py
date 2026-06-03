linguagens = []

while True:
    try:
        print("Selecione a ação desejada...\n"
        "[1] - Adicionar\n"
        "[2] - Remover\n"
        "[3] - Editar\n"
        "[0] - Sair")
        acao: int = int(input(">>"))

        if acao not in range(0, 4):
            raise ValueError("Digite uma das opções informadas")
        
        elif acao == 1:
            linguagem: str = input("Informe qual linguagem deseja adicionar: ").strip().lower()
            linguagens.append(linguagem)

        elif acao == 2:
                if not linguagens:
                    raise Exception("Sua lista não possui nenhuma linguagem.")
    
                linguagem: str = input("Informe qual linguagem deseja remover: ").strip().lower()
                linguagens.remove(linguagem)

        elif acao == 3:
            valor_atual = input("Qual linguagem você deseja editar? ").strip().lower()

            if valor_atual not in linguagens:
                raise Exception("Linguagem não encontrada!")
            
            valor_novo = input("Para qual linguagem? ").strip().lower()

            index = linguagens.index(valor_atual)
            linguagens[index] = valor_novo

        elif acao == 0:
            break

        print(f"Essas são as linguagens na lista: {linguagens}")

    except ValueError as err:
        print(f"Atenção! {err}")

    except Exception as err:
        print(f"Atenção! {err}")

print(f"Essas são todas as linguagens na lista: {linguagens}")


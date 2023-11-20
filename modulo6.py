import csv
from datetime import datetime

def menu_inicial():
    escolha = int(input("Escolha uma opção: \n1.Doar Produtos\n2.Lista de Produtos\n3.Histórico de Doações\n4.Sair\n"))
    match escolha:
        case 1:
            doar_produtos()
        case 2:
            lista_produtos()
        case 3:
            historico_doacoes()
        case 4:
            print("Saindo...")
            SystemExit

def doar_produtos():
    print("------Doar Produtos------")
    produtoEncontrado = False

    with open('itens_registrados.csv', 'r') as arquivo:
        # Cria um objeto DictReader
        leitor = csv.DictReader(arquivo)
        count=1

        # Itera sobre as linhas do arquivo csv para mostrar os produtos disponíveis
        print("\nProdutos disponíveis:")
        for linha in leitor:
            print(f"\nProduto {count}.\nNome do produto: {linha['Nome do item']}, Nome do cliente: {linha['Nome do cliente']}, Escolha de doação: {linha['escolha de doacao']}")
            count+=1
            
        # Retorna ao início do arquivo
        arquivo.seek(0)
        next(leitor)  # Pula o cabeçalho

        # Pede ao usuário para inserir o nome do produto
        nomeProduto = input("\nDigite o nome do produto que voce deseja doar.\nNome do produto: ")

        # Itera sobre as linhas do arquivo csv
        for linha in leitor:
            if linha['Nome do item'].lower() == nomeProduto.lower():
                produtoEncontrado = True
                print("Produto encontrado!")
                if linha["escolha de doacao"] == 0:
                    print(f"O produto {linha['Nome do item']} não pode ser doado.")
                    menu_inicial()
                else:
                    HoraAtual = datetime.now()
                    data_hora = HoraAtual.strftime("%d/%m/%Y %H:%M:%S")

                    print(f"O produto {linha['Nome do item']} foi doado.")
                    # Adiciona a doação ao histórico
                    with open('historico_doacoes.csv', 'a', newline='') as arquivo_doacoes:
                        campos = ['Nome do item', 'Nome do cliente']
                        escritor = csv.DictWriter(arquivo_doacoes, fieldnames=campos)

                        # Escreve o cabeçalho apenas se o arquivo estiver vazio
                        if arquivo_doacoes.tell() == 0:
                            escritor.writeheader()
                        escritor.writerow({'Nome do item': linha['Nome do item'], 'Nome do cliente': linha['Nome do cliente'] + " - " + data_hora})
        if not produtoEncontrado:
            print("Produto não encontrado.")
            menu_inicial()

def lista_produtos():
    count=1
    print("\nProdutos disponíveis:")
    with open('itens_registrados.csv', 'r') as arquivo:
    # Cria um objeto DictReader
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            print(f"\nProduto {count}.\nNome do produto: {linha['Nome do item']}, Nome do cliente: {linha['Nome do cliente']}, Escolha de doação: {linha['escolha de doacao']}\n")
            count+=1
        menu_inicial()

def historico_doacoes():
    with open('historico_doacoes.csv', 'r') as arquivo:
        print("\n ------ Histórico de Doações ------\n")
        for linha in arquivo:
            print(linha)
menu_inicial()

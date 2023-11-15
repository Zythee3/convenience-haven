import string
import random
import csv
class itens:
    def __init__(self,nome_cliente, nome_item, descricao_item, condicao_item, id_produto, escolha_doacao, aprovacao, pontos, justificacao ):
        self.nome_cliente = nome_cliente
        self.nome_item = nome_item
        self.descricao_item = descricao_item
        self.condicao_item = condicao_item
        self.id_produto = id_produto
        self.escolha_doacao = escolha_doacao
        self.aprovacao = aprovacao
        self.pontos = pontos
        self.justificacao = justificacao


def escreve_csv():
    for nome in itens_registrados:
        auxiliar_nomes.append([nome.nome_cliente, nome.nome_item, nome.descricao_item, nome.condicao_item, nome.id_produto, nome.escolha_doacao])
        id_dos_produtos.append(nome.id_produto)
    with open("itens_registrados.csv", "a", newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        for linha in auxiliar_nomes:
            escritor_csv.writerow(linha)


def escreve_arquvio(conteudo):
    with open("itens_registrados.txt", "a") as arquivo:
        arquivo.write(conteudo)


itens_registrados = []
dados = [
    ['Nome do cliente', 'Nome do item', 'Descricao', 'condicao', 'id do produto', 'escolha de doacao', 'aprovacao', 'pontos', 'jutificacao']
    
]
auxiliar_nomes = []
id_dos_produtos = []

def cria_item():
    print("Informe os dados abaixo!")
    nome_cliente = input("Nome do cliente: ")
    nome_cliente = nome_cliente.capitalize()
    nome_item = input("Nome do item: ")
    nome_item = nome_item.capitalize()
    descricao_item = input("Descrição do item: ")
    condicao_item = input("Condição atual do item: ")
    id_letra_produto = ""
    for x  in range(4):
        id_letra_produto += random.choice(string.ascii_letters)
    id_numero_produto = random.randint(0, 999)
    id_produto =f"{id_letra_produto} - {id_numero_produto}"
    while True:
        try:
            escolha_doacao = int(input("[0] doar\n[1] vender\n"))
            if escolha_doacao >=0 and escolha_doacao <=1:
                break
            else:
                print("Opção inválida, tente novamente")
        except ValueError:
            print("Opção inválida, tente novamente")
    novo_item = itens(nome_cliente, nome_item, descricao_item, condicao_item, id_produto, escolha_doacao, "", "", "")
    itens_registrados.append(novo_item)
    escreve_csv()


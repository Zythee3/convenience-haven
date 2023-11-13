import random
import string

class itens:
    def __init__ (self, nome, descricao, condicao, id, doacao):
        self.nome = nome
        self.descricao = descricao
        self.condicao = condicao
        self.id = id
        self.doacao = doacao

itens_registrados = []
def cria_arquivo(nome_item):
    nome_item + ".txt"
    with open(nome_item, "w") as arquivo:
        print()
        
def cria_item():
    print("Para cadastrar seu item basta informar os seguintes dados")
    nome_item = input("Nome do produto: ")
    descricao_item = input("Descrição do produto: ")
    condicao_item = input("Condição atual do produto: ")
    id_letra_produto = ""
    while True:
        try:
            escolha_doacao = int(input("[0] doar\n[1] vender\n"))
            if escolha_doacao >=0 and escolha_doacao <=1:
                break
        except ValueError:
            print("Opção inválida, tente novamente")
        
    for x  in range(4):
        id_letra_produto += random.choice(string.ascii_letters)
    
    id_numero_produto = random.randint(0, 999)
    id_produto =f"{id_letra_produto} - {id_numero_produto}"

    dados_item = f"Nome: {nome_item}\nDescricao: {descricao_item}\nCondicao: {condicao_item}\nID: {id_produto}\nOpcao doar(0)/vender(1): {escolha_doacao}"
    escreve_arquivo(nome_item, dados_item)
    novo_item = itens(nome_item, descricao_item, condicao_item, id_produto, escolha_doacao)
    
    itens_registrados.append(novo_item)


def escreve_arquivo(nome_item, conteudo):
    nome_item + ".txt"
    with open(nome_item, "a") as arquivo:
        arquivo.write(conteudo)

cria_item()







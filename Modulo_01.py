import random
import string

class itens:
    def __init__ (self, nome_cliente, nome, descricao, condicao, id, doacao):
        self.nome_cliente = nome_cliente
        self.nome = nome
        self.descricao = descricao
        self.condicao = condicao
        self.id = id
        self.doacao = doacao


itens_registrados = []
nome_itens_registrados = []

item1 = itens("Samuel", "Cadeira","Item de decoração e utilidade domiciliar","bom estado", "CHYd - 679", 1)
item2 = itens("Vinicius","Ventilador", "Aparelho eletronico", "Necessita de pequenas manutencoes", "zhSG - 464", 0)
item3 = itens("Fernanda","Impressora", "Aparelho de impressao", "Bom estado", "TFmI - 991", 1)

itens_registrados.append(item1)
itens_registrados.append(item2)
itens_registrados.append(item3)

nome_itens_registrados.append(item1.nome)
nome_itens_registrados.append(item2.nome)
nome_itens_registrados.append(item3.nome)




def cria_item():
    print("Para cadastrar seu item basta informar os seguintes dados")
#parte dos inputs
    nome_cliente_item = input("Nome do cliente: ")
    nome_item = input("Nome do produto: ")
    descricao_item = input("Descrição do produto: ")
    condicao_item = input("Condição atual do produto: ")
    id_letra_produto = ""
#escolha doar ou vender 
    while True:
        try:
            escolha_doacao = int(input("[0] doar\n[1] vender\n"))
            if escolha_doacao >=0 and escolha_doacao <=1:
                break
            else:
                print("Opção inválida, tente novamente")
        except ValueError:
            print("Opção inválida, tente novamente")

#parte onde o id é gerado    
    for x  in range(4):
        id_letra_produto += random.choice(string.ascii_letters)
    id_numero_produto = random.randint(0, 999)
    id_produto =f"{id_letra_produto} - {id_numero_produto}"
#conclusão da função onde os dados são escrito no arquivo e o item vai para a lista dos itens registrados
    dados_item = f"Nome: {nome_item}\nDescricao: {descricao_item}\nCondicao: {condicao_item}\nID: {id_produto}\nOpcao doar(0)/vender(1): {escolha_doacao}"
    escreve_arquivo(nome_item, dados_item)
    novo_item = itens(nome_cliente_item, nome_item, descricao_item, condicao_item, id_produto, escolha_doacao)
    itens_registrados.append(novo_item)
    nome_itens_registrados.append(nome_item)

def escreve_arquivo(nome_item, conteudo):
    nome_item + ".txt"
    with open(nome_item, "w") as arquivo:
        arquivo.write(conteudo)


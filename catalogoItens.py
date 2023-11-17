import csv
# from itensregistrados import *

class itens:
    def __init__ (self, nome, descricao, condicao, id, doacao):
        self.nome = nome
        self.descricao = descricao
        self.condicao = condicao
        self.id = id
        self.doacao = doacao
        
        

def ler_itens():
    try:
        with open("itensregistrados.csv", 'r') as arquivo:
            ler = csv.DictReader(arquivo)
            
            print('Catálogo de itens:')
            print('------------------------------')
            for coisa in ler:
                nomeItem = coisa['Nome do item']
                idItem = coisa['id']
                creditos = coisa['Creditos']
                print(f'Item: {nomeItem}\nID do item: {idItem}\nCréditos retornados: {creditos}')
                
    except FileNotFoundError:
        print(f'O arquivo itensregistrados não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
  
  
def encontrarCliente(nome_cliente):
    try:
        with open('itenscadastrados', 'r') as arquivo:
            ler = csv.DictReader(arquivo)
            for coisa in ler:
                if coisa['Nome do cliente'] == nome_cliente:
                    return True
        return False
    except FileNotFoundError:
        print(f'O arquivo itensregistrados não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
  
def trocarItens(id_item):
    
    nome_cliente = input('Insira o seu nome:')
    if encontrarCliente(nome_cliente):
        try:
            with open('itensregistrados.csv','r') as arquivo:
                ler = csv.DictReader(arquivo)
                lista = list(ler)
                nome_item = None
                creditos_necessarios = 0
                for linha in lista:
                    if linha['id do produto'] == id_item:
                        nome_item = linha['Nome do item']
                        
                        creditos_necessarios = int(linha.get('Creditos',0))
                        if creditos_necessarios <= 0:
                            print(f' O item com o ID {nome_item} ainda não possui créditos adquiridos.')
                            return 
                        creditos_cliente = int(linha.get('Creditos',0))
                        elif creditos_necessarios > creditos_cliente:
                            print(f'Cliente {nome_cliente} não possui créditos sulficientes para trocar pelo item.')
                            return
                        else:
                            linha['Creditos'] = creditos_necessarios
                        
def main():
    ler_itens()
    id_item = input('Insira o ID do item que deseja: ')
    
    
            


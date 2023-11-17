import csv
# from itensregistrados import *

class itens:
    def __init__ (self, nome, descricao, condicao, id, doacao):
        self.nome = nome
        self.descricao = descricao
        self.condicao = condicao
        self.id = id
        self.doacao = doacao
        
        

def ler_arquivo():
    try: 
        with open("itensregistrados.csv", 'r') as arquivo:
            # leitor = csv.reader(arquivo)
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                
                
    except FileNotFoundError:
        print(f'O arquivo {caminho_do_arquivo} não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    

ler_arquivo()


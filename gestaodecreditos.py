import csv
# from itensregistrados import *
def adicionar_creditos(credporitem):
    try:
        with open("itensresgitrados", 'r') as arquivo:
            ler = csv.DictReader(arquivo)

            item = list(ler)

            item[0]['Creditos'] = 'Creditos'
            # coisa é uma variavel para que eu possa interagir com o arquivo 
            for coisa in item:
                nomeItem = coisa['Nome do item']
                
                    # atribuir credito ao item
                creditos = credporitem.get(nomeItem, 0)
                coisa['Creditos'] = creditos
        
        with open('itensresgitrados','w',newline =' ') as arquivoModificado:
            escrever = csv.DictReader(arquivoModificado, fieldnames = ler.fieldnames + ['Creditos'])
            escrever.writeheader()
            escrever.writerows(item) 
    except FileNotFoundError:
        print(f'O arquivo itensregistrados.csv não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')   
        
def mostrarItens():
    try:
        with open('itensregistrados', 'r') as arquivo:
            ler = csv.DictReader(arquivo)

            print('itens e seus status de aprovação:')
            print('-------------------------------------') 
            for coisa in ler:
                nomeItem = coisa['Nome do item']
                aprovacao = coisa['aprovacao']
                print(f'Item: {nomeItem}, Aprovação: {aprovacao}')
    except FileNotFoundError:
        print(f'O arquivo itensregistrados.csv não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')  
        
def main(args=None):
    mostrarItens()
    
    
main()      
            
        
        
                


    
import csv
import os
def adicionar_creditos(nome_item,credito):
    try:
        if not os.path.exists('itensregistrados.csv'):
            raise FileNotFoundError(f'O arquivo itensregistrados.csv não foi encontrado.')

        # Lê o arquivo CSV
        with open('itensregistrados.csv', 'r', newline='') as arquivo:
            ler = csv.DictReader(arquivo)
            fieldnames = ler.fieldnames
            itens = list(ler)

        encontrado = False  
        # Marca se o item foi encontrado no arquivo

        for item in itens:
            if item['Nome do item'] == nome_item:
                item['Creditos'] = credito
                encontrado = True
                break  

        
        if not encontrado:
            print(f'O item "{nome_item}" não foi encontrado no arquivo.')

        with open('itensregistrados.csv', 'w', newline='') as arquivo_modificado:
            escrever = csv.DictWriter(arquivo_modificado, fieldnames=fieldnames + ['Creditos'])
            escrever.writeheader()
            escrever.writerows(itens)

        print(f'Créditos para o item "{nome_item}" adicionados com sucesso.')
 
        
        
    except FileNotFoundError:
        print(f'O arquivo itensregistrados.csv não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')   
        
def mostrarItens():
    try:
        with open('itensregistrados.csv', 'r') as arquivo:
            ler = csv.DictReader(arquivo)

            print('itens e seus status de aprovação:')
            print('-------------------------------------') 
            for coisa in ler:
                nomeItem = coisa['Nome do item']
                condicao = coisa['condicao']
                aprovacao = coisa['aprovacao']
                print(f'Item: {nomeItem},Condição: {condicao} ,Aprovação: {aprovacao}')
    except FileNotFoundError:
        print(f'O arquivo itensregistrados.csv não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')  
        
def main(args=None):
    mostrarItens()
    nome_item = input('Insira o nome do item que adicionar creditos:')
    credito = int(input('Insira os creditos que quer adicionar para o item:'))
    adicionar_creditos(nome_item,credito)
    
    
main()      
            
        
        
                


    
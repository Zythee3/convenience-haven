import csv
def adicionar_creditos(nome_item,credito):
    try:
        with open("itensregistrados.csv", 'r', newline='') as arquivo:
            ler = csv.DictReader(arquivo)
            fieldnames = ler.fieldnames + ['Creditos']
            
        with open('itensregistrados.csv','r',newline='') as arquivo:
            ler = csv.DictReader(arquivo)
            itens = list(ler)
                
        for item in itens:
            if item['Nome do item'] == nome_item:
                item['Creditos'] = credito    

        #     itens = list(ler)
        # encontrado = False
        # for item in itens:
        #         if item['Nome do item'] == nome_item:
        #             item['Creditos'] = credito
        #             encontrado = True
        #             break
        # if not encontrado:
        #     print(f'O item {nome_item} não foi encontrado no arquivo.')
                    
        # with open('itensregistrados.csv','a',newline ='') as arquivoModificado:
        #     escrever = csv.DictWriter(arquivoModificado, fieldnames = ler.fieldnames + ['Creditos'])
        #     escrever.writeheader()
        #     escrever.writerows(itens) 
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
                aprovacao = coisa['aprovacao']
                print(f'Item: {nomeItem}, Aprovação: {aprovacao}')
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
            
        
        
                


    
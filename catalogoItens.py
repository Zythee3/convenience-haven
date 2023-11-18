import csv


        
        

def ler_itens():
    try:
        with open("itensregistrados.csv", 'r') as arquivo:
            ler = csv.DictReader(arquivo)
            
            print('Catálogo de itens:')
            print('------------------------------')
            for coisa in ler:
                nomeItem = coisa['Nome do item']
                idItem = coisa['id do produto']
                creditos = coisa['Creditos']
                print(f'Item: {nomeItem}ID do item: {idItem} Créditos retornados: {creditos}')
                
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
    try:
        nome_cliente = input('Insira o seu nome:')
        #verificar se o cliente existe no sistema
        if encontrarCliente(nome_cliente) == True:
            with open('itensregistrados','r') as arquivo:
                ler = csv.DictReader(arquivo)
                itens = list(ler)
                
                for item in itens:
                    if item['id do produto'] == id_item:
                        nome_item = item['Nome do item']
                        #captura a quantidade de créditos que o cliente precisa para adquirir o produto
                        creditos_necessarios = int(item.get('creditos',0))
                        
                        if creditos_necessarios <= 0:
                            print(f'Item com ID {id_item} ainda não possui créditos adicionados a ele.')
                            return
                        
                        creditos_cliente = int(item.get('creditos',0))
                        
                        if creditos_necessarios > creditos_cliente:
                            print(f'O cliente {nome_cliente} não possui créditos sulficientes para o item.')
                            return
                        else:
                            item['creditos'] -= creditos_necessarios
                            
            with open('itensregistrados.csv','w',newline='') as arquivomodificado:
                escrever = csv.DictWriter('itensregistrados.csv',fieldnames=ler.fieldnames)
                escrever.writeheader()
                escrever.writerows(itens)
                
            print(f'Troca realizada do item {nome_item} com sucesso pelo cliente {nome_cliente}.')
        else:
            print(f'Cliente {nome_cliente} não encontrado.')
    except FileNotFoundError:
        print('O arquivo itensregistrados.csv não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        
                   
    
                        
def main():
    ler_itens()
    id_item = input('Insira o ID do item que deseja: ')
    trocarItens(id_item)
    
main()
    
    
            


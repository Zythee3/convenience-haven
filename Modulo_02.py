from Novo_Modulo_01 import *

def opcao_sim_nao(variavel):
    while True:
        if variavel == "Sim":
            break

        elif variavel == "Nao":
            break

        else:
            print("opção inválida, tente novamente\n\n")
            avaliação_item()
            break



def avaliação_item():
    with open("itens_registrados.csv", "r") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        auxiliar = []
        
        for linha in leitor_csv:
            print(f"\nNome do item: {linha['Nome do item']}\nCondição: {linha['condicao']}\n\n")
            auxiliar.append(f"{linha['Nome do item']}")
            

        escolha_item_avaliação = input("Digite o nome do item que deseja avaliar: ")
        escolha_item_avaliação = escolha_item_avaliação.capitalize()
        if escolha_item_avaliação in auxiliar:
            escolha_aprovacao = input("O item selecionado possui aprovação para venda ou doação?: ")
            escolha_aprovacao = escolha_aprovacao.capitalize()
            opcao_sim_nao(escolha_aprovacao)
            
            
            if escolha_aprovacao == "Sim":
                pontuacao_item = int(input("Informe a quantidade de créditos que esse item vale: "))
                for linha in auxiliar:
                    if linha == escolha_item_avaliação:
                        # Abre o arquivo csv para leitura
                        with open('itens_registrados.csv', newline='') as arquivo_entrada:
                            # Cria um objeto DictReader
                            leitor = csv.DictReader(arquivo_entrada, delimiter=',')
                            # Cria uma lista vazia para armazenar as linhas modificadas
                            linhas = []
                            # Itera sobre as linhas do arquivo csv
                            for linha in leitor:
                                # Verifica se o nome do item é 'Cadeira'
                                if linha['Nome do item'] == escolha_item_avaliação:
                                    # Atribui um novo valor à chave 'Descricao'
                                    linha['aprovacao'] = 'Aprovado'
                                    linha['pontos'] = pontuacao_item
                                # Adiciona a linha modificada à lista
                                linhas.append(linha)
                                

                        # Abre o arquivo csv para escrita
                        with open('itens_registrados.csv', 'w', newline='') as arquivo_saida:
                            # Cria um objeto DictWriter
                            escritor = csv.DictWriter(arquivo_saida, delimiter=',', fieldnames=leitor.fieldnames)
                            # Escreve o cabeçalho do arquivo csv
                            escritor.writeheader()
                            # Escreve as linhas modificadas no arquivo csv
                            escritor.writerows(linhas)

            
            elif escolha_aprovacao == "Nao":
                justificativa_item = input("Informe o motivo: ")
                for linha in auxiliar:
                    if linha == escolha_item_avaliação:
                        with open('itens_registrados.csv', 'r') as arquivo_entrada:
                            # Cria um objeto DictReader
                            leitor = csv.DictReader(arquivo_entrada)
                            fieldnames = leitor.fieldnames

                            # Cria uma lista vazia para armazenar as linhas modificadas
                            linhas = []

                            # Itera sobre as linhas do arquivo csv
                            for linha in leitor:
                                # Verifica se o nome do item é 'Cadeira'
                                if linha['Nome do item'] == escolha_item_avaliação:
                                    # Atribui um novo valor à chave 'Descricao'
                                    linha['aprovacao'] = 'Reprovado'
                                    linha['pontos'] = '0'
                                    linha['justificacao'] = justificativa_item

                                # Adiciona a linha modificada à lista
                                linhas.append(linha)


                        with open('itens_registrados.csv', 'w', newline='') as arquivo_saida:
                            # Cria um objeto DictWriter
                            if 'justificacao' not in fieldnames:
                                fieldnames.append('justificacao')
                            escritor = csv.DictWriter(arquivo_saida, delimiter=',', fieldnames=fieldnames)

                            # Escreve as linhas modificadas no arquivo csv
                            escritor.writeheader()
                            escritor.writerows(linhas)
            else:
                print("Opção inválida!!")       
                avaliação_item()                 
        else:
            print("Nome do produto não encontrado\n")
            avaliação_item()
cria_item()
avaliação_item()

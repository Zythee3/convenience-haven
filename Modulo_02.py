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
# def complemento_arquvio(conteudo):
#     with open(, "a")as arquivo:
#         arquivo.write(conteudo)


def avaliação_item():
    with open("itens_registrados.csv", "r") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        auxiliar = []
        
        for linha in leitor_csv:
            print(f"\nNome do item: {linha['Nome do item']}\nCondição: {linha['condicao']}\n\n")
            auxiliar.append(f"{linha['Nome do item']}")
            

        escolha_item_avaliação = input("Digite o nome do item que deseja avaliar: ")
        if escolha_item_avaliação in auxiliar:
            escolha_aprovacao = input("O item selecionado possui aprovação para venda ou doação?: ")
            escolha_aprovacao = escolha_aprovacao.capitalize()
            opcao_sim_nao(escolha_aprovacao)
            if escolha_aprovacao == "Sim":
                pontuacao_item = int(input("Informe a quantidade de créditos que esse item vale: "))
                for linha in auxiliar:
                    if linha == escolha_item_avaliação:
                        with open("itens_registrados.csv", "a", newline='') as arquivo_:
                            escritor_csv = csv.writer(arquivo)
                            
                            escritor_csv.writerow(linha)
                        
                            


                
            
            # elif escolha_aprovacao == "Nao":
            #     justificativa = input("Informe o motivo: ")
            #     dados_avaliacao_item = f"\nItem aprovado: {escolha_aprovacao}\nJustificativa: {justificativa}\nCreditos: 0"
            #     complemento_arquvio(escolha_item_avaliação, dados_avaliacao_item)
        else:
            print("Nome do produto não encontrado\n")
            avaliação_item()

avaliação_item()

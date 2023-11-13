from Modulo_01 import *

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
def complemento_arquvio(nome_arquivo, conteudo):
    nome_arquivo + ".txt"
    with open(nome_arquivo, "a")as arquivo:
        arquivo.write(conteudo)


def avaliação_item():
    for item in itens_registrados:
        print(f"Nome: {item.nome}\nCondição: {item.condicao}\n\n")
    escolha_item_avaliação = input("Digite o nome do item que deseja avaliar: ")
    if escolha_item_avaliação.capitalize() in nome_itens_registrados:
        escolha_aprovacao = input("O item selecionado possui aprovação para venda ou doação?: ")
        escolha_aprovacao = escolha_aprovacao.capitalize()
        opcao_sim_nao(escolha_aprovacao)
        if escolha_aprovacao == "Sim":
            pontuacao_item = int(input("Informe a quantidade de créditos que esse item vale: "))
            dados_avaliacao_item = f"\nItem aprovado: {escolha_aprovacao}\nCreditos: {pontuacao_item}\n"
            complemento_arquvio(escolha_item_avaliação, dados_avaliacao_item)
        
        elif escolha_aprovacao == "Nao":
            justificativa = input("Informe o motivo: ")
            dados_avaliacao_item = f"\nItem aprovado: {escolha_aprovacao}\nJustificativa: {justificativa}\nCreditos: 0"
            complemento_arquvio(escolha_item_avaliação, dados_avaliacao_item)

    else:
        print("Nome do produto não encontrado\n")
        avaliação_item()

avaliação_item()

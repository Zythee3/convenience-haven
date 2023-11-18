from Modulo_01 import *
from Modulo_02 import*

def sub_menu_criacao_itens():
    print("\n\n[1] Cadastrar um novo item")
    print("[2] Avaliar um item\n")
    
    try:
        escolha_sub_menu = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida, tente novamente\n")
        sub_menu_criacao_itens()
    
    if escolha_sub_menu > 2 or escolha_sub_menu < 1:
        print("Opcção inválida, tente novamente!")
        sub_menu_criacao_itens()
    
    match (escolha_sub_menu):

        case 1:
            cria_item()
        case 2:
            avaliação_item()

sub_menu_criacao_itens()
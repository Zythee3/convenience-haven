class Produtos:
    def __init__(self, nome,categoria, precoUnitario,qtdEstoque):
        self.nome = nome
        self.categoria = categoria
        self.precoUnitario = precoUnitario
        self.qtdEstoque = qtdEstoque

Produto1 = Produtos("Camiseta","Vestuário", 50.00, 100)
Produto2 = Produtos("Calça","Vestuário", 100.00, 50)
Produto3 = Produtos("Salgadinho","Comida", 8.00, 35)

produtos = [
    Produto1,
    Produto2,
    Produto3
]



def menuInicial():
    try:    
        esc = int(input("\nEscolha umas das opções abaixo: \n1. Vender Produto \n2. Cadastrar Produto \n3. Listar Produtos \n4. Sair \n"))
        match esc:
            case 1:
                venderProduto()
            case 2:
                cadastrarProduto()
            case 3:
                listarProdutos(False)
            case 4:
                print("Saindo...")
                SystemExit
            case _:
                print("Opção inválida! Tente novamente.")
                menuInicial()                
    except:
        print("\nOpção inválida! Tente novamente.")
        menuInicial()


def venderProduto():
    try:
        listarProdutos(True)
        print("\n---- Vender Produto ----")
        nomeProduto = input("Digite o nome do produto que deseja vender: ")
        produtoEncontrado = False
        for produto in produtos:
            if produto.nome.lower() == nomeProduto.lower():
                produtoEncontrado = True
                print("Produto encontrado!")
                qtdVenda = int(input("Digite a quantidade que deseja vender: "))
                if qtdVenda > produto.qtdEstoque:
                    print("Quantidade em estoque insuficiente!")
                    menuInicial()
                else:
                    produto.qtdEstoque -= qtdVenda
                    print("Venda realizada com sucesso!")
        if not produtoEncontrado:
            print("Produto não encontrado! Tente novamente.")
            menuInicial()        
        menuInicial()
    except:
        print("\nErro ao vender produto! Tente novamente.")
        menuInicial()    


def cadastrarProduto():
    try:
        print("---- Cadastrar Produto ----")
        nome = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto: ")
        precoUnitario = float(input("Digite o preço unitário do produto (R$): "))
        qtdEstoque = int(input("Digite a quantidade em estoque do produto: "))

        produtos.append(Produtos(nome,categoria,precoUnitario,qtdEstoque))
        print("\nProduto cadastrado com sucesso!")
        menuInicial()
    except:
        print("\nErro ao cadastrar produto! Tente novamente.")
        menuInicial()          


def listarProdutos(inFuncao):
    count = 0
    print("---- Listar Produtos ----")
    if len(produtos) == 0:
        print("Não a produtos cadastrados!")
    for produto in produtos:
        count += 1
        print(f"Produto {count}:")
        print("Nome: ", produto.nome)
        print("Categoria: ", produto.categoria)
        print("Preço Unitário: R$", produto.precoUnitario)
        print("Quantidade em estoque: ", produto.qtdEstoque)
        print("------------------------------\n\n")
    if inFuncao == False:
        input("Pressione qualquer tecla para voltar ao menu inicial")
        menuInicial()    
menuInicial()    
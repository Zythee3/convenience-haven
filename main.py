import json 

class Cliente:
    def __init__(self, nome, itens_aprovados=[]):
        self.nome = nome
        self.itens_aprovados = itens_aprovados

    def to_dict(self):
        return {'nome': self.nome, 'itens_aprovados': self.itens_aprovados}

    @classmethod
    def from_dict(cls, data):
        return cls(nome=data['nome'], itens_aprovados=data['itens_aprovados'])

class Funcionario:
    def atribuir_creditos(self, cliente, item, avaliacao):
        valor_creditos = self.calcular_valor_creditos(avaliacao)
        cliente.itens_aprovados.append({'item': item, 'avaliacao': avaliacao, 'creditos': valor_creditos})

    def calcular_valor_creditos(self, avaliacao):
        return 2 * avaliacao

def exibir_informacoes_cliente(cliente):
    print(f'{cliente.nome} - Itens Aprovados:')
    for item in cliente.itens_aprovados:
        print(f"  Item: {item['item']}, Avaliação: {item['avaliacao']}, Créditos: {item['creditos']}")

def salvar_cliente_em_arquivo(clientes, arquivo):
    clientes_data = [cliente.to_dict() for cliente in clientes]
    with open(arquivo, 'w') as f:
        json.dump(clientes_data, f)

def carregar_clientes_do_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as f:
            data = json.load(f)
            return [Cliente.from_dict(cliente_data) for cliente_data in data]
    except FileNotFoundError:
        return []

clientes = carregar_clientes_do_arquivo('clientes.json')  # Tenta carregar os clientes do arquivo

funcionario = Funcionario()

while True:
    print("\nMenu:")
    print("1. Cadastrar Cliente")
    print("2. Atribuir Créditos")
    print("3. Exibir Informações do Cliente")
    print("0. Sair")

    escolha = input('Digite o número da opção desejada: ')

    if escolha == '1':
        nome_cliente = input('Digite o nome do cliente: ')
        novo_cliente = Cliente(nome=nome_cliente)
        clientes.append(novo_cliente)
        salvar_cliente_em_arquivo(clientes, 'clientes.json')  # Salva os clientes no arquivo
        print('Cliente cadastrado com sucesso!')

    elif escolha == '2':
        if clientes:
            nome_cliente = input('Digite o nome do cliente: ')
            cliente = next((c for c in clientes if c.nome == nome_cliente), None)

            if cliente:
                item_aprovado = input('Digite o nome do item aprovado: ')
                avaliacao = -1
                while avaliacao > 100 or avaliacao < 0:
                    avaliacao = float(input('Digite a avaliação do item (0 a 100): '))

                funcionario.atribuir_creditos(cliente, item_aprovado, avaliacao)
                salvar_cliente_em_arquivo(clientes, 'clientes.json')  # Atualiza o arquivo com as informações mais recentes
                print('Créditos atribuídos com sucesso!')
            else:
                print('Erro: Cliente não encontrado.')
        else:
            print('Erro: Cadastre um cliente primeiro.')

    elif escolha == '3':
        if clientes:
            nome_cliente = input('Digite o nome do cliente: ')
            cliente = next((c for c in clientes if c.nome == nome_cliente), None)

            if cliente:
                exibir_informacoes_cliente(cliente)
            else:
                print('Erro: Cliente não encontrado.')
        else:
            print('Erro: Cadastre um cliente primeiro.')

    elif escolha == '0':
        print('Saindo do programa. Até mais!')
        break

    else:
        print('Opção inválida. Tente novamente.')

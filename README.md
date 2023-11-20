
## Gerenciador de Transações
Este projeto inclui um gerenciador de transações que permite a um gerente realizar o balanço de vendas e gerar relatórios de vendas.

### Funcionalidades do Gerente
O gerente tem acesso a uma funcionalidade que permite realizar o balanço de vendas. Isso permite que o gerente verifique as transações realizadas em um determinado período.

### Filtragem de Vendas
É possível filtrar as vendas por data, categoria de produto e valor total. Isso permite que o gerente veja apenas as transações que atendem a critérios específicos.

### Relatórios de Vendas
Os relatórios de vendas apresentam dados como o total de vendas, os itens trocados e os produtos mais populares. Isso fornece uma visão geral do desempenho das vendas.

### Como usar
Para usar o gerenciador de transações, crie uma instância da classe Manager e use os métodos fornecidos para realizar o balanço de vendas, filtrar vendas e gerar relatórios.

### Por exemplo:

```
manager = Manager('itensregistrados.csv')

# Define the start and end dates for the report
# Defina o inicio e o fim da data de relatorio

start_date = datetime.strptime('2022-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2023-12-31', '%Y-%m-%d')

# Generate a report for a specific category and minimum total value
# Gerar um relatório para uma categoria específica e valor total mínimo.

report = manager.generate_report(start_date, end_date, 'category', 0)

# Print the report
print(report)
```


## **Gerador de Dados de Transações**
Este projeto inclui um gerador de dados de transações que cria um conjunto de dados aleatórios para simular transações de vendas. O gerador cria um arquivo CSV com 20 linhas de dados, cada uma representando uma transação única.

### Funcionalidades do Gerente
O gerente tem acesso a uma funcionalidade que permite realizar o balanço de vendas. Isso permite que o gerente verifique as transações realizadas em um determinado período.

### Filtragem de Vendas
É possível filtrar as vendas por data, categoria de produto e valor total. Isso permite que o gerente veja apenas as transações que atendem a critérios específicos.

### Relatórios de Vendas
Os relatórios de vendas apresentam dados como o total de vendas, os itens trocados e os produtos mais populares. Isso fornece uma visão geral do desempenho das vendas.

### Como usar
Para usar o gerador de dados de transações, execute o script gerador.py. Isso criará um arquivo itensregistrados.csv com 20 linhas de dados de transações.

Para usar a funcionalidade do gerente, crie uma instância da classe Manager e use os métodos fornecidos para realizar o balanço de vendas, filtrar vendas e gerar relatórios.

## Dependências
Este projeto usa as bibliotecas faker e random do Python para gerar dados aleatórios. Certifique-se de instalar essas bibliotecas antes de executar o script.



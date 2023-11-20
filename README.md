
<p align="center">
  <img src="image.png" alt="Alternate Text" />
</p>


# Convenience Haven
Este projeto é um sistema de gerenciamento para a loja Convenience Haven. Ele permite que o gerente da loja acesse relatórios e estatísticas sobre a atividade do sistema.

## Funcionalidades
Relatórios e Estatísticas
O gerente tem acesso a relatórios e estatísticas sobre a atividade do sistema. Isso inclui:

- Número de itens cadastrados
- Número de itens avaliados
- Número de itens trocados
- Número de itens doados
Essas informações são essenciais para o gerente entender a atividade da loja e tomar decisões informadas.

## Geração de Relatórios
O gerente também tem acesso a uma funcionalidade de geração de relatórios sobre as vendas e trocas realizadas na loja. Isso permite que o gerente acompanhe as vendas e trocas ao longo do tempo e identifique tendências ou problemas.

## Como usar
Para gerar um relatório, o gerente deve abrir a janela de relatórios e selecionar as datas de início e fim para o relatório. Em seguida, o gerente pode selecionar a categoria para a qual deseja gerar o relatório. Se nenhuma categoria for selecionada, o relatório será gerado para todas as categorias.

Depois que o gerente selecionar as opções desejadas, ele pode clicar no botão "Gerar relatório" para gerar o relatório. O sistema então gera o relatório e exibe uma mensagem informando que o relatório está sendo gerado.

## Código
O código para este projeto está contido em vários arquivos Python:

- menu.py: Este arquivo contém o código para a interface do usuário do sistema. Ele permite que o gerente selecione as opções para o relatório e gera o relatório quando o gerente clica no botão "Gerar relatório".
- gera_relatorio.py: Este arquivo contém o código para gerar o relatório. Ele pega as opções selecionadas pelo gerente e usa essas opções para gerar o relatório.
- graficos.py: Este arquivo contém o código para gerar os gráficos que são incluídos no relatório.
## Requisitos
Este projeto requer as seguintes bibliotecas Python:

- PIL
- tkinter
- tkcalendar
- pandas

Você pode instalar essas bibliotecas usando pip:
```
pip install pillow tkinter tkcalendar pandas
```


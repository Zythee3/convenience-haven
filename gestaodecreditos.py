import csv

def adicionar_creditos(creditosporitem):
    try: 
        with open("itensresgitrados", 'r') as arquivo:
            leitor = vsc.reader(arquivo)
            
            linhas= list(leitor)
            
        with open("itensregistrados", 'w', newline=' ') as arquivonovo:
            escrito = csv.writer(arquivonovo)
            
            
    
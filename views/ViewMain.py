import sys,os

os.path.abspath(os.curdir)

class ViewMain:
    def tela_opcoes(self):
        print("------ OPÇÕES ------")
        print("1 - LOGIN")
        print("2 - CADASTRAR")
        print("3 - EXCLUIR CADASTRO")
        print("4 - RANKING MELHORES JOGADORES")
        print("0 - SAIR DO GAME")


        opcao = int(input("Escolha a opcao:"))
        return opcao
    
    def msg(self, mensagem):
        print("----------------------------------------")
        print(mensagem)
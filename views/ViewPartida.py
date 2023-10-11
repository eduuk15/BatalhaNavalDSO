import sys,os

os.path.abspath(os.curdir)

class ViewPartida:

    def tela_opcoes(self):
        print("------ OPÇÕES ------")
        print("1 - POSICIONAR AS EMBARCAÇÕES")
        print("2 - #########")
        print("3 - #########")

        opcao = int(input("Escolha a opcao:"))
        return opcao
    
    
    def msg(self, mensagem):
        return mensagem
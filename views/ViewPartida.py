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
    

    def posicionar_embarcacoes(self):
        print("AS EMBARCÇÕES SERÃO POSICIONADAS NA DIREÇÃO HORIZONTAL OU VERTICAL")
        print("BOTES(B)        → QNTD: 3 → OCUPA 1 POSIÇÃO(ÕES)")
        print("SUBMARINOS(S)   → QNTD: 2 → OCUPA 2 POSIÇÃO(ÕES)")
        print("FRAGATAS(F)     → QNTD: 2 → OCUPA 3 POSIÇÃO(ÕES)")
        print("PORTA AVIÕES(P) → QNTD: 1 → OCUPA 4 POSIÇÃO(ÕES)")
        
        posicoes_escolhidas = []
        print("--------------------------------------------------")
        for i in range(1,4):
            print("POSICIONE O",i,"° BOTE (",i,"/3) - OCUPA APENAS 1 POSICAO:")
            posicao = str(input())
            posicoes_escolhidas.append(posicao)

        print("2 - #########")
        print("3 - #########")
    
    def msg(self, mensagem):
        return mensagem
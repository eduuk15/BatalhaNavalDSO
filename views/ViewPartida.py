import sys,os

os.path.abspath(os.curdir)

class ViewPartida:

    def tamanho_mar(self):
        print("--------------------------------------------------")
        print("---------------- CRIANDO  PARTIDA ----------------")
        print("ESCOLHA A DIFICULDADE: ")
        print("1 - FÁCIL [5x5]")
        print("2 - DIFÍCIL [10x10]")

        opcao = int(input("DIFICULDADE DESEJADA: "))
        return opcao
    
    def observacoes(self):
        print("------------------------------------------------------------------")
        print("-------------------------- OBSERVAÇÕES ---------------------------")
        print("AS EMBARCÇÕES SERÃO POSICIONADAS NA DIREÇÃO HORIZONTAL OU VERTICAL")
        print("NÃO SERÁ PERMETIDO SOBREPOSICÇÃO DE EMBARACAÇÕES")
        print("BOTES(B)        → QNTD: 3 → OCUPA 1 POSIÇÃO(ÕES)")
        print("SUBMARINOS(S)   → QNTD: 2 → OCUPA 2 POSIÇÃO(ÕES)")
        print("FRAGATAS(F)     → QNTD: 2 → OCUPA 3 POSIÇÃO(ÕES)")
        print("PORTA AVIÕES(P) → QNTD: 1 → OCUPA 4 POSIÇÃO(ÕES)")
        
    def texto_pega_coordenadas(self):
        print("INDIQUE A POSIÇÃO INICIAL E A FINAL, RESPECTIVAMENTE")
        print("EXEMPLO: Li,Ci  Lf,Cf")
        print("POSIÇÃO DESEJADA: ")

    def pegar_coordenadas(self):
        posicoes_escolhidas = []
        print("------------------------------------------------------------------")
        for i in range(1,4):
            print("POSICIONE O",i,"° BOTE (",i,"/3) - OCUPA 1 POSIÇÃO:")
            posicao = [str(input())]
            posicoes_escolhidas.append(posicao)
        for i in range(1,3):
            print("POSICIONE O",i,"° SUBMARINOS (",i,"/2) - OCUPA 2 POSIÇÕES")
            self.texto_pega_coordenadas()
            posicao = [str(input())]
            posicoes_escolhidas.append(posicao)
        for i in range(1,3):
            print("POSICIONE O",i,"° FRAGATAS (",i,"/2) - OCUPA 3 POSIÇÕES")
            self.texto_pega_coordenadas()
            posicao = [str(input())]
            posicoes_escolhidas.append(posicao)
        for i in range(1):
            print("POSICIONE O",i,"° SUBMARINOS (",i,"/1) - OCUPA 4 POSIÇÕES")
            self.texto_pega_coordenadas()
            posicao = [str(input())]
            posicoes_escolhidas.append(posicao)
        
        return posicoes_escolhidas


    def mensagens(self, mensagem: str):
        print(mensagem)
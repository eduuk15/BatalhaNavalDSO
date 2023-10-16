from models.ModelMar import Mar
from views.ViewMar import ViewMar
                            

class ControllerMar:
    def __init__(self, controle_main):
        self.__mar_jogador = Mar
        self.__mar_pc = Mar
        self.__viewMar = ViewMar()
        self.__controlador_main =  controle_main


    def criar_mar(self, dificuldade: int):
        if dificuldade == 1:
            mar = [[0 for _ in range(5)] for _ in range(5)]
            self.__mar_jogador.mar = mar
            self.__mar_pc.mar = mar
        if dificuldade == 2:
            mar = [[0 for _ in range(10)] for _ in range(10)]
            self.__mar_jogador.mar = mar
            self.__mar_pc.mar = mar
    
        self.__controlador_main.mares_criados()

    def verifica_coordenadas(self, posicao, tamanho, letra):
        colunas = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}

        if tamanho != 1:
            posicoes = posicao.split(',')
            coluna_inicial = colunas[posicoes[0][-1]]
            coluna_final = colunas[posicoes[1][-1]]
            linha_inicial = int(posicoes[0][0:-1])-1
            linha_final = int(posicoes[1][0:-1])-1

            if abs(coluna_final - coluna_inicial) == tamanho + 1:
                if coluna_final > coluna_inicial:
                    for i in range(coluna_inicial, coluna_final + 1):
                        mar = self.__mar_jogador.mar
                        if mar[linha_inicial][i] == 0:
                            self.insere_coordenada(linha_inicial, i, letra)
                else:
                    for i in range(coluna_final, coluna_inicial + 1):
                        mar = self.__mar_jogador.mar
                        if mar[linha_inicial][i] == 0:
                            self.insere_coordenada(linha_inicial, i, letra)

            elif abs(linha_final - linha_inicial) == tamanho + 1:
                if linha_final > linha_inicial:
                    for i in range(linha_inicial, linha_final + 1):
                        mar = self.__mar_jogador.mar
                        if mar[i][coluna_inicial] == 0:
                            self.insere_coordenada(i, coluna_inicial, letra)
                else:
                    for i in range(coluna_final, coluna_inicial + 1):
                        mar = self.__mar_jogador.mar
                        if mar[i][coluna_inicial] == 0:
                            self.insere_coordenada(i, coluna_inicial, letra)
        else:
            coluna = colunas[posicao[1]]
            linha = int(posicao[0]) - 1
            mar = self.__mar_jogador.mar
            if mar[linha][coluna] == 0:
                self.insere_coordenada(linha, coluna, letra)
                
                
    def insere_coordenada(self, linha, coluna, letra):
        self.__mar_jogador.mar[linha][coluna] = letra
    
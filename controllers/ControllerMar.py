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
        colunas = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10}

        if tamanho != 1:
            posicoes = posicao.split(',')
            coluna_inicial = int(colunas[posicoes[0][-1]])
            coluna_final = int(colunas[posicoes[1][-1]])
            linha_inicial = int(posicoes[0][0:-1])
            linha_final = int(posicoes[1][0:-1])

            if abs(coluna_final - coluna_inicial) + 1 == tamanho:
                if coluna_final > coluna_inicial:
                    for i in range(coluna_inicial, coluna_final + 1):
                        mar = self.__mar_jogador.mar
                        if mar[linha_inicial - 1][i - 1] == 0:
                            self.insere_coordenada(linha_inicial, i, letra)
                        else:
                            return False
                else:
                    for i in range(coluna_final, coluna_inicial + 1):
                        mar = self.__mar_jogador.mar
                        if mar[linha_inicial - 1][i - 1] == 0:
                            self.insere_coordenada(linha_inicial, i, letra)
                        else:
                            return False

            elif abs(linha_final - linha_inicial) + 1 == tamanho:
                if linha_final > linha_inicial:
                    for i in range(linha_inicial, linha_final + 1):
                        mar = self.__mar_jogador.mar
                        if mar[i - 1][coluna_inicial - 1] == 0:
                            self.insere_coordenada(i, coluna_inicial, letra)
                        else:
                            return False
                else:
                    for i in range(coluna_final, coluna_inicial + 1):
                        mar = self.__mar_jogador.mar
                        if mar[i - 1][coluna_inicial - 1] == 0:
                            self.insere_coordenada(i, coluna_inicial, letra)
                        else:
                            return False
        else:
            coluna = int(colunas[posicao[1]])
            linha = int(posicao[0])
            mar = self.__mar_jogador.mar
            if mar[linha - 1][coluna - 1] == 0:
                return self.insere_coordenada(linha, coluna, letra)
            else:
                return False
            
        return True
                

    def insere_coordenada(self, linha, coluna, letra):
        self.__mar_jogador.mar[linha - 1][coluna - 1] = letra
        return True
    
    def ve_mar(self):
        self.__viewMar.ver_mar(self.__mar_jogador.mar)
    
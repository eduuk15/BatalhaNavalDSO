import sys
import os

sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/models')
sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/views')


class Partida:
    def __init__(self, jogador, mar):
        self.__jogador = jogador
        self.__mar = mar
        self.__pontuacao = None
        self.__lista_de_disparos = []

    @property
    def ver_pontuaco(self):
        return self.__pontuacao
    

    def alterar_pontucao(self, pontuacao):
        self.__pontuacao = pontuacao
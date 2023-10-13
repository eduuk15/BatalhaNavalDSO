import sys
import os

sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/models')
sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/views')


from models.ModelMar import Mar

class Partida:
    def __init__(self, jogador, mar):
        self.__jogador = jogador
        self.__mar = Mar
        self.__pontuacao = None
        self.__lista_de_disparos = []


    def pontucao(self):
        return self.__pontuacao
    
    def alterar_pontucao(self, pontuacao):
        self.__pontuacao = pontuacao  

    def ver_diparos_feitos(self):
        return self.__lista_de_disparos
    
    def incluir_disparo(self, disparo):
        self.__lista_de_disparos.append(disparo)


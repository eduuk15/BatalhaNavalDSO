from models.ModelMar import Mar

class Partida:
    def __init__(self, jogador, mar):
        self.__jogador = jogador
        self.__mar = Mar
        self.__pontuacao = None
        self.__lista_de_disparos = []

    @property
    def pontucao(self):
        return self.__pontuacao
    
    @pontucao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao  

    @property
    def lista_de_disparos(self):
        return self.__lista_de_disparos
    
    def adicioanr_disparo(self, disparo: str):
        self.__lista_de_disparos.append(disparo)
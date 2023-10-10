from models.ModelPartida import Partida
from datetime import date as Date

class Jogador:
    def __init__(self, nome: str, nascimento: Date, senha: str):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__senha = senha
        self.__historico = []
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def nasciemnto(self):
        return self.__nascimento
    
    @nasciemnto.setter
    def nascimento(self, nascimento: Date):
        self.__nascimento = nascimento
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def ver_historico(self):
        return self.__historico
    
    def incluir_partida(self, partida: Partida):
    # assim quando a partida acaba deve ser incluida na lista de partidas do jogador
        if isinstance(partida, Partida):
            self.__historico.append(partida)
    
    # deve retornar a melhor partida do jogador (maior pontuação)
    #def melhor_partida(self, partida: Partida)
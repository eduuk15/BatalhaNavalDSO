from views.ViewPartida import ViewPartida
from models.ModelPartida import Partida

class ControllerPartida:
    def __init__(self, controle_main):
        self.__partida = Partida
        self.__view_partida = ViewPartida()
        self.__controlador_main =  controle_main

    def comecar_partida(self):
        dificuldade = self.__view_partida.tamanho_mar()
        self.__controlador_main.tamanho_mar(dificuldade)

    def mensagens(self, mensagem):
        self.__view_partida.mensagens(mensagem)
        
        
        

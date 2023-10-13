import sys
import os

sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/models')
sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/views')

from views.ViewPartida import ViewPartida
from models.ModelPartida import Partida

class ControllerPartida:
    def __init__(self, controle_main):
        self.__partida = Partida
        self.__view_partida = ViewPartida()
        self.__controlador_main =  controle_main

    def comecar_partida(self):
        self.posicionar_embarcacoes()
    
    def posicionar_embarcacoes(self):
        self.__view_partida.posicionar_embarcacoes()


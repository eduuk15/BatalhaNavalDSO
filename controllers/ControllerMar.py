import sys

sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/models')
sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/views')

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
            self.__mar_jogador.tamanho_mar(mar)
            self.__mar_pc.tamanho_mar(mar)
        if dificuldade == 2:
            mar = [[0 for _ in range(10)] for _ in range(10)]
            self.__mar_jogador.tamanho_mar(mar)
            self.__mar_pc.tamanho_mar(mar)

        self.__controlador_main.mares_criados()
    
   #def verificar_posicoes(self, posicoes_embarcacoes):
    
import sys


sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/models')
sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/views')


class ControllerEmbarcacao:
    def __init__(self, controlador_main) -> None:
        self.__embarcacoes_jogador = []
        self.__embarcacoes_pc = []
        self.__controlador_main = controlador_main
            
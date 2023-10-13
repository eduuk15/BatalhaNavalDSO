import sys
import os

sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/controllers')
sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/views/ViewMain.py')


from controllers.ControllerJogador import ControllerJogador
from controllers.ControllerPartida import ControllerPartida
from views.ViewMain import ViewMain

class ControllerMain:
    def __init__(self) :
        self.__viewMain = ViewMain()
        self.__contollerJogador = ControllerJogador(self)
        self.__controllerPartida = ControllerPartida(self)

    
    def inicializa_sistema(self):
        if self.__contollerJogador.existe_jogador_cadastrado():
            self.mostra_tela_main()
        else:
            self.__contollerJogador.cadastrar()
            self.__contollerJogador.abre_tela()

    def logar(self):
        self.__contollerJogador.logar()
        self.__contollerJogador.abre_tela()

    def cadastra_jogador(self):
        self.__contollerJogador.cadastrar()

    def comeca_partida(self):
        self.__controllerPartida.comecar_partida()

    def mensagem(self, mensagem):
        self.__viewMain.msg(mensagem)
    
    def exclui_cadastro(self):
        self.__contollerJogador.excluir_jogador()

    def encerra_sistema(self):
        exit(0)
            
    def mostra_tela_main(self):
        lista_opcoes = {1: self.logar, 2: self.cadastra_jogador, 3: self.exclui_cadastro, 0: self.encerra_sistema}
        
        while True:
            opcao_escolhida = self.__viewMain.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
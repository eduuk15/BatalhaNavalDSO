from controllers.ControllerJogador import ControllerJogador
from views.ViewMain import ViewMain


class ControllerMain:
    def __init__(self) :
        self.__viewMain = ViewMain
        self.__contollerJogador = ControllerJogador

    
    def inicializa_sistema(self):
        if len(self.__contollerJogador.jogadores) > 0 :
            self.mostra_tela_main()
        else:
            self.__contollerJogador.cadastrar()
    
    def cadastro(self):
        self.__contollerJogador.cadastrar()
    
            
    def mostra_tela_main(self):
        lista_opcoes = {1: self.logar, 2: self.cadastra_amigos, 0: self.encerra_sistema}
        
        while True:
            opcao_escolhida = self.__viewMain.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
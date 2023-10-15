from controllers.ControllerJogador import ControllerJogador
from controllers.ControllerPartida import ControllerPartida
from controllers.ControllerMar import ControllerMar
from controllers.ControllerEmbarcacao import ControllerEmbarcacao
from views.ViewMain import ViewMain

class ControllerMain:
    def __init__(self):
        self.__viewMain = ViewMain()
        self.__contollerJogador = ControllerJogador(self)
        self.__controllerPartida = ControllerPartida(self)
        self.__controllerMar = ControllerMar(self)
        self.__controllerEmbarcacao = ControllerEmbarcacao(self)

    # Parte de Jogador/Login/Cadastro
    def inicializa_sistema(self):
        if self.__contollerJogador.existe_jogador_cadastrado():
            self.mostra_tela_main()
        else:
            self.__contollerJogador.cadastrar()
            self.__contollerJogador.abre_tela()

    def logar(self):
        if self.__contollerJogador.existe_jogador_cadastrado():
            if self.__contollerJogador.logar():
                self.__contollerJogador.abre_tela()
            else:
                self.__contollerJogador.logar()
        else:
            self.inicializa_sistema()
    
    def cadastra_jogador(self):
        self.__contollerJogador.cadastrar()

    def exclui_cadastro(self):
        self.__contollerJogador.excluir_jogador()

    #Parte de Criacao da Partida
    def comeca_partida(self):
        self.__controllerPartida.comecar_partida()

    def tamanho_mar(self, dificuldade):
        self.__controllerMar.criar_mar(dificuldade)

    def mensagens_mar_para_partida(self, msg):
        self.__controllerPartida.mensagens(msg)

    def mensagem(self, mensagem):
        self.__viewMain.msg(mensagem)

    def encerra_sistema(self):
        exit(0)
            
    def mostra_tela_main(self):
        lista_opcoes = {1: self.logar, 2: self.cadastra_jogador, 3: self.exclui_cadastro, 0: self.encerra_sistema}
        
        while True:
            opcao_escolhida = self.__viewMain.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
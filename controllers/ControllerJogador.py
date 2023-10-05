from models.ModelJogador import Jogador
from views.ViewJogador import ViewJogador
from datetime import date as Date

class ControllerJogador:
    def __init__(self, controle_main):
        self.__jogadores = []
        self.__view_jogador = ViewJogador()
        self.__controlador_main =  controle_main

    
    def lista_de_jogadores(self):
        for player in self.__jogadores:
            self.__view_jogador.mostrar_jogador({"nome": player.nome, "nascimento": player.nascimento})
    
    def pega_jogador_por_nome_e_senha(self, nome: str, senha: str):
        for player in self.__jogadores:
            if player.nome == nome and player.senha == senha:
                return player
        return None

    def cadastrar(self):
        dados_jogador = self.__view_jogador.pega_dados_jogador()
        novo_jogador= Jogador(dados_jogador["nome"], dados_jogador["nascimento"], dados_jogador["senha"])
        self.__jogadores.append(novo_jogador)

    def alterar_cadastro(self):
        self.lista_de_jogadores()
        dados_player =  self.__view_jogador.seleciona_jogador()
        player = self.pega_jogador_por_nome_e_senha(dados_player["nome"], dados_player["nascimento"])

        if player is not None:
            novos_dados_jogador =  self.__view_jogador.pega_dados_jogador()
            player.nome = novos_dados_jogador["nome"]
            player.nascimento =  novos_dados_jogador["nasciemnto"]
            player.senha = novos_dados_jogador["senha"]
            self.lista_de_jogadores()
        else:
            self.__view_jogador.mostrar_mensagem("Jogador não existe")


    def abre_tela(self):
        lista_opcoes = {1: self.jogar, 2: self.cadastrar, 3: self.alterar_cadastro, 4: self.excluir_cadastro, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__view_jogador.tela_opcoes()]()
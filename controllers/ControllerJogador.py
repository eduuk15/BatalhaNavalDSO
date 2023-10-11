import sys
import os

sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/models')
sys.path.insert(0, '/Layon/UFSC/2° Semestre/DSO/Trabalho/BatalhaNavalDSO/views')

from views.ViewJogador import ViewJogador
from models.ModelJogador import Jogador


class ControllerJogador:
    def __init__(self, controle_main):
        self.__jogadores = []
        self.__view_jogador = ViewJogador()
        self.__controlador_main =  controle_main

    @property
    def jogadores(self):
        return self.__jogadores
    
    def existe_jogador_cadastrado(self):
        if len(self.__jogadores) > 0 :
            return True

    def lista_de_jogadores(self):
        for player in self.__jogadores:
            self.__view_jogador.mostrar_jogador({"nome": player.nome, "nascimento": player.nascimento})
    
    def pega_jogador_por_nome_e_senha(self, nome: str, senha: str):
        for player in self.__jogadores:
            if player.nome == nome and player.senha == senha:
                return player
        return None
    
    def jogar(self):
        self.__controlador_main.mostra_tela_main()

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
            self.__view_jogador.mensagem("Jogador não existe")

    def excluir_jogador(self):
        self.lista_de_jogadores()
        dados_player = self.__view_jogador.seleciona_jogador()
        player = self.pega_jogador_por_nome_e_senha(dados_player)
        
        if player is not None:
            self.__jogadores.remove(player)
            self.__view_jogador.mensagem("Jogador Removido")
            self.lista_de_jogadores()
        else:
            self.__view_jogador.mensagem("Jogador não cadastrado")
    
    def retornar_main(self):
        self.__controlador_main.mostra_tela_main()

    def abre_tela(self):
        self.__view_jogador.tela_opcoes()
        lista_opcoes = {1: self.jogar, 2: self.cadastrar, 3: self.alterar_cadastro, 4: self.excluir_jogador, 0: self.retornar_main}

        continua = True
        while continua:
            lista_opcoes[self.__view_jogador.tela_opcoes()]()
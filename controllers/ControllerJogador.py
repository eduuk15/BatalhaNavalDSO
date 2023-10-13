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
        self.__jogador1 = None

    @property
    def jogadores(self):
        return self.__jogadores
    
    def existe_jogador_cadastrado(self):
        if len(self.__jogadores) > 0 :
            return True
        
    @property
    def jogador1(self):
        return self.__jogador1
    
        
    def logar(self):
        self.__view_jogador.login()
        dados_jogador = self.__view_jogador.seleciona_jogador()
        jogador = self.pega_jogador_por_nome_e_senha(dados_jogador["nome"], dados_jogador["senha"])
        if jogador is not None:
            self.__jogador1 = jogador
            self.__view_jogador.mensagem("Bem-Vindo " + self.__jogador1.nome)
        else:
            self.__controlador_main.mensagem("JOGADOR NÃO CADASTRADO")


    def lista_de_jogadores(self):
        for player in self.__jogadores:
            self.__view_jogador.mostrar_jogador({"nome": player.nome, "nascimento": player.nascimento})
    
    def pega_jogador_por_nome_e_senha(self, nome: str, senha: str):
        for player in self.__jogadores:
            if player.nome == nome and player.senha == senha:
                return player
        return None
    
    def compara_nomes_e_senhas(self, nome: str, senha: str):
        for player in self.__jogadores:
            if player.nome == nome:
                return "NOME JÁ EM USO. ESCOLHA OUTRO NOME."
            elif player.senha == senha:
                return "SENHA INDISPONÍVEL."
        return True         

    def jogar(self):
        self.__controlador_main.comecar_partida()

    def historico(self):
        return self.__jogador1.ver_historico

    def cadastrar(self):
        self.__view_jogador.cadastro()
        dados_jogador = self.__view_jogador.pega_dados_jogador()
        validacao_cadastro = self.compara_nomes_e_senhas(dados_jogador["nome"], dados_jogador["senha"])
        if validacao_cadastro == True:
            novo_jogador= Jogador(dados_jogador["nome"], dados_jogador["nascimento"], dados_jogador["senha"])
            self.__jogadores.append(novo_jogador)
        else:
            self.__view_jogador.mensagem(validacao_cadastro)


    def alterar_cadastro(self):
        self.lista_de_jogadores()
        dados_player =  self.__view_jogador.seleciona_jogador()
        player = self.pega_jogador_por_nome_e_senha(dados_player["nome"], dados_player["senha"])

        if player is not None:

            novos_dados_jogador =  self.__view_jogador.pega_dados_jogador()
            player.nome = novos_dados_jogador["nome"]
            player.nascimento =  novos_dados_jogador["nascimento"]
            player.senha = novos_dados_jogador["senha"]
            self.lista_de_jogadores()
            self.abre_tela()
        else:
            self.__view_jogador.mensagem("Jogador não existe")
            self.alterar_cadastro()

    def excluir_jogador(self):
        self.lista_de_jogadores()
        dados_player = self.__view_jogador.seleciona_jogador()
        player = self.pega_jogador_por_nome_e_senha(dados_player["nome"], dados_player["senha"])
        
        if player is not None:
            self.__jogadores.remove(player)
            self.__view_jogador.mensagem("Jogador Removido")
            self.lista_de_jogadores()
        else:
            self.__view_jogador.mensagem("Jogador não cadastrado")
    
    def retornar_main(self):
        self.__controlador_main.mostra_tela_main()

    def abre_tela(self):
        lista_opcoes = {1: self.jogar, 2: self.historico, 3: self.alterar_cadastro, 0: self.retornar_main}

        continua = True
        while continua:
            lista_opcoes[self.__view_jogador.tela_opcoes()]()
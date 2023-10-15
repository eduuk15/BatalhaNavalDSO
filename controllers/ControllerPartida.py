from views.ViewPartida import ViewPartida
from models.ModelPartida import Partida

class ControllerPartida:
    def __init__(self, controle_main):
        self.__partida = Partida
        self.__view_partida = ViewPartida()
        self.__controlador_main =  controle_main

    def cria_partida(self):
        dificuldade = self.__view_partida.tamanho_mar()
        self.__controlador_main.tamanho_mar(dificuldade)
            
    def leva_embarcacoes_para_o_mar(self, posicoes_embarcacoes):
        self.__controlador_main.leva_embarcacoes_para_o_mar(posicoes_embarcacoes)
       
    def posiciona_embarcacoes_jogador(self):
       self.__view_partida.observacoes()
       posicoes_escolhidas = self.__view_partida.pegar_coordenadas()
       self.decifra_colunas(posicoes_escolhidas)

    #Substitui as letras(colunas) por n°
    def decifra_colunas(self, posicoes_escolhidas):
        posicao_embarcacoes = {"b1": None, "b2": None, "b3": None,"s1": None, "s2": None,"f1": None, "f2": None,"p1": None}
        colunas = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10}

        for posicoes, embarcacao in zip(posicoes_escolhidas, posicao_embarcacoes):
            posicoes[2] = colunas[posicoes[2]]
            posicoes[6] = colunas[posicoes[6]]
            posicao_embarcacoes[embarcacao] = posicoes

        self.leva_embarcacoes_para_o_mar(posicao_embarcacoes)
        

        


    def mensagens(self, mensagem):
        self.__view_partida.mensagens(mensagem)
        
        
        

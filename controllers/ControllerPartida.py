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
    
       b = 1
       while b <= 3:
        posicao = self.__view_partida.pegar_coordenadas(b, 3, 'BOTES', 1)
        if self.__controlador_main.verifica_coordenadas(posicao, 1, 'B'):
            self.__controlador_main.ve_mar()
        else:
            self.__view_partida.erro_inserir_coordenada()
            b -= 1
        b += 1

       s = 1
       while s <= 2:
        posicao = self.__view_partida.pegar_coordenadas(s, 2, 'SUBMARINOS', 2)
        if self.__controlador_main.verifica_coordenadas(posicao, 2, 'S'):
            self.__controlador_main.ve_mar()
        else:
           self.__view_partida.erro_inserir_coordenada()
           s -= 1
        s += 1
       
       f = 1
       while f <= 2:
        posicao = self.__view_partida.pegar_coordenadas(f, 2, 'FRAGATAS', 3)
        if self.__controlador_main.verifica_coordenadas(posicao, 3, 'F'):
            self.__controlador_main.ve_mar()
        else:
           self.__view_partida.erro_inserir_coordenada()
           f -= 1
        f += 1

       p = 1
       while p <= 1: 
        posicao = self.__view_partida.pegar_coordenadas(p, 1, 'PORTA-AVIÕES', 4)
        if self.__controlador_main.verifica_coordenadas(posicao, 4, 'P'):
            self.__controlador_main.ve_mar()
        else:
           self.__view_partida.erro_inserir_coordenada()
           p -= 1
        p += 1

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
        
        
        

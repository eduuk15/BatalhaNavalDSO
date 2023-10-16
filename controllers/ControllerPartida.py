from views.ViewPartida import ViewPartida
from models.ModelPartida import Partida

class ControllerPartida:
    def __init__(self, controle_main):
        self.__partida = Partida
        self.__view_partida = ViewPartida()
        self.__controlador_main =  controle_main
        self.__lista_de_barcos =    [   {'tipo': 'BOTES', 'quantidade': 3, 'tamanho':1      },
                                        {'tipo': 'SUBMARINOS', 'quantidade': 2, 'tamanho':2 },
                                        {'tipo': 'FRAGATAS', 'quantidade': 2, 'tamanho': 3  },
                                        {'tipo': 'PORTA-AVIÕES', 'quantidade': 1, 'tamanho': 4}   ]

    def cria_partida(self):
        dificuldade = self.__view_partida.tamanho_mar()
        self.__controlador_main.tamanho_mar(dificuldade)
            
    def leva_embarcacoes_para_o_mar(self, posicoes_embarcacoes):
        self.__controlador_main.leva_embarcacoes_para_o_mar(posicoes_embarcacoes)
       
    def posiciona_embarcacoes_jogador(self):
        self.__view_partida.observacoes()

        for barcos in self.__lista_de_barcos:
            tipo = barcos['tipo']
            qntd = barcos['quantidade']
            tamanho = barcos['tamanho']

            i = 1
            while i <= qntd:
                posicao = self.__view_partida.pegar_coordenadas(i, qntd, tipo, tamanho)
                if self.__controlador_main.verifica_coordenadas(posicao, tamanho, tipo[0]):
                    i += 1
                    continue
                else:
                    self.__view_partida.erro_inserir_coordenadas_embarcacao()
                    continue
                


    def mensagens(self, mensagem):
        self.__view_partida.mensagens(mensagem)
        
        
        

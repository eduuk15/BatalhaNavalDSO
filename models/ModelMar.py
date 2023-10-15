

class Mar:
    def __init__(self):
        self.__matriz = None
        self.__posicoes_embarcacoes = {"b1": None, "b2": None, "b3": None,
                                       "s1": None, "s2": None,
                                       "f1": None, "f2": None,
                                       "p1": None}
        
    @property
    def matriz(self):
        return self.__matriz
    
    def tamanho_mar(self, mar):
        self.__matriz = mar


class Mar:
    def __init__(self):
        self.__mar = []
        self.__posicoes_embarcacoes = {b1: None, b2: None, b3: None,
                                       s1: None, s2: None,
                                       f1: None, f2: None,
                                       p1: None}
        
    @property
    def mar(self):
        return self.mar
    
    @mar.setter
    def mar(self, mar):
        self.mar = mar  
    
    
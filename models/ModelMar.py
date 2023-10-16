

class Mar:
    def __init__(self):
        self.__mar = []
        
    @property
    def mar(self):
        return self.__mar
    
    @mar.setter
    def mar(self, mar):
        self.__mar = mar  
    
    def tamanho_mar(self, mar):
        self.__matriz = mar
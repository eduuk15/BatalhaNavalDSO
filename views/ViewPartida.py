class ViewPartida:

    def tamanho_mar(self):
        print("--------------------------------------------------")
        print("---------------- CRIANDO  PARTIDA ----------------")
        print("ESCOLHA A DIFICULDADE: ")
        print("1 - FÁCIL [5x5]")
        print("2 - DIFÍCIL [10x10]")

        opcao = int(input("DIFICULDADE DESEJADA: "))
        return opcao
    
    def mensagens(self, mensagem: str):
        print(mensagem)
class ViewMain:
    def tela_opcoes(self):
        print("----------------- MENU PRINCIPAL -----------------")
        print("1 - LOGIN")
        print("2 - CADASTRAR")
        print("3 - EXCLUIR CADASTRO")
        print("4 - RANKING MELHORES JOGADORES")
        print("0 - SAIR DO GAME")


        opcao = int(input("Escolha a opcao:"))
        return opcao
    
    def msg(self, mensagem):
        print("--------------------------------------------------")
        print(mensagem)

    def exibe_ranking(self, ranking):
        print("----------------------------- RANKING ----------------------------")
        for nome, pontuacao in ranking.items():
            print(f'Nome: {nome} - Pontuação Total: {pontuacao}')
        print("------------------------------------------------------------------")

    def erro_tela(self):
        print("--------------------------------------------------")
        print("Erro ao acessar tela. Certifique-se de escolheu uma opção válida.")
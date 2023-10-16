

class ViewJogador:
    def tela_opcoes(self):
        print("--------------------- OPÇÕES ---------------------")
        print("ESCOLHA ALGUMA OPÇÃO")
        print("1 - JOGAR")
        print("2 - VER HISTÓRICO DE PARTIDAS")
        print("3 - ALTERAR CADASTRO")
        print("0 - RETORNAR")


        opcao =  int(input("Escolha a opcao: "))
        return opcao
    
    def login(self):
        print("------------------ FAÇA O LOGIN ------------------")

    def cadastro(self):
        print("------------------- CADASTRO ---------------------")
        
        
    def pega_dados_jogador(self):
        print("----------- INSIRA OS SEGUINTES DADOS ------------")
        nome = input("Nome do Player: ")
        nascimento = input("Data de nascimento do player (##/##/####): ")
        senha = input("Senha: ")
        return {"nome": nome, "nascimento" : nascimento, "senha": senha}
    
    def mostrar_jogador(self, dados_jogador):
        print("--------------------------------------------------")
        print("NOME DO PLAYER: ", dados_jogador["nome"])
        print("DATA DE NASCIMENTO: ", dados_jogador["nascimento"])
        print("\n")
    
    def seleciona_jogador(self):
        print("--------------------------------------------------")
        nome = input("Digite o no Player: ")
        senha = input("Digite a senha: ")

        return {"nome": nome, "senha": senha}
    
    def mensagem(self, mensagem: str):
        print("--------------------------------------------------")
        print(mensagem)

    def exibe_historico(self, lista_disparos, n_partida):
        print("--------------- PARTIDA " +  str(n_partida + 1) + " --------------")
        for i in range(0, len(lista_disparos)):
            print(lista_disparos[i])
        print("------------------------------------------------------------------")

    def erro_data(self):
        print("--------------------------------------------------")
        print("Formato de data inválido. Certifique-se de que a data está no formato 'dd/mm/aaaa'.")

    def erro_nome(self):
        print("--------------------------------------------------")
        print("Nome vazio. Certifique-se de preencher o nome.")

    def erro_senha(self):
        print("--------------------------------------------------")
        print("Senha vazia. Certifique-se de preencher a senha.")

    def erro_tela(self):
        print("--------------------------------------------------")
        print("Erro ao acessar a tela. Certifique-se de escolheu uma opção válida.")

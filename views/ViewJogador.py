

class ViewJogador:
    def tela_opcoes(self):
        print("------ OPÇÕES ------")
        print("Escolha a opção")
        print("1 - Jogar")
        print("2 - Cadastrar Novo Jogador")
        print("3 - Alterar Cadastro")
        print("4 - Excluir Cadastro")
        print("0 - Retonar")

        opcao =  int(input("Escolha a opcao: "))
        return opcao
        
    def pega_dados_jogador(self):
        print("-------- INSIRA OS SEGUINTES DADOS ----------")
        nome = input("Nome do Player: ")
        nascimento = input(" Data de nascimento do player (##/##/####): ")
        senha = input("Senha: ")
        return {"nome": nome, "nascimento" : nascimento, "senha": senha}
    
    def mostrar_jogador(self, dados_jogador):
        print("NOME DO PLAYER: ", dados_jogador["nome"])
        print("DATA DE NASCIMENTO: ", dados_jogador["nascimento"])
        print("\n")
    
    def seleciona_jogador(self):
        nome = input("Digite o no Player: ")
        senha = input("Digite a senha: ")

        return {"nome": nome, "senha": senha}
    
    def mensagem(self, mensagem: str):
        print(mensagem)
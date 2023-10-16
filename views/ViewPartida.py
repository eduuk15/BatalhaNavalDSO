class ViewPartida:

    def tamanho_mar(self):
        print("--------------------------------------------------")
        print("---------------- CRIANDO  PARTIDA ----------------")
        print("ESCOLHA A DIFICULDADE: ")
        print("1 - FÁCIL [5x5]")
        print("2 - DIFÍCIL [10x10]")

        opcao = int(input("DIFICULDADE DESEJADA: "))
        return opcao
    
    def observacoes(self):
        print("------------------------------------------------------------------")
        print("-------------------------- OBSERVAÇÕES ---------------------------")
        print("AS EMBARCÇÕES SERÃO POSICIONADAS NA DIREÇÃO HORIZONTAL OU VERTICAL")
        print("NÃO SERÁ PERMITIDO SOBREPOSIÇÃO DE EMBARCAÇÕES")
        print("BOTES(B)        → QNTD: 3 → OCUPA 1 POSIÇÃO(ÕES)")
        print("SUBMARINOS(S)   → QNTD: 2 → OCUPA 2 POSIÇÃO(ÕES)")
        print("FRAGATAS(F)     → QNTD: 2 → OCUPA 3 POSIÇÃO(ÕES)")
        print("PORTA AVIÕES(P) → QNTD: 1 → OCUPA 4 POSIÇÃO(ÕES)")
        
    def texto_pega_coordenadas(self):
        print("INDIQUE A POSIÇÃO INICIAL E A FINAL, RESPECTIVAMENTE")
        print("A VERIFICAÇÃO SE A EMBARCAÇÃO SERÁ DIRECIONADA NA VERTICAL OU HORIZONTAL, DEPENDE DA SUA ESCOLHA:")
        print("CASO OS NÚMEROS - LINHAS -  FOREM IGUAIS,  A EMBARCAÇÃO ESTARÁ NA HORIZONTAL")
        print("CASO AS LETRAS - COLUNAS - FOREM IGUAIS, A EMBARCAÇÃO ESTARÁ NA VERTICAL")
        print("EXEMPLO: 5A,7A")
        print("POSIÇÃO DESEJADA: ")

    def pegar_coordenadas(self, i, qtd_embarcacoes, nome_embarcacao, qtd_posicoes):
        print("------------------------------------------------------------------")
        print("POSICIONE O",i,"°", nome_embarcacao, "(",i,"/", qtd_embarcacoes,") - OCUPA", qtd_posicoes, "POSIÇÃO:")
        if qtd_posicoes != 1:
            self.texto_pega_coordenadas()
        posicao = input().upper()
        return posicao
    
    def erro_inserir_coordenadas_embarcacao(self):
        print("------------------------------------------------------------------")
        print(" ATENÇÃO : COORDENADAS INVÁLIDAS")
        self.observacoes()
       #erro_inserir_coordenadas_embarcacao
        


    def mensagens(self, mensagem: str):
        print(mensagem)

    def erro_inserir_coordenada(self):
        print("ERRO AO INSERIR COORDENADA. TENTE NOVAMENTE!")

    def fazer_jogada(self):
        print("------------------------------------------------------------------")
        print("FAÇA SUA JOGADA!")
        posicao = input().upper()
        return posicao
    
    def erro_ao_jogar(self):
        print("JOGADA INVÁLIDA. TENTE NOVAMENTE.")

    def acertou(self, posicao, letra, mar_exibicao):
        embarcacoes = {'B': 'Bote', 'F': 'Fragata', 'S': 'Submarino', 'P': 'Porta-Aviões'}
        nome_embarcacao = embarcacoes[letra]
        print('EM ' + posicao + ' VOCÊ ACERTOU UM(A) ' + nome_embarcacao + '!.')
        for i in range(0, len(mar_exibicao)):
            print(mar_exibicao[i])
    def errou(self, posicao, mar_exibicao):
        print('EM ' + posicao + ' NÃO HÁ NENHUMA EMBARCAÇÃO. VOCÊ ERROU!')
        for i in range(0, len(mar_exibicao)):
            print(mar_exibicao[i])

    def ganhou(self):
        print('PARABÉNS! VOCÊ AFUNDOU TODAS AS EMBARCAÇÕES INIMIGAS. VOCÊ GANHOU!')

    def perdeu(self):
        print('OPS... O COMPUTADOR AFUNDOU TODAS AS SUAS EMBARCAÇÕES. VOCÊ PERDEU!')

    def computador_acertou(self, posicao, letra):
        embarcacoes = {'B': 'Bote', 'F': 'Fragata', 'S': 'Submarino', 'P': 'Porta-Aviões'}
        nome_embarcacao = embarcacoes[letra]
        print('EM ' + posicao + ' O COMPUTADOR ACERTOU UM(A) ' + nome_embarcacao + '!.')
    def computador_errou(self, posicao):
        print('EM ' + posicao + ' NÃO HÁ NENHUMA EMBARCAÇÃO. O COMPUTADOR ERROU!')

    def exibe_pontuacao(self, pontuacao):
        print("------------------------------------------------------------------")
        print('PONTUAÇÃO DA PARTIDA')
        print('JOGADOR ' + str(pontuacao[0]) + ' X ' + 'COMPUTADOR ' + str(pontuacao[1]))
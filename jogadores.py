jogadores = []
def  cadastrar_jogadores():

    quantidade = int(input("Quantas pessoas vão jogar? "))

    for i in range(quantidade):
        nome = input(f"Qual o nome do jogador {i + 1}? ")
        jogador = {"nome" : nome,
                   "saldo" : 2458000,
                   "posicao" : 0,
                   "propriedades":[],
        }
        jogadores.append(jogador)
cadastrar_jogadores()
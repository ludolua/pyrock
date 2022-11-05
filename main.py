import random

papel = "Velho Papel Amarelado"
pedra = "Pedra da Lua"
tesoura = "Tesoura de Prata"
perguntar = int(input('''Olá Viajante... escolha uma das opções abaixo: 

[0] Pedra da Lua    
[1] Velho Papel Amarelado
[2] Tesoura Antiga
 
Digite sua escolha: '''))
computador = random.randint(0,2)

if computador == 0:
    print('O bardo escolheu: ' + pedra)
    if perguntar == 0:
        print("Empate!")
    elif perguntar == 1:
        print("Jogador perdeu")
    elif perguntar == 2:
        print("Bardo venceu")
    else:
        print("Operacao invalida")

elif computador == 1:
    print('O bardo escolheu: ' + papel)
    if perguntar == 0:
        print("Computador perdeu")
    elif perguntar == 1:
        print("Empate!")
    elif perguntar == 2:
        print("Jogador venceu")
    else:
        print("Operacao invalida")
elif computador == 2:
    print('O bardo escolheu: '+ tesoura)
    if perguntar == 0:
        print("Jogador venceu")
    elif perguntar == 1:
        print("Bardo venceu")
    elif perguntar == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")


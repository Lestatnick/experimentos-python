import random

valor_secreto = random.randint(1,100) # definição do valor aleatorio secreto
tentativas = 5

while tentativas > 0:
    print(f'Tentativas restantes: \033[1;35m[{(tentativas-5)*-1}/5]\033[m')
    chute = int(input("Tente Adivinhar um numero de (1 a 100): ")) # Input que pergunta o valor a ser chutado
    tentativas -= 1
    print("\033[H\033[J", end="")

    if chute == valor_secreto:
        print(f'Parabéns você acertou o valor era: \033[1;32m[{valor_secreto}]\033[m')
        break
    elif valor_secreto > chute:
        print(f'O valor é MAIOR que: \033[1;31m[{chute}]\033[m')
    elif valor_secreto < chute:
        print(f'O valor é MENOR que: \033[1;31m[{chute}]\033[m')

print(f"O valor era \033[1;32m[{valor_secreto}]\033[m")
    
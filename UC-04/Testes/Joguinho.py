import random

chute = random.randint(1, 100)
tentativas = 5

while tentativas > 0:
    print(f"Tentativas restantes: [{tentativas}]")
    valor = int(input("Tente adivinhar! Informe-me um valor inteiro de 1 a 100: "))
    tentativas -= 1
    print("\033[H\033[J", end="")
    
    if valor == chute:
        print("Parabéns você acertou!")
        break

    elif valor < chute:
        print(f"O valor é MAIOR que [{valor}], tente novamente!")

    elif valor > chute:
        print(f"O valor é MENOR que [{valor}], tente novamente!")

print(f"Tentativas restantes: {tentativas}")
print("Você Fracassou!")
print(f"O valor era: {chute}")
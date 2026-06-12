#Exemplo 1.1
""" 
frase = str(input('Digite um texto: ')).strip().upper()

palavras = frase.split()
junto = ' '.join(palavras)

inverso = ' '

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print('O texto fica: {}'.format(inverso))
"""
#Exemplo 1.2
"""
frase = str(input('Digite um texto: ')).strip().upper()
palavras = frase.split()
junto = ' '.join(palavras)

inverso = junto[::-1]

print('O texto fica: {}'.format(inverso))
"""

#Exemplo 2.1 usando While
"""
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
"""
#Exemplo 2.2 usando FOR
""" for contador in range(5):
    print(contador) """

#Exemplo 3
""" soma = 0

num = int(input("Digite um número (0 para subir): "))

while num != 0:
    soma += num
    num = int(input("Digite outro número (0 para sair): "))

print(f"Soma total: {soma}") """
#exemplo 4
""" res = 'S'

while res == 'S':
    num = int(input('Digite um número: '))
    res = str(input('Deseja continuar? [S/N] ')).upper()

print("FIM") """
#Exemplo 5 Joguinho de adivinhação
"""
numero_secreto = 7

tentativa = int(input("Adivinhe o numero secreto (1 a 10): "))

while tentativa != numero_secreto:
    print("Tente novamente!")
    tentativa = int(input("Adivinhe o número secreto (1 a 10): "))

print("Parabéns, você acertou!")
"""
#Exemplo 6
""" contador = 0

while contador < 10:

    if contador == 6:
        break

    print(contador)
    contador += 1 """

""" 
while condicao:

    if condicao_para_pular:
        continue """
#Exemplo 7
""" while True:
    opcao = int(input('1 - somar ou 2 - Sair: '))

    if opcao == 1:

        n1 = int(input('Informe o número: '))
        n2 = int(input('Informe outro número: '))

        soma = n1 + n2

        print(soma)
    else:
        print('Saiu do Laço!')

        break """

#exemplo 8
""" 
numero_secreto = 7
tentativa = 0
tentativas = 0
tentativas_maximas = 3

while tentativa != numero_secreto:
    tentativa = int(input("Advinhe o numero secreto (1 a 10): "))
    tentativas += 1

    if tentativas >= tentativas_maximas and tentativa != numero_secreto:
        print("Você excedeu o numero máximo de tentativas.") 
        break
else:
    print("Parabéns, Você advinhou o número!")

 """
#exemplo 9

""" 
while True:
    calcular = input('1 - Para Somar ou 2 - Para Subtrair: ')
    if calcular == '1':
        print('Bem vindo a soma!')
        break
    
    elif calcular == '2':
        print('Bem vindo a subtração!')
        break
    
    else:
        print('Digitou número invalido! Tente novamente!')

        sair = input('Sair do programa? [s]im ou n[ao]: ').lower().startswith('s')

        if sair is True:
            break

        else:
            continue"""

#Atividade 1

while True:
    print('\nMenu:\n1. Adicionar\n2. Remover\n3. Sair')
    opcao = int(input('Escolha uma opção: '))
    print("\033[H\033[J", end="")

    if opcao == 1:
        print('Você escolheu Adicionar.')

    elif opcao == 2:
        print('Você decidiu Remover')

    elif opcao == 3:
        print('Saindo do Programa...')
        break
        
    else:
        print('Opção invalida. Tente novamente!')

#Exemplo 1

frutas = ['Abacate','Maçã', 'Banana', 'Laranja', 'Uva']

for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}: {fruta}")

#Exemplo 2
"""
for pessoa in range(1, 6):
    peso = float(input(f"Peso da {pessoa}ª pessoa: "))
"""
#Exemplo 3
"""
#Exemplo 3.1
for i in range(5): # irá iterar o 0 até 4
    print(i)
#Exemplo 3.2
for cont in range(5):
    print(cont, end=' ')
"""
#exemplo 4
""" #Exemplo 4.1
for i in range(1, 10, 2):
    print(i)
#Exemplo 4.2
for i in range(10, 0, -2):
    print(i) """
#exemplo 5
""" 
for linha in range(1, 2):
    print("Tabuada:", linha)

    for coluna in range(10):
        print(f'{linha} + {coluna} = {linha + coluna}') """

""" for linha in range(1, 6):
    print(f'Tabuada do:',linha)

    for coluna in range(1, 11):
        print(f'{linha} x {coluna} = {linha * coluna}')
 """
#Exemplo 6
""" soma = 0
cont = 0

for num in range(1, 7):
    valor = int(input('Digite o {} valor: '.format(num)))

    if valor % 2 == 0:
        soma += valor
        cont += 1

print(f"Você informou {cont} números e a soma é {soma}") """
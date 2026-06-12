#Exemplos 1

""" frutas = ['maçã', 'banana', 'laranja']

print(frutas[0]) # Saída: maçã
print(frutas[2]) # Saída: laranja

print(frutas[-1]) # Saída: laranja

frutas[1] = 'uva'

print(frutas) # Saída: ['maçã', 'uva', 'laranja']

frutas.append('morango')

print(frutas) # Saída: ['maçã', 'uva', 'laranja', 'morango']

frutas.insert(1, 'pêra')

print(frutas) # Saída: ['maçã', 'pêra', 'uva', 'laranja', 'morango']

frutas.remove('laranja') # Remove laranja da lista

print(frutas)

del frutas[0] # deleta o primeiro valor do indice

print(frutas)

print(len(frutas)) # Informa o tamanho de variaveis dentro da lista """

#Exemplo 2
""" lista = ['Maria', 12]
lista2 = ['Paulo', 25]

lista.extend(lista2)

print(lista) """

#Exemplo 3
""" lista = ['Maria', 12]

print(lista.pop(1))

print(lista) """

#exemplo 4
""" lista = []

for indice in range(2):
    nome = input('informe-me seu nome: ')
    lista.append(nome)

print(lista)
 """

#Exercicio 1
""" lista = []

for indice in range(2):
    nome = input("Nome: ")
    idade = input("Idade: ")
    profissao = input("Profissão: ")
    lista.append([nome, idade, profissao])

print(lista) """

#Exercicio 2.1
""" lista = []

for indice in range(2):
    nome = input('Nome: ')
    
    lista.append(nome)

print(lista)

print('Flavio' in lista) """

#Exercicio 2.2 (modelo consulta)
""" lista = []

for indice in range(2):
    nome = input('Qual o seu nome?')

    lista. append(nome)

nome2 = input('Qual o nome que deseja consultar: ')
print(f'o nome {nome2} faz parte da lista? {nome2 in lista}') """

#exemplo 5 (tuplas)
""" 
minha_tupla = (1, 2, 3, 'python', False)

print(minha_tupla[0])
print(minha_tupla[3])
"""
#alterando o tipo de lista para tupla e vice e versa
""" tupla = ('Maria', 12, 1.56, True)

lista = list(tupla)
lista.append('Novo valor')
tupla = tuple(lista)

print(tupla) """

#Exemplo 6
""" 
minha_tupla = (10, 20, 30, 40, 50)

print(minha_tupla[1:4]) """

#exemplo 7
""" 
tupla_numeros = (4, 10, -2, 5, 9)

maior_numero = max(tupla_numeros)

menor_numero = min(tupla_numeros)

print(f"Maior número: {maior_numero}, Menor número: {menor_numero}") """

#Exercicio 3
""" lista = []
lista2 = []

for indice in range(3):
    valor = int(input(f'Digite o {indice+1}º numero: '))
    lista.append(valor)

for indice in lista:
    if lista % 2 == 0:
        lista2.append(indice)

print(lista2) """

#Modelo correto
"""
lista = []
lista2 = []

for indice in range(3):
    valor = int(input(f'Digite o {indice + 1}º numero: '))
    lista.append(valor)

for item in lista:
    if item % 2 == 0:
        lista2.append(item)

print(lista2) """

#Exercicio 4
""" lista = ['banana','laranja','maçã','morango','graviola']
print(lista[3]) """

#Exercicio 5

lista = []
tupla = ()

for indice in range(4):
    val = int(input('Informe o número: '))
    lista.append(val)

print(lista)

tupla = tuple(lista)

print(tupla)


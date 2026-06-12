""" 
#exemplo 1
num1 = float(input("Diga um numero: "))
num2 = float(input("Diga um numero: "))
soma = num1 + num2

print("A soma entre", num1, "e", num2, "é", soma)

print("A soma entre " + str(num1) + " e " + str(num2) + " é " + str(soma))

print(f"A soma entre {num1} e {num2} é {soma}")

print("A soma entre {} e {} é {}".format(num1, num2, soma))
print("A soma entre {1} e {0} é {2}".format(num1, num2, soma))
 """

"""
     #Exercicio 1:
valor = input("Digite seu nome: ")
print(f"O valor informado é: {valor}")
print("O tipo é:",type(valor))

valor = int(input("Digite um valor: "))
print(f"O valor informado é: {valor}")
print("O tipo é:",type(valor))

valor = float(input("Digite um valor (real): "))
print(f"O valor informado é: {valor}")
print("O tipo é:",type(valor))

valor = bool(input("Digite algo: "))
print(f"O valor informado é: {valor}")
print("O tipo é:",type(valor)) 
"""


""" 
    #Exercicio 2:
#Entrada de dados
nota1 = float(input("Informe-me a primeira nota do aluno: "))
nota2 = float(input("Informe-me a segunda nota do aluno: "))

#Calculo da media
media = (nota1 + nota2)/2

#Saida de dados
print("A média entre",nota1,"e",nota2,"é:",media)
print(f"A média entre {nota1} e {nota2} é: {media}")
print("A média entre {} e {} é: {}".format(nota1,nota2,media)) 
"""

#Atividade 1
""" 
#Entrada de dados
nome = str(input("Informe-me seu nome: "))
altura = float(input("Informe-me sua altura: "))
peso = float(input("Informe-me seu peso: "))

#Calculo do IMC
imc = peso/(altura**2)

#Saida Formatada
print("-"*30, "resultado do IMC","-"*30)
print(f"Olá, {nome}")
print(f"Sua altura é de: {altura} e seu peso é: {peso}")
print("IMC: ", imc)
print(f"IMC: {imc:.2f}") """

#(Atividade 1 teste) Condicionais para informar estado do IMC
"""
if imc < 18.5:
    print("Abaixo do peso")
elif imc > 18.5 and imc < 24.9:
    print("Peso normal") 
elif imc > 25 and imc < 29.9:
    print("Sobrepeso")
elif imc > 30 and imc < 34.9:
    print("Obesidade Grau I") 
elif imc > 35 and imc < 40:
    print("Obesidade grau II")
else:
    print("Obesidade grau III (Morbida)") 
"""

#Operadores Aritimetricos e condicionais
""" 
    #Atividade 2
#Entrada de dados
val1 = float(input("Informe-me o primeiro numero: "))
val2 = float(input("Informe-me o segundo numero: "))

#Saida de dados
print("-"*30+"Resultados"+"-"*30)
print("A soma é:",val1 + val2)
print("A subtração é:",val1 - val2)
print("A Multiplicação é:",val1 * val2)
print("A Divisão é:",val1 / val2)
print("A Potencia é:",val1 ** val2)
print("O Resto da Divisão é:",val1 % val2)
"""

""" 
#Atividade 3

x = float(input("Informe-me um numero: "))
x += 10
print("Depois de somar 10:",x)
x -= 5
print("Depois de subtrair 5:",x)
x *= 2
print("Depois de multiplicar por 2:",x)
x /= 3
print("Depois de dividir por 3:",x)
"""
""" 
    #Atividade 4
#Entrada de dados
num1 = float(input("Informe-me o primeiro numero: "))
num2 = float(input("Informe-me o segundo numero: "))
#Saida de dados
print("-"*30+"Resultado"+"-"*30)
print(f"{num1} é maior que {num2}? {num1 > num2}")
print(f"{num1} é menor que {num2}? {num1 < num2}")
print(f"{num1} é maior ou igual que {num2}? {num1 >= num2}")
print(f"{num1} é menor ou igual {num2}? {num1 <= num2}")
print(f"{num1} é igual a {num2}? {num1 == num2}")
print(f"{num1} é diferente de {num2}? {num1 != num2}")
 """

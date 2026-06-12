#Exercicio 1
""" texto = 'Programação'

print(texto[0:4]) # 4 primeiras letras
print(texto[3:7]) # Apenas o "gram"
print(texto[-3:]) # Apenas o "cao"
print(texto[:]) # Todo o texto
print(texto[-1]) # Ultima letra
print(texto[::-1]) # Texto ao contrario """

#Exercicio 2

""" print('\033[1;33mOlá mundo!\033[m')

saldo = 100
print(f'Seu saldo é de: \033[4;32m{saldo}\033[m reais') """

#Exercicio 3

""" a = 'menino'
b = 'menina'

print(f'O sexo do bebê é \033[1;34m{a}\033[m ou \033[1;35m{b}\033[m?')

print('O sexo do bebê é \033[1;34m{}\033[m ou \033[1;35m{}\033[m?'.format(a,b))

print('O sexo do bebê é\033[1;34m',a,'\033[mou\033[1;35m',b,'\033[m?')

print('O sexo do bebê é \033[1;34m'+ a +'\033[m ou \033[1;35m'+ b +'\033[m?') """

#Exercicio 4
""" 
a = 'menino'
b = 'menina'

print(f'O sexo é \033[32m{a}\033[m ou \033[35m{b}\033[m?')
print(f'O sexo é \033[7;0;45m{b}\033[m!!!')
"""

#Exercicio 5
""" 
valor = float(input("Informe-me um valor: "))
resto = valor % 2

if resto == 0:
    print("O valor é: \033[1;32m[PAR]\033[m")
else:
    print("O valor é: \033[1;31m[IMPAR]\033[m") """

#Exercicio 6

nota1 = float(input("Informe-me a primeira nota: "))
nota2 = float(input("Informe-me a segunda nota: "))

media = (nota1 + nota2)/2

if media > 7:
    print("\033[1;30;42mAPROVADO!\033[m")
elif media >= 5:
    print("\033[1;30;43mRECUPERACAO!\033[m")
else:
    print("\033[1;30;41mREPROVADO!\033[m")
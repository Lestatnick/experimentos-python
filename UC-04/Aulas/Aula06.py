#O uso do "\" permite quebrar codigo para facilitar legibilidade
""" total = 4 + \
        7 + \
      5
print(total)
"""
#O uso do "\" permite quebrar codigo para facilitar legibilidade
"""
nome = "maria", \
       "luiza",\
       "paulo"
print(nome) 
"""
# uso do ''' dentro da declaração de uma string permite: ordenar o texto como quiser
""" texto = '''
    oi
      bom dia
             boa tarde
        boa noite    
'''
print(texto)
"""
#len: le a string e retorna o numero de caracteres
""" 
a = "malabarismo atletico"
print(len(a)) """
#in: questiona um parametro dentro da string e retorna verdadeiro ou falso
""" frase = "Eae lestat"
print("lestat" in frase)
 """
#.lower: deixa a string completamente em CAIXA ALTA
""" texto = "Eae Meu Federa!"
print(texto.upper())
"""
#.lower: deixa a string completamente em CAIXA BAIXA
"""
texto = "FALA MEU CONSAGRADO!"
print(texto.lower())
"""
#capitalize: coloca a primeira letra de uma string maiscula e o resto minuscula
"""
texto = "bom Dia"
print(texto.capitalize())
"""
#split: separa strings em uma lista com base em parametros
"""
texto = "Abacate Abacaxi, Cenoura"
print(texto.split(","))
"""
#strip: remove espaçamento de string
"""
nome = "             Mario"
print(nome.strip())
"""
#replace: metodo para subistituir frases dentro de uma string
"""
frase = "texto exemplo"
print(frase.replace("texto","Teste"))
"""
#.islower(): metodo para descobrir se a string esta em CAIXA BAIXA
"""
texto = "AaaaAAAA"
print(texto.islower()) """

#.replace: metodo para subistituir frases dentro de uma string
"""
texto = "Curso de Programador de Sistemas"
print(texto.replace("Programador de Sistemas","Python"))
"""
#Testes.1
"""
frase = "Curso de Programador de Sistemas"
print(frase.count("a"))
print(frase.count("A"))
print(frase.upper().count("A")) 
"""

#Exercicio 1
info = input("Digite uma informação: ")
print("A informação é do tipo?",type(info))
print("A informação é um numero?",info.isnumeric())
print("A informação é um alfabetico?",info.isalpha())
print("A informação é um alfanumerico?",info.isalnum())
print("A informação é um espaco?",info.isspace())
print("A informação é capitalizada?",info.istitle())
print("A informação é maiusculo?",info.isupper())
print("A informação é minusculo?",info.islower())
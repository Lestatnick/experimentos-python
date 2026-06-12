#Exercicio 1
"""
sexo = str(input('Informe seu sexo: [M/F]: ')).upper().strip()[0]

while sexo not in 'MF':
        sexo = input('Dados invalidos. Informe seu sexo: [M/F]: ').upper().strip()[0]

print(f'Sexo {sexo} registrado com sucesso!')
"""
#Exercicio 2 (tentativa falha)
""" 
soma = 0

while True:
    valor = int(input('Digite um número ou [00] para sair: '))
    if valor != 0:
        soma += valor
    elif valor == 0:
        print(f'A soma dos números é {soma}')
        break
"""
#Exercicio 2 (Resposta da professora!)
"""
num = 0
soma = 0

while True:
    num = int(input('Digite um número ou [00] para sair: '))

    if num == 0:
        break

    soma += num

print(f'A soma dos números é {soma}')
"""
#Exercicio 3 (minha resposta)
"""
valor = 0
mult = 1

while True:
    valor = int(input('Qual a tabuada? '))
    if valor >= 0:
        for mult in range(1,11):
            print(f'{valor} x {mult} = {valor *mult}')
    else:
        print("** PROGRAMA FINALIZADO **") 
"""
#Exercicio 3 (Resposta da professora)
""" 
valor = 0
mult = 1

while True:
    valor = int(input('Qual a tabuada? '))
    
    if valor <= 0:
        break

    for mult in range(1,11):

        print(f'{valor} x {mult} = {valor *mult}')

print("** PROGRAMA FINALIZADO **")
"""
#Exercicio 4 (minha resposta)
"""
i = 0
while i in range(0,50):
    i += 1
    print(i, end=' ')
"""
#Teste com for
"""
for i in range(1,51):
    print(i, end=' ') 
"""

#Exercicio 4 (Resposta da professora)
"""
contador = 1

while contador <= 50:

    print(contador, end=' ')

    contador += 1
"""
#Atividade 5 (minha resposta)
"""
nota = float(input('Digite uma nota de 0 até 10: '))
while True:
    if nota >= 0 and nota <= 10:
        print("Nota válida!")
        break

    nota = float(input('Nota inválida. Tente novamente: '))
"""
#Atividade 5 (Resposta da professora)
"""
nota = float(input('Digite uma nota de 0 até 10: '))

while nota < 0 or nota > 10:
    nota = float(input('Nota inválida. Tente novamente: '))

print("Nota válida!") 
"""

#Atividade 6 (Minha resposta)
"""
login = str(input('Digite o login: '))
senha = str(input('Digite a senha: '))

while senha == login:
    print("Senha deve ser diferente de login")
    senha = str(input('Digite a senha: '))
print("Senha aprovada")
"""

#Atividade 7 (minha resposta totalmente errada...)
""" while True:
    nome = str(input('Digite seu nome: '))
    while len(nome) >3:
        idade = int(input('Digite sua idade: '))
        while idade >= 0 and idade <= 150:
            salario = float(input('Digite seu salario (R$): '))
            while salario >= 0:
                print('-'*30)
                print('Informacoes do usuario:')
                print(f'Nome: {nome}, Idade: {idade}, e salario: R$ {salario}')
                break """

#Atividade 7 (resposta da professora)
""" 
# Validação do nome
nome = input('Digite seu nome: ')
while len(nome) <= 3:
    nome = input('Nome invalido! Digite um nome com mais de 3 caracteres: ')

# Validação da idade
idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade inválida! Digite uma idade entre 0 e 150 anos: '))

# Validação do salário
salario = float(input('Digite seu salário: R$ '))
while salario < 0:
    salario = float(input('Salário inválido! Digite um valor maior ou igual a zero: R$ '))

# Exibe os dados somente após todas as validações
print('\n'+'-' * 50)
print('DADOS CADASTRADOS COM SUCESSO!')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: R$ {salario :.2f}')
print('-' * 50)
"""
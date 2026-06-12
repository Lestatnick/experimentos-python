#Exercicio 1

""" aluno = {
    "nome": [],
    "nota": []
}

for indice in range(3):
    aluno["nome"].append(str(input('Nome: ')))
    aluno["nota"].append(float(input('Nota: ')))

print('Alunos cadastrados!')

for alunos in range(len(aluno["nome"])):
    print(f"Nome: {aluno['nome'][alunos]} - Nota: {aluno["nota"][alunos]}") """

#Exercicio 1 (resposta da professora)

""" alunos = {}

for i in range(3):
    nome = input('Nome:')
    nota = float(input('Nota: '))

    alunos[nome] = nota

print('\nAlunos cadastrados:')

for nome, nota in alunos.items():
    print(f'{nome} - Nota: {nota}') """

#Exercicio 2 - revisão

""" num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O maior número é: {num1}')
elif num2 > num1:
    print(f'O maior número é: {num2}')
else:
    print("Os numeros sao iguais")

print(f'Soma: {num1+num2}')
print(f'Subtração: {num1-num2}')
print(f'Multiplicação: {num1*num2}')

if num1 == 0 or num2 == 0:
    print('Erro: Divisão por zero não permitida.')
else:
    print(f'Divisão: {num1/num2:.2f}') """

#Exercicio 3 - Revisão
""" 
frase = str(input('Digite uma frase: '))

print("Número de caracteres:",len(frase))
print(f'Frase em maiúsculas: {frase.upper()}')

if "python" in frase.lower():
    print("A palavra 'Python' está presente na frase")
else:
    print("A palavra 'Python' não está presente na frase") """

#Exercicio 4 - Revisão
""" 
valor = int(input('Figite um número (inteiro) para ver sua tabuada: '))

for i in range(1,11,2):
    print(f'{valor} x {i} = {valor*i}') """

#Exercicio 4.1 - Revisão

""" valor = int(input('Figite um número (inteiro) para ver sua tabuada: '))

contador = 1

while contador <= 10:
    print(f'{valor} x {contador} = {valor*contador}')
    contador += 1 """

#Exercicio 5 - Revisão
nome = []
idade = []
profissao = []

for i in range(2):
    print(f'pessoa {i+1}:')
    nome.append(str(input("Digite o nome: ")))
    idade.append(int(input("Digite a idade: ")))
    profissao.append(str(input("Digite a profissao: ")))

for i in range(len(nome)):
    print(f'Nome: {nome[i]}, Idade: {idade[i]}, Profissão: {profissao[i]}')
    
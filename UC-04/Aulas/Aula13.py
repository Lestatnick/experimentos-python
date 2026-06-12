#Exemplo 1
""" frutas = {'maçã', 'banana', 'laranja', 'maçã'}

print(frutas)

frutas.add('morango')
print(frutas)

frutas.remove('banana')
print(frutas)

frutas.clear()
print(frutas)
 """
#exemplo 2
""" 
pessoa = {
    "nome": 'Alice',
    "idade": 30,
    "cidade": "São Paulo"
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cidade'])

print(f'A {pessoa['nome']} tem {pessoa['idade']} anos.')

    #Exemplo 2.1

pessoa['Profissão'] = 'Engenheira'

pessoa['idade'] = 31

del pessoa['cidade']

print(pessoa) """

#Exemplo 3: Criando um dicionario aninhado
""" empresa = {
    "nome": "Tech Solutions",
    "funcionarios": [
        {"nome": "Alice", "cargo": "Engenheira"},
        {"nome": "Bob", "cargo": "Designer"}
    ]
}

print(empresa["funcionarios"][0]["nome"])
print(empresa["funcionarios"][1]["cargo"]) """

#Exemplo 4
""" 
frutas_cores = {
    "maçã": "vermelha",
    "banana": "amarela",
    "laranja": "laranja"
}
 """
    # Percorrendo chaves e valores
""" for fruta, cor in frutas_cores.items():
    print(f"A {fruta} é {cor}.") """

    # Acessando uma chave que existe
""" cor_maca = frutas_cores.get('maçã')

print(f'Cor da maçã: {cor_maca}')

cor_abacaxi = frutas_cores.get('abacaxi')

print(f'Cor do abacaxi: {cor_abacaxi}')

cor_uva = frutas_cores.get('uva', 'Desconhecida')

print(f'Cor da uva: {cor_uva}') """

    # Modificando, adicionando e removendo

""" frutas_cores['banana'] = 'verde'

print(frutas_cores) """

        # Adicionando um novo par chave:valor
""" frutas_cores['morango'] = 'vermelho'
print(frutas_cores)
 """
        # Removendo um item com pop()
""" cor_laranja = frutas_cores.pop('laranja')

print(cor_laranja) """

        # Usando del para remover um item
""" del frutas_cores['maçã']

print(frutas_cores) """

#Exemplo 5
""" 
pessoas = {
    'nome': 'ana',
    'sexo': 'F',
    'idade': 22
}

print(pessoas.values())
print(pessoas.keys())

for valor in pessoas.values():
    print(valor)

for chave in pessoas.keys():
    print(chave)

for chave, valor in pessoas.items():
    print(f'{chave}: {valor}') """

#Exemplo 6

""" emails_shopping = {
    'recife': 'shoppingrecife@gmail.com',
    'tacaruna': 'tacaruna@gmail.com',
    'guararapes': 'guararapes@gmail.com',
}

if 'tacaruna' in emails_shopping:
    print('tem sim')
else:
    print('tem não')

if 'tacaruna@gmail.com' in emails_shopping.values():
    print('O e-mail está presente no dicionario') """

#Exercicio 1
""" 
produtos = {
    'arroz': 8.50,
    'macarrao': 2.99,
    'ovo': 17.99
}

produto = input('Digite o nome do produto: ').lower()

if produto in produtos:
    print(f'Preco: R$ {produtos[produto]:.2f}')
else:
    print('Produto não encontrado') """

#Exercicio 2

""" clientes = {
    'Maria': 5000.00,
    'João': 3200.00,
    'Ana': 7500.00
}

cliente = input('Cliente: ')

if cliente in clientes:
    ajuste = input('Novo saldo: ')
    clientes[cliente] = ajuste
    print('Saldo atualizado com sucesso!')
else:
    print('Cliente não encontrado!')
print(clientes)
"""
#Exercicio 2 (resposta da professora)


clientes = {
    'Maria': 5000.00,
    'João': 3200.00,
    'Ana': 7500.00
}

nome = input('Cliente: ').capitalize()

if nome in clientes:
    novo_saldo = float(input('Novo saldo: '))
    clientes[nome] = novo_saldo
    print('Saldo atualizado com sucesso!')
    print(clientes)
else:
    print('Cliente não encontrado.')
""" #Exercicio 1

cracha = input("Informe-me se o aluno possui crachá (S/N): ")
professor = input("Informe-me se o aluno está acompanhando do professor (S/N): ")
lab = input("Informe-me se o laboratorio está aberto (S/N): ")

if cracha == "S" and lab == "S" or professor == "S":
    print("Acesso liberado")
else:
    print("Acesso negado!") """

""" #Exercicio 2

idade = int(input("Digite sua idade: "))

if idade >= 12:
    print("Você pode assistir ao filme")
else:
    print("Você não pode assistir ao filme") """

""" 
#Exercicio 3

val = float(input("Digite um numero: "))
if val >= 0:
    print("Numero positivo")
elif val < 0:
    print("Numero negativo")
else:
    print("Numero neutro") """

#Exercicio 4

""" temp = int(input("Digite a temperatura (C°): "))

if temp > 35:
    print("Muinto quente")
elif temp >= 25:
    print("Quente")
elif temp >= 15:
    print("Agradavel")
else:
    print("Frio") """

#Exercicio 5

idade = int(input("Digite sua idade: "))
ingresso = str(input(f"Tem ingresso? (sim/nao): ")).strip().lower()
vip = str(input(f"É convidado espécial? (sim/nao): ")).strip().lower()

if (idade > 18 and ingresso == "sim") or vip == "sim":
    print("Você pode entrar no evento.")
else:
    print("Você não pode entrar no evento.")

if not ingresso == "sim":
    print("Atenção: Você não possui o ingresso.")
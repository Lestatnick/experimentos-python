#ATIVIDADE 1

print("="*30,"\033[1;37;45mLOJA C&A\033[m","="*30)

#Declarando entrada de preço!
preco = float(input("Valor das compras: R$ "))

print("\033[1;31mFORMAS DE PAGAMENTO\033[m")

#Declarando Opções de entrada!

print('''\033[1;0;41m[ 1 ]\033[m à vista dinheiro/pix \033[1;32m(10% de desconto)\033[m
\033[1;0;41m[ 2 ]\033[m à vista cartão \033[1;32m(5% de desconto)\033[m
\033[1;0;41m[ 3 ]\033[m 2x no cartão \033[1;33m(5% de acréscimo)\033[m
\033[1;0;41m[ 4 ]\033[m 3x até 10x no cartão \033[1;33m(10% de acréscimo)\033[m''')

#Entrada de dados formato de pagamento!

forma_pag = input("\033[1;31mQual a forma de pagamento?\033[m ")
if forma_pag >= 1 and forma_pag <= 4:
    if forma_pag == 1:
        print(f"O total da compra será de \033[0;0;42mR$ {preco*0.9:.2f}\033[m.")
    elif forma_pag == 2:
        print(f"O total da compra será de \033[0;0;42mR$ {preco*0.95:.2f}\033[m.")
    elif forma_pag == 3:
        print(f"O valor da parcela será 2x de R$ \033[1;31m{(preco*1.05)/2}\033[m com juros.")
        print(f"O Total da compra será de \033[0;0;42mR$ {preco*1.05:.2f}\033[m")
    elif forma_pag == 4:
        parcela_tipo = int(input("Em quantas parcelas (de 3x até 10x)? "))
        if parcela_tipo >= 3 and parcela_tipo <= 10:
            print(f"O valor da parcela será {parcela_tipo}x de R$ \033[1;31m{(preco*1.1)/parcela_tipo:.2f}\033[m com juros.")
            print(f"O Total da compra será de \033[0;0;42mR$ {preco*1.1:.2f}\033[m")
        else:
            print("Forma invalida!")
else:
    print("Forma invalida!")
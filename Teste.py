import random as r

x = r.randint(1,3)

print('===== PEDRA PAPEL E TESOURA =====')

print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

opcao = int(input('Digite a opção: '))

if opcao == x:
    print('empate')

elif opcao == 1 and x == 2:
    print('Computador: Papel')
    print('Papel vence pedra! Você Perdeu!')

elif opcao == 1 and x == 3:
    print('Computador: Tesoura')
    print('Tesoura perde para pedra! Você Venceu!')

elif opcao == 2 and x == 1:
    print('Computador: Pedra')
    print('Pedra perde para papel, Você Venceu!')

elif opcao == 2 and x == 3:
    print('Computador: Tesoura')
    print('Tesoura ganha de pedra! Você Perdeu!')

elif opcao == 3 and x == 1:
    print('Computador: pedra')
    print('Pedra ganha de tesoura, Você perdeu!')

elif opcao == 3 and x == 2:
    print('Computador: papel')
    print('papel perde para tesoura, Você Venceu!')
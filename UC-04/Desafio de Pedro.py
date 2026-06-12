participante = []
participacao = []
curso = []
nota1 = []
nota2 = []
nota3 = []
situacao = []

while True:

    print('''
    TECHCONNECT EVENTOS
    =================================

    1 - Cadastrar participante
    2 - Listar participantes
    3 - Buscar participante
    4 - Exibir estatísticas
    5 - Exibir ranking
    6 - Sair''')

    # 1° - MENU DE CADASTRO
    opcao = int(input('\nDigite a opção: '))
    if opcao == 1:
        nome = input('Digite o nome: ')
        participante.append(nome) 

        curso_op = input('Digite o curso: ')
        curso.append(curso_op)

        presenca = int(input('Digite a presença: '))
        participacao.append(presenca)

        nota_1 = float(input('Digite a 1ª nota: '))
        nota1.append(nota_1)

        nota_2 = float(input('Digite a 2ª nota: '))
        nota2.append(nota_2)

        nota_3 = float(input('Digite a 3ª nota: '))
        nota3.append(nota_3)

        media = (nota_1 + nota_2 + nota_3)/3

        if media >= 7 and presenca >= 75:
            situacao.append('Aprovado')
        
        elif media >= 5 and presenca >= 75:
            situacao.append('Recuperação')
        elif media < 5 or presenca < 75:
            situacao.append('Reprovado')

        print('Participante cadastrado com sucesso!')

    # 2° - MENU DE LISTAGEM
    elif opcao == 2:

        for indice in range(len(participante)):
            print(f'{'-'*30} PARTICIPANTE: {indice+1}º {'-'*30}')
            print(f'NOME: {participante[indice]}')
            print(f'PRESENÇA: {participacao[indice]}')
            print(f'Primeira nota: {nota1[indice]}')
            print(f'Segunda Nota: {nota2[indice]}')
            print(f'Terceira nota: {nota3[indice]}')
            print(f'Situação: {situacao[indice]}\n')

        saida = input('DIGITE [ENTER] PARAR SAIR')
        continue

    # 3° - MENU DE BUSCA
    elif opcao == 3:
        continue
    
    # 4° - MENU DE ESTATISTICAS
    elif opcao == 4:
        continue
    
    # 5° - MENU DE RANKING
    elif opcao == 5:
        continue
    
    # 6° - SAIR
    elif opcao == 6:
        print("\033[H\033[J", end="")
        break
    
    # OUTPUT PARA ERRO
    else:
        print('Opção invalida!')
        continue
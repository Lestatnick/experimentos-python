participantes = []
while True:
    print("\n=================================")
    print("TECHCONNECT EVENTOS")
    print("=================================")
    print("1 - Cadastrar participante")
    print("2 - Listar participantes")
    print("3 - Buscar participante")
    print("4 - Exibir estatísticas")
    print("5 - Exibir ranking")
    print("6 - Sair")
    print("=================================")
    # escolha de menu
    while True:
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao not in [1, 2, 3, 4, 5, 6]:  # ← dentro do try!
                print("Digite uma opção entre 1 e 6!")
            else:
                break
        except ValueError:
            print("Digite apenas números!")
    if opcao == 1:
        print("\n--- Cadastrar Participante ---")
        # cadastro do nome
        while True:
            nome = input('Qual nome do participante: ').strip()
            if not nome.replace(' ', '').isalpha():
                print("Digite apenas letras!")
            else:
                nome = nome.title()
                break
        # cadastro do curso
        while True:
            curso = input('Qual o curso: ').strip()
            if not curso.replace(' ', '').isalpha():
                print("Digite apenas letras!")
            else:
                curso = curso.title()
                break
        #cadastro porcetagem
        while True:
            try:
                presença = float(input('Qual o percentual(%) de presença: '))
                if not (0 <= presença <=100):
                    print('Presença deve esta entre 0 e 100')
                break
            except ValueError:
                print("Digite apenas números!")
        # cadastro nota1
        while True:
            try:
                nota1 = float(input('Nota numero 01: '))
                if not (0 <= nota1 <= 10):
                    print("Nota 01 deve ser entre 0 e 10!")
                    continue
            except ValueError:
                print("Digite apenas números!")
                continue
        # cadastro nota2
            try:
                nota2 = float(input('Nota numero 02: '))
                if not (0 <= nota2 <= 10):
                    print("Nota 02 deve ser entre 0 e 10!")
                    continue
            except ValueError:
                print("Digite apenas números!")
                continue
        # cadastro nota3
            try:
                nota3 = float(input('Nota numero 03: '))
                if not (0 <= nota3 <= 10):
                    print("Nota 03 deve ser entre 0 e 10!")
                    continue
            except ValueError:
                print("Digite apenas números!")
                continue
            break
        # media
        media = (nota1 + nota2 + nota3) / 3
        # situação
        if media >= 7 and presença >= 75:
            situação = 'APROVADO'
        elif media >= 5 and presença >= 75:
            situação ='RECUPERAÇÃO'
        else:
            situação = 'REPROVADO'
        # adiciona a lista e salva cadastro
        participantes.append([nome, curso, presença, nota1, nota2, nota3,situação])
        print('Cadastrado com sucesso!')
        # lista participantes
    elif opcao == 2:
        print("\n--- Lista de Participantes ---")
        if not participantes:
            print("Nenhum participante cadastrado.")
        else:
            print(f"\n{'#':<4} {'nome':<20} {'curso':<20} {'presença':>8} {'nota1':>6} {'nota2':>6} {'nota3':>6} {'media':>6} {'situação':<12}")
            print("-" * 90)
            for i, p in enumerate(participantes, 1):
                media = (p[3] + p[4] + p[5]) / 3
                print(f"{i:<4} {p[0]:<20} {p[1]:<20} {p[2]:>7}% {p[3]:>6.1f} {p[4]:>6.1f} {p[5]:>6.1f} {media:>6.1f} {p[6]:<12}")
            print("-" * 90)
            print(f"Total: {len(participantes)} participante(s)")
    elif opcao == 3:                          # ← mesmo nível do elif acima
        print("\n--- Buscar Participante ---")
        print("Buscar por:")
        print("1 - Nome")
        print("2 - Curso")
        print("3 - Situação (APROVADO / RECUPERAÇÃO / REPROVADO)")
        while True:
            try:
                tipo = int(input("Escolha: "))
                if tipo not in [1, 2, 3]:
                    print("Digite 1, 2 ou 3!")
                else:
                    break
            except ValueError:
                print("Digite apenas números!")
        busca = input("Digite o que deseja buscar: ").strip().lower()
        indice = {1: 0, 2: 1, 3: 6}[tipo]
        encontrados = [p for p in participantes if busca in p[indice].lower()]
        if not encontrados:
            print("Nenhum participante encontrado.")
        else:
            print(f"\n{'#':<4} {'Nome':<20} {'Curso':<20} {'Presença':>8} {'Média':>6} {'Situação':<12}")
            print("-" * 75)
            for i, p in enumerate(encontrados, 1):
                media = (p[3] + p[4] + p[5]) / 3
                print(f"{i:<4} {p[0]:<20} {p[1]:<20} {p[2]:>7}% {media:>6.1f} {p[6]:<12}")
            print("-" * 75)
            print(f"Encontrado(s): {len(encontrados)} participante(s)")
    elif opcao == 4:
        print("\n--- Estatísticas ---")
        if not participantes:
            print("Nenhum participante cadastrado.")
        else:
            medias = [(p[3] + p[4] + p[5]) / 3 for p in participantes]
            media_geral = sum(medias) / len(medias)
            maior_media = max(medias)
            menor_media = min(medias)
            aprovados = sum(1 for p in participantes if p[6] == 'APROVADO')
            recuperacao = sum(1 for p in participantes if p[6] == 'RECUPERAÇÃO')
            reprovados = sum(1 for p in participantes if p[6] == 'REPROVADO')
            print(f"\nTotal de participantes : {len(participantes)}")
            print(f"Média geral da turma   : {media_geral:.1f}")
            print(f"Maior média            : {maior_media:.1f}")
            print(f"Menor média            : {menor_media:.1f}")
            print(f"\nAprovados              : {aprovados}")
            print(f"Em Recuperação         : {recuperacao}")
            print(f"Reprovados             : {reprovados}")
    elif opcao == 5:
        print("\n--- Ranking de Participantes ---")
        if not participantes:
            print("Nenhum participante cadastrado.")
        else:
            ranking = sorted(participantes, key=lambda p: (p[3] + p[4] + p[5]) / 3, reverse=True)
            print(f"\n{'#':<4} {'Nome':<20} {'Curso':<20} {'Média':>6} {'Situação':<12}")
            print("-" * 65)
            for i, p in enumerate(ranking, 1):
                media = (p[3] + p[4] + p[5]) / 3
                print(f"{i:<4} {p[0]:<20} {p[1]:<20} {media:>6.1f} {p[6]:<12}")
            print("-" * 65)
    elif opcao == 6:
        print("Encerrando o sistema. Até logo!")
        break
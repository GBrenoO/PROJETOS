valor_inicial = int(input('Digite o valor inicial: '))
lista_saida_entrada = []


while True:
    saida_entrada = input('[S]aida ou [E]ntrada: ').lower()
    if saida_entrada == 's':
        motivo_saida = input('Escreva o motivo da saida: ')
        saida = int(input('Digite o valor de saida: '))
        valor_atual = valor_inicial - saida
        print(f'Valor inicial: {valor_inicial}')
        valor_inicial = valor_atual
        motivo_e_saida = (f'{motivo_saida}: -{saida}')
        lista_saida_entrada.append(motivo_e_saida)
        for i in lista_saida_entrada:
            print(i)
            print(f'Valor atual: {valor_atual}')

    elif saida_entrada == 'e':
        motivo_entrada = input('Escreva o motivo da entrada: ')
        entrada = int(input('Digite o valor de entrada: '))
        valor_atual = valor_inicial + entrada
        print(f'Valor inicial: {valor_inicial}')
        valor_inicial = valor_atual
        motivo_e_entrada = (f'{motivo_entrada}: +{entrada}')
        lista_saida_entrada.append(motivo_e_entrada)
        for i in lista_saida_entrada:
            print(i)
            print(f'Valor atual: {valor_atual}')

        continue

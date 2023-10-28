carrinho = []
while True:
    menu = input('Escolha uma opção: [I]nserir, [A]pagar, [L]istar: ').lower()
    if menu == 'i':
        inserir_produto = input('Digite o que deseja inserir: ')
        carrinho.append(inserir_produto)
    elif menu == 'a':
        for produtos in range(len(carrinho)):
            apagar_produto = input('Digite o que deseja apagar: ')
        try:
            int_apagar = int(apagar_produto)
            del carrinho[int_apagar]
        except IndexError:
            print('Ocorreu algum erro ao tentar executar')
            continue
        continue
    elif menu == 'l':
        if carrinho == []:
            print('Não ah nenhum produto na lista!')
            continue
        else:
            for produtos in range(len(carrinho)):
                print(f'{produtos}: {carrinho[produtos]}')

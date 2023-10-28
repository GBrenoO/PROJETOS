"""
nome = 'Gleyson Breno' 

indice = 0 
novo_nome = ' '
while indice < len(nome):
    letra = nome[indice]
    novo_nome += (f'*{letra}')
    indice += 1
    if indice == 13:
        print(novo_nome)
        break
"""


while True:
    number_1 = input('Digite o primeiro numero: ')
    allowed_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    if not all(char in allowed_chars for char in number_1):    
        print('Isso não é um numero!')   
    else:
        int_number_1 = int(number_1)
        float_number_1 = float(int_number_1)
        operador = input(
            'Digite a operação desejada com + para soma, - para subtração, * para multiplicação e / para divisão: ')
        if operador not in ('+', '-', '*', '/'):
            print('Isso não é um operador!')

        else:
            number_2 = input('Digite o segundo numero: ')
            if number_2.isdigit():
                int_number_2 = int(number_2)
                float_number_2 = float(int_number_2)
            else:
                print('Isso não é um numero!')
                break

            resultado_soma = float_number_1 + float_number_2
            resultado_multiplicacao = float_number_1 * float_number_2
            resultado_subtracao = float_number_1 - float_number_2
            resultado_divisao = float_number_1 / float_number_2
            if operador == '+':
                print(f'O resultado da operação é: {resultado_soma}')
            elif operador == '-':
                print(f'O resultado da operação é: {resultado_subtracao}')
            elif operador == '*':
                print(
                    f'O resultado da operação é: {resultado_multiplicacao}')
            elif operador == '/':
                print(f'O resultado da operação é: {resultado_divisao}')

            else:
                print('Isso não é uma operação')

print('Operção finalizada!')



# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

numero = input('Digite um numero: ')

if numero.isdigit():
    numero_int = int(numero)

    if numero_int % 2 == 0:
        print('É um numero par')

    elif numero_int % 2 == 1:
        print('É um numero impar')

    else:
        print('Não digitou nenhum numero')

else:
    print('Não é um numero inteiro')

# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
# descrito, exiba a saudação apropriada. Ex.
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

horas = input('Que horas são agora? ')

horas_int = int(horas)

if horas_int >= 00 and horas_int <= 11:
    print(f'Bom dia, são exatamente {horas} horas da manhã!')

elif horas_int >= 12 and horas_int <= 17:
    print(f'Bom tarde, são exatamente {horas} horas da tarde!')

elif horas_int >= 18 and horas_int <= 23:
    print(f'Bom noite, são exatamente {horas} horas da noite!')

else:
    print('Isso não é um horaio!')

# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

nome = input('Qual é o seu nome? ')

if not nome.isalpha():
    print('Isso não é um nome!')

else:
    if len(nome) <= 4:
        print('Seu nome é curto')

    elif len(nome) >= 5 and len(nome) <= 6:
        print('Seu nome é normal')

    elif len(nome) > 6:
        print('Seu nome é muito grande')

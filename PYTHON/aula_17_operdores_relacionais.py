"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1 
>=      maior ou igual      2 >= 2 
<       menor               1 < 2 
<=      menor               2 <= 2 
==       igual               'a' == 'a' 
!=       diferente           'a' != 'b' 
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(diferente)

primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor {primeiro_valor} é maior que segundo valor {segundo_valor}')
    
elif segundo_valor > primeiro_valor:
    print(f'Segundo valor {segundo_valor} é maior que primeiro valor {primeiro_valor}')

elif primeiro_valor == segundo_valor: 
    print('Primeiro e segundo valor são iguais!')
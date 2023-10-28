"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
import sys
import random
digite = ''
cpf = re.sub(
    r'[^0-9]', 
    '',
    digite
)

for i in range(9): 
    cpf += str(random.randint(0, 9))
print(cpf)

if cpf == cpf[0] * len(cpf): 
    print('CPF invalido!') 
    sys.exit()
else:
    cpf_digitado = []
    cpf_digitado.append(cpf)

    for digito in cpf_digitado: 
        di_1 = int(digito[0])
        di_2 = int(digito[1])
        di_3 = int(digito[2])
        di_4 = int(digito[3])
        di_5 = int(digito[4])
        di_6 = int(digito[5])
        di_7 = int(digito[6])
        di_8 = int(digito[7])
        di_9 = int(digito[8])

        n1 = 10 * di_1
        n2 = 9 * di_2
        n3 = 8 * di_3
        n4 = 7 * di_4
        n5 = 6 * di_5
        n6 = 5 * di_6
        n7 = 4 * di_7
        n8 = 3 * di_8
        n9 = 2 * di_9

        soma_n = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 

        dez_x_soma_n = soma_n * 10

        resto_n = dez_x_soma_n % 11 

        resto_n_1 = 0 if resto_n > 9 else resto_n

        str_resto_n_1 = str(resto_n_1)

        cpf += str_resto_n_1

        cpf_digitado_1 = []
        cpf_digitado_1.append(cpf)
        
        #SEGUNDO DIGITO 

        for digito in cpf_digitado_1: 
            di_0 = int(digito[0])
            di_1 = int(digito[1])
            di_2 = int(digito[2])
            di_3 = int(digito[3])
            di_4 = int(digito[4])
            di_5 = int(digito[5])
            di_6 = int(digito[6])
            di_7 = int(digito[7])
            di_8 = int(digito[8])
            di_9 = int(digito[9])
            n0 = 11 * di_0    
            n1 = 10 * di_1
            n2 = 9 * di_2
            n3 = 8 * di_3
            n4 = 7 * di_4
            n5 = 6 * di_5
            n6 = 5 * di_6
            n7 = 4 * di_7
            n8 = 3 * di_8
            n9 = 2 * di_9
            soma_n = n0 + n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 

            dez_x_soma_n = soma_n * 10

            resto_n = dez_x_soma_n % 11 

            resto_n_2 = 0 if resto_n > 9 else resto_n

            str_resto_n_2 = str(resto_n_2)

            cpf += str_resto_n_2
            cpf_digitado_2 = []
            cpf_digitado_2.append(cpf)

            cpf_final = str(cpf_digitado_2[0])
            print(f'CPF: {cpf_final}')

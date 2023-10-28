import re
import random
for cpf in range(1):
    inicio = input('Digite G e pressione ENTER para gerar um CPF: ').lower()
    if inicio == 'g':
        cpf = re.sub(
            r'^[0, 9]',
            '',
            ''
        )
        for i in range(9):
            cpf += str(random.randint(0, 9))

        if cpf == cpf[0] * len(cpf):
            print('CPF INVALIDO!')

        else:
            nove_digitos = cpf[:9]
            contador_regressivo = 10
            resultado_d1 = 0
            for digito in nove_digitos:
                resultado_d1 += int(digito) * contador_regressivo
                contador_regressivo -= 1
            d1 = ((resultado_d1 * 10) % 11)
            d1 = d1 if d1 <= 9 else 0

            dez_digitos = nove_digitos + str(d1)
            contador_regressivo_2 = 11

            resultado_2 = 0
            for digito_2 in dez_digitos:
                resultado_2 += int(digito_2) * contador_regressivo_2
                contador_regressivo_2 -= 1
            d2 = ((resultado_2 * 10) % 11)
            d2 = d2 if d2 <= 9 else 0

            cpf_final = dez_digitos + str(d2)
            print(
                f'CPF: {cpf_final[0:3]}.{cpf_final[3:6]}.{cpf_final[6:9]}-{cpf_final[9:11]}')

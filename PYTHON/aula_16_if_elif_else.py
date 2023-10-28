# if / elif....../ else
# se / se não se / se não

entrada = input('Você quer entrar ou sair do sistema?')

if entrada == 'entrar':
    print('Você entrou no sistema')

elif entrada == 'sair':
    print('Você saiu do sistema')

else:
    print('Você não digitou nem "entrar" nem "sair"')

condicao1 = False
condicao2 = False 
condicao3 = True 
condicao4 = False 

if condicao1:
    print('Condição numero 1')
    print('Condição numero 1/2')
    
elif condicao2:
    print('Condição numero 2')
    
elif condicao3:
    print('Condição numero 3')
    
elif condicao4:
    print('Condição numero 4') 
    
else: 
    print('Nenhuma das condições foi aceita')
    

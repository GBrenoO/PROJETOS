"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega
VEL_CARRO_PASSOU_RADAR = velocidade > RADAR_1
CARRO_DENTRO_RANGE = local_carro - LOCAL_1 == RADAR_RANGE or LOCAL_1 - local_carro == RADAR_RANGE or local_carro == LOCAL_1

if VEL_CARRO_PASSOU_RADAR: 
    print('O carro esta acima da velocidade permitida')
    
    if CARRO_DENTRO_RANGE:
        print('Carro foi multado') 
    
    else: 
        print('O carro não foi multado')
    
else: 
    print('O carro esta dentro da velocidade permitida')
    
    
''' Classificar os tipos de um triangulo
se possuir um angulo interno igual a 90 é Rêtangulo
se possuir um angulo maior que 90 é Obtusângulo
se possuir todos os angulos internos agudos (menores que 90) é Acutângulo
'''
# Verificando ângulo 1
etapa1 = int(input('informe o primeiro ângulo do triângulo.'))
if etapa1 < 1 or etapa1 > 180:
    sys.exit('ERRO. Informe um número válido.')
# Verificando ângulo 2
etapa2 = int(input('informe o segundo ângulo do triângulo.'))
if etapa2 < 1 or etapa2 > 180:
    sys.exit('ERRO. Informe um número válido.')
# Verificando ângulo 3
etapa3 = int(input('Informe o terceiro ângulo do triângulo.'))
if etapa3 < 1 or etapa3 > 180:
    sys.exit(input('ERRO. Informe um número válido.'))
# Classificando o tipo de triângulo
if etapa1 == 90 or etapa2 == 90 or etapa3 == 90:
   print('Triângulo Retângulo.')
elif etapa1 > 90 or etapa2 > 90 or etapa3 > 90:
    print('Triângulo Obtusângulo.')
elif etapa1 > 90 or etapa2 == 90 or etapa3 == 90:
    print('Triângulo Obtusângulo.')
elif etapa1 > 90 or etapa2 > 90 or etapa3 == 90:
    print('Triângulo Obtusângulo.')
elif etapa1 < 90 or etapa2 > 90 or etapa3 > 90:
    print('Triângulo Obtusângulo.')
elif etapa1 < 90 or etapa1 < 90 or etapa3 < 90:
    print('Triângulo Acutângulo.')
else:
    print('Triângulo com ângulos invalidos para formar um triângulo comum.')
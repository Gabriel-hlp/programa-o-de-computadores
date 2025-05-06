# Programa para calcular distância no MRUV

# Entrada de dados
v0 = float(input("Digite a velocidade inicial (em m/s): "))
t = float(input("Digite o tempo (em segundos): "))
a = float(input("Digite a aceleração (em m/s²): "))

# Cálculo da distância
delta_s = v0 * t + (a * t**2) / 2

# Saída do resultado
print(f"A distância percorrida é: {delta_s:.2f} metros")

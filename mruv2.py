# Solicita os dados do usuário
d = float(input("Digite a distância entre Lajes e Natal (em km): "))
v0 = float(input("Digite a velocidade inicial do carro (em km/h): "))
a = float(input("Digite a aceleração do carro (em m/s²): "))
t = float(input("Digite um valor de tempo (em segundos): "))

# Converte km e km/h para metros e m/s
d = d * 1000  # km para metros
v0 = v0 / 3.6  # km/h para m/s

# Aplica a fórmula da questão (mesmo que errada)
resultado = (a * t ** 2) / 2 + v0 * t - d

print(f"Resultado da fórmula: t = (a*t²)/2 + v0*t - d")
print(f"Com os valores inseridos, resultado = {resultado:.2f}")

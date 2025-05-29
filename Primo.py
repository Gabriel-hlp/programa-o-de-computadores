# Programa para verificar se um número é primo 

numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print(f"{numero} não é um número primo.")
else:
    Divisor = 2
    Primo = True

    while Divisor <= int(numero ** 0.5):
        if numero % Divisor == 0:
            Primo = False
        Divisor += 1

    if Primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
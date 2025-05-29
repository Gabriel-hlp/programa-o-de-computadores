# Programa para calcular o fatorial 

numero = int(input("Digite um número inteiro para calcular o fatorial: "))

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:
    fatorial = 1
    contador = 1

    while contador <= numero:
        fatorial *= contador
        contador += 1

    print(f"O fatorial de {numero} é {fatorial}.")
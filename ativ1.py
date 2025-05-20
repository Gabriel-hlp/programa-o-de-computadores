entrada = input("Digite um número inteiro positivo de até 4 dígitos: ")

if "," in entrada or "." in entrada or "-" in entrada:
    print("Número inválido. Não pode ter vírgula, ponto ou sinal negativo.")
else:
    try:
        numero = int(entrada)

        if numero > 0 and numero < 10000:
            soma = 0
            for caractere in entrada:
                digito = int(caractere)  # Converte cada caractere para número
                soma = soma + digito
            print("A soma dos algarismos é:", soma)
        else:
            print("Número inválido. Deve ser positivo e ter no máximo 4 dígitos.")
    except:
        print("Entrada inválida. Use apenas números inteiros.")

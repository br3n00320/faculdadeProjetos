
# Solicita ao usuário para inserir um número inteiro N
N = int(input("Digite um número inteiro N: "))

# Inicializa a variável para armazenar a soma
soma = 0

# Loop para somar os números de 1 a N
for numero in range(1, N + 1):
    soma += numero

# Mostra o resultado da soma
print("A soma dos números de 1 a", N, "é:", soma)

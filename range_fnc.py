def soma_intervalo(inicio, fim):
    """
    Calcula a soma de todos os números no intervalo [inicio, fim].
    """
    soma = 0  # Inicializa a variável para armazenar a soma
    for numero in range(inicio, fim + 1):  # Range vai de 'inicio' até 'fim' (inclusive)
        soma += numero  # Adiciona cada número à soma
    return soma  # Retorna o resultado

# Exemplo de uso
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

resultado = soma_intervalo(inicio, fim)
print(f"A soma dos números de {inicio} a {fim} é: {resultado}")
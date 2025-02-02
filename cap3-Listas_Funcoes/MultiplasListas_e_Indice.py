# Listas para armazenar os dados
equipamentos = []
valores = []
series = []
departamentos = []

# Loop para adicionar equipamentos
while True:
    # Solicita os dados do equipamento
    equipamento = input("Equipamento: ")
    valor = input("Valor: ")
    serial = input("Número de Série: ")
    departamento = input("Departamento: ")

    # Adiciona os dados às listas correspondentes
    equipamentos.append(equipamento)
    valores.append(valor)
    series.append(serial)
    departamentos.append(departamento)

    # Pergunta se o usuário deseja continuar
    resposta = input("Digite \"Y\" para continuar: ").upper()
    if resposta != "Y":
        break  # Sai do loop se a resposta não for "Y"

# Exibe os dados cadastrados
print("\nEquipamentos cadastrados:")
for i in range(len(equipamentos)):
    print(f"Equipamento: {equipamentos[i]}")
    print(f"Valor: {valores[i]}")
    print(f"Número de Série: {series[i]}")
    print(f"Departamento: {departamentos[i]}")
    print("-" * 20)  # Linha separadora
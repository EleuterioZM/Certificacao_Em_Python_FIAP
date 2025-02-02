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

# Busca por um equipamento
busca = input("\nNome do equipamento que deseja buscar: ").strip()  # Remove espaços extras
encontrado = False  # Variável para verificar se o equipamento foi encontrado

for i in range(len(equipamentos)):
    if busca.lower() == equipamentos[i].lower():  # Busca case-insensitive
        print(f"Equipamento: {equipamentos[i]}")
        print(f"Valor: {valores[i]}")
        print(f"Número de Série: {series[i]}")
        print(f"Departamento: {departamentos[i]}")
        print("-" * 20)  # Linha separadora
        encontrado = True  # Marca que o equipamento foi encontrado

# Se o equipamento não for encontrado
if not encontrado:
    print(f"Equipamento '{busca}' não encontrado.")
# Lista para armazenar os equipamentos
gaveta = []

# Loop para adicionar equipamentos
while True:
    # Solicita os dados do equipamento
    equipamento = input("Equipamento: ")
    valor = input("Valor: ")
    serial = input("Número Serial: ")
    departamento = input("Departamento: ")

    # Cria um dicionário para o equipamento
    equipamento_info = {
        "Equipamento": equipamento,
        "Valor": valor,
        "Serial": serial,
        "Departamento": departamento
    }

    # Adiciona o dicionário à lista "gaveta"
    gaveta.append(equipamento_info)

    # Pergunta se o usuário deseja continuar
    resposta = input("Digite \"Y\" para continuar: ").upper()
    if resposta != "Y":
        break  # Sai do loop se a resposta não for "Y"

# Exibe a lista de equipamentos cadastrados
print("\nEquipamentos cadastrados:")
for item in gaveta:
    print(item)
# Listas para armazenar os dados
from pyclbr import Function

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

# Busca por um equipamento pelo número de série
busca = input("\nNúmero de série do equipamento que deseja excluir: ").strip()  # Remove espaços extras
encontrado = False  # Variável para verificar se o equipamento foi encontrado

# Loop para buscar e remover o equipamento
for i in range(len(series)):
    if busca.lower() == series[i].lower():  # Busca case-insensitive
        print(f"Equipamento: {equipamentos[i]}")
        print(f"Valor: {valores[i]}")
        print(f"Número de Série: {series[i]}")
        print(f"Departamento: {departamentos[i]}")
        print("-" * 20)  # Linha separadora
        encontrado = True  # Marca que o equipamento foi encontrado

        # Remove o equipamento de todas as listas
        equipamentos.pop(i)
        valores.pop(i)
        series.pop(i)
        departamentos.pop(i)
        print("Equipamento removido com sucesso!")
        break  # Sai do loop após remover o equipamento

# Se o equipamento não for encontrado
if not encontrado:
    print(f"Equipamento com número de série '{busca}' não encontrado.")

# Exibe a lista atualizada
print("\nLista atualizada de equipamentos:")
for i in range(len(equipamentos)):
    print(f"Equipamento: {equipamentos[i]}")
    print(f"Valor: {valores[i]}")
    print(f"Número de Série: {series[i]}")
    print(f"Departamento: {departamentos[i]}")
    print("-" * 20)  # Linha separadora


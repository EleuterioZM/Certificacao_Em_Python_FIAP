def preencherInventario(lista):
    while True:
        equipamento = [
            input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")
        ]
        lista.append(equipamento)

        # Condição para sair do loop
        continuar = input("Deseja adicionar outro equipamento? (s/n): ").strip().lower()
        if continuar != 's':
            break

def exibirLista(lista):
    print("\nLista de Equipamentos:")
    for elemento in lista:
        print("-" * 30)
        print(f"Nome         : {elemento[0]}")
        print(f"Valor        : {elemento[1]:.2f}")
        print(f"Serial       : {elemento[2]}")
        print(f"Departamento : {elemento[3]}")
    print("-" * 30)

def localizarPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")
    encontrado = False
    for elemento in lista:
        if busca == elemento[0]:  # Substituído __eq__ por ==
            print("\nEquipamento encontrado:")
            print(f"Valor  : {elemento[1]:.2f}")
            print(f"Serial : {elemento[2]}")
            encontrado = True
            break  # Para evitar continuar a busca após encontrar o equipamento
    if not encontrado:
        print("Equipamento não encontrado.")

def depreciarPorNome(lista, porc):
    depreciacao = input("\nDigite o nome do equipamento que sera depreciado: ?")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * elemento[1]
            print("Novo Valor: ", elemento[1])
#
def excluirPorserial(lista):
    busca = int(input("\nNúmero de série do equipamento que deseja excluir: ").strip())
    for elemento in lista:
        if elemento[2] == busca:
            lista.remove(elemento)
    return "Itens excluidos. "

def resumirValores(lista) :
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
        if len(valores) > 0  :
            print("O equipamento mais caro custa:", max(valores))
            print("O equipamento menos caro custa:", min(valores))
            print("O total de  equipamentos e de :", sum(valores))
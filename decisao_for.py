tabuada = int(input("Digite um numero para exibir a tabuada: "))
print("Tabuada do numero", tabuada)
for valor in range(1, 13, 1):
    print(f"{tabuada} X {valor} = {tabuada * valor}")
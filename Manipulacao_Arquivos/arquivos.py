base_de_dados = []

with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines() :
        base_de_dados.append(registro.split(","))

print(base_de_dados)

print(float(base_de_dados[0] [0]) + float(base_de_dados[0][1]))
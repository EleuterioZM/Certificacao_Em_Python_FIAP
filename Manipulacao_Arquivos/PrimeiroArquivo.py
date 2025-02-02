from binascii import a2b_qp
from shutil import which

#arquivo = open("primeiro_arquivo.txt", "w")
#arquivo.write("Meu primeiro arquivo!")
#arquivo.close()


# Writing to the file
#a - appendice
#w - limpa e adiciona
# Writing to the file
with open("primeiro_arquivo.txt", "w") as arquivo:
    arquivo.write("Este e o primeiro arquivo.\n")
    arquivo.write("Estou aprendendo a manipular arquivos em Python.\n")

# Reading from the file
with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo após escrita:")
    print(conteudo)

# Appending to the file
with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("Adicionando mais uma linha ao arquivo.\n")

# Reading from the file again
with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("\nConteúdo do arquivo após append:")
    print(conteudo)
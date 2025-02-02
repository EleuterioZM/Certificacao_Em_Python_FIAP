from Funcoes.IdentificacaoDeFuncoes import *
minhaLista = []
print("prenchendo....")
preencherInventario(minhaLista)
print("Exibindo")
exibirLista(minhaLista)

print("Pesquisando...")
localizarPorNome(minhaLista)
print("Alterando..")
depreciarPorNome(minhaLista, 20)

print("excluindo..")
print(excluirPorserial(minhaLista))
exibirLista(minhaLista)

print("Resumindo ...")
resumirValores(minhaLista)
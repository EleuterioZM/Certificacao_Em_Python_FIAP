import socket

while True:
    url = input("Digite uma URL: ")
    try:
        ip = socket.gethostbyname(url)
        print("O IP referente à URL informada é:", ip)
    except socket.gaierror:
        print("Erro: URL inválida ou não pôde ser resolvida.")

    resposta = input("Pressione <Enter> para continuar ou digite 'N' para sair: ")
    if resposta.upper() == "N":
        break
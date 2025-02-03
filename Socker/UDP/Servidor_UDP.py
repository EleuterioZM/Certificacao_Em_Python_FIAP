from socket import *

# Configurações do servidor
servidor = "localhost"
porta = 5000

# Cria um socket UDP
servidor_socket = socket(AF_INET, SOCK_DGRAM)

# Associa o socket ao endereço e porta
servidor_socket.bind((servidor, porta))

print(f"Servidor UDP a escutar em {servidor}:{porta}...\n")

while True:
    # Recebe mensagem do cliente
    dados, endereco_cliente = servidor_socket.recvfrom(1024)
    mensagem_cliente = dados.decode()

    print(f"Cliente {endereco_cliente}: {mensagem_cliente}")

    # Se o cliente enviar "sair", encerra a comunicação
    if mensagem_cliente.lower() == "sair":
        print(f"Cliente {endereco_cliente} saiu da conversa.")
        continue

    # Responde ao cliente com entrada do utilizador
    resposta = input("Servidor: ")
    servidor_socket.sendto(resposta.encode(), endereco_cliente)


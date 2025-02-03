from socket import *

# Configuração do servidor
servidor = "localhost"
porta = 5000

# Cria socket UDP
cliente_socket = socket(AF_INET, SOCK_DGRAM)

print("Digite 'sair' para encerrar a conversa.")

while True:
    # Entrada do utilizador
    mensagem = input("Cliente: ")

    # Envia mensagem para o servidor
    cliente_socket.sendto(mensagem.encode(), (servidor, porta))

    # Se o utilizador digitar "sair", encerra a comunicação
    if mensagem.lower() == "sair":
        print("Conexão encerrada pelo cliente.")
        break

    # Aguarda resposta do servidor
    resposta, _ = cliente_socket.recvfrom(1024)
    print(f"Servidor: {resposta.decode()}")

# Fecha o socket ao sair do loop
cliente_socket.close()

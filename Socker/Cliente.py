from socket import *

# Configurações do servidor
servidor = "localhost"  # Endereço do servidor
porta = 5000            # Porta do servidor

# Cria um socket TCP/IP
cliente_socket = socket(AF_INET, SOCK_STREAM)

# Conecta ao servidor
cliente_socket.connect((servidor, porta))


# Envia uma mensagem ao servidor
mensagem = input("Escreva uma mensagem para o servidos :")
cliente_socket.send(mensagem.encode())

# Recebe a resposta do servidor
resposta = cliente_socket.recv(1024).decode()
print(f"Resposta do servidor: {resposta}")

# Fecha a conexão
cliente_socket.close()
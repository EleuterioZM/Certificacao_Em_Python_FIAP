usuarios = {}
emails = ["xpto@yxz.com", "asadasd@sadas.com"]

# Enumerate emails to create a list of tuples (index, email)
enumerated_emails = list(enumerate(emails))

# Loop through the enumerated emails
for chave in range(0, len(enumerated_emails)):
    print("Email:", enumerated_emails[chave][1])

    # Prompt the user for name and level
    nome = input("Digite o nome: ")
    nivel = input("Digite o nivel: ")

    # Store the user data in the dictionary
    usuarios[enumerated_emails[chave]] = [nome, nivel]

# Print all user information
for chave, dado in usuarios.items():
    print("\nUsuario.:", chave[0])  # Index
    print("Email.:", chave[1])  # Email
    print("Nome.:", dado[0])  # Name
    print("Nivel.:", dado[1])  # Level
name = input("Digite seu nome :")
idade = int(input("Digite sua idade :"))
doencaInfectocontagiosa = input("Suspeita de uma doenca infectocontagiosa? ").upper()
if idade >= 65 :
    print(f"O paciente {name}, POSSUI um atendimento prioritario")
elif  doencaInfectocontagiosa == "SIM" :
    print(f"O paciente {name} deve ser direcionado a sala de reserva")
else :
    print(f"O paciente {name}, NAO possui o  atendimento prioritario")
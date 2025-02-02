usuarios = {}
print(usuarios)

usuarios = \
    {
        "chaves" : ["Chaves do 8", "24/12/2017", "Recep_01"],
        "quico" : ["Quico Flores", "20/12/2017", "Raiox_03"]

    }
print(usuarios)

usuarios["florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_03"]
print(usuarios)

print("_" * 80)
print(usuarios.get("quico"))
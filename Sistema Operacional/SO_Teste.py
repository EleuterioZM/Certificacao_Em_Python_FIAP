import platform
import getpass
from  datetime import datetime

print("Nome da maquina:.............", platform.node())
print("Arquitectura:.............", platform.architecture())
print("Sistema Operacional:.............", platform.system())
print("Processador:.............", platform.processor())
print("Versao do Python:.............", platform.python_version())
print("Versao do SO:.............", platform.release())


print(datetime.now().month)

print(getpass.getuser())

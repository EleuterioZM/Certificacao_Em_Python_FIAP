from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario = input("Digite o nome do usuario :")
senha = input("Digite a senha :")

ftp.login(usuario, senha)
print("Directorio actual do trabalho", ftp.pwd())

ftp.cwd('pub')
print("Directorio correte", ftp.pwd())
print(ftp.retrlines('LIST'))

ftp.quit()
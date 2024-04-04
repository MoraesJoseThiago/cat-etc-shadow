#!/usr/bin/python3
import crypt

# Solicita ao usuário que insira a hash
hashcompleta = input("Coloque o que você quer decifrar: ")
# Exemplo: #kali:$y$j9T$dl4ti9p1KPx6HrZ59TPMJ/$drMOLlRW8BZmsDQ0riDlPnUDsfyIvRL4qfgODnuZVz4:19500:0:99999:>

# Divide a hash completa usando ':' como delimitador e pega a segunda parte (índice 1)
hashlimpa = hashcompleta.split(":")[1]
print(hashlimpa)

# Extrai as partes do sal
parts = hashlimpa.split("$")[1:4]
saltcompleto = "$" + "$".join(parts) + "$"

print("Salt completo:", saltcompleto)

# Abre o arquivo com lista de senhas
with open("listacomsenha.txt", "r") as file:
    # Lê cada linha do arquivo
    for line in file:
        # Remove caracteres de quebra de linha
        password = line.strip()
        # Gera o hash da senha usando o salt completo
        hashed_password = crypt.crypt(password, saltcompleto)
         #Verifica se o hash gerado é igual à hash original
        if hashed_password == hashlimpa:
            print("Senha encontrada:", password)
            break
        else:
            # Se o hash não corresponder, continue para a próxima senha
            print("Testamos a senha:", password)

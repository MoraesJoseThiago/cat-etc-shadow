# Decifrador de Hashes UNIX

Este script em Python é utilizado para decifrar hashes do tipo Unix utilizando uma técnica de força bruta. Ele solicita ao usuário a hash completa que deseja decifrar, extrai o "sal" da hash e, em seguida, verifica se há correspondência com uma lista de senhas fornecida em um arquivo de texto.

## Como usar

1. Certifique-se de ter o Python 3 instalado no seu sistema.
2. Clone este repositório ou baixe os arquivos `decifrador.py e listacomsenhas.txt`.
3. Execute o script com o comando `./decifrador.py`.
4. Insira a hash completa que deseja decifrar quando solicitado.

## Exemplo de Uso

```bash
$decifrador.py
Coloque o que você quer decifrar: #kali:$y$j9T$dl4ti9p1KPx6HrZ59TPMJ/$drMOLlRW8BZmsDQ0riDlPnUDsfyIvRL4qfgODnuZVz4:19500:0:99999:>
Salt completo: $y$j9T$dl4ti9p1KPx6HrZ59TPMJ/$
Testamos a senha: senha123
Senha encontrada: senhasecreta

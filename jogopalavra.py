palavra_secreta = "python"

print("===ADVINHE A PALAVRA===")


tentativas = 0


while True:
  letra = input('Digite uma Letra: ').lower()
  tentativa += 1

  resultado = ''

  for caracter in palavra_secreta:

    if caracter == letra:
      resultado += caracter

    else:
      resultado += '*'

  print(resultado)

  if '*'  not in resultado:
    print("Tu venceu")
    break

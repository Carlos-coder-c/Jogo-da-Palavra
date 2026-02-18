palavra_secreta = "python"

letras_acertadas = ''

print("===ADVINHE A PALAVRA===")


tentativas = 0


while True:
  letra = input('Digite uma Letra: ').lower()
  tentativas += 1

  resultado = ''

  if letra in palavra_secreta:
    letras_acertadas += letra

  for caracter in palavra_secreta:

    if caracter in letra_acertadas:
      resultado += caracter

    else:
      resultado += '*'

  print(resultado)

  if '*'  not in resultado:
    print(f"Tu venceu  \
    Tentativa: {tentativas}")
    break

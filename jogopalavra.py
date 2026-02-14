palavra_secreta = "Python"
tentativas = tentativas += 1

i = palavra_secreta.count('')

letras = palavra_secreta[i]

print("===ADVINHE A PALAVRA===")

for palavra in palavra_secreta:
    entrada = str(input ('Digite um letra: '))

    print(' Suas tentativa: ', tentativa'x')

    if entrada == letras:
        print(' Você acertou a letra: ' , letras)

    else:
        print('Você errou tente novamente')

    for acerto in palavra_secreta:
      palavra_chance = input('Digite a palavra: ')

      if palavra_chance == palavra_secreta:
        print("Você acertou, fim de jogo!")
        break

      else:
        print("Você errou tente novamente!")



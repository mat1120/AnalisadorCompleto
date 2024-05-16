somaidade = 0
mediaidade = 0
maiorhomemidade = 0
nomevelho = ""
menoridadehomem = 100
nomevelho1 = ""
maioridademulher = 0
nomemulher = ""
menoridademulher = 100
nomemulherNova = ""

for c in range(1, 5):
    nome = str(input("Digite o nome da {}ª pessoa: ".format(c))).strip()
    idade = int(input("Digite a idade da {}ª pessoa: ".format(c)))
    sexo = str(input("Digite o sexo da {}ª pessoa [M/F]: ".format(c))).upper()
    somaidade += idade
    mediaidade = somaidade / 4

    if c == 1 and sexo in "Mm":
        maiorhomemidade = idade
        nomevelho = nome
        menoridadehomem = idade
        nomevelho1 = nome
    if sexo in "Mm" and idade > maiorhomemidade:
        maiorhomemidade = idade
        nomevelho = nome
    if sexo in "Mm" and idade < menoridadehomem:
        menoridadehomem = idade
        nomevelho1 = nome

    if c == 1 and sexo in "Ff":
        maioridademulher = idade
        nomemulher = nome
        menoridademulher = idade
        nomemulherNova = nome
    if sexo in "Ff" and idade > maioridademulher:
        maioridademulher = idade
        nomemulher = nome
    if sexo in "Ff" and idade < menoridademulher:
        menoridademulher = idade
        nomemulherNova = nome
print("-=-"*20)
print("A média de idade do grupo é {}".format(mediaidade))
print("-=-"*20)
print("\033[31m-=-\033[m"*20)
if maiorhomemidade > 0:
    print("O homem mais velho se chama {} e tem {}".format(nomevelho, maiorhomemidade))
else:
    print("Não há homens no grupo")
if menoridadehomem < 100:
    print("O homem mais novo se chama {} e tem {} ".format(nomevelho1, menoridadehomem))
else:
    print("Não há homens no grupo")
print("\033[31m-=-\033[m"*20)
print("\033[35m-=-\033[m"*20)
if maioridademulher > 0:
    print("A mulher mais velha se chama {} e tem {}".format(nomemulher, maioridademulher))
else:
    print("Não há mulheres no grupo")
if menoridademulher < 100:
    print("A mulher mais nova se chama {} e tem {}".format(nomemulherNova, menoridademulher))
else:
    print('Não tem mulher mais nova, pois ambas têm a mesma idade')
print("\033[35m-=-\033[m"*20)

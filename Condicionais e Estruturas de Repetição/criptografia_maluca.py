palavra_1, palavra_2 = map(str,input().split(' '))

if len(palavra_1) == len(palavra_2):

    letra_maiuscula = False

    for x in range(len(palavra_1)):

        if palavra_1[x] == palavra_1[x].upper() and palavra_1[x].isnumeric() == False or palavra_2[x] == palavra_2[x].upper() and palavra_2[x].isnumeric() == False:

            letra_maiuscula = True

if len(palavra_1) != len(palavra_2) or letra_maiuscula == True:

    print('ERRO')

else:

    vogais = ['a', 'e', 'i', 'o', 'u']
    cript_palavra = ''

    for x, p1 in enumerate(palavra_1):

        if p1 == palavra_2[x] and p1 not in vogais:

            cript_palavra += palavra_1[x]

        elif x % 2 == 0:

            cript_palavra += palavra_1[x].upper()

        else:

            cript_palavra += '!!'

    print(cript_palavra)
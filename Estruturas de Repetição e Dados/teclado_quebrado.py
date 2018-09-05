excluir = ["[","]"]
beiju = ''
palavra = input()

for x in palavra:

    if x not in excluir:

        beiju += x

print(beiju)

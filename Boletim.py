ficha = []

while True:
    nome = str(input('Nome: ')).title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    if media < 7:
        ficha.append([nome, [n1, n2], media,'Reprovado'])
    else:
        ficha.append([nome, [n1, n2], media,'Aprovado'])


    perg = str(input('Quer continuar: [S/N]: ')).upper().strip()
    if perg == 'N':
        break

print('=' *15)
print(f'{"Nome":<10}{"Media":>10}')
for i, a in enumerate(ficha): #i = indice  #a = aluno
    print(f'{a[0]:<10} {a[2]:>8} {a[3]:>5}')
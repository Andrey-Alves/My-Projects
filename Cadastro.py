pessoas = []
tot = 0

while True:
    nome = str(input('Digite seu nome: ')).strip().title()
    s = str(input('Qual seu sexo? [M/F] : ')).upper().strip()
    while s not in 'MmFf':
        print(('Sexo INVALIDO.'))
        s =str(input('Qual seu sexo? [M/F] : ')).upper().strip()
    if s == 'M':
        s = 'Masculino'
    else:
        s = 'Feminino'

    idade = int(input('Idade: '))
    pessoas.append((nome, s, idade))
    tot += 1

    print('Cadastrar outra pessoa?')
    perg = str(input('S/N: ').upper()).strip()
    print('=' *20)
    if perg == 'N':
        break

print('=' *20)
print(f'Foram cadastradas {tot} pessoas')
for p in pessoas:
    print(f'{p[0]}, tem {p[2]} anos, seu sexo é {p[1]}')
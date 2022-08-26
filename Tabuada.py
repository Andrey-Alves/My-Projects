print('=' *10, 'TABUADA', '=' *10)

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    for c in range(1,11):
        print(f'{num} x {c} = {num*c}')
    
    print('=' *10)
    perg = str(input('Deseja saber a tabuada de outro número? [S/N]: ')).upper().strip()
    if perg == 'N':
        break
print('Programa Finalizado')

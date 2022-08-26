print('=' *10, 'TABUADA', '=' *10)

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print(f'{num} x {c} = {num*c}')
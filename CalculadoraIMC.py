print('='*10, 'Calculadora de IMC', '='*10)

altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = (peso / ( altura *2))

if imc < 18.5:
    print(f'Seu IMC foi {imc:.1f}')
    print('Abaixo do Peso')

elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC foi {imc:.1f}')
    print('Peso Ideal')

elif imc >= 25 and imc <= 29.9:
    print(f'Seu IMC foi {imc:.1f}')
    print('Sobrepeso')

elif imc >= 30 and imc <= 39.9:
    print(f'Seu IMC foi {imc:.1f}')
    print('Obesidade')

else:
    print(f'Seu IMC foi {imc:.1f}')
    print('Obesidade Grave')
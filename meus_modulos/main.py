from numeros.soma import somar
from numeros.sub import subtrair
from numeros.divisao import dividir
from numeros.multi import multiplicar
def menu():
    while True:
        print('1 - Somar')
        print('2 - Subtrair')
        print('3 - Dividir')
        print('4 - Multiplicar')
        print('5 - Sair')
        opcao = input('Selecione uma opção: ')
        if opcao == '1':
            a = float(input('Digite o primeiro valor: '))
            b = float(input('Digite o segundo valor: '))
            print(f'Resultado: {somar(a, b)}')
        elif opcao == '2':
            a = float(input('Digite o primeiro valor: '))
            b = float(input('Digite o segundo valor: '))
            print(f'Resultado: {subtrair(a, b)}')
        elif opcao == '3':
            a = float(input('Digite o primeiro valor: '))
            b = float(input('Digite o segundo valor: '))
            print(f'Resultado: {dividir(a, b)}')
        elif opcao == '4':
            a = float(input('Digite o primeiro valor: '))
            b = float(input('Digite o segundo valor: '))
            print(f'Resultado: {multiplicar(a, b)}')
        elif opcao == '5':
            print('Você saiu da calculadora!')
            break
menu()
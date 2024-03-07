opcao = 1

while opcao != 0:
    print('-- Contulta Sequência de Fibonacci --')
    numero = int(input('\nDigite o valor: '))

    soma = 0
    ultimo = 1
    penultimo = 0

    while soma < numero:
        soma = penultimo + ultimo
        penultimo = ultimo
        ultimo = soma

    if numero == soma:
        print('O numero pertence a sequência de Fibonacci')
    else:
        print('O numero não pertence a sequência de Fibonacci')

    opcao = int(input('Deseja continuar a consulta: \n1 - Sim \n0 - Não\n'))

print('Programa encerrado')

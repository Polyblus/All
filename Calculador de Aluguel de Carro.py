dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
km = float(input('Digite a quantidade de km que o carro percorreu: '))
valor = (dias * 60) + (km * 0.15)
print('O valor total a ser pago é de R$ {:.2f}'.format(valor))
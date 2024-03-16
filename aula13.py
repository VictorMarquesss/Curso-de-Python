nome = 'Emerson Victor'
altura = 1.75
peso = 95
imc = peso / (altura * altura)
linha_1 = f' {nome} tem {altura:.2f} de altura ' 
linha_2 = f'pesa {peso} quilos e seu imc é, '
linha_3 = f'{imc:.2f}'
# o F significa formatação 
print( linha_1)
print(linha_2)
print(linha_3)
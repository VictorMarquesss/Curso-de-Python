# Operadores Logicos
# and (e) or (ou) not (não)
# and - Todas as condições precisao ser, 
# verdadeiras
# se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy ( que a gente ja viu )
# 0 0.0'' False
# Também existe o tipo None que é,
# Usado para representar um não valor
entrada = input('[E] entrar [S] sair: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'


if (entrada == 'E'or entrada == 'e' ) and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair ')     

# Avaliação de curto circuito     
#print(True and True and True and False)
#print(bool (''))
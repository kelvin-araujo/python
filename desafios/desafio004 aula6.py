n = input('Digite algo:')
print('O tipo primitivo de {} é:'.format(n),type(n))
print('{} tem espaços?'.format(n), n.isspace())
print('{} é um numero?'.format(n), n.isnumeric())
print('{} é alfabético?'.format(n), n.isalpha())
print('{} é alfanumérico?'.format(n), n.isalnum())
print('{} tem maiúscula:'.format(n), n.isupper())
print('{} tem minúscula?'.format(n), n.islower())
print('{} é capitalizada?'.format(n), n.istitle())





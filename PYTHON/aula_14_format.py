a = 'A'
b = 'B'
c = 1.1

string = 'a={0} b={1} c={2}'
formato = string.format(a, b, c)
print(formato)

string = 'a={nome1} b={nome2} c={nome3}'
formato = string.format(nome1 = a, nome2 = b, nome3 =c)

print(formato)

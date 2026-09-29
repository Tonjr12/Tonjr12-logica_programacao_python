n = int(input('quantos termos deseja mostrar: '))
t1 = 0
t2 = 1
print (f'{t1} -> ', end=' ' )
print(f'{t2} -> ', end=' ' )
while t1 < n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'{t3} -> ', end=' ' )
print('FIM')



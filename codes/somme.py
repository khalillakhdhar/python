print('donnez un entier:')
x = input()
x=int(x)
c=int(x / 100)
d=int(x % 100 / 10)
u=x%10
print(c+d+u)
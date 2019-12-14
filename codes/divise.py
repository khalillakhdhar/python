print('donnez un entier:')
x = input()
x=int(x)
c=int(x / 100)
d=int(x % 100 / 10)
u=x%10
s=c+d+u
if(s%3==0):
    print(str(s)+"est divisible par 3")
else:
    print(str(s)+" n'est pas divisible par 3")
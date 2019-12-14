def controle(x):
    while x<1:
        print("donner un entier positif")
        x=int(input())
    return x
def pgcd(x,y):
    a=x
    b=y
    while x!=y:
        if x>y:
            x-=y
        else:
            y=y-x
    print("le pgcd entre %s et %s est de: %s"%(a,b,x))
a=-1
b=-1
a=controle(a)
b=controle(b)
pgcd(a,b)
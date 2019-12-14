y =-1
x=-1
def controle(vr):
    while vr <2:
        print("donnez un entier >1")
        vr=int(input())
    return vr
def fact(w):
    fact=1
    for i in range(2,w+1):
    #fact*=y
        fact=fact*i
    print("la factorielle est : "+str(fact))
x=controle(x)
y=controle(y)
fact(x)
fact(y)

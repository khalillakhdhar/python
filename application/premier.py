x=6
for i in range(2,x):
    if(x%i==0):
        break
if i<=int(x/2):
    print(" n est pas premier")
else:
    print("premier")
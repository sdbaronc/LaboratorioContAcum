a =int(input("ingrese un valor"))
b=0
c=0

while b<=a:
    b =b+1
    if a%b==0:
        c+=1
if c >2:
    print("el numero no es primo")
else:
    print("el numero es primo")



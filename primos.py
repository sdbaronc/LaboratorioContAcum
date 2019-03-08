a=int(input("ingrese a"))
cont=0

for i in range(1,a+1,1):
    if a%i==0:
        cont+=1

if cont >2:
    print("el numero " + str(a) + " no es primo")
else:
    print("el numero" + str(a) + " es primo")

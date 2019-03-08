print("comienzo")
print()
n1=int(input("Escriba un numero: "))

for i in range(1,n1):
    print()
division= n1%i
residuo0= division==0
print("Su residuo es: ",division)
print("El residuo es 0: ",residuo0)
print()
print("Fin")
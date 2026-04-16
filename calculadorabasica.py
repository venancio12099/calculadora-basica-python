# Definiendo variables a calcular
a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))
c = (input("Que operacion quieres desarrolar: "))

# Operaciones 
if c == ("+"):
    print("El resultado de la suma es", a+b)
elif c == ("-"):
    print("El resultado de la resta es", a-b)
elif c == ("*"):
    print("El resultado de la multiplicacion es", a*b)
elif c == ("/"):
    print("El resultado de la division es", a/b)
else:
    print("Ha habido un error")

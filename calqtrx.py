# NOMBRE DEL PROGRAMA
print("CALQTRX")

# NÚMERO A EVALUAR
numero = input("Ingresa el número a convertir: ")

# VALIDAR QUE SEA NÚMERO
while (numero.isdigit()==False):
    print("Has ingresado un caracter no numérico")
    numero = input("Ingresa el número a convertir: ")


# DESCARTAR DECIMALES : CONVERTIR NEGATIVOS E IMPRIMIR POSITIVOS
if (0<int(numero)<10):
    print(numero)


# ACCEDER A LOS ELEMENTOS DEL STRING
def extraerDecimales(*numTexto):
  for elemento in numTexto:
    yield from elemento


# GUARDAR EN LISTA LOS DECIMALES EXTRAIDOS – 1RA RONDA
listaTexto = list(extraerDecimales(*numero))
#print("print listaTexto", listaTexto)


# CONVERTIR LISTA str A int
listaNumeros = [int(i) for i in listaTexto]
#print("print listaNumeros", listaNumeros)


# SUMAR ELEMENTOS listaInt
sumaLista = sum(listaNumeros)
print("Resultado 1:", sumaLista)


# REVISAR QUE SEA UN NÚMERO DECIMAL O REPETIR 
if (sumaLista<10):
    print("if", sumaLista)
else:
    numero = str(sumaLista)
    listaTexto = list(extraerDecimales(*numero))
    listaNumeros = [int(i) for i in listaTexto]
    sumaLista = sum(listaNumeros)
    print("Resultado 2:", sumaLista)


if (sumaLista<10):
    print("if", sumaLista)
else:
    numero = str(sumaLista)
    listaTexto = list(extraerDecimales(*numero))
    listaNumeros = [int(i) for i in listaTexto]
    sumaLista = sum(listaNumeros)
    print("Resultado 3:", sumaLista)



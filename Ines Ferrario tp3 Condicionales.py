#Actividad 1
edad1 = int(input("Ingrese su edad: "))
mayorDeEdad = 18

if edad1 > mayorDeEdad:
    print("Es mayor de edad.")


#Actividad 2
nota= int (input("Ingrese su nota."))
minimaNota= 6

if nota >= minimaNota:
    print("Aprobado.")
else:
    print("Desaprobado.")


#Actividad 3
numero= int (input("Ingrese un número par."))

if numero%2==0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")


#Actividad 4
edad4= int (input("Ingrese su edad."))

if edad4< 12:
    print("Niño/a: menor de 12 años.")
elif (edad4 >= 12 and edad4 <18):
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif (edad4 >=18 and edad4<30):
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
else:
    print("Adulto/a: mayor o igual que 30 años.")


#Actividad5
contrasenia= (input("Ingrese una contraseña de entre 8 y 14 caracteres:"))
longitud= len(contrasenia)

if longitud >=8 and longitud <= 14:
    print ("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


#Actividad6
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

from statistics import mean, median, mode
media = mean(numeros_aleatorios)
mediana= median(numeros_aleatorios)
moda= mode(numeros_aleatorios)

print(f"Media:{media}")
print(f"Mediana:{mediana}")
print(f"Moda:{moda}")

if media > mediana and mediana > moda:
    print("La distribución tiene un sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print("La distribución tiene un sesgo negativo o a la izquierda.")
else:
    print("La distribución no tiene sesgo.")


#Actividad7
palabra= (input("Ingrese una frase o palabra."))
ultimaLetra= palabra[-1]

if ultimaLetra== "a" or ultimaLetra== "e" or ultimaLetra== "i" or ultimaLetra== "o" or ultimaLetra== "u" or ultimaLetra== "A" or ultimaLetra== "E" or ultimaLetra== "I" or ultimaLetra== "O" or ultimaLetra== "U" :
    print (palabra + "!") 
else:
    print (palabra)


#Atividad8
nombre= (input("Ingrese su nombre:"))
opcion= (input("Ingrese el número 1 si desea su nombre en mayúsculas , 2 en minúsculas, o 3 con la primera letras mayúscula:"))

if opcion=="1":
    nombreMayusculas= nombre.upper()
    print(nombreMayusculas)
elif opcion=="2":
    nombreMinusculas= nombre.lower()
    print(nombreMinusculas)
elif opcion=="3":
    nombreTitulo= nombre.title()
    print(nombreTitulo)
else:
    print("Opción no válida. Por favor, ingrese 1,2 o 3")


#Actividad9
magnitud= (input("Ingrese la magnitud del terremoto:"))

if magnitud <"3":
    print("Muy leve (imperceptible).")
elif magnitud >= "3" and magnitud< "4":
    print("Leve (ligeramente perceptible).")
elif magnitud >="4" and magnitud <"5":
    print ("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >="5" and magnitud <"6":
    print ("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >="6" and magnitud <"7":
    print ("Muy Fuerte (puede causar daños significativos).")
else:
    print ("Extremo (puede causar graves daños a gran escala).")


#Actividad10
hemisferio= (input("Ingrese en qué hemisferio se encuentra (N/S):"))
mes= int(input("Ingrese qué mes del año es:"))
dia= int(input("Ingrese qué día del año es:"))

if (mes == 12 and dia >= 21) or (mes <= 3 and mes > 0 and dia <= 20) or (mes == 1 and mes == 2):
    estacion_norte = "Invierno"
elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
else: 
    estacion_norte = "Otoño"

if hemisferio.upper() == "N":
    print(f"La estación es: {estacion_norte}")
elif hemisferio.upper() == "S":
    if estacion_norte == "Invierno":
        print("La estación es: Verano")
    elif estacion_norte == "Primavera":
        print("La estación es: Otoño")
    elif estacion_norte == "Verano":
        print("La estación es: Invierno")
    else:
        print("La estación es: Primavera")
else:
    print("Hemisferio no válido.")






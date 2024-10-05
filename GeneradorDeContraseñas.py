import random

password = []

#Generar 16 caracteres
while len(password) < 16 :
    #Generando un numero aleatorio
    numero = random.randint(65, 122)
    #Haciendo el control de los ascii
    if numero < 91 or numero > 96 :
        asciiNumber = chr(numero)
        password.append(asciiNumber)

# Convertir la lista a una cadena para mostrarla
password_str = ''.join(password)

print("Contraseña: " + password_str)
print("¡Hola!")

name = input("¿Cómo te llamas?: ")
print("Bienvenido/a " + name + " a mi primer programa de Python")

age = input("¿Qué edad tienes?: ")
print(name + " tiene " + age + " años. ¿Es correcto? (si/no)")
confirm = input()
print(confirm)

# Definición de las respuestas esperadas
si = "si"
no = "no"

# Comprobación de la confirmación
if confirm.lower() == si:
    print("Gracias por confirmar")
else:
    print("Saliendo del programa...")

# Asegurarse de que la edad sea un número
age = int(age)  # Convertimos `age` a entero para poder realizar operaciones aritméticas

age2 = input("Espera, pon otra edad: ")
age2 = int(age2)  # Convertimos `age2` a entero

# Sumar las edades
sum_ages = age + age2
print("La suma de edades es igual a " + str(sum_ages))  # Convertimos `sum_ages` a cadena para imprimir

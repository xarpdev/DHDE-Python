# -*- coding: utf-8 -*-
"""
Ejercitación3_Quispe.ipynb

Automatically generated by Colaboratory.
"""

# Crear un programa que solicite un número entero positivo.
# Implementar la función mitad_numero que recibe un número y retorna su mitad.
# Finalmente imprimir el mensaje: "La mitad de su número es:..."
def mitad_numero(num):
  mitad = num / 2
  return mitad

numero = int(input("Ingrese un número: "))
rtd = mitad_numero(numero)

print("La mitad de su número es: ", rtd)

# Crear un programa que pregunte por pantalla el nombre completo del usuario.
# Luego muestre por pantalla el usuario tres veces de la siguiente manera:
# Primero con todas las letras minúsculas, segundo con mayúsculas y tercero en invertida.

nombre_completo = input("Ingresa tu nombre completo: ")
nombre_invertido = nombre_completo[::-1]
print(nombre_completo.lower())
print(nombre_completo.upper())
print(nombre_invertido)
#Calculadora de resistencias electronicas

#diccionario para almacenar el valor de cada color

codigo_colores = {
    "negro"    :0,
    "cafe"     :1,
    "rojo"     :2,
    "naranja"  :3,
    "amarillo" :4,
    "verde"    :5,
    "azul"     :6,
    "violeta"  :7,
    "gris"     :8,
    "blanco"   :9,
    "dorado"   :5,
    "plata"    :10
}

tolerancias = {
    "rojo":"2%",
    "dorado":"5%",
    "plata":"10%"
}

#Variable para sufijo de resistencia K, M, G
notacion = ""
print("-----CALCULADORA DE VALOR DE RESISTENCIAS-----")
banda1 = input("Ingresa el color de la primera banda: ")
banda2 = input("Ingresa el color de la segunda banda: ")
banda3 = input("Ingresa el color de la tercera banda: ")
banda4 = input("Ingresa el color de la cuarta banda(tolerancia): ")


resultado = (codigo_colores[banda1.lower()]*10 + codigo_colores[banda2.lower()]) * (10**codigo_colores[banda3.lower()])

if resultado >= 1000 and resultado <= 990000:
    resultado = resultado / 1000
    notacion = "K"
elif resultado > 990000 and resultado < 9900000000:
    resultado = resultado / 1000000
    notacion = "M"
elif resultado >= 9900000000:
    resultado = resultado / 1000000000
    notacion ="G"

tolerancia = tolerancias[banda4.lower()]

print("\nValor de la resistencia")
print(f"{resultado}{notacion} Ohms +/-{tolerancia}")
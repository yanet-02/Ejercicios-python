import datetime

nombre = input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto: ")
total_compra = float(input("Ingresa el total de tu compra: "))
folio = 100  
fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
else:
    descuento = 0
    total_final = total_compra

ticket = f"""
================================ TICKET DE COMPRA ================================
Tienda: Tienda XYZ
Folio: {folio}
Fecha y hora: {fecha_hora}
---------------------------------------------------------------------------------
Cliente: {nombre}
Producto: {producto}
Total de la compra: ${total_compra:.2f}
Descuento aplicado: ${descuento:.2f}
Total a pagar: ${total_final:.2f}
---------------------------------------------------------------------------------
¡Gracias por tu compra, Feliz día! ¡Vuelve pronto!
"""
print(ticket)
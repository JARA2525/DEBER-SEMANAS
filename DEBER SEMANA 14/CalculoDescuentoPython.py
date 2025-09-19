def calcular_descuento(monto, descuento=15):
    """
    Calcula el monto del descuento sobre una compra.
    Parámetros:
      monto (float): monto total de la compra
      descuento (int, opcional): porcentaje de descuento 15%
    Retorna:

      float: monto del descuento calculado
    """
    monto_descuento = monto * (15 / 100)
    return monto_descuento


monto_compra = float(input("Ingrese el monto total de la compra: "))
descuento_calculado = calcular_descuento(monto_compra)

print(f" Cliente frecuente aplica el 15% DESCUENTO: ${descuento_calculado:.2f}")
print(f"El monto final a pagar: ${monto_compra - descuento_calculado:.2f}")


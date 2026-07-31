# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona
 
anchoReporte = 44
limitComisionAlta = 30000
tasaComisionAlta = 0.08
limitBono = 50000
montoBono = 500
tasaComisionBase = 0.05
decimalesMoneda = 2
 
# lista de vendedores
vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]

def calcularTotalVendedor(ventasMensuales):
    # si vendio mas de 30000
    if ventasMensuales > limitComisionAlta:
        # calcula la comision del 8%
        tasaComision = tasaComisionAlta
    else:
        # calcula la comision del 5%
        tasaComision = tasaComisionBase

    comision = ventasMensuales * tasaComision
    comision = round(comision, decimalesMoneda)

    # el bono es de 300
    if ventasMensuales > limitBono:
        bono = montoBono
    else:
        bono = 0

    return round(comision + bono, decimalesMoneda)

def calcular_comisiones():
    resultados = []
    totalPagar = 0

    # recorre la lista
    for nombreVendedor, ventasMensuales in vendedores:
        totalVendedor = calcularTotalVendedor(ventasMensuales)
        resultados.append((nombreVendedor, totalVendedor))
        totalPagar = totalPagar + totalVendedor

    return resultados, totalPagar


def imprimir_reporte(resultados, totalPagar):
    print("=" * anchoReporte)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * anchoReporte)

    for nombreVendedor, totalVendedor in resultados:
        print(nombreVendedor + ": Q " + str(totalVendedor))

    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * anchoReporte)
    print(
        "Total a pagar: Q "
        + str(round(totalPagar, decimalesMoneda))
    )


resultados, totalPagar = calcular_comisiones()
imprimir_reporte(resultados, totalPagar)
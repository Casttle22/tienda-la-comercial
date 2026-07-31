# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona
 
# lista de vendedores
vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]
 
def calcularComisiones():
    totalAPagar = 0
    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)
    # recorre la lista
    for d in vendedores:
        # si vendio mas de 30000
        if d[1] > 30000:
            # calcula la comision del 8%
            comision = d[1] * 0.08
            comision = round(comision, 2)
            # el bono es de 300
            if d[1] > 50000:
                bono = 500
            else:
                bono = 0
            totalVendedor = round(comision + bono, 2)
            totalAPagar = totalAPagar + totalVendedor
            print(d[0] + ": Q " + str(totalVendedor))
        else:
            # calcula la comision del 5%
            comision = d[1] * 0.05
            comision = round(comision, 2)
            bono = 0
            totalVendedor = round(comision + bono, 2)
            totalAPagar = totalAPagar + totalVendedor
            print(d[0] + ": Q " + str(totalVendedor))
    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * 44)
    print("Total a pagar: Q " + str(round(totalAPagar, 2)))
 
calcularComisiones()

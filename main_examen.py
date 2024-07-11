import funciones_examen as fn
detalle_trabajadores = []
import csv

while True:
    print("     MENU     ")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar Sueldos")
    print("3. Ver Estadistica")
    print("4. Reporte de Sueldos")
    print("5. Salir del programa")

    try:
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            fn.asignacion_sueldos(detalle_trabajadores)
        elif opc == 2:
            fn.clasificacion_sueldos(detalle_trabajadores)
        elif opc == 3:
            fn.ver_estadistica(detalle_trabajadores)
        elif opc == 4:
            fn.reporte_sueldos(detalle_trabajadores)
        elif opc == 5:
            print("Finalizando programa...")
            print("Desarrollado por Alfonso Gonzalez")
            print("RUT 19.152.401-2")
            break
        else:
            print("Opcion fuera de rango, intentelo otra vez")

    except ValueError:
        print("Error: Opcion invalida")
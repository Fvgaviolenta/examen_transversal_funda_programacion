import random as rd
import statistics as st
import csv

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

def asignacion_sueldos(detalle_trabajadores):
    for trabajador in trabajadores:
        sueldo_aleatorio = rd.randint(300000, 2500000)
        detalle_trabajadores.append({trabajador:sueldo_aleatorio})
    print(detalle_trabajadores)
    return detalle_trabajadores
    

def clasificacion_sueldos(detalle_trabajadores):
    if not detalle_trabajadores:
        print("\nNo hay trabajadores registrados...\n")
    else:
        sueldos_menores = 0
        bajo_8k = []
        sueldos_medios = 0
        entremedio = []
        sueldos_superiores = 0
        sobre_2m = []

        for diccionarios in detalle_trabajadores:
            for key,value in diccionarios.items():
                if value < 800000:
                    sueldos_menores +=1
                    bajo_8k.append({key:value})

                elif value >= 800000 and value <= 2000000:
                    sueldos_medios +=1
                    entremedio.append({key:value})

                else:
                    sueldos_superiores +=1
                    sobre_2m.append({key:value})

        print("\nSueldos menores a $800.000")
        print(f"Total: {sueldos_menores}")
        print("Nombre Emplado:    Sueldo:")
        for diccionario in bajo_8k:
            for key, value in diccionario.items():
                print(key,"    ",value)
        print()

        print("Sueldos entre $800.000 y $2.000.000")
        print(f"Total: {sueldos_medios}")
        print("Nombre Empleado:    Sueldo:")
        for diccionario in entremedio:
            for key, value in diccionario.items():
                print(key,"    ",value)
        print()

        print("Sueldos superiores a $2.000.000")
        print(f"Total: {sueldos_superiores}")
        print("Nombre Empleado:    Sueldo:")
        for diccionario in sobre_2m:
            for key, value in diccionario.items():
                print(key,"    ",value)
        print()

def ver_estadistica(detalle_trabajadores):
    if not detalle_trabajadores:
        print("\nNo hay trabajadores registrados...\n")
    else:
        valores_sueldo = []
        for diccionarios in detalle_trabajadores:
            for sueldos in diccionarios.values():
                valores_sueldo.append(sueldos)
        print(f"\nSueldo mas alto: {max(valores_sueldo)}")
        print(f"Sueldo mas bajo: {min(valores_sueldo)}")
        print(f"Promedio sueldos {sum(valores_sueldo)/len(valores_sueldo)}")
        print(f"Media geometrica: {st.geometric_mean(valores_sueldo)}")
        print()

def reporte_sueldos(detalle_trabajadores):
    if not detalle_trabajadores:
        print("\nNo hay trabajadores registrados...\n")
    else:
        detalle_reporte = []
        for detalles in detalle_trabajadores:
            for key,value in detalles.items():
                desc_salud = round(value*0.07) 
                desc_afp = round(value*0.12)
                sueldo_liq = value - (desc_afp + desc_afp)
                detalle_reporte.append([key,value,desc_salud,desc_afp,sueldo_liq])

        print("NOMBRE EMPLEADO    SUELDO BASE    DESC SALUD    DESC AFP    SUELDO LIQUIDO")
        for listas in detalle_reporte:
            print(f"{listas[0]}        ${listas[1]}        ${listas[2]}        ${listas[3]}       ${listas[4]}")

        encabezados_csv = ["NOMBRE EMPLEADOR", "SUELDO BASE", "DESC SALUD", "DESC AFP", "SUELDO LIQUIDO"]
        with open("report_trabajadores.csv","w") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(encabezados_csv)
            for listas in detalle_reporte:
                escritor.writerow(listas)


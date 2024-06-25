import random


def grabar_datos():
        print("Grabar")
        while True:
            try:
                tipo= int(input("Ingrese el tipo de vehiculo\n1. Automovil\n2.Camion\n3.Camioneta\n4.Moto\n"))#DATO 1
            except:
                tipo=0
            if tipo <1 or tipo >4:
                print("Por favor ingrese una opcion valida")
                    
            elif tipo == 1:
                tipo= "Automovil"
                break
            elif tipo == 2:
                tipo= "Camion"
                break
            elif tipo ==3:
                tipo= "Camioneta"
                break
            elif tipo ==4:
                tipo ="Moto"
                break
            #fin if
        #fin while
        while True:
            
            patente= input("Ingrese su patente, Por ejemplo FGHJ12\n")
            if len(patente) <6:
                print("Por favor re-ingresar su patente\n")
            else:
                break
            
        while True:
            marca= input("Por favor ingrese la marca del vehiculo a grabar\n")
            if len(marca) <2 or len(marca)>15:
                print("Por favor ingrese una marca valida")
            elif marca == " ":
                marca_val=marca.replace(" ","")
                print("Por favor intentelo de nuevo")
            else:
                break
        while True:
            try:
                precio= int(input("Por favor ingrese el precio del vehiculo\n"))
            except:
                precio = 0
                
            if precio <0 or precio < 5000000:
                print("Precio del vehiculo debe ser mayor a cinco millones")
            else:
                break
        while True:
            try:
                multas= int(input("Ingrese la cantidad de multas que posee\n"))
            except:
                multas = 0
            
            if multas ==0:
                multas = "ninguna"
                break
            elif multas ==1:
                multas = 1
                break
            else:
                break
                
        while True:
            try:
                fecha_registro= int(input("ingrese la fecha en que se registró el vehiculo (Formato: DDMMAAAA, ejemplo 25122002)\n"))
            except:
                fecha_registro = 0
            
            if fecha_registro >99999999:
                print("Ingrese una fecha valida")
            else:
                break
        while True:
            try:
                run= int(input("Ingrese su rut sin digito verificador\n"))
                if run > 25000000:
                    print("rut invalido")
            except:
                run = 0
                
            nombre_dueño= input("Ingrese el nombre del dueño del vehiculo\n")
            if marca == " ":
                marca_val=marca.replace(" ","")
                print("Por favor intentelo de nuevo")
            else: 
                break
            break
                
        datosvehiculo=({
        "Tipo":tipo,
        "Patente":patente,
        "Marca":marca,
        "Precio":precio,
        "Multas":multas,
        "Fecha de Registro":fecha_registro,
        "RUN":run,
        "Nombre":nombre_dueño})
        
        return datosvehiculo

def buscar_datos():
        patente_aux= input("Ingrese la patente que desea:\n")
        if patente_aux == datosvehiculo[1]["Patente"]:
            print("Tipo \t Patente \t Marca \t Precio $ \t Multas \t Fecha Registro \t RUN \t Nombre Dueño")
        for elem in datosvehiculo:
            for k,v in elem.items():
                print(k,v)
            print(".")

def imprimir_cert():
    op =input("Ingrese su opcion\n1. Emision de contaminantes\n2.Anotaciones vigentes\n3.Multas")
    if op == 1:
        print("Emision de contaminantes")
        emision = print(random.randrange(1000,5000,500))
        print(f"su emision es de {emision}, patente{datosvehiculo[1]["Patente"]}, nombre{datosvehiculo[7]["Nombre"]},run{[6]["RUN"]}")
            
    elif op==2:
        print("Anotacones Negativas")
        anotaciones = print(random.randrange(1000,5000,500))
        print(f"El vehiculo tiene{anotaciones},patente{datosvehiculo[1]["Patente"]}, nombre{datosvehiculo[7]["Nombre"]},run{[6]["RUN"]}")
    elif op ==3:
        print("Multas")
        print(f"El vehiculo tiene{datosvehiculo[4]["Multas"]},patente{datosvehiculo[1]["Patente"]}, nombre{datosvehiculo[7]["Nombre"]},run{[6]["RUN"]}")
            


#Principa
while True:
    print("""Bienvenido a la plataforma de AutoSeguro.
      Menu
      1.Grabar vehiculo
      2.Buscar vehiculo
      3.Imprimir Certificados
      4.Salir
      """)
    try:
        op= int(input("Por favor ingrese su opcion: "))
    except:
        op = 0
        
    if op <0 or op >4:
        print("Por favor ingrese solo numeros del 1 al 4.")
        
    if op == 1:
        print(grabar_datos())
        datosvehiculo = grabar_datos()
        break

    elif op == 2:
        print(buscar_datos())
        break
    
    elif op == 3:
        print(imprimir_cert())
        break
    else:
        print("Saliendo del programa")
        break
    


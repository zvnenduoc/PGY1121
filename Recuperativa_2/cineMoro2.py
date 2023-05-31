import os
# NOMBRE: ESTEBAN VICENTE RAMOS HORTA
# ARCHIVO: RECUPERATIVA 2 (CINE MORO EN PYTHON)
# valores de precio
valnin=5500
valjov=7000
valadt=9000
# strings de entradas
nin="Niño"
jov="Joven"
adt="Adulto"
# contadores de entradas
contnin=0
contjov=0
contadt=0
# porcentajes
pcjnin=0
pcjjov=0
pcjadt=0
# totales por entrada
ttlnin=0
ttljov=0
ttladt=0
entradasTotales=0
tickets=0
# totales finales
totalpay=0
ganancia=0
ventotal=0
# prevariables
cat1=0
selection=0
a=0
response=0
# empieza el juego
while selection!=3: #while principal
    while True:
        try:
            os.system("CLS")
            print(":::::::::::::::::Bienvenido al cine Moro::::::::::::::::::")
            print("\nMenú Principal\nIngrese 1 para realizar venta\nIngrese 2 para ver los datos de las ventas\nIngrese 3 para salir")
            selection=int(input())
            if selection==1: # REALIZAR VENTA
                contnin=0
                contjov=0
                contadt=0
                totalpay=0
                entradasTotales=0
                r=0
                print("\n:::::::::::::::::::::::::::::::::")
                print("Ha seleccionado 1: realizar venta")
                print(":::::::::::::::::::::::::::::::::\n")
                while selection==1: #VENTA
                    while r<1:
                        try:
                            run=str(input("\nIngrese Run de cliente: \n"))
                            break
                        except Exception as errorRun:
                            print(f"\nIngrese run válido: {errorRun}\n")
                    while True: # CATEGORIA
                        try:
                            print("::::::::::::::::::::::::::::::::::::::::")
                            print(f"\nPrecios por edad: \n{nin}: {valnin}\n{jov}: {valjov}\n{adt}: {valadt}")
                            cat1=int(input("\n¿Qué categoría de entradas desea comprar?\nIngrese 1 para Niño\nIngrese 2 para Joven\nIngrese 3 para Adulto\n"))
                            print("::::::::::::::::::::::::::::::::::::::::")
                            if cat1==1:
                                print(f"\nHa seleccionado: {nin}\n")
                                valsel=valnin
                            elif cat1==2:
                                print(f"\nHa seleccionado: {jov}\n")
                                valsel=valjov
                            elif cat1==3:
                                print(f"\nHa seleccionado: {adt}\n")
                                valsel=valadt
                            else:
                                print("\n¡Debe ingresar 1 a 3!\n")
                            if cat1 in range(1,4):
                                break
                        except Exception as errorCat1:
                            print(f"\nPor favor ingrese un número válido: {errorCat1}\n")
                    while True: #NUMERO DE ENTRADAS
                        try:
                            print("::::::::::::::::::::::::::::::::::::::::")
                            numEnt=int(input("¿Cuántas entradas desea comprar?: "))
                            print("::::::::::::::::::::::::::::::::::::::::")
                            if numEnt>0:
                                print(f"\nHa ingresado comprar: {numEnt} entradas\n")
                                totalpay+=(numEnt*valsel)
                                entradasTotales+=numEnt
                                if cat1==1:
                                    contnin+=numEnt
                                elif cat1==2:
                                    contjov+=numEnt
                                elif cat1==3:
                                    contadt+=numEnt
                                break
                            else:
                                print("\nIngrese un número mayor a 0\n")
                        except Exception as errorEntrada:
                            print(f"\nIngrese número de entradas válido: {errorEntrada}\n")
                    a=0
                    while a<1: #COMPRAR MAS ENTRADAS
                        try:
                            response=int(input(f"\n¿Le gustaría comprar otras entradas de diferente categoría?\nIngrese 1 para Sí\nIngrese 2 para No\n"))
                            if response==1:
                                print("\nEntendido, vuelva a comprar, los cargos se le agregaran a su boleta.\n")
                                a=1
                                r=1
                            elif response==2:
                                print("\nEntendido, tenga su boleta:\n")
                                while True: #BOLETAA
                                    try:
                                        print(":::::::::::::::::::::::::")
                                        print("Boleta Cliente")
                                        print(f"Run: {run}")
                                        print(f"Entradas compradas: {entradasTotales}")
                                        print(f"{nin}: {contnin}")
                                        print(f"{jov}: {contjov}")
                                        print(f"{adt}: {contadt}\n")
                                        print(f"Total a pagar: {totalpay}")
                                        print(":::::::::::::::::::::::::")
                                        boleta=int(input(f"\nIngrese 1 para confirmar su compra\nIngrese 2 para cancelar\n"))
                                        if boleta==1:
                                            print("\nGracias por su compra, disfrute la función\n")
                                            tickets+=entradasTotales
                                            ganancia+=totalpay
                                            ventotal+=1
                                            ttlnin+=contnin
                                            ttljov+=contjov
                                            ttladt+=contadt
                                            input("\nPresione enter para continuar\n")
                                            a=1
                                            break
                                        elif boleta==2:
                                            print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                            print(f"Entendido, la compra para el cliente {run}, se ha cancelado.")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                                            input("Presione enter para continuar")
                                            a=1
                                            break
                                    except Exception as errorBoleta:
                                        print(f"Ingrese 1 o 2 para confirmar o cancelar la compra: {errorBoleta}")
                            else:
                                print("\nIngrese 1 o 2 por favor\n")
                        except Exception as errorDecision:
                            print(f"Debe ingresar un número válido: {errorDecision}")
                        if response!=1:
                            selection=0
            elif selection==2: # DATOS DE VENTAS
                print("\n::::::::::::::::::::::::::::::::::::::::::")
                print("Ha seleccionado 2: ver los datos de ventas")
                print("::::::::::::::::::::::::::::::::::::::::::\n")
                while selection==2:
                    try:
                        print(f"______________\nMenu Operador\n______________\n")
                        pcjnin = ttlnin*100/tickets
                        pcjjov = ttljov*100/tickets
                        pcjadt = ttladt*100/tickets
                        #GANANCIAS VENDEDOR
                        print("::::::::::::::::::::::::::")
                        print(f"Ganancias, porcentaje, y ventas\n")
                        print(f"Ganancias: {ganancia}\n")
                        print(f"Ventas totales: {ventotal}")
                        print(f"Entradas vendidas: {tickets}")
                        print("\nVentas & Porcentajes:")
                        print(f"{nin}: {ttlnin} | {pcjnin} %")
                        print(f"{jov}: {ttljov} | {pcjjov} %")
                        print(f"{adt}: {ttladt} | {pcjadt} %")
                        print("::::::::::::::::::::::::::::::")
                    except Exception as errorSel2:
                        print("\n_____________________\nNo se han realizado ventas\n_____________________")
                    input("\nPresione enter para volver al menú\n")
                    break
            elif selection==3:
                print("\n::::::::::::::::::::::::::::::::::::")
                print("Ha seleccionado salir del programa")
                print("::::::::::::::::::::::::::::::::::::\n")
                break
            else:
                print("\nPor favor ingrese 1, 2, o 3\n")
        except Exception as errorMenu:
            print(f"\nDebe ingresar un numero válido: {errorMenu}\n")
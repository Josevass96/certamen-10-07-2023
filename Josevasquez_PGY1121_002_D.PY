import os
os.system("cls")

listaentradas = []
listarut = []
listaplatinum = []
listagold = []
listasilver = []

platinum = 120000
gold = 80000
silver = 50000

menu = """
1. Comprar entradas
2. Ubicaciones Disponibles
3. Lista de Asistentes
4. Ganancias Totales
5. Salir
"""
while True:
    try:
        opc = int(input(menu))
        if opc == 5:
            print("Muchas Gracias, Hasta Luego")
            break
            
        elif opc == 1:
            while True:
                try:
                    entrada = int(input("cuantas entradas desea: "))
                    if entrada >= 1 and entrada <= 3:
                       listaentradas.append(entrada)
                       print(listaentradas)
                    else:
                        print("reintente")
                except:
                    print("ocurrio una excepcion")
                    while True:
                        try:
                            
                            asiento = input("""
                            Precio de asientos:
                            -------------------------------------------
                            PLatinum_____ $120.000 - 
                            Gold_________ $80.000  -
                            Silver_______ $50.000  -
                            -------------------------------------------
                            Ingrese Asiento:
                            """)
                            if asiento == "platinum":
                                cantplatinum = int(input("""
                                platinum -- $120.000
                                ____________________________
                                seleccione asientos (1-20)
                                """))
                                if cantplatinum >= 1 and cantplatinum <= 20:
                                    listaplatinum.append(cantplatinum)
                                    print(listaplatinum)
                                    break
                                else:
                                    print("ocurrio una excepcion")
                            elif asiento =="gold":
                                cantgold = int(input("""
                                gold -- $80.000
                                ____________________________
                                seleccione asientos (21 - 50)
                                """))
                                if cantgold >= 21 and cantgold <= 50:
                                    listagold.append(cantgold)
                                    print(listagold)
                                    break                            

                        except:
                            print("ocurrio una excepcion")
                            


    except:
     print("ocurrio una excepcion")
                            

    
       
                




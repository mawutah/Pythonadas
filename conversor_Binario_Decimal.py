import os # llama al sistema operativo
os.system("clear") # llama al sistema operativo para limpiar la pantalla
x = "p" # es una especie de bandera para usar la emulacion de do while
while True:
   if  x !="q":
    os.system("clear")
    bit = int(input("Ingrese un numero binario valido,(solo 0 y 1):"))
    os.system("clear")
    con2 = bit # igualo el binaro ingresado para poder mostrarlo en pantalla despues
    con1 = con2 % 10 # separo de a un bit
    con2 = con2 // 10 # guardo el resto
    deci = 0 # aca guardo el numero convertido
    i = 0 # variable contado para generar las potencias
    flag = 0 # esta bandera la uso para saber si el numero ingresado fue o no valido
    while (con1 !=0 or con2 !=0): # valida el fin del numero binario
        if (con1 == 1 or con1 == 0): # valida que los numero ingresados sean 1 o 0
           deci += con1 * (2 ** i)  # se eleva 2 a la potencia de la pocicion del bit con la variable i
           con1 = con2 % 10 # condicion para el ciclo while, vuelve a dividir el binario ingresado
           con2 = con2 // 10 # guarda el resto del binario
           i += 1 # ingrementa en 1 el contado de pocicion para la potencia
        else:    # condicion si el numero ingresado no es valido, cancela el while y pone la bandera en 1
           con1 = 0
           con2 = 0
           flag = 1

    if flag != 1  : # segun el estado de la bandera, muestra el resultado.
        print("El numero binario", bit, "es:",deci ,"en decimal")
    else:
     print("El numero ingresado", bit, "no es un binario valido") # hasta aca el programa principal
    print(" ") 
    x = input("Pulse cualquier tecla si quiere convertir de nuevo, o ingrese Q para finalizar:") # es para validar el dowhile
    x = x.lower()
    if x == "q": #condicion de salida del dowhile
       break
os.system("clear")
print("Gracias por usar el programa")

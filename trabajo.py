

valores={}


ingreso= int(input("Desea ingresar, editar o eliminar un color\n1.Ingresar \n2.Editar \n3.Eliminar \n4.Salir \n"))

while ingreso == 1:

    llaves=input("ingresa clave del valor: ")
    valores=input("Ingresa valor: ")
    valores.update({llaves:valores})
    print(valores)
    ingreso= int(input("Desea ingresar, editar o eliminar un valor\n1:Ingresar \n2:Editar \n3:Eliminar \n4.: \n"))
while ingreso ==2:
    llaves=input("Ingresa clave del valor: ")
    valores=input("Ingresa valor: ")
    valores.update({llaves:valores})
    print(valores)
    ingreso= int(input("Desea ingresar, editar o eliminar un valor\n1.Ingresar \n2.Editar \n3.Eliminar \n4.Salir \n"))
while ingreso ==3:
    llaves=input("ingrese clave del valor: ")
    valores.pop(llaves)
    print(valores)
    ingreso= int(input("Desea ingresar, editar o eliminar un color\n1:Ingresar \n2:Editar \n3:Eliminar \n4:Salir \n"))
while ingreso ==4:
    break
while ingreso <0 or ingreso >4:
    print  ("Opción invalida")
    ingreso= int(input("Desea ingresar, editar o eliminar un valor\n1:Ingresar \n2:Editar \n3:Eliminar \n4:Salir \n"))
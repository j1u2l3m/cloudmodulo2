import boto3
#crear funcion para listar tablas de dynamodb
def listar_tablas():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)
  
  opcion =  1
  
  while opcion 1 = 0:
      print("Ingrese la opc que desea")
      print("1.listar tablas de dyanmodb de la cuenta")
      print("0. Salir")
      opcion =int(input())
    if opcion == 1:
      listar_tablas()
    elif opcion  == 0:
      print ("Hasta luego")
    else:  
      print("opcion no valida ")
        
listar_tablas()

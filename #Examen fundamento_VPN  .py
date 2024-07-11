
import os,random,csv,time
os.system ("cls")
#listas

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
empleados=[]

#menu
def menu():
    
    print("----------MENU-----------")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5.Salir")


#opcion1
def asignar():
    for melon in trabajadores:
        info={}
        sueldo=random.randint(300000,2500000)
        info={'Nombre':melon,'Sueldo':sueldo,'Descuento Salud':int(sueldo*0.07),'Descuento Afp':int(sueldo*0.12),'Descuento Liquido':int(sueldo*0.81)}
        empleados.append(info)

#opcion2
def clasificar():
    total=0
    menor=[i for i in empleados if i['Sueldo']<=800000]
    mitad=[i for i in empleados if i['Sueldo']>800000 and i['Sueldo']<=2000000]
    mayor=[i for i in empleados if i['Sueldo']>2000000]
    print(f'Sueldos menores a $800.000 TOTAL: {len(menor)}')
    print('Nombre\t\tSueldo')
    for melon in menor:
        print(f'{melon['Nombre']}\t${melon['Sueldo']:,}')
    print(f'Sueldos entre $800.000 y $2.000.000 Total:{len(mitad)}')
    print('Nombre\t\tSueldo')
    for melon in mitad:
        print(f'{melon['Nombre']}\t${melon['Sueldo']:,}')
    print(f'Sueldos superiores a $2.000.000 TOTAL{len(mayor)}')
    print('Nombre\t\tSueldo')
    for melon in mayor:
        print(f'{melon['Nombre']}\t${melon['Sueldo']:,}')
    for melon in empleados:
        total+=melon['Sueldo']
    print(f'Total De Los Sueldos: ${total:,}')
    
    
#opcion3
def reporte():
    with open('Reporte De Sueldos.csv','w',newline='') as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(['Nombre empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Liquido'])
        for melon in empleados:
            escritor.writerow([melon['Nombre'],melon['Sueldo'],melon['Descuento Salud'],melon['Descuento Afp'],melon['Descuento Liquido']])

#opcion4
def estadistica():
    if not empleados:
        asignar()
    larga=max(empleados,key=lambda x: x['Sueldo'])
    corta=min(empleados,key=lambda x: x['Sueldo'])
    print(f'Sueldo mas alto {larga['Nombre']} con un sueldo de ${larga['Sueldo']:,}')
    print(f'Sueldo mas bajo {corta['Nombre']} con un sueldo de ${corta['Sueldo']:,}')
    total2=sum(melon['Sueldo'] for melon in empleados)
    total2=int(total2/10)
    print(f'El promedio de sueldos es de ${total2:,}')
while True:
    menu()
    try:
        op=int(input("Ingrese opcion\n"))
    except:
        print("opcion no valida")
    
    if op==1:
        asignar()
        print('Sueldos Establecidos!')
        time.sleep(2)
        
    elif op==2:
        print("Clasificando....")
        clasificar()
        time.sleep(2)
    elif op==3:
        print("Cargando reporte.....")
        time.sleep(2)
        reporte()
        print("Reporte cargado")
    elif op==4:
        
        estadistica()
        
    else:
        
        print("Finalizando programa.....")
        time.sleep(2)
        
        print('Desarrollado por Valentina Pino N')
        print('RUT 20.242.811-8')
        time.sleep(1)
        break
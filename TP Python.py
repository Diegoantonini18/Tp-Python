import operator
import csv
############# Funciones Administrador ######################


##Funcion registrar cliente



def registrocliente (dic_dni,dic_dnisinsaldo):
    lista_clientes=[]
    dni=int(input("\nIngrese el número de DNI: "))
    if dni in dic_dni:
        print("\nEl cliente ya se encuentra registrado")
    if dni not in dic_dni:
        nombre=input("Ingrese nombre: ")
        #mail=input("Ingrese mail: ")
        #tel=int(input("Ingrese nro de telefono: "))
        saldo=0
        compras=0
        pagos=0
        lista_clientes.append(nombre)
        lista_clientes.append(saldo)
        lista_clientes.append(compras)
        lista_clientes.append(pagos)
        dic_dni[dni]=lista_clientes
        dic_dnisinsaldo[dni]=lista_clientes[0:1]
    print("\nLista de clientes: ",dic_dnisinsaldo)
    

        
##Función agregar productos
def agregarproductos(dic_codigo,dic_reporte2,dic_reporte5,dic_aux,dic_agrupar):
    lista_productos=[]
    codprod=int(input("\nIngrese el código del producto: "))
    if codprod in dic_codigo:
        print("\nEl código del producto ya está registrado")
    if codprod not in dic_codigo:
        descriproducto=input("Ingrese una descripción del producto: ")
        lista_productos.append(descriproducto)
        importeproducto=float(input("Ingrese el importe del producto: "))
        lista_productos.append(importeproducto)
        dic_codigo[codprod]=lista_productos              
    return dic_codigo

## Función Emitir Reportes
        
        

def emitirreportes(dic_dni,dic_dnisinsaldo,dic_reporte2,dic_reporte5,dic_aux,dic_agrupar,dic_codigo,dic_pagos,dic_auxiliar,dic_reporte1):
    print("\n1_ Monto facturado")
    print("2_ Top 10 clientes facturados")
    print("3_ Medio de pago mas utilizado")
    print("4_ Deudores")
    print("5_ Productos mas vendidos")
    
    opx=int(input("\n¿Qué desea emitir? : "))
    if(opx==1):
        acumuladorreporte1=0
        listatotalreporte1=[]
        fechainferior1=int(input("\nIngrese la fecha inferior: "))
        fechasuperior1=int(input("Ingrese la fecha superior: "))
        for i in range(fechainferior1,fechasuperior1+1):
            if i in dic_reporte1:
                listareporte1=dic_reporte1.get(i)
                acumuladorreporte1=listareporte1+acumuladorreporte1
                listatotalreporte1.append(listareporte1)
        print("\nEl monto facturado entre las fechas",fechainferior1,"y",fechasuperior1,"es",acumuladorreporte1)
    if(opx==2):
        reporte2={}
        fechainferior3=int(input("\nIngrese la fecha inferior (AAAAMMDD): "))
        fechasuperior3=int(input("\nIngrese la fecha superior (AAAAMMDD): "))
        for z in range (fechainferior3,fechasuperior3+1):
            if z in dic_reporte2:
                icreporte2=dic_reporte2.get(z)
                for x in dic_auxiliar:                    
                    if x in reporte2:
                            rreporte=reporte2.get(x)
                            reporte=icreporte2.get(x)
                            if (reporte==None):
                                reporte2[x]=rreporte
                            if (reporte!=None):
                                reporte2[x]=reporte + rreporte
                    if x not in reporte2:
                        reporte=icreporte2.get(x)
                        reporte2[x]=reporte
                        if(reporte==None):
                            reporte2[x]=0
        
        resultado = sorted(reporte2.items(),key=operator.itemgetter(1))
        resultado.reverse()
        print("\nLos más facturados entre las fechas",fechainferior3,"y",fechasuperior3,"son: ",resultado)
    if(opx==3):
        if(dic_pagos[0]>=dic_pagos[1] and dic_pagos[0]>=dic_pagos[2]):
            print("\nEl medio de pago más utilizado es la tarjeta de crédito")
        if(dic_pagos[1]>=dic_pagos[0] and dic_pagos[1]>=dic_pagos[2]):
            print("\nEl medio de pago más utilizado es el pago facil")
        if(dic_pagos[2]>=dic_pagos[0] and dic_pagos[2]>=dic_pagos[1]):
            print("\nEl medio de pago más utilizado es la transferencia bancaria")
    if(opx==4):
        montodeuda=float(input("\nIngrese un monto: "))
        dicdeuda={}       
        for clave in dic_dni:
            listadeuda=[]
            listadeuda=dic_dni.get(clave)
            if(listadeuda[1]>=montodeuda):
                dicdeuda[clave]=listadeuda[0:2]
        print("\nLos clientes que tienen una deuda mayor o igual a:",montodeuda, "son: ",dicdeuda)
    if(opx==5):
        max=0
        max2=0
        dic_agrupar={}
        fechainferior2=int(input("Ingrese la fecha inferior(AAAAMMDD): "))
        fechasuperior2=int(input("Ingrese la fecha superior(AAAAMMDD): "))
        for i in range(fechainferior2,fechasuperior2+1):
            if i in dic_reporte5:
                dicreporte5=dic_reporte5.get(i)
                for l in range(0,100):
                    if l in dicreporte5:
                        if l in dic_agrupar:
                            lista5=dic_agrupar.get(l)
                            lista555=dicreporte5.get(l)
                            dic_agrupar[l]=lista555+lista5
                        if l not in dic_agrupar:
                            lista55=dicreporte5.get(l)
                            dic_agrupar[l]=lista55
        for a in range(0,100):
            if a in dic_agrupar:
                
                maxvenprod=dic_agrupar.get(a)
                if(maxvenprod>max):
                    max=maxvenprod
                    max2=a
                    tipovent=dic_codigo.get(a)
        print("\nEl producto más vendido entre las fechas",fechainferior2,"y",fechasuperior2,"fue",max2 and tipovent,"codigo:",max2,"con",max,"ventas")
#Funcion importar productos

def importarproductos(dic_codigo):
     
    with open("archivoo.csv","r") as csv_file:
        csv_reader=csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            if line[0] not in dic_codigo:
                lista_codigo=[]
                lista_codigo.append(line[1])
                lista_codigo.append(float(line[2]))
                dic_codigo[int(line[0])]=lista_codigo
        print("Los productos que importó son: ",dic_codigo)
    
###Funcion Exportar Información
    
def exportarinfo(dic_dni,dic_reporte5):
    print("\n1_ Listado de compras")
    print("2_ Saldo clientes")
    opr5=int(input("\n¿Qué desea exportar?: "))
    if(opr5==1):
        import csv
        m1=open("listadocompras.csv","w")
        m1_c=csv.writer(m1)
        l=[dic_reporte5]
        m1_c.writerow(l)
        m1.close()
        print("\nEl archivo ha sido exportado")
    if(opr5==2):
        import csv
        m2=open("saldoclientes.csv","w")
        m2_c=csv.writer(m2)
        l2=[dic_dni]
        m2_c.writerow(l2)
        m2.close()
        print("\nEl archivo ha sido exportado")



        



############## Funciones cliente #####################################
#Función registrar compra

def registrarcompra(dic_dnisinsaldo,dic_dni,dic_codigo,dic_auxiliar,dic_reporte5,dic_reporte2):
    dni2=int(input("\nIngrese su DNI: "))

    if dni2 in dic_dnisinsaldo:
        listasaldo=dic_dni.get(dni2)
        if(listasaldo[1]>500):
            print("\nSu saldo es insuficiente, debe realizar un pago para seguir con su compra")
        if(listasaldo[1]<=500):
            print("\nLa lista de productos es: ",dic_codigo)
            fechacompra=int(input("\nIngrese la fecha de hoy(AAAAMMDD): "))
            codcompra=int(input("\nIngrese el código del producto que desea comprar: "))       
                  
            if codcompra in dic_codigo:
                dic_auxiliar[dni2]=0
                dic_reporte5bis={}
                cantcompra=int(input("Ingrese la cantidad que desea comprar: "))
                eleccompra=dic_codigo.get(codcompra,[])
                preciopagar=eleccompra[1]*cantcompra
                listasaldo[1]=listasaldo[1]+preciopagar
                listasaldo[2]=listasaldo[2]+preciopagar
                
                if fechacompra in dic_reporte5:
                    dic_reporte5bis={}  
                    dic_reporte5bis=dic_reporte5.get(fechacompra)
                    if codcompra in dic_reporte5bis:
                        lista_reporte5bis=dic_reporte5bis.get(codcompra)
                        dic_reporte5bis[codcompra]=lista_reporte5bis+cantcompra
                    if codcompra not in dic_reporte5bis:
                        dic_reporte5bis.setdefault(codcompra,cantcompra)
                        dic_reporte5[fechacompra]=dic_reporte5bis
                if fechacompra not in dic_reporte5:
                    diccodcomprabis={codcompra:cantcompra}
                    dic_reporte5.setdefault(fechacompra,diccodcomprabis)
                        
                if fechacompra in dic_reporte2:
                    dic_reporte2bis={}  
                    dic_reporte2bis=dic_reporte2.get(fechacompra)
                    if dni2 not in dic_reporte2bis:
                        dic_reporte2bis.setdefault(dni2,preciopagar)
                        dic_reporte2[fechacompra]=dic_reporte2bis
                    if dni2 in dic_reporte2bis:
                        lista_reporte2bis=dic_reporte2bis.get(dni2)
                        dic_reporte2bis[dni2]=lista_reporte2bis+preciopagar
                if fechacompra not in dic_reporte2:
                    diccodcomprabis2={dni2:preciopagar}
                    dic_reporte2.setdefault(fechacompra,diccodcomprabis2)
                    
            if codcompra not in dic_codigo:
                print("\nEl código ingresado no pertenece a ningun producto")        
    if dni2 not in dic_dnisinsaldo:
        print("\n El DNI ingresado no se encuentra registrado")
        print("\n La lista de clientes es: ",dic_dnisinsaldo)                                   
    
        

### Funcion registrar pago


def registrarpago(dic_dnisinsaldo,dic_reporte1,dic_dni,dic_pagos):
    dni3=0
    dni3=int(input("\nIngrese su DNI: "))
    lista_dnipagos=[]
    if dni3 in dic_dnisinsaldo:
        lista_reporte1=[]
        importepago=float(input("Ingrese el importe: "))
        agregarfechapago=int(input("\nIngrese la fecha de pago (AAAAMMDD}): "))
        
        if agregarfechapago in dic_reporte1:
            fechapago1=dic_reporte1.get(agregarfechapago,[])
            fechapago2=fechapago1+importepago
            dic_reporte1[agregarfechapago]=fechapago2
        if agregarfechapago not in dic_reporte1:
            dic_reporte1[agregarfechapago]=importepago
        acreditarpago=dic_dni.get(dni3)
        acreditarpago[1]=acreditarpago[1]-importepago
        acreditarpago[3]=acreditarpago[3]+importepago
        lista_dnipagos.append(importepago)
        print("\n1_ Tarjeta de Crédito")
        print("2_ Pago Fácil")
        print("3_ Transferencia Bancaria")
        opmediopago=int(input("\nElija un medio de pago: "))
        if(opmediopago==1):
            dic_pagos[0]=dic_pagos[0]+1
        if(opmediopago==2):
           dic_pagos[1]=dic_pagos[1]+1
        if(opmediopago==3):
            dic_pagos[2]=dic_pagos[2]+1
           
    if dni3 not in dic_dnisinsaldo:
        print("\n El DNI ingresado no se encuentra registrado")
        print("\n La lista de clientes es: ",dic_dnisinsaldo)
        
    return(dic_pagos)

   
    
     
#################################### MENU ##############################################


### MENU PRINCIPAL
def menuprincipal():
    acumuladormediopago1=0
    acumuladormediopago2=0
    acumuladormediopago3=0
    acumuladorpagostotales=0
    dic_reporte1={}
    dic_reporte4={}
    dic_dni={}
    dic_dnisinsaldo={}
    dic_codigo={}
    dic_aux={}
    op=0
    listasaldo=[]
    dic_reporte5={}
    dic_reporte2={}
    dic_auxiliar={}
    dic_agrupar={}
    dic_pagos=[]
    dic_pagos.append(acumuladormediopago1)
    dic_pagos.append(acumuladormediopago2)
    dic_pagos.append(acumuladormediopago3)
 
    while (op!=3):
        print("\n1_ Modo Administrador")
        print("2_ Modo Cliente")
        print("3_ Salir")
        op=int(input("\n¿En qué modo desea ingresar? : "))
        if(op==1):
            menuadmin(dic_dni,dic_dnisinsaldo,dic_codigo,dic_reporte2,dic_reporte5,dic_aux,dic_agrupar,dic_pagos,dic_auxiliar,dic_reporte1)
        if(op==2):
            menucliente(dic_dni,dic_dnisinsaldo,dic_codigo,dic_auxiliar,dic_reporte5,dic_reporte2,dic_reporte1,dic_pagos)

        

## MENU ADMINISTRADOR
def  menuadmin(dic_dni,dic_dnisinsaldo,dic_codigo,dic_reporte2,dic_reporte5,dic_aux,dic_agrupar,dic_pagos,dic_auxiliar,dic_reporte1):
    op1=0
    while op1!=6:
        print("\n1_ Registrar cliente")
        print("2_ Agregar producto")
        print("3_ Emitir reportes")
        print("4_ Importar artículos")
        print("5_ Exportar información")
        print("6_ Volver al menu principal")
        op1=int(input("\n¿Qué desea realizar? : "))
        if(op1==1):
            registrocliente(dic_dni,dic_dnisinsaldo)
        if(op1==2):
##            dic_pagos = agregarproductos(dic_codigo)
            agregarproductos(dic_codigo,dic_reporte2,dic_reporte5,dic_aux,dic_agrupar)
        if(op1==3):
            emitirreportes(dic_dni,dic_dnisinsaldo,dic_reporte2,dic_reporte5,dic_aux,dic_agrupar,dic_codigo,dic_pagos,dic_auxiliar,dic_reporte1)
        if(op1==4):
            importarproductos(dic_codigo)
        if(op1==5):
            exportarinfo(dic_dni,dic_reporte5)

    
##MENU CLIENTE   
def menucliente(dic_dni,dic_dnisinsaldo,dic_codigo,dic_auxiliar,dic_reporte5,dic_reporte2,dic_reporte1,dic_pagos):
    op2=0
    while op2!=3:
        print("\n1_ Registrar compra")
        print("2_ Registrar pago")
        print("3_ Volver al menu principal")
        op2=int(input("\n¿Qué desea realizar? : "))
        if(op2==1):
            registrarcompra(dic_dnisinsaldo,dic_dni,dic_codigo,dic_auxiliar,dic_reporte5,dic_reporte2)
        if(op2==2):
            registrarpago(dic_dnisinsaldo,dic_reporte1,dic_dni,dic_pagos)
       
    
    
########################################################    PROGRAMA PRINCIPAL  ##############################################################################   
print("\nMini Supermercado Online")
menuprincipal()

    
    
    
    






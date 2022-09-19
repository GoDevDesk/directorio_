import sqlite3
from tkinter import *
from tabulate import tabulate
import tkinter_interfaz

link = sqlite3.connect("directorio_vital.db")
cursorsql = link.cursor()

diccionar_sucursales ={
"Administracion Central": 200,
"San Justo":203,
"Burzaco":202,
"Moreno":206, 
"Laferrere":201,
"Malvinas":207,
"Tronador":208,
"Abasto":204,
"Quilmes":209, 
"La Plata": 213,
"Loma Hermosa": 214,
"El Talar":215,
"Avellaneda":216,
"Posadas":217,
"Resistencia":218,
"Neuquen":219,
"Santa Fe":220,
"Mar del Plata":221,
"Bahia Blanca":222, 
"Pilar": 223, 
"Salta": 224,      
"Call Center":1500 
}
                        
diccionar_sectores ={
"RRHH":1,
"Seguridad":2,
"Gerencia":3,
"Creditos":4,
"Rac":5,
"Directorio":6,
"Expedicion":7,
"Control":8,
"Cajas":9, 
"Deposito":10,       
"Fiambreria":11, 
"Precios":12, 
"Facturacion":13,
"Kiosco":14,
"Computos":15, 
"Fax Recepcion":16,       #######HASTA ACA SON SECTORES DE SUCURSALES#######
"Auditoria y Procesos":19,
"Comercio Exterior":20,
"Compras":21,
"Compras - Ventas":22,
"Compras Internas":23,
"Contabilidad":24,
"Control de Gestion":25,
"Cuentas a Pagar":27,
"Finanzas":28,
"Legales":29,
"Mesa de trafico":30,
"Mantenimiento":32,
"Marketing":33,
"Operaciones":34,
"Pagos":35,
"Recursos Humanos":36,
"Sistemas":37,
"Stock":47,
"Ventas":48,}  


class consultas(): 

    def consultaSinNombre(suc, sec):
        print(diccionar_sectores[sec])
        sql_consultar = str("select usuario_nombre,puesto,interno,email from Usuarios where suc_id= ? and sector_id = ?;")
        sucursal_sector = (diccionar_sucursales[suc],diccionar_sectores[sec])
        cursorsql.execute(sql_consultar, sucursal_sector, )
        filas = cursorsql.fetchall()
        print(suc,",",sec)
        print(tabulate(filas,headers=['Nombre ', 'Puesto', 'Interno', 'E-mail'],tablefmt='fancy_grid',stralign='center',))
        print("----" * 20)
        for n in filas:
            var1 = n[0]
            var2 = n[1]
            var3 = diccionar_sucursales[suc],n[2]
            var4 = n[3]
            
            tkinter_interfaz.insertarValoresEnTablas(var1,var2,var3,var4)
        print()
        link.commit()

    def consultaConNombre(suc, sec, nombre):      
        
        print (suc)
        #####################CONSULTA USUARIO######################
        sql_consultar = str("select usuario_nombre,puesto,interno,email from Usuarios where usuario_nombre ='"+nombre+"' AND suc_id = '"+str(diccionar_sucursales[suc])+"';")
        
        cursorsql.execute(sql_consultar)
        filas = cursorsql.fetchall()
        print(suc, ",", sec)
        print("----" * 20)
        print(tabulate(filas, headers=['Nombre ', 'Puesto', 'Interno', 'E-mail'],tablefmt='fancy_grid',stralign='center'))
        print("----" * 20)
        for n in filas:
            var1 = n[0]
            var2 = n[1]
            var3 = diccionar_sucursales[suc],n[2]
            var4 = n[3]            
            print(var1, var2, var3, var4)
            tkinter_interfaz.insertarValoresEnTablas(var1,var2,var3,var4)
        link.commit()
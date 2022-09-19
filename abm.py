from itertools import count
from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter_interfaz
import app
link = sqlite3.connect("directorio_vital.db")
cursorsql = link.cursor()

#=============================INTERFAZ GRAFICA ABM==========================================#
class abm_interfaz:

    def creacionVentanaAbm():
        global root2
        root2 = Tk()
        root2.title("ABM")
        root2.geometry("480x180+800+300") 
        root2.state("normal") 
        root2.eval('tk::PlaceWindow . root')


        #root.resizable(0, 0)
        frameAbm1 = Frame(root2,height=200,width=200,pady=30,padx=20)
        #frameAbm1.grid_propagate(False)
        frameAbm1.grid(column=1)


        ##---------------BOTONES PRIMARIOS ---------------------------#
        botonAlta = Button(frameAbm1, text="ALTA",width=12, height=3,command=abm_usuario.registrandoUsuario)
        botonAlta.grid(column=1,row=2, padx=15, pady=20)
        botonAlta.config(font="HELVETICA")

        botonBaja = Button(frameAbm1, text="BAJA",width=12, height=3,command=abm_usuario.bajaUsuario)
        botonBaja.grid(column=2,row=2, padx=15, pady=20)
        botonBaja.config(font="HELVETICA")


        botonModif = Button(frameAbm1, text="MODIFICACION",width=12, height=3,command=abm_interfaz.botonPrimarioModificacion)
        botonModif.grid(column=3,row=2, padx=15, pady=20)
        botonModif.config(font="HELVETICA")       

        root2.mainloop()
    

    def volverABM():
        ventanaRegistro.state("withdraw")
        abm_interfaz.creacionVentanaAbm()
      

    def botonPrimarioBaja():
        root2.state("withdraw")
        global ventana
        ventana = Toplevel()
        #bajasVentana.geometry("300x100")
        ventana.title("Ventana 2")
        ventana.state("normal")

        
    def botonPrimarioModificacion():
        root2.state("withdraw")
        global ventana
        ventana = Toplevel()
        ventana.title("Ventana 2")
        ventana.state("normal")

    
#=========================================ALTA BAJA Y MODIFICACION DE USUARIOS ================================================#

class abm_usuario:       


 ##############======================GENERACION DE PANEL PARA LA CREACION DEL USUARIO==================##################   
    def registrandoUsuario():   
            root2.state("withdraw")   
            global ventanaRegistro         
            ventanaRegistro = Toplevel(padx=15,pady=5)
            ventanaRegistro.geometry("+800+300")
            ventanaRegistro.title("Registro de usuario")
            ventanaRegistro.state("normal")

            # etiqueta sucursal
            sector_label = Label(ventanaRegistro, text="Sucursal")
            sector_label.grid(row=1, column=0, pady=10)
            sector_label.config(font="helvetica")

            # menu desplegable sucursal
            data_entry_suc = StringVar()
            suc_combo = ttk.Combobox(ventanaRegistro, value=tkinter_interfaz.opciones_suc, textvariable=data_entry_suc, width=20, state="readonly")
            suc_combo.grid(row=1, column=1)
            suc_combo.config(font="helvetica")
            suc_combo.bind("<<ComboboxSelected>>",abm_usuario.generarOpcionesSector)

            # etiqueta sector
            sector_label = Label(ventanaRegistro, text="Sector")
            sector_label.grid(row=2, column=0, padx=5, pady=10)
            sector_label.config(font="helvetica")


            ###########       el combobox sector se genera a cuando se escoje sucursal    linea 41       #####################

            # etiqueta nombre o legajo
            global dato_entrada_nombre
            nombre_label = Label(ventanaRegistro, text="Nombre y apellido")
            nombre_label.grid(row=3, column=0, padx=10, pady=10)
            nombre_label.config(font="helvetica")        
            dato_entrada_nombre = Entry(ventanaRegistro, width=33)
            dato_entrada_nombre.grid(row=3, column=1)   

            ###### ====================email=====================#########
            global dato_entrada_email
            email_label = Label(ventanaRegistro, text="Email corporativo")
            email_label.grid(row=4, column=0, padx=10, pady=10)
            email_label.config(font="helvetica")        
            dato_entrada_email = Entry(ventanaRegistro, width=33)
            dato_entrada_email.grid(row=4, column=1)             


            #################puesto##################
            global puesto_entrada              
            puesto_label = Label(ventanaRegistro, text="Puesto")
            puesto_label.grid(row=5, column=0, padx=10, pady=10)
            puesto_label.config(font="helvetica")            
            puesto_entrada = Entry(ventanaRegistro, width=33)
            puesto_entrada.grid(row=5, column=1) 
             
             
            # etiqueta interno
            global dato_entrada_interno
            interno_label = Label(ventanaRegistro, text="Interno")
            interno_label.grid(row=6, column=0, padx=10, pady=10)
            nombre_label.config(font="helvetica")                  
            dato_entrada_interno = Spinbox(ventanaRegistro,from_=200, to=600, width=5)
            dato_entrada_interno.grid(row=6, column=1)   


            #==========boton para volver para atras===============================#
            botonVolver = Button(ventanaRegistro, text="VOLVER",width=6, height=1,command=abm_interfaz.volverABM)
            botonVolver.grid(column=0,row=8, padx=5, pady=5)



#=========================INSERT NUEVO USUARIO A LA BASE DE DATOS=====================================#
    def insertUsuario():
        nombre = str(dato_entrada_nombre.get())
        suc = app.diccionar_sucursales[suc_combo]
        sec = app.diccionar_sectores[sec_combo]
        puesto = puesto_entrada.get()
        email = dato_entrada_email.get()
        spinbox = str(dato_entrada_interno.get())
        

        ####comprobacion del mail######
        sql_consultar = str("select email from Usuarios where email= '"+email+"';")        
        cursorsql.execute(sql_consultar,)
        comparandoEmail = cursorsql.fetchone()
        print (comparandoEmail)

        sql_consultar = str("select interno from Usuarios where interno= '"+spinbox+"';")        
        cursorsql.execute(sql_consultar,)
        comparandoInterno = cursorsql.fetchone()
        
        
        ## VERIFICAR SI ESTAN TODOS LOS CAMPOS COMPLETOS ##
        if email and puesto and nombre:
        ##COMPARAR SI EL MAIL YA EXISTIA##
            if comparandoEmail:                 
                negativa = Label(ventanaRegistro, text="    El email ya existe asociado a otro usuario    ",fg="red")
                negativa.grid(row=9, column=2, padx=10, pady=10)
        ##COMPARA SI YA EXISTE EL INTERNO##    
            elif comparandoInterno:
                print(comparandoInterno)
                negativa = Label(ventanaRegistro, text="    El interno  ya existe asociado a otro usuario    ",fg="red")
                negativa.grid(row=9, column=2, padx=10, pady=10)
            else:                    
                try:
                    print("estoy en el try")
                    print(type(puesto))
                    sql_insertar = str("insert into Usuarios (suc_id, usuario_nombre, puesto,interno,email,sector_id) values (?,?,?,?,?,?);")
                    datos_query = (suc,nombre,puesto,spinbox,email,sec)        
                    cursorsql.execute(sql_insertar, datos_query)               
                    link.commit()
                    confirmacion = Label(ventanaRegistro, text="                        Usuario generado                        ",fg="green")
                    confirmacion.grid(row=9, column=2, padx=10, pady=10)
                    print("Operacion ok")
                except sqlite3.OperationalError:        
                    print("Ocurrio un problema")            
        else:
            print("falta mail nombre y puesto")
            negativa = Label(ventanaRegistro, text="Debe proporcionar nombre,email y puesto",fg="red")
            negativa.grid(row=9, column=2, padx=10, pady=10)


#================= combobox sector =====================================================================#
    def generarOpcionesSector(event):
            global suc_combo
            suc_combo = event.widget.get()
            if suc_combo == "Administracion Central":
                valor = tkinter_interfaz.opciones_sec_admCentral
                data_entry_sec = StringVar()
                sec_combo = ttk.Combobox(ventanaRegistro, values=valor, textvariable=data_entry_sec, width=20, state="readonly")
                sec_combo.grid(row=2, column=1)
                sec_combo.config(font="helvetica")
                sec_combo.bind("<<ComboboxSelected>>",abm_usuario.seleccionSector)                
                interno_label = Label(ventanaRegistro, text=app.diccionar_sucursales[suc_combo])
                interno_label.grid(row=6, column=1, pady=10,sticky="w")                       
                


            else:
                valor =tkinter_interfaz.opciones_sec_sucursal
                data_entry_sec = StringVar()
                sec_combo = ttk.Combobox(ventanaRegistro, values=valor, textvariable=data_entry_sec, width=20, state="readonly")
                sec_combo.grid(row=2, column=1)
                sec_combo.config(font="helvetica")  
                interno_label = Label(ventanaRegistro, text=app.diccionar_sucursales[suc_combo])
                interno_label.grid(row=6, column=1, pady=10,sticky="w")  
                sec_combo.bind("<<ComboboxSelected>>",abm_usuario.seleccionSector)


    def seleccionSector(event):
        global sec_combo
        sec_combo = event.widget.get()
        # boton buscar
        boton_buscar = Button(ventanaRegistro,text="GENERAR USUARIO",command=abm_usuario.insertUsuario)
        boton_buscar.grid(column=2,row=8)     

            


    def bajaUsuario():          
            root2.state("withdraw")   
            global ventanaRegistro         
            ventanaRegistro = Toplevel(padx=7,pady=5)
            ventanaRegistro.geometry("+800+300")
            ventanaRegistro.title("Baja de usuario")
            ventanaRegistro.state("normal")

            
            instruccion_label = Label(ventanaRegistro, text="Busque al usuario para realizar la baja")
            instruccion_label.grid(row=0, column=1, padx=10, pady=10)
            instruccion_label.config(font="helvetica")       
            

            # etiqueta nombre o legajo
            global dato_entrada_nombre
            nombre_label = Label(ventanaRegistro, text="Nombre y apellido")
            nombre_label.grid(row=3, column=0, padx=10, pady=10)
            nombre_label.config(font="helvetica")        
            dato_entrada_nombre = Entry(ventanaRegistro, width=33)
            dato_entrada_nombre.grid(row=3, column=1)   

           
            # boton buscar
            boton_buscar = Button(ventanaRegistro,text="BUSCAR",command=abm_usuario.busquedaParaBaja)
            boton_buscar.grid(column=2,row=8)           
             

            #==========boton para volver para atras===============================#
            botonVolver = Button(ventanaRegistro, text="VOLVER",width=6, height=1,command=abm_interfaz.volverABM)
            botonVolver.grid(column=0,row=8, padx=5, pady=5)
            
    
    def busquedaParaBaja():
        nombreParaBaja = dato_entrada_nombre.get()
        ####busqueda por nombre######
        sql_consultar = str("select usuario_id, puesto from Usuarios where usuario_nombre= '"+nombreParaBaja+"';")        
        cursorsql.execute(sql_consultar,)        
        filas = cursorsql.fetchall()
        for n in filas:
            var1 = n[0]
            var2 = n[1]
        print (var1,var2)
        negativa = Label(ventanaRegistro, text=(nombreParaBaja,var1,var2),fg="green")
        negativa.grid(row=9, column=2, padx=10, pady=10)
    
    
    #def modificacionUsuario():


from tkinter import *
from tkinter import ttk
from app import *
from abm import * 


#############################################

root = Tk()
root.geometry("+800+300")
root.title("Busqueda Vital")
root.resizable(0, 0)


# frame contenedor1

miFrame = Frame(root)
miFrame.grid(row=0, column=0,sticky=W)

# --------------------frame contenedor2--------------------------------------
miFrame2 = Frame(root,padx=10,pady=5)
miFrame2.grid(row=1)
valor = None

# -----
# opciones desplegables
opciones_suc = (
"Administracion Central",
"San Justo",
"Burzaco",
"Moreno",
"Laferrere",   
"Malvinas",
"Tronador",
"Abasto",
"Quilmes",      
"La Plata",
"Loma Hermosa",
"El Talar",
"Avellaneda",
"Posadas",
"Resistencia",
"Neuquen",
"Santa Fe",
"Mar del Plata",   
"Bahia Blanca",
"Pilar",
"Salta",
"Call Center")

opciones_sec_admCentral = (
"Auditoria y Procesos",
"Comercio Exterior",
"Compras",
"Compras - Ventas",
"Compras Internas",
"Contabilidad",
"Control de Gestion",
"Créditos",
"Cuentas a Pagar",
"Finanzas",
"Legales",
"Mesa de trafico",
"Mantenimiento",
"Marketing",
"Operaciones",
"Pagos",
"Recursos Humanos",
"Sistemas",
"Stock",
"Ventas"
)

opciones_sec_sucursal = (
"RRHH",
"Seguridad", 
"Gerencia",
"Creditos",
"Rac", 
"Directorio",
"Expedicion",
"Control", 
"Cajas", 
"Deposito",     
"Fiambreria",
"Precios", 
"Especificos",
"Facturacion",
"Seguridad",
"Kiosco", 
"Computos",
"Fax Recepcion"
)
# ----


##============================================FUNCIONES GRAFICAS==================================================##

def limpiadores():
    
    def limpiar():
        for i in tablas.get_children():
            tablas.delete(i)             

    limpiar()
    

#########FUNCION QUE CAMBIA VALORES DEL COMBOBOX SECTOR #######################

def generarOpcionesSector(event):
    suc_combo = event.widget.get()
    if suc_combo == "Administracion Central":
        valor = opciones_sec_admCentral
        data_entry_sec = StringVar()
        sec_combo = ttk.Combobox(miFrame, values=valor, textvariable=data_entry_sec, width=20, state="readonly")
        sec_combo.grid(row=1, column=1)
        sec_combo.config(font="helvetica")
        sec_combo.bind("<<ComboboxSelected>>", seleccionSector)

    else:
        valor = opciones_sec_sucursal
        data_entry_sec = StringVar()
        sec_combo = ttk.Combobox(miFrame, values=valor, textvariable=data_entry_sec, width=20, state="readonly")
        sec_combo.grid(row=1, column=1)
        sec_combo.config(font="helvetica")
        sec_combo.bind("<<ComboboxSelected>>", seleccionSector)

###########Comprueba si hay un data entry o no######
def comprobacion1():
    
    if dato_entrada.get():
        
        consultas.consultaConNombre(data_entry_suc.get(),sec_combo,dato_entrada.get())      
        
    else:
        consultas.consultaSinNombre(data_entry_suc.get(),sec_combo)

##############Toma la seleccion del comboBox sector###################
def seleccionSector(event):
    global sec_combo
    sec_combo = event.widget.get()
    # boton buscar
    boton_buscar = Button(miFrame, text="BUSCAR", command=comprobacion1)
    boton_buscar.grid(row=3, column=2, padx=10, )




# ------------------------------miframe---------------------------------------------- #


# etiqueta sucursal
sector_label = Label(miFrame, text="Sucursal")
sector_label.grid(row=0, column=0, pady=10)
sector_label.config(font="helvetica")

# menu desplegable sucursal
data_entry_suc = StringVar()
suc_combo = ttk.Combobox(miFrame, value=opciones_suc, textvariable=data_entry_suc, width=20, state="readonly")
suc_combo.grid(row=0, column=1)
suc_combo.config(font="helvetica")
suc_combo.bind("<<ComboboxSelected>>", generarOpcionesSector)


# etiqueta sector

sector_label = Label(miFrame, text="Sector")
sector_label.grid(row=1, column=0, padx=5, pady=10)
sector_label.config(font="helvetica")

###########       el combobox sector se genera a cuando se escoje sucursal    linea 41       #####################


# etiqueta nombre o legajo
nombre_label = Label(miFrame, text="Nombre ")
nombre_label.grid(row=3, column=0, padx=10, pady=10)
nombre_label.config(font="helvetica")

# entry ingrese nombre o legajo
dato_entrada = Entry(miFrame, width=33)
dato_entrada.grid(row=3, column=1)




# --------------miframe2----------------------------------------------    
    
#----------------------------------------------------------------------
 ############TABLA PRINCIPAL TREEVIEW##########################


tablas = ttk.Treeview(miFrame2,height = 10, columns = ('Nombre','Puesto','Interno','Email'),show="headings")
tablas.grid(row=0, column=0,columnspan=1)
scrollbar = Scrollbar(miFrame2, orient=VERTICAL, command=tablas.yview)
scrollbar.grid(column=4,row=0,sticky=NS)
tablas.configure(yscroll=scrollbar.set)
tablas.heading(0,text="Nombre")
tablas.heading(1,text="Puesto")
tablas.heading(2,text="Interno")
tablas.heading(3,text="Email")
tablas.column("Nombre",stretch=NO, anchor=CENTER)
tablas.column("Puesto",stretch=NO, anchor=CENTER)
tablas.column("Interno",stretch=NO, anchor=CENTER)
tablas.column("Email",stretch=NO, anchor=CENTER)



#

##############BOTON LIMPIAR##############
boton_limpiar = Button(miFrame, text="LIMPIAR", command=limpiadores)
boton_limpiar.grid(row=3, column=3, padx=10, )


######################funciones de las tablas#################################

def insertarValoresEnTablas(var1,var2,var3,var4):
    tablas.insert("", 'end',values=(var1, var2, var3, var4))



##########################BOTON ABM#################################################


boton_abm = Button(miFrame2, text="ABM",command=abm_interfaz.creacionVentanaAbm,padx=7,pady=5)
boton_abm.config(width=8, height=1)
boton_abm.grid(row=1, column=0, sticky="w", pady=4)
# ----------------------------------------------------------------
root.mainloop()
from tkinter import *
from tkinter import messagebox

#--------------------funciones-----------------------------------------
def conectarBBDD():
    try:
        #creo el archivo donde se alojara la base de datos
        miConexion=sqlite3.connect('Registro Personas')
        #creo el cursor de la base de datos
        miCursor=miConexion.cursor()
        #creo la base de datos
        miCursor.execute('''
            CREATE TABLE tablaPersonas(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre      VARCHAR(10),
                Apellido    VARCHAR(10),
                PASSWORD    VARCHAR(10),
                DIRECCION   VARCHAR(20),
                COMENTARIOS VARCHAR (100)
            )
        ''')
        #cerrar archivo
        miConexion.close()
        messagebox.showinfo('BBDD','BBDD creada con exito')
    except:
        messagebox.showwarning('¡Atencion!','La base de datos ya fue creada')
    pass

def createBoton():
    print('create')
    #nombreRecojo=nombre.get()
    #apellidoRecojo=apellido.get()
    #passwordRecojo=password.get()
    #direccionRecojo=direccion.get()
    #abro el archivo donde se alojara la base de datos
    miConexion=sqlite3.connect('Registro Personas')
    #creo el cursor de la base de datos
    miCursor=miConexion.cursor()
    #insertar registro en la base de datos
    #recojo cada uno de los datos de la persona
    Persona=[
        (
            nombre.get(),
            apellido.get(),
            password.get(),
            direccion.get(),
            Comentarioscuadro.get(1.0, "end")
        )
    ]
    #necesito insertarlo en la base de datos
    #utilizo executemany para insertar los registros de la lista a la tabla
    miCursor.executemany('INSERT INTO tablaPersonas VALUES(NULL,?,?,?,?,?)',Persona)
    #verifico el cambio
    miConexion.commit()
    #cerrar archivo
    miConexion.close()
    nombreRecojo=nombre.set('')
    apellidoRecojo=apellido.set('')
    passwordRecojo=password.set('')
    direccionRecojo=direccion.set('')
    Comentarioscuadro.delete(1.0,END)#punto de partida y punto final
    messagebox.showinfo('usuario creado con exito con exito')
    pass

def readBoton():
    print('read')
    #abro el archivo donde se alojara la base de datos
    miConexion=sqlite3.connect('Registro Personas')
    #creo el cursor de la base de datos
    miCursor=miConexion.cursor()
    #recupero los datos de la tabla
    miCursor.execute('SELECT * FROM tablaPersonas WHERE ID=' + id.get())
    #lo almaceno en una variable para poder leerlo
    recuperoPersona=miCursor.fetchall()
    for i in recuperoPersona:
        #print(i)
        id.set(i[0])
        nombre.set(i[1])
        apellido.set(i[2])
        password.set(i[3])
        direccion.set(i[4])
        Comentarioscuadro.insert(1.0,i[5])
    #verifico el cambio
    miConexion.commit()
    #cerrar archivo
    miConexion.close()
    pass

def updateBoton():
    print('update')
    #abro el archivo donde se alojara la base de datos
    miConexion=sqlite3.connect('Registro Personas')
    #creo el cursor de la base de datos
    miCursor=miConexion.cursor()
    #actualizo
    miCursor.execute("UPDATE tablaPersonas SET Nombre='"+nombre.get()+
        "',Apellido='"+apellido.get()+
        "',PASSWORD='"+password.get()+
        "',DIRECCION='"+direccion.get()+
        "',COMENTARIOS='"+Comentarioscuadro.get('1.0',END)+
        "'WHERE ID="+ id.get())
    #verifico el cambio
    miConexion.commit()
    #cerrar archivo
    miConexion.close()
    nombreRecojo=nombre.set('')
    apellidoRecojo=apellido.set('')
    passwordRecojo=password.set('')
    direccionRecojo=direccion.set('')
    Comentarioscuadro.delete(1.0,END)#punto de partida y punto final
    messagebox.showinfo('usuario actualizado con exito')
    pass

def deleteBoton():
    print('delete')
    #abro el archivo donde se alojara la base de datos
    miConexion=sqlite3.connect('Registro Personas')
    #creo el cursor de la base de datos
    miCursor=miConexion.cursor()
    #apunto al ID para eliminarID
    miCursor.execute('DELETE FROM tablaPersonas WHERE ID=' + id.get())
    #verifico el cambio
    miConexion.commit()
    #cerrar archivo
    miConexion.close()
    messagebox.showinfo('usuario eliminado con exito')
    pass

def salirBoton():
    print('salir')
    salir=messagebox.askquestion('atencion','esta apunto de salir de la app')
    if(salir=='yes'):
        raiz.destroy()
    pass

def cleanAll():
    print('limpiar todo')
    nombreRecojo=nombre.set('')
    apellidoRecojo=apellido.set('')
    passwordRecojo=password.set('')
    direccionRecojo=direccion.set('')
    Comentarioscuadro.delete(1.0,END)#punto de partida y punto final
    pass

#-------------------------------interfaz-------------------------------------

raiz=Tk()#raiz con la clase TK()
raiz.title('Intrfaz grafica')

#creo una caja que contendra todos los elementos (caja padre)
barraMenu=Menu(raiz)#creo el menu
raiz.config(menu=barraMenu)

#--------------creacion de elemento del menu (subcajas) (cajas madres)----------

archivoMenu1=Menu(barraMenu, tearoff=0)#elemento empatetado dentro de la caja menu
barraMenu.add_cascade(label='BBCD', menu=archivoMenu1)#agregar texto al elemento creado

archivoMenu2=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='Delete', menu=archivoMenu2)

archivoMenu3=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='CRUD', menu=archivoMenu3)

archivoMenu4=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='Help', menu=archivoMenu4)

#-------------------crear submenus (subcajas) (cajas hijos)---------------------
archivoMenu1.add_command(label='conectar',command=conectarBBDD)
archivoMenu1.add_command(label='salir', command=salirBoton)

archivoMenu2.add_command(label='Borrar Campos',command=cleanAll)

archivoMenu3.add_command(label='Create',command=createBoton)
archivoMenu3.add_command(label='Read',command=readBoton)
archivoMenu3.add_command(label='Update',command=updateBoton)
archivoMenu3.add_command(label='Delete',command=deleteBoton)

archivoMenu4.add_command(label='Licencia')
archivoMenu4.add_command(label='Acerca de...')

#-------------------------------Frame1--------------------------------------
miFrame=Frame()
#miFrame.config(bg='red')
miFrame.config(width=350,height=450)

miFrame.pack()#se empaquete en la raiz

#-------------------------------Labels------------------------------------
#miLabel=Label(miFrame,text='hola mundo').pack()
Id=Label(miFrame,text='ID')
Id.grid(row=0,column=0,sticky='e',padx=10,pady=10)

Nombre=Label(miFrame,text='Nombre')
Nombre.grid(row=1,column=0,sticky='e',padx=10,pady=10)

Apellido=Label(miFrame,text='Apellido')
Apellido.grid(row=2,column=0,sticky='e',padx=10,pady=10)

Password=Label(miFrame,text='Password')
Password.grid(row=3,column=0,sticky='e',padx=10,pady=10)

Direccion=Label(miFrame,text='Direccion')
Direccion.grid(row=4,column=0,sticky='e',padx=10,pady=10)

Comentarios=Label(miFrame,text='Comentarios')
Comentarios.grid(row=5,column=0,sticky='e',padx=5,pady=5)


#------------------------------------Entrys----------------------------------
#necesito recoger los valores de cada uno de los Entry para crear la funciones de limpiar los campos
id=StringVar()
nombre=StringVar()
apellido=StringVar()
password=StringVar()
direccion=StringVar()

Idcuadro=Entry(miFrame, textvariable=id)
Idcuadro.grid(row=0,column=1,sticky='w',padx=10,pady=10)

Nombrecuadro=Entry(miFrame, textvariable=nombre)
Nombrecuadro.grid(row=1,column=1,sticky='w',padx=10,pady=10)

Apellidocuadro=Entry(miFrame, textvariable=apellido)
Apellidocuadro.grid(row=2,column=1,sticky='w',padx=10,pady=10)

Passwordcuadro=Entry(miFrame, textvariable=password)
Passwordcuadro.grid(row=3,column=1,sticky='w',padx=10,pady=10)

Direccioncuadro=Entry(miFrame, textvariable=direccion)
Direccioncuadro.grid(row=4,column=1,sticky='w',padx=10,pady=10)

#------------------------------cuadro de texto---------------------------------
Comentarioscuadro=Text(miFrame, width=15,height=5)
Comentarioscuadro.grid(row=5,column=1,sticky='e',padx=10,pady=5)
ScrollVert=Scrollbar(miFrame,command=Comentarioscuadro.yview)
ScrollVert.grid(row=5,column=2,sticky='nsew')
Comentarioscuadro.config(yscrollcommand=ScrollVert.set)

#-----------------Frame2-------------------------------------------------
miFrame2=Frame()
miFrame2.pack()

#------------------botones-------------------
botonCreate=Button(miFrame2,text='Create',command=createBoton)
botonCreate.grid(row=6,column=0,padx=5,pady=5)

botonRead=Button(miFrame2,text='Read',command=readBoton)
botonRead.grid(row=6,column=1,padx=5,pady=5)

botonUpdate=Button(miFrame2,text='Update',command=updateBoton)
botonUpdate.grid(row=6,column=2,padx=5,pady=5)

botonDelete=Button(miFrame2,text='Delete',command=deleteBoton)
botonDelete.grid(row=6,column=3,padx=5,pady=5)


raiz.mainloop()

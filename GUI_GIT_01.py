from GUI_05 import *
from tkinter import *

#--------------------funciones-----------------------------------------
def conectarBBDD():
    try:
        messagebox.showinfo('BBDD','BBDD creada con exito')
    except:
        messagebox.showwarning('¡Atencion!','La base de datos ya fue creada')
    pass

def createBoton():
    print('create')
    pass

def readBoton():
    print('read')
    pass

def updateBoton():
    print('update')
    pass

def deleteBoton():
    print('delete')
    pass

def salirBoton():
    print('salir')
    pass

def cleanAll():
    print('limpiar todo')
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
'''
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

'''

raiz.mainloop()

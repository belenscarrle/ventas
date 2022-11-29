from tkinter import *
from tkinter import ttk


    

class Ventana(Frame):
       
    def __init__(self, master=None):
        super().__init__(master,width=240, height=260)
        self.master = master
        self.pack()
        self.create_widgets()
        
    def fNuevo(self):         
        pass
    
    def fGuardar(self):        
        pass
                 
    def fModificar(self):        
        pass
    
    def fEliminar(self):
        pass

    def fCancelar(self):
        pass

    def create_widgets(self):
        frame1 = Frame(self,bg="#FFFFFF")
        frame1.place(x=0,y=0,width=93, height=259)        
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevo, bg="red", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="red", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="red", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)        
        frame2 = Frame(self,bg="#FFFFFF")
        frame2.place(x=95,y=0,width=150, height=259)                                      
        lbl2 = Label(frame2,text="Nombre producto ")
        lbl2.place(x=3,y=55)        
        self.txtName=Entry(frame2)
        self.txtName.place(x=3,y=75,width=100, height=20)        
        lbl3 = Label(frame2,text="Stock:")
        lbl3.place(x=3,y=105)        
        self.txtProducto=Entry(frame2)
        self.txtProducto.place(x=3,y=125,width=100, height=20)                
        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10,y=210,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=210,width=60, height=30)               


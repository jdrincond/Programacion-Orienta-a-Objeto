#Proyecto final
#Desarrollar una aplicación visual con la librería tkinter que permita implementar los algoritmos 
#de carga de artículos, consulta por código y listado completo, esto debe estar integrado con Mysql
#para almacenar los datos.

#Importar librerías necesarias
import tkinter as tk                    #Librería para crear la interfaz gráfica
from tkinter import ttk                 #Librería para crear widgets de interfaz gráfica
from tkinter import messagebox as mb    #Librería para mostrar mensajes emergentes
from tkinter import scrolledtext as st  #Librería para crear un área de texto desplazable
import articulos                        #Importar el módulo articulos.py que contiene la clase Articulo y sus métodos

#Crear la clase principal de la aplicación
class FormulariosArticulos:
    def __init__(self):
        self.articulo1 = articulos.Articulos()
        self.ventana1-tk.Tk()
        self.ventanal.title("Formulario de artículos")
        self.cuaderno1-ttk.Notebook(self.ventanal)
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.cuaderno1.grid(column=9, row=0, padx=10, pady=10)
        self.ventana1.mainloop()
        
    def carga_articulos(self):
        self.paginal=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.paginal, text="Carga de artículos")
        self.LabelFrame1-ttk.LabelFrame(self.paginal, text="Artículos")
        self.LabelFrame1.grid(column=0, row=0, padx=5, pady=10)
        self.label1-ttk.Label(self.LabelFramel, text="Descripcion: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.LabelFramel, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2-ttk.Label(self.LabelFramel, text="Precio: ")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)     
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.LabelFramel, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
        self.boton1-ttk.Button(self.LabelFramel, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4) # boton para confirmar la carga

    def agregar (self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Informacion", "Los datos fueron cargados correctamente")
        self.descripcioncarga.set("")
        self.preciocarga.set("")       
    
    def consulta_por_codigo(self):
        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Articulo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=0)
        self.label1=ttk.Label(self.labelframe2, text="Código: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Descripción: ")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Precio: ")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=0, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), ) 
        respuesta=self.articulo1.consulta (datos)
        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:            
            self.descripcion.set("")
            self.precio.set("") 
            mb.showinfo("Informacion", "No exite un articulo con dicho código")

    def listado_completo (self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Articulo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1-st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete(1.0, tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "codigo:"+str(fila[0])+"\ndescripcion:"+str(fila[1])+"\nprecio:"+str(fila[2])+"\n\n")

aplicacion1=FormulariosArticulos() #Crear una instancia de la clase FormulariosArticulos para ejecutar la aplicación
#Fin del código        



      
      
# Proyecto final

import tkinter as tk #Se importa la libreria y se le da un título
from tkinter import *  # Librería que importa todos los módulos de la clase
from PIL import Image, ImageTk as itk #librería de imagenes
from tkinter import ttk

# ---------Ventana principal------------
window = Tk()
window.title("Sky-Voyage")
window.geometry("400x300")
window.config(bg = "white")
window.resizable(0, 0)
window.iconbitmap("avion.ico")

#-----------Se crea un lienzo-----------
lienzo = tk.Frame(window, bg = "white") #.frame es un contenedor visual de widgets
lienzo.pack(pady=40)

#------Agregar el logo a la ventana------
imagen = itk.PhotoImage(file="avion.png")
logo = Label(lienzo, image=imagen, bg="white")
logo.grid(columnspan=3, row=0, pady=20)

#----------Etiquetas y entradas----------
#-----------------Código-----------------
codigo_tex = tk.Label(lienzo, text="Código", bg="White") #.label para copiar texto 
codigo_tex.grid(row=1, column=0, padx=0, pady=10)

codigo_entry = tk.Entry(lienzo)
codigo_entry.grid(row=2, column=0, padx=10, pady=5)

#-----------------Apellido---------------
apellido_tex = tk.Label(lienzo, text="Apellido", bg="White")
apellido_tex.grid(row=1, column=1, padx=0, pady= 10)

apellido_entry = tk.Entry(lienzo)
apellido_entry.grid(row=2, column=1, padx=0, pady=5)

#------función de datos ingresados por el usuario--------
def datos_ingresados():
    codigo = codigo_entry.get() #Para guardar los datos de código
    apellido = apellido_entry.get() #Para guardar los datos de apellido
    #---Guardar los datos en un archivo de texto---
    with open("datos_usuario.txt", "a") as file:
        file.write(f"Código: {codigo} - Apellido: {apellido}\n") #Cómo se guardan los datos en el txt

    #---Función nueva ventana---
    nueva_ventana_vuelos()

#-------------Botón check-in-------------
checkin_b = tk.Button(lienzo, text="Realizar Check-in", bg="red", fg="white", command=datos_ingresados)
checkin_b.grid(row=3, columnspan=3, pady=10)

def nueva_ventana_vuelos():
    #---Crear una nueva ventana---
    ventana_vuelos = tk.Toplevel(window) #Abrir la ventana nueva encima de la ventana principal
    ventana_vuelos.title("Sky-Voyage")
    ventana_vuelos.geometry("800x400")
    ventana_vuelos.config(bg = "white")
    ventana_vuelos.resizable(0, 0)
    ventana_vuelos.iconbitmap("avion.ico")

    lienzo_2 = tk.Frame(ventana_vuelos, bg = "white") #.frame es un contenedor visual de widgets
    lienzo_2.pack(pady=40, fill="x")

    #----Barra de personas e ida----
    barra = tk.Frame(lienzo_2, bg="white", bd=0, relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra.pack(pady=0, padx=20, fill="x")

    #---------Botón de ida----------
    solo_ida = tk.Label(barra, text="     Solo ida", relief="flat", bg="white", fg= "black", highlightbackground='red', highlightthicknes=1)
    solo_ida.pack(side="left", padx=10, pady=5)

    #-----Cantidad de personas------
    barra_2 = tk.Frame(barra, bg="white", bd=0, relief=tk.FLAT, highlightbackground="red", highlightthicknes=1)
    barra_2.pack(pady=10, padx=10, side="right")   
    personas = tk.Label(barra_2, text="Personas:", bg="white")
    personas.pack (side="left", padx=5, pady=5)
    personas_cant = ttk.Combobox(barra_2, values=[str(i) for i in range(1,11)], width=3)
    personas_cant.current(0) #para al iniciar siempre empezar en la pocision 0 , osea 1
    personas_cant.pack(side="right", padx=5, pady=5)

    #------marco de busqueda--------
    barra_3 = tk.Frame(lienzo_2, bg="white", bd=2, relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_3.pack(pady=0, padx=20, fill="x")

    #-------------Origen------------
    barra_4 = tk.Frame(barra_3, bg="white", bd=0, relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_4.pack(pady=20, padx=10, side="left")
    origen = tk.Label(barra_4, text="origen", bg="white")
    origen.grid(row=0, column=0, padx=10, pady=5)

    #------------Destino------------
    barra_5 = tk.Frame(barra_3, bg="white", bd=0, relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_5.pack(pady=20, padx=0, side="left")
    destino = tk.Label(barra_5, text="Destino", bg="white")
    destino.grid(row=0, column=0, padx=10, pady=5)

    #-------------Más---------------
    barra_6 = tk.Frame(barra_3, bg="white", bd=0, relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_6.pack(pady=20, padx=20, side="left")
    destino = tk.Label(barra_6, text="Más", bg="white")
    destino.grid(row=0, column=0, padx=10, pady=5)
    
    #-------------Botón Buscar-------------
    btn_buscar = tk.Button(barra_3, text="Buscar", bg="red", fg="white", command=nueva_ventana_asientos)
    btn_buscar.pack(pady=20)


def nueva_ventana_asientos():
    #-------Crear una nueva ventana--------
    ventana_asientos = tk.Toplevel(window) #Abrir la ventana nueva encima de la ventana principal
    ventana_asientos.title("Sky-Voyage")
    ventana_asientos.geometry("800x500")
    ventana_asientos.config(bg = "white")
    ventana_asientos.resizable(0, 0)
    ventana_asientos.iconbitmap("avion.ico")

    #----------------Lienzo----------------
    lienzo_3 = tk.Frame(ventana_asientos, bg="white")
    lienzo_3.pack(pady=10, fill="x")

    #--------selección de asientos---------
    seleccion = tk.Label(lienzo_3, text="Selección de Asientos", font=("Times new roman", 12), bg="white")
    seleccion.pack(pady=0, padx=80, side="left")

    #-----Marco para asientos y etiquetas---
    marco = tk.Frame(ventana_asientos, bg="white")
    marco.pack(pady=5)

    marco_asientos = tk.Frame(marco, bg="mistyrose")
    marco_asientos.pack(side="left", pady=5)

    marco_clases = tk.Frame(marco, bg="white")
    marco_clases.pack(padx=20, side="right", pady=5)  # Relleno a la derecha para separar las etiquetas de clase

    #----Crear etiquetas para las columnas----
    columnas = ["A", "B", "C", "D", "E", "F"]
    for i, columna in enumerate(columnas):
        lbl = tk.Label(marco_asientos, text=columna, bg="mistyrose")
        lbl.grid(row=0, column=i+1)

    #--Crear los botones para los asientos (72 asientos, 12 filas x 6 columnas)---
    num_filas = 12
    num_columnas = 6

    for r in range(num_filas):
        lbl = tk.Label(marco_asientos, text=str(r+1), bg="mistyrose")
        lbl.grid(row=r+1, column=0)
        for c in range(num_columnas):
            clase = "Aluminio" if r >= 8 else "Diamante" if r >= 4 else "Premium"
            color = "lightcoral" if clase == "Premium" else "brown" if clase == "Diamante" else "red"
            btn = tk.Button(marco_asientos, bg=color, width=2, height=1, relief="flat")
            btn.grid(row=r+1, column=c+1, padx=2, pady=2)

    #-----Crear las etiquetas para las clases------
    lbl_premium = tk.Label(marco_clases, text="Premium", bg="lightcoral", width=10)
    lbl_premium.pack(pady=40)

    lbl_diamante = tk.Label(marco_clases, text="Diamante", bg="brown", width=10)
    lbl_diamante.pack(pady=40)

    lbl_aluminio = tk.Label(marco_clases, text="Aluminio", bg="red", width=10)
    lbl_aluminio.pack(pady=40)

    #-------Botón de selección-------
    btn_seleccionar = tk.Button(ventana_asientos, text="Seleccionar", bg="red", fg="white", command=ventana_ofertas)
    btn_seleccionar.pack(pady=10, padx=30, side="right")

def ventana_ofertas():
    ventana_ofertas = tk.Toplevel(window) #Abrir la ventana nueva encima de la ventana principal
    ventana_ofertas.title("Sky-Voyage")
    ventana_ofertas.geometry("800x500")
    ventana_ofertas.config(bg = "white")
    ventana_ofertas.resizable(0, 0)
    ventana_ofertas.iconbitmap("avion.ico")


window.mainloop()
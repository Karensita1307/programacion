# Proyecto final

import tkinter as tk #Se importa la libreria y se le da un título
from tkinter import *  # Librería que importa todos los módulos de la clase
from PIL import Image, ImageTk as itk#librería de imagenes

# ---------Ventana principal------------
window = Tk()
window.title("Sky-Voyage")
window.geometry("400x300")
window.config(bg = "white")
window.resizable(0, 0)

#-----------Se crea un lienzo-----------
lienzo = tk.Frame(window, bg = "white") #.frame es un contenedor visual de widgets
lienzo.pack(pady=40)

#------Agregar el logo a la ventana------
imagen = itk.PhotoImage(file="avion.png")
logo = Label(lienzo, image=imagen, bg="white")
logo.grid(columnspan=3, row=0, pady=20)

#----------Etiquetas y entradas----------
#-----------------Código-----------------
codigo_tex = tk.Label(lienzo, text="Código", bg="White")
codigo_tex.grid(row=1, column=0, padx=0, pady=10)

codigo_entry = tk.Entry(lienzo)
codigo_entry.grid(row=2, column=0, padx=10, pady=5)

#-----------------Apellido---------------
apellido_tex = tk.Label(lienzo, text="Apellido", bg="White")
apellido_tex.grid(row=1, column=2, padx=0, pady= 10)

apellido_entry = tk.Entry(lienzo)
apellido_entry.grid(row=2, column=2, padx=0, pady=5)

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
    ventana_vuelos.resizable(0, 0)

    #----Barra de personas e ida----
    barra = tk.Frame(ventana_vuelos, bg='white', bd=0, relief=tk.FLAT, highlightbackground='red', highlightthicknes=2)
    barra.pack(pady=20, padx=20, fill='x')

    #---------Botón de ida----------
    barra_1 = tk.Frame(barra, bg='white', bd=0, relief=tk.FLAT, highlightbackground='red', highlightthicknes=2)
    barra_1.pack(pady=10, padx=5, side="left")
    solo_ida = tk.Button(barra_1, text="     Solo ida", relief="flat", bg="white", fg= "black")
    solo_ida.pack(side="right", padx=10, pady=5)

    #-----Cantidad de personas------
    barra_2 = tk.Frame(barra, bg='white', bd=0, relief=tk.FLAT, highlightbackground='red', highlightthicknes=2)
    barra_2.pack(pady=10, padx=5, side="right")   


window.mainloop()
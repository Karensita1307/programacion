from tkinter import *  # Librería que importa todos los módulos de la clase

# Se crea la ventana
window = Tk()

# ---------Configuration-------------
window.title("Vuelos.com")
window.geometry("1000x500")
window.config(bg = "white")
window.resizable(0, 0)

# -----------Cambiar icono------------- 
window.iconbitmap("Avion.ico")  # Poner la imagen despues de convertirla
#window.image_names("real.ico") # una imagen que vaya dentro de la ventana

window.mainloop()
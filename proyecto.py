# Proyecto final

import tkinter as tk #Se importa la libreria y se le da un título
from tkinter import *  # Librería que importa todos los módulos de la clase
from PIL import Image, ImageTk as itk #librería de imagenes
from tkinter import ttk # LLibrería para los combobox y mas comandos
from tkinter import messagebox # Ventana emergente
from datetime import datetime # Para el tiempo

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

matriz = [
['Z328', '2024-06-5', '08:13:00', '10:35:00', 244463, 538669, 1666594, 'Santa Marta', 'Bogota'],
['X633', '2024-06-6', '02:55:00', '05:58:00', 483669, 640186, 4023518, 'Santa Marta', 'Cartagena'],
['G611', '2024-06-12', '16:50:00', '17:07:00', 295876, 915371, 2684321, 'Medellin', 'Santa Marta'],
['N891', '2024-06-13', '07:15:00', '11:48:00', 438164, 692289, 2927741, 'Cali', 'Bogota'],
['E350', '2024-06-26', '15:52:00', '17:10:00', 279458, 506496, 1066916, 'Cartagena', 'Bogota'],
['J773', '2024-06-6', '10:21:00', '11:03:00', 293612, 972660, 4265332, 'Bogota', 'Santa Marta'],
['B552', '2024-06-13', '13:28:00', '15:29:00', 390970, 781301, 2636179, 'Cali', 'Bogota'],
['I352', '2024-06-19', '18:33:00', '20:33:00', 112548, 607120, 3138340, 'Cartagena', 'Medellin'],
['Y874', '2024-06-5', '15:17:00', '16:50:00', 108548, 889209, 4215978, 'Santa Marta', 'Cartagena'],
['A823', '2024-06-19', '02:55:00', '06:03:00', 286051, 887727, 1794728, 'Medellin', 'Bogota'],
['J837', '2024-06-5', '17:01:00', '18:02:00', 182306, 601733, 3060789, 'Cartagena', 'Bogota'],
['Z343', '2024-06-19', '13:47:00', '17:42:00', 248460, 849734, 1382792, 'Cali', 'Medellin'],
['E747', '2024-06-19', '06:53:00', '09:52:00', 426098, 767319, 4081864, 'Medellin', 'Bogota'],
['D141', '2024-06-27', '17:29:00', '20:54:00', 330781, 531990, 2817297, 'Cartagena', 'Bogota'],
['E387', '2024-06-26', '03:32:00', '07:00:00', 473622, 609433, 2821653, 'Cartagena', 'Medellin'],
['P636', '2024-06-12', '10:52:00', '12:50:00', 183918, 644497, 3018149, 'Santa Marta', 'Bogota'],
['K776', '2024-06-6', '19:01:00', '21:36:00', 340848, 968318, 1259865, 'Santa Marta', 'Cali'],
['W556', '2024-06-19', '21:50:00', '23:03:00', 169404, 896128, 4830564, 'Cartagena', 'Medellin'],
['L703', '2024-06-19', '07:09:00', '07:17:00', 107432, 765044, 1848939, 'Santa Marta', 'Cali'],
['L890', '2024-06-20', '11:09:00', '13:32:00', 391458, 673038, 4485596, 'Medellin', 'Cartagena'],
['G714', '2024-06-20', '08:01:00', '10:34:00', 368435, 552773, 3427251, 'Bogota', 'Cartagena'],
['H152', '2024-06-12', '19:12:00', '23:48:00', 143776, 899772, 3900612, 'Cartagena', 'Santa Marta'],  
['I966', '2024-06-26', '08:57:00', '09:37:00', 228361, 600499, 2154222, 'Cartagena', 'Cali'],
['R874', '2024-06-19', '05:31:00', '08:40:00', 185702, 943771, 4208738, 'Cartagena', 'Santa Marta'],    
['U929', '2024-06-19', '15:02:00', '17:21:00', 115796, 647904, 2932337, 'Bogota', 'Medellin'],
['E389', '2024-06-6', '16:46:00', '20:32:00', 420182, 557153, 4055065, 'Cali', 'Medellin'],
['L505', '2024-06-12', '04:52:00', '05:23:00', 378191, 677832, 1759483, 'Medellin', 'Cali'],
['J786', '2024-06-26', '15:44:00', '16:20:00', 464673, 723388, 4718254, 'Cali', 'Bogota'],
['I506', '2024-06-26', '12:13:00', '13:48:00', 156761, 955557, 4359006, 'Medellin', 'Cartagena'],
['W151', '2024-06-27', '01:46:00', '03:28:00', 158668, 887450, 1527895, 'Santa Marta', 'Bogota'],
['I657', '2024-06-5', '23:46:00', '2:48:00', 227358, 920227, 3299390, 'Bogota', 'Medellin'],
['A722', '2024-06-6', '12:32:00', '14:25:00', 335925, 718598, 3201428, 'Medellin', 'Santa Marta'],
['G542', '2024-06-27', '10:15:00', '12:58:00', 364902, 620659, 3822832, 'Cali', 'Bogota'],
['R419', '2024-06-13', '18:45:00', '21:11:00', 263221, 823412, 1802097, 'Cali', 'Bogota'],
['K387', '2024-06-12', '08:52:00', '12:58:00', 111358, 837315, 1740776, 'Medellin', 'Cartagena'],
['I684', '2024-06-6', '18:25:00', '22:33:00', 268461, 861073, 4378830, 'Santa Marta', 'Cartagena'],      
['T366', '2024-06-6', '15:59:00', '16:30:00', 441718, 551893, 1443926, 'Bogota', 'Medellin'],
['G973', '2024-06-27', '07:51:00', '09:59:00', 107735, 812320, 4667378, 'Cartagena', 'Medellin'],
['P628', '2024-06-20', '20:47:00', '21:45:00', 259683, 878251, 1406197, 'Cali', 'Bogota'],
['V577', '2024-06-20', '19:47:00', '23:12:00', 321437, 838480, 2594022, 'Bogota', 'Medellin'],
['Y916', '2024-06-5', '19:05:00', '20:07:00', 146788, 717336, 2479818, 'Bogota', 'Medellin'],
['C616', '2024-06-6', '14:43:00', '19:14:00', 251102, 768356, 3231604, 'Bogota', 'Medellin'],
['Z502', '2024-06-27', '02:33:00', '04:46:00', 135039, 739155, 3841687, 'Santa Marta', 'Medellin'],       
['O706', '2024-06-19', '03:33:00', '08:12:00', 108543, 552765, 4776384, 'Cartagena', 'Medellin'],
['A425', '2024-06-12', '05:16:00', '07:38:00', 428767, 803167, 3465554, 'Bogota', 'Cartagena'],
['A643', '2024-06-27', '02:41:00', '06:50:00', 133731, 965070, 1155231, 'Bogota', 'Santa Marta'],
['C594', '2024-06-6', '20:14:00', '22:16:00', 179770, 755917, 3525256, 'Cartagena', 'Cali'],
['X712', '2024-06-5', '04:28:00', '05:47:00', 367356, 997236, 2511543, 'Santa Marta', 'Cartagena'],      
['X517', '2024-06-26', '13:23:00', '16:23:00', 409500, 657451, 2024557, 'Cali', 'Cartagena'],
['M302', '2024-06-20', '15:15:00', '17:10:00', 138614, 638674, 4057270, 'Cartagena', 'Cali'],
['X448', '2024-06-12', '14:57:00', '16:48:00', 256801, 649687, 2492053, 'Medellin', 'Bogota'],
['K415', '2024-06-6', '01:59:00', '02:58:00', 118208, 955980, 3967119, 'Cartagena', 'Cali'],
['N999', '2024-06-20', '00:02:00', '01:28:00', 113404, 742916, 3870717, 'Cali', 'Bogota'],
['Q579', '2024-06-19', '10:13:00', '13:46:00', 442756, 900225, 4970730, 'Bogota', 'Cali'],
['O632', '2024-06-5', '10:46:00', '11:04:00', 450503, 759587, 3350417, 'Cali', 'Medellin'],
['W768', '2024-06-5', '00:14:00', '02:37:00', 309428, 530313, 3146101, 'Cartagena', 'Santa Marta'],      
['N700', '2024-06-20', '17:02:00', '21:47:00', 428761, 586568, 4387318, 'Cali', 'Medellin'],
['A198', '2024-06-13', '10:07:00', '11:34:00', 471496, 637023, 3708333, 'Santa Marta', 'Cali'],
['N508', '2024-06-20', '07:49:00', '11:17:00', 380455, 885626, 1079810, 'Cali', 'Bogota'],
['S830', '2024-06-26', '06:11:00', '08:05:00', 136210, 609050, 1031737, 'Medellin', 'Bogota'],
['B193', '2024-06-12', '11:55:00', '16:16:00', 322687, 776707, 3559620, 'Santa Marta', 'Medellin'],     
['N925', '2024-06-20', '20:09:00', '23:27:00', 348655, 584679, 2803067, 'Bogota', 'Cali'],
['O805', '2024-06-19', '08:11:00', '12:14:00', 180125, 637210, 4660148, 'Cartagena', 'Cali'],
['B165', '2024-06-20', '00:21:00', '03:01:00', 285230, 798592, 4037787, 'Medellin', 'Cali'],
['Q419', '2024-06-6', '18:09:00', '20:04:00', 336342, 966902, 3843081, 'Santa Marta', 'Bogota'],
['H905', '2024-06-6', '11:56:00', '13:11:00', 345069, 702454, 1287428, 'Cali', 'Santa Marta'],
['R873', '2024-06-6', '00:14:00', '04:15:00', 209011, 932430, 2499023, 'Santa Marta', 'Cali'],
['T810', '2024-06-6', '22:03:00', '00:13:00', 353905, 622617, 1739971, 'Medellin', 'Santa Marta'],
['R507', '2024-06-20', '03:35:00', '05:14:00', 338290, 891960, 3268081, 'Cartagena', 'Bogota'],
['E279', '2024-06-27', '03:32:00', '07:31:00', 112594, 535012, 2407140, 'Cali', 'Bogota'],
['T179', '2024-06-5', '21:42:00', '23:56:00', 194995, 970417, 3446179, 'Medellin', 'Bogota'],
['E348', '2024-06-6', '14:21:00', '17:45:00', 200805, 661664, 1423079, 'Cartagena', 'Cali'],
['V809', '2024-06-5', '15:17:00', '18:30:00', 412564, 851500, 4680941, 'Santa Marta', 'Medellin'],
['D483', '2024-06-12', '04:31:00', '09:24:00', 232173, 607087, 4661950, 'Cali', 'Cartagena'],
['F592', '2024-06-20', '20:57:00', '23:35:00', 387337, 666898, 4024585, 'Medellin', 'Cartagena'],
['B209', '2024-06-6', '07:51:00', '10:33:00', 422422, 832491, 3948879, 'Santa Marta', 'Cartagena'],     
['F812', '2024-06-26', '04:51:00', '08:56:00', 100947, 539536, 3632244, 'Cali', 'Cartagena'],
['X552', '2024-06-26', '04:54:00', '07:10:00', 271127, 656834, 4845023, 'Cartagena', 'Santa Marta'],     
['I848', '2024-06-5', '07:45:00', '12:08:00', 180814, 648460, 4560674, 'Cartagena', 'Bogota'],
['J755', '2024-06-20', '02:52:00', '07:15:00', 352497, 973921, 4954962, 'Cali', 'Medellin'],
['Y216', '2024-06-19', '02:44:00', '05:12:00', 339920, 690835, 3549467, 'Cartagena', 'Santa Marta'],     
['G442', '2024-06-12', '01:09:00', '03:41:00', 346049, 850291, 4890999, 'Medellin', 'Cali'],
['V932', '2024-06-12', '16:57:00', '18:53:00', 368937, 836969, 2128948, 'Santa Marta', 'Medellin'],     
['Q252', '2024-06-20', '08:20:00', '13:01:00', 477214, 801662, 4676437, 'Cartagena', 'Cali'],
['D848', '2024-06-27', '11:08:00', '14:48:00', 239379, 992500, 3004583, 'Bogota', 'Santa Marta'],
['S569', '2024-06-5', '14:40:00', '16:24:00', 198988, 955922, 4074101, 'Bogota', 'Medellin'],
['I656', '2024-06-13', '20:31:00', '23:13:00', 283863, 587002, 3987051, 'Medellin', 'Cali'],
['S129', '2024-06-6', '18:08:00', '19:08:00', 377016, 650034, 1915104, 'Medellin', 'Cartagena'],
['N232', '2024-06-5', '16:35:00', '19:08:00', 186616, 590890, 2616295, 'Medellin', 'Santa Marta'],
['M191', '2024-06-20', '03:11:00', '07:02:00', 343481, 664520, 3274677, 'Cartagena', 'Medellin'],
['H180', '2024-06-20', '00:19:00', '02:53:00', 314037, 672798, 3793121, 'Santa Marta', 'Cali'],
['V900', '2024-06-19', '10:39:00', '13:52:00', 361362, 575041, 4335294, 'Santa Marta', 'Cali'],
['Q449', '2024-06-27', '18:37:00', '20:56:00', 407816, 703210, 4323741, 'Santa Marta', 'Cali'],
['R250', '2024-06-26', '16:28:00', '18:29:00', 478289, 965855, 2387745, 'Cali', 'Bogota'],
['T654', '2024-06-26', '12:11:00', '14:20:00', 358074, 736442, 4444497, 'Santa Marta', 'Bogota'],
['Y804', '2024-06-12', '14:28:00', '16:34:00', 261803, 548104, 1150859, 'Cali', 'Bogota'],
['E971', '2024-06-12', '22:07:00', '23:12:00', 362030, 972110, 1721417, 'Santa Marta', 'Cartagena'],      
['U728', '2024-06-12', '15:55:00', '18:43:00', 352021, 909057, 3924712, 'Santa Marta', 'Medellin'],
['U522', '2024-06-13', '12:46:00', '14:54:00', 169490, 503891, 2723741, 'Bogota', 'Cartagena'],
['V560', '2024-06-26', '08:41:00', '11:20:00', 118816, 675485, 2104917, 'Santa Marta', 'Cali'],
]

def volver():
    ventana_vuelos.destroy()
    window.deiconify()

def nueva_ventana_vuelos():
    global ventana_vuelos, personas_cant, origen_txt, destino_txt, fecha_txt
    window.withdraw()

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
    barra = tk.Frame(lienzo_2, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra.pack(pady=0, padx=20, fill="x")

    #---------Botón de ida----------
    solo_ida = tk.Label(barra, text="     Solo ida", relief="flat", bg="white", fg= "black", highlightbackground='red', highlightthicknes=1)
    solo_ida.pack(side="left", padx=5, pady=5)

    #-----Cantidad de personas------
    barra_2 = tk.Frame(barra, bg="white", relief=tk.FLAT, highlightbackground="red", highlightthicknes=1)
    barra_2.pack(pady=10, padx=10, side="right")   
    personas = tk.Label(barra_2, text="Personas:", bg="white")
    personas.pack (side="left", padx=5, pady=5)
    personas_g = tk.StringVar()
    personas_cant = ttk.Combobox(barra_2, values=[str(i) for i in range(1,11)], width=3, textvariable=personas_g)
    personas_cant.pack(side="right", padx=5, pady=5)

    #------marco de busqueda--------
    barra_3 = tk.Frame(lienzo_2, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_3.pack(side="top", pady=0, padx=20, fill="x")
    busqueda = tk.Frame(barra_3, bg="white", relief=tk.FLAT)
    busqueda.pack(side="bottom", pady=0, padx=20, fill="x")

    #-------------Origen------------
    barra_4 = tk.Frame(barra_3, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_4.pack(pady=20, padx=20, side="left")
    origen = tk.Label(barra_4, text="Origen", bg="white")
    origen.grid(row=0, column=0, padx=5, pady=2)
    
    #-------Ciudades de origen------
    ciudades = set() # set() es para datos repetidos en un conjunto
    ciudades_origen = [] # Lista donde se van a almacenar

    # Recorre cada lista en la matriz
    for o in matriz:
    # Obtiene el dato número 7 (ciudad de origen) y lo agrega al conjunto
        ciudad_ori = o[7]
        ciudades.add(ciudad_ori) # add para añadir al conjunto

    # Imprime las ciudades únicas
    for ciudad in ciudades:
        ciudades_origen.append(ciudad) # Añadir las ciudades a la lista
    
    origen_g = tk.StringVar()
    origen_txt = ttk.Combobox(barra_4, values=ciudades_origen, width=20, textvariable=origen_g)
    origen_txt.grid(row=1, column=1, padx=5, pady=2)
    origen_txt.bind("<<ComboboxSelected>>", lambda event: actualizar_fechas_disponibles())

    #------------Destino------------
    barra_5 = tk.Frame(barra_3, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_5.pack(pady=20, padx=0, side="left")
    destino = tk.Label(barra_5, text="Destino", bg="white")
    destino.grid(row=0, column=0, padx=5, pady=2)

    #-------Ciudades de destino------
    ciudades_destino = [] # Lista donde se van a almacenar

    # Recorre cada lista en la matriz
    for d in matriz:
    # Obtiene el dato número 8 (ciudad de destino) y lo agrega al conjunto
        ciudad_des = d[8]
        ciudades.add(ciudad_des) # add para añadir al conjunto

    # Imprime las ciudades únicas
    for des in ciudades:
        ciudades_destino.append(des) # Añadir las ciudades a la lista


    destino_g = tk.StringVar()
    destino_txt = ttk.Combobox(barra_5, values=ciudades_destino, width=20, textvariable=destino_g)
    destino_txt.grid(row=1, column=1, padx=5, pady=2)
    destino_txt.bind("<<ComboboxSelected>>", lambda event: actualizar_fechas_disponibles())

    #-------------Fecha---------------
    barra_6 = tk.Frame(barra_3, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_6.pack(pady=20, padx=20, side="right")
    fecha = tk.Label(barra_6, text="Fecha", bg="white")
    fecha.grid(row=0, column=0, padx=5, pady=2)
    
    #------------fechas----------------
    fechass = set()
    fechas = [] # Lista donde se van a almacenar

    # Recorre cada lista en la matriz
    for f in matriz:
    # Obtiene el dato número 1 (fecha) y lo agrega al conjunto
        fecha_ida = f[1]
        fechass.add(fecha_ida) # add para añadir al conjunto

    # Imprime las ciudades únicas
    for fech in fechass:
        fechas.append(fech) # Añadir las ciudades a la lista
    
    fecha_g = tk.StringVar()
    fecha_txt = ttk.Combobox(barra_6, values=fechas, width=25, textvariable=fecha_g)
    fecha_txt.grid(row=1, column=1, padx=5, pady=2)

    #----guardar----
    guardar = tk.Checkbutton(busqueda, text="Guardar datos", command=guardar_selecciones)
    guardar.grid(row=0, column=0, padx=5, pady=2)

    #---------Botón Buscar-----------
    btn_buscar = tk.Button(busqueda, text="Buscar", bg="red", fg="white", command=nueva_ventana_asientos)
    btn_buscar.grid(row=1, column=5, padx=5, pady=2)

        #---------Botón Volver-----------
    btn_volver = tk.Button(busqueda, text="Atrás", bg="red", fg="white", command=volver)
    btn_volver.grid(row=1, column=4, padx=5, pady=2)

def actualizar_fechas_disponibles():
    origen_seleccionado = origen_txt.get()
    destino_seleccionado = destino_txt.get()

    fechas_disponibles = set()
    for vuelo in matriz:
        if vuelo[7] == origen_seleccionado and vuelo[8] == destino_seleccionado:
            fechas_disponibles.add(vuelo[1])  # Añadir la fecha del vuelo si coincide con el origen y destino seleccionados

    # Actualizar las opciones de fecha
    fecha_txt['values'] = tuple(fechas_disponibles)

def guardar_selecciones():
    global ori, des, cant, fech
    des = destino_txt.get()    
    ori = origen_txt.get()
    cant = int(personas_cant.get())
    fech = fecha_txt.get()

asientos_seleccionados = 0

def cambiar_estado(boton):
    if boton['bg'] == "mistyrose":
        global asientos_seleccionados
        # Deseleccionar el asiento
        boton.config(bg="red")
        asientos_seleccionados -= 1
    else:
        # Seleccionar el asiento
        if asientos_seleccionados < cant:
            boton.config(bg="mistyrose")
            asientos_seleccionados += 1
        else:
            tk.messagebox.showinfo("Error", f"Solo se pueden seleccionar {cant} asientos.")

def volver_1():
    ventana_asientos.destroy()
    ventana_vuelos.deiconify()

def nueva_ventana_asientos():
    global ventana_asientos, color
    ventana_vuelos.withdraw()
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
    marco.pack(pady=10, padx=10)

    marco_asientos = tk.Frame(marco, bg="mistyrose")
    marco_asientos.pack(side="left", pady=5)

    marco_clases = tk.Frame(marco, bg="white")
    marco_clases.pack(padx=20, side="right", pady=5)  # Relleno a la derecha para separar las etiquetas de clase

    #----Crear etiquetas para las columnas----
    columnas = ["A", "B", "C", "D", "E", "F"]

    #--Crear los botones para los asientos (72 asientos, 12 filas x 6 columnas)---
    num_filas = 12
    num_columnas = 6

    for fila in range(num_filas):
        for columna in range(num_columnas):
            clase = "Aluminio" if fila >= 8 else "Diamante" if fila >= 4 else "Premium"
            color = "lightcoral" if clase == "Premium" else "brown" if clase == "Diamante" else "red"
            boton = tk.Button(marco_asientos, text=f"{fila+1}{columnas[columna]}", bg=color, width=3)
            boton.config(command=lambda b=boton: cambiar_estado(b))
            boton.grid(row=fila, column=columna)

    #-----Crear las etiquetas para las clases------
    lbl_premium = tk.Label(marco_clases, text="Premium", bg="lightcoral", width=10)
    lbl_premium.pack(pady=40)

    lbl_diamante = tk.Label(marco_clases, text="Diamante", bg="brown", width=10)
    lbl_diamante.pack(pady=40)

    lbl_aluminio = tk.Label(marco_clases, text="Aluminio", bg="red", width=10)
    lbl_aluminio.pack(pady=40)
        
    #-------Botón de selección-------
    btn_seleccionar = tk.Button(ventana_asientos, text="Seleccionar", bg="red", fg="white", command=nueva_ventana_ofertas)
    btn_seleccionar.pack(pady=10, padx=10, side="right")

    #----------Botón volver----------
    btn_volver = tk.Button(ventana_asientos, text="Atrás", bg="red", fg="white", command=volver_1)
    btn_volver.pack(pady=10, padx=0, side="right")

    guardar_asientos = tk.Checkbutton(ventana_asientos, text="Guardar datos")
    guardar_asientos.pack(pady=10, padx=30, side="bottom")

precio_menor = []
precio_regular = []
precio_mayor = []

def precios():
    global precio_menor, precio_mayor, precio_regular

    for vuelo in matriz: 
        if vuelo[1] == fech and vuelo[7] == ori and vuelo[8] == des:
            precio_menor.append(vuelo[4])

    for vuelo in matriz:
        if vuelo[1] == fech and vuelo[7] == ori and vuelo[8] == des:
            precio_regular.append(vuelo[5])

    for vuelo in matriz:
        if vuelo[1] == fech and vuelo[7] == ori and vuelo[8] == des:
            precio_mayor.append(vuelo[6])

menor = []
regular = []
mayor = []

def horas():
    global menor, mayor, regular

    for vuelo in matriz:
        if vuelo[1] == fech and vuelo[7] == ori and vuelo[8] == des and vuelo[4] == precio_menor:
            ida = vuelo[2]
            vuelta = vuelo[3]
            hora_ida = datetime.strptime(ida, "%H:%M:%S").strftime("%H:%M")
            hora_vuelta = datetime.strptime(vuelta, "%H:%M:%S").strftime("%H:%M")
            menor.append(hora_ida)
            menor.append(hora_vuelta)


    for vuelo in matriz:
        if vuelo[1] == fech and vuelo[7] == ori and vuelo[8] == des and vuelo[4] == precio_regular:
            ida = vuelo[2]
            vuelta = vuelo[3]
            hora_ida = datetime.strptime(ida, "%H:%M:%S").strftime("%H:%M")
            hora_vuelta = datetime.strptime(vuelta, "%H:%M:%S").strftime("%H:%M")
            regular.append(hora_ida)
            regular.append(hora_vuelta)           

    for vuelo in matriz:
        if vuelo[1] == fech and vuelo[7] == ori and vuelo[8] == des and vuelo[4] == precio_mayor:
            ida = vuelo[2]
            vuelta = vuelo[3]
            hora_ida = datetime.strptime(ida, "%H:%M:%S").strftime("%H:%M")
            hora_vuelta = datetime.strptime(vuelta, "%H:%M:%S").strftime("%H:%M")
            mayor.append(hora_ida)
            mayor.append(hora_vuelta)      

def calcular_tiempo_transcurrido(hora_inicio, hora_fin):
    # Convertir las horas de cadena a objetos datetime
    hora_inicio_obj = datetime.strptime(hora_inicio, "%H:%M")
    hora_fin_obj = datetime.strptime(hora_fin, "%H:%M")
    
    # Calcular la diferencia de tiempo
    tiempo_transcurrido = hora_fin_obj - hora_inicio_obj
    
    # Calcular el tiempo transcurrido en horas y minutos
    horas = tiempo_transcurrido.seconds // 3600
    minutos = (tiempo_transcurrido.seconds % 3600) // 60
    
    return horas, minutos

def volver_2():
    ventana_ofertas.destroy()
    ventana_asientos.deiconify()

def nueva_ventana_ofertas():
    global ventana_ofertas
    ventana_asientos.withdraw()

    ventana_ofertas = tk.Toplevel(window) #Abrir la ventana nueva encima de la ventana principal
    ventana_ofertas.title("Sky-Voyage")
    ventana_ofertas.geometry("800x500")
    ventana_ofertas.config(bg = "white")
    ventana_ofertas.resizable(0, 0)
    ventana_ofertas.iconbitmap("avion.ico")

    # ------- Se crea un lienzo---------
    lienzo_4 = tk.Frame(ventana_ofertas, bg = "white")
    lienzo_4.pack(pady=40, fill="x")

    # ------ Barra de ida -------
    barra_7 = tk.Frame(lienzo_4, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_7.pack(pady=0, padx=20, fill="x")

    #------ boton de Ida---------
    ida_ofertas = tk.Label(barra_7, text= "   Ida:", relief="flat", bg="white", fg="black",highlightbackground="white", highlightthickness=1)
    ida_ofertas.pack(side="left", padx=5, pady=5)

    text = (f"{ori} a {des}")
    viaje = tk.Label(barra_7, text=text , relief="flat", bg="white", fg="black",highlightbackground="white", highlightthickness=1)
    viaje.pack(side="left", padx=0, pady=8)

    #----Barra de ordenar por------
    barra_8 = tk.Frame(lienzo_4, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_8.pack(pady=0, padx=20, fill="x")

    # ----Botones de ordenar----------
    ordenar = tk.Label(barra_8, text= "ordenado por:", relief="flat", bg="white", fg="black",highlightbackground="white", highlightthickness=1)
    ordenar.pack(side="left", padx=3, pady=3)
    
    mejor_precio = tk.Button(barra_8, text= "Mejor Precio ", relief="solid", bg="white")
    mejor_precio.pack(side="left", padx=3, pady=5)

    #-------Barra para vuelos-------
    barra_9 = tk.Frame(lienzo_4, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_9.pack(pady=5, padx=20, fill="x")

    #------primer posible-------------
    vuelo_1 = tk.Frame(barra_9, relief=tk.RAISED, bg="white")
    vuelo_1.pack(pady=5, padx=10, fill="x")

    texx = menor[0]
    hora_ida = tk.Label(vuelo_1, text=texx, bg="white")
    hora_ida.grid(row=0, column=0, padx=5, pady=1)

    origen = ori[:3].upper() # .upper para pasarlo a mayusculas
    ciudad_1 = tk.Label(vuelo_1, text=origen, bg="white")
    ciudad_1.grid(row=1, column=0, padx=5, pady=1)

    lineas = tk.Label(vuelo_1, text="-------------------", bg="white")
    lineas.grid(row=0, column=1, padx=5, pady=1)

    horas, minutos = calcular_tiempo_transcurrido(menor[0], menor[1])
    texto = (f"{horas}h {minutos}m")
    tiempo = tk.Label(vuelo_1, text=texto, bg="white")
    tiempo.grid(row=1, column=1, padx=5, pady=1)

    texxt = menor[1]
    hora_ida = tk.Label(vuelo_1, text=texxt, bg="white")
    hora_ida.grid(row=0, column=2, padx=5, pady=1)

    origen = des[:3].upper() # .upper para pasarlo a mayusculas
    ciudad_1 = tk.Label(vuelo_1, text=origen, bg="white")
    ciudad_1.grid(row=1, column=2, padx=5, pady=1)

    precio = tk.Frame(vuelo_1, bg="gray", relief=tk.FLAT)
    precio.grid(row=0, column=3, padx=5, pady=1)

    desde = tk.Label(precio, text="Desde", bg="gray", relief=tk.FLAT)
    desde.grid(row=0, column=0, padx=5, pady=1)

    precio_m = precio_menor[0]
    valor = tk.Label(precio, text=precio_m, bg="gray", relief=tk.FLAT)
    valor.grid(row=1, column=1, padx=5, pady=1)

    #------Segundo posible------------
    vuelo_2 = tk.Button(barra_9, relief=tk.RAISED)
    vuelo_2.pack(pady=5, padx=10, fill="x")

    #------Tercer posible-------------
    vuelo_3 = tk.Button(barra_9, relief=tk.RAISED)
    vuelo_3.pack(pady=5, padx=10, fill="x")

    #-------Botón de selección-------
    btn_pasar = tk.Button(ventana_ofertas, text="Seleccionar", bg="red", fg="white", command=nueva_ventana_reserva)
    btn_pasar.pack(pady=10, padx=10, side="right")

    #-------Botón de volver-------
    btn_volver = tk.Button(ventana_ofertas, text="Atrás", bg="red", fg="white", command=volver_2)
    btn_volver.pack(pady=10, padx=0, side="right")

def volver_3():
    ventana_reserva.destroy()
    ventana_ofertas.deiconify()

def nueva_ventana_reserva():
    global ventana_reserva
    ventana_ofertas.withdraw()

    ventana_reserva = tk.Toplevel(window) #Abrir la ventana nueva encima de la ventana principal
    ventana_reserva.title("Sky-Voyage")
    ventana_reserva.geometry("800x500")
    ventana_reserva.config(bg = "white")
    ventana_reserva.resizable(0, 0)
    ventana_reserva.iconbitmap("avion.ico")

    # ------- Se crea un lienzo---------
    lienzo_5 = tk.Frame(ventana_reserva, bg = "white")
    lienzo_5.pack(pady=40, fill="x")

    # ------ Barra de ida -------
    barra_10 = tk.Frame(lienzo_5, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_10.pack(pady=0, padx=20, fill="x")

    #------ boton de Ida---------
    ida_reserva = tk.Label(barra_10, text= "   Ida:", relief="flat", bg="white", fg="black",highlightbackground="white", highlightthickness=1)
    ida_reserva.pack(side="left", padx=5, pady=5)

    text = (f"{ori} a {des}")
    viaje_ida = tk.Label(barra_10, text=text , relief="flat", bg="white", fg="black",highlightbackground="white", highlightthickness=1)
    viaje_ida.pack(side="left", padx=0, pady=8)

    btn_pas = tk.Button(ventana_reserva, text="Seleccionar", bg="red", fg="white", command=nueva_ventana_registro)
    btn_pas.pack(pady=10, padx=30, side="right")

    btn_vol = tk.Button(ventana_reserva, text="Atrás", bg="red", fg="white", command=volver_3)
    btn_vol.pack(pady=10, padx=30, side="right")

def volver_4():
    ventana_registro.destroy()
    ventana_reserva.deiconify()

def nueva_ventana_registro():
    global ventana_registro
    ventana_reserva.withdraw()

    ventana_registro = tk.Toplevel(window) #Abrir la ventana nueva encima de la ventana principal
    ventana_registro.title("Sky-Voyage")
    ventana_registro.geometry("800x400")
    ventana_registro.config(bg = "white")
    ventana_registro.iconbitmap("avion.ico")
    ventana_registro.resizable(0, 0)

    lienzo_5 = tk.Frame(ventana_registro, bg="white")
    lienzo_5.pack(pady=40, fill="x")

    cua_regist = tk.Frame(lienzo_5, bg="white")
    cua_regist.pack(fill="x", padx=40, pady=0)
    registro_t = tk.Label(cua_regist, text="Realizar un vuelo", bg="white", relief="flat")
    registro_t.pack(side="left", padx=40, pady=0)

    recuadro = tk.Frame(lienzo_5, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    recuadro.pack(fill="x", pady=10, padx=10)

    genero_c = tk.Frame(recuadro, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    genero_c.grid(row=0, column=0, padx=1, pady=5)
    genero_t = tk.Label(genero_c, text="Género", bg="white")
    genero_t.grid(row=0, column=0, padx=1, pady=5)
    genero = ttk.Combobox(genero_c, values=["Masculino", "Femenino","Otro"])
    genero.current(0)
    genero.grid(row=0, column=1, padx=1, pady=5)

    primer_n= tk.Frame(recuadro, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    primer_n.grid(row=0, column=1, padx=1, pady=5)
    nombre_t = tk.Label(primer_n, text="Primer Nombre", bg="white")
    nombre_t.grid(row=0, column=0, padx=1, pady=5)
    nombre = tk.Entry(primer_n)
    nombre.grid(row=0, column=1, padx=1, pady=5)

    primer_a = tk.Frame(recuadro, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    primer_a.grid(row=0, column=2, padx=1, pady=5)
    apellido_t = tk.Label(primer_a, text="Primer Apellido", bg="white")
    apellido_t.grid(row=0, column=0, padx=1, pady=5)
    apellido = tk.Entry(primer_a)
    apellido.grid(row=0, column=1, padx=1, pady=5)

    iden_c = tk.Frame(recuadro, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    iden_c.grid(row=1, column=0, padx=5, pady=5)
    identi_t = tk.Label(iden_c, text="Identificación", bg="white")
    identi_t.grid(row=0, column=0, padx=1, pady=5)
    identi = tk.Entry(iden_c)
    identi.grid(row=0, column=1, padx=1, pady=5)

    naci_c = tk.Frame(recuadro, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    naci_c.grid(row=1, column=1, padx=1, pady=5)
    naci_t = tk.Label(naci_c, text="Nacionalidad", bg="white")
    naci_t.grid(row=0, column=0,columnspan=1, padx=5, pady=5)
    nacionalidad = tk.Entry(naci_c)
    nacionalidad.grid(row=0, column=1, padx=1, pady=5)
    
    fecha_c= tk.Frame(recuadro, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    fecha_c.grid(row=1, column=2, padx=1, pady=5)
    fecha_t = tk.Label(fecha_c, text="Fecha Nacimiento", bg="white", width=20)
    fecha_t.grid(row=0, column=0, padx=1, pady=5)
    fecha = tk.Entry(fecha_c)
    fecha.grid(row=0, column=1, padx=1, pady=5)

    tele_c= tk.Frame(recuadro, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    tele_c.grid(row=2, column=0, padx=1, pady=5)
    tele_t = tk.Label(tele_c, text="Teléfono", bg="white")
    tele_t.grid(row=0, column=0, padx=1, pady=5)
    telefono = tk.Entry(tele_c)
    telefono.grid(row=0, column=1, padx=1, pady=5)

    correo_c= tk.Frame(recuadro, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    correo_c.grid(row=2, column=1, padx=1, pady=5)
    correo_t = tk.Label(correo_c, text="Correo electrónico", bg="white", width=20)
    correo_t.grid(row=0, column=0, padx=1, pady=5)
    correo = tk.Entry(correo_c)
    correo.grid(row=0, column=1, padx=1, pady=5)

    asis_c = tk.Frame(recuadro, bg="white", relief=tk.FLAT, highlightbackground="red", highlightthicknes=1)
    asis_c.grid(row=2, column=2, padx=1, pady=5)
    asis_t = tk.Checkbutton(asis_c, text="Asistencia en el vuelo", bg="white")
    asis_t.grid(row=0, column=0, padx=1, pady=5)

    continuar = tk.Button(recuadro, text="Continuar", bg="red", fg="white", command=nueva_ventana_tarjeta)
    continuar.grid(row=3, column=1, padx=5, pady=5)

    volver = tk.Button(recuadro, text="Atrás", bg="red", fg="white", command=volver_4)
    volver.grid(row=3, column=0, padx=5, pady=5)

def volver_5():
    ventana_tarjeta.destroy()
    ventana_registro.deiconify()

def nueva_ventana_tarjeta():
    global ventana_tarjeta
    ventana_registro.withdraw()

    ventana_tarjeta = tk.Toplevel(window) #Abrir la ventana nueva encima de la ventana principal
    ventana_tarjeta.title("Sky-Voyage")
    ventana_tarjeta.geometry("800x400")
    ventana_tarjeta.config(bg = "white")
    ventana_tarjeta.iconbitmap("avion.ico")
    ventana_tarjeta.resizable(0, 0)

    lienzo_6 = tk.Frame(ventana_tarjeta, bg="white")
    lienzo_6.pack(pady=40, fill="x")

    contenedor_1 = tk.Frame(lienzo_6, bg="white", highlightbackground="red", highlightthickness=1)
    contenedor_1.pack(side="left", pady=5, padx=1)
    contenedor_2 = tk.Frame(lienzo_6, bg="white", highlightbackground="red", highlightthickness=1)
    contenedor_2.pack(side="right", pady=5, padx=1)

    datos = tk.Label(contenedor_1, text="Datos de la tarjeta", bg="white")
    datos.pack(side="top", pady=5, padx=1)

    resumen = tk.Label(contenedor_2, text="Resumen de compra", bg="white")
    resumen.pack(side="top", pady=5, padx=1)



window.mainloop()
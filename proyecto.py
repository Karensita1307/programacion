# Proyecto final

import tkinter as tk #Se importa la libreria y se le da un título
from tkinter import *  # Librería que importa todos los módulos de la clase
from PIL import Image, ImageTk as itk #librería de imagenes
from tkinter import ttk # LLibrería para los combobox y mas comandos
from tkinter import messagebox, Canvas # Ventana emergente y dar geometria
from datetime import datetime# Para el tiempo
import random, string, re

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

def guardar_datos():
    global codigo, apellido
    codigo = codigo_entry.get()
    apellido = apellido_entry.get()
    datos_ingresados()

#------función de datos ingresados por el usuario--------
def datos_ingresados():
    usuario_registrado =[]
    codigo = codigo_entry.get() #Para guardar los datos de código
    apellido = apellido_entry.get() #Para guardar los datos de apellido
    with open("datos_usuario.txt", "r") as file:
        for line in file:
            usuario_registrado.append(line.strip().split(','),) #Cómo se guardan los datos en el txt
    if [codigo, apellido] in usuario_registrado:
        messagebox.showinfo(title="Bienvenido Usuario", message="Bienvenido de nuevo")
        nueva_ventana_vuelos()
    else:
        messagebox.showinfo(title="Usuario no encontrado", message="No se encuentra en la base de datos, por favor regístrese")
        nueva_ventana_registro()

def abrir_datos_registro():
    with open("registro.txt", "a") as file:
        datos_registro = [line.strip().split(",") for line in file]
    return datos_registro

vuelo2 = []
fecha = []
hora_salida = []
hora_llegada = []
valormin = []
valormmedio = []
valormmax = []
ciudad_origen = []
ciudad_destino = []

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

for i in range(len(matriz)):
    if matriz[i][0]:
        vuelo2.append(matriz[i][0])
    if matriz[i][1]:
        fecha.append(matriz[i][1])
    if matriz[i][2]:
        hora_salida.append(matriz[i][2])
    if matriz[i][3]:
        hora_llegada.append(matriz[i][3])
    if matriz[i][4]:
        valormin.append(matriz[i][4])
    if matriz[i][5]:
        valormmedio.append(matriz[i][5])
    if matriz[i][6]:
        valormmax.append(matriz[i][6])
    if matriz[i][7]:
        ciudad_origen.append(matriz[i][7])
    if matriz[i][8]:
        ciudad_destino.append(matriz[i][8])

def guardar_datos_registro():
    global ape, nom
    nom = nombre.get()
    ape = apellido.get()
    gen = genero.get()
    nac = nacionalidad.get()
    ide = identi.get()
    fec = fecha.get()
    asi = asis_t.get()
    cor = correo.get()
    tel = telefono.get()
    generar_codigo_checkin()

    if len(nom and ape and gen and nac and ide and fec and asi and cor and tel) != 0:
        with open("registro.txt", "a") as file:
            file.write(f"{nom},{ape},{gen},{nac},{ide},{fec},{asi},{cor},{tel}\n")
        nueva_ventana_vuelos()    
    else:
        messagebox.showwarning(title="Error", message="Llene todos los campos")

def generar_codigo_checkin():
    apellido = ape
    codigo = apellido[0] + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    with open("datos_usuario.txt", "a") as file:
        file.write(f"{codigo},{apellido}\n")
    messagebox.showinfo(title="Código", message=f"Tu código es {codigo}")
    return codigo

def validar():
    tele = telefono.get()
    corre = correo.get()
    contador = 0

    for i in corre:
        if i == "@":
            contador += 1
            if contador == 1 and (i == "."):
                contador += 1

    if tele.isdigit() and len(tele) == 10:
        guardar_datos_registro()
        if contador == 2:
            guardar_datos_registro()
        else:     
            messagebox.showwarning(title="Correo", message="Correo no válido")
    else:
        messagebox.showwarning(title="Número", message="Número no válido")
    corre = correo.get()

def nueva_ventana_registro():
    global ventana_registro, telefono, correo, nombre, apellido, identi, nacionalidad, fecha, asis_t, genero
    window.withdraw()

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
    asis_t = ttk.Combobox(asis_c, values=["Si", "No"])
    asis_t.grid(row=0, column=0, padx=1, pady=5)

    continuar = tk.Button(recuadro, text="Continuar", bg="red", fg="white", command=validar)
    continuar.grid(row=3, column=1, padx=5, pady=5)


def volver_1():
    ventana_vuelos.destroy()
    window.deiconify()

def nueva_ventana_vuelos():
    global ventana_vuelos, personas_cant, num, fecha_txt, origen_g, destino_g, fecha_g, personas_g
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
    num = personas_g.get()

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
    btn_volver = tk.Button(busqueda, text="Atrás", bg="red", fg="white", command=volver_1)
    btn_volver.grid(row=1, column=4, padx=5, pady=2)

def actualizar_fechas_disponibles():
    origen_seleccionado = origen_g.get()
    destino_seleccionado = destino_g.get()

    fechas_disponibles = set()
    for vuelo in matriz:
        if vuelo[7] == origen_seleccionado and vuelo[8] == destino_seleccionado:
            fechas_disponibles.add(vuelo[1])  # Añadir la fecha del vuelo si coincide con el origen y destino seleccionados

    # Actualizar las opciones de fecha
    fecha_txt['values'] = tuple(fechas_disponibles)

def guardar_selecciones():
    global ori, des, cant, fech
    des = destino_g.get()    
    ori = origen_g.get()
    cant = int(personas_cant.get())
    fech = fecha_g.get()

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

def volver_2():
    ventana_asientos.destroy()
    ventana_vuelos.deiconify()

def nueva_ventana_asientos():
    global ventana_asientos, color, clase
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
        posi = []
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
    btn_seleccionar = tk.Button(ventana_asientos, text="Seleccionar", bg="red", fg="white", command=mostrar_vuelos)
    btn_seleccionar.pack(pady=10, padx=10, side="right")

    #----------Botón volver----------
    btn_volver = tk.Button(ventana_asientos, text="Atrás", bg="red", fg="white", command=volver_2)
    btn_volver.pack(pady=10, padx=0, side="right")

    guardar_asientos = tk.Checkbutton(ventana_asientos, text="Guardar datos")
    guardar_asientos.pack(pady=10, padx=30, side="bottom")

precio_menor = []
precio_regular = []
precio_mayor = []
menor = []
regular = []
mayor = []

def precios():
    global hora_l, hora_s, valormi, valorme, valorma, codigo, origen_seleccionado, destino_seleccionado
    origen_seleccionado = origen_g.get()
    destino_seleccionado = destino_g.get()
    hora_s = []
    hora_l = []
    valormi = []
    valorme = []
    valorma = []
    codigo = []
    for i in range(len(matriz)): 
        if ciudad_origen[i] == origen_seleccionado and ciudad_destino[i] == destino_seleccionado  and fecha[i] == fecha_g.get():
            valormi.append(valormin[i])
            valorme.append(valormmedio[i])
            valorma.append(valormmax[i])
            codigo.append(vuelo2[i])
            hora_s.append(hora_salida[i])
            hora_l.append(hora_llegada[i])

def volver_3():
    ventana_vuelos.destroy()
    ventana_asientos.deiconify()

def mostrar_vuelos():
    global ventana_vuelos
    ventana_asientos.withdraw() 

    # Crear la nueva ventana
    ventana_vuelos = tk.Toplevel(window)
    ventana_vuelos.title("Sky-Voyage")
    ventana_vuelos.geometry("1000x500")
    ventana_vuelos.config(bg="white")
    ventana_vuelos.resizable(0, 0)
    ventana_vuelos.iconbitmap("avion.ico")

    # ------- Se crea un lienzo---------
    lienzo_4 = tk.Frame(ventana_vuelos, bg="white")
    lienzo_4.pack(pady=40, fill="x")

    # ------ Barra de ida -------
    barra_7 = tk.Frame(lienzo_4, bg="white", relief=tk.FLAT, highlightbackground="red", highlightthicknes=1)
    barra_7.pack(pady=0, padx=20, fill="x")

    #------ boton de Ida---------
    ida_ofertas = tk.Label(barra_7, text= "   Ida:", relief="flat", bg="white", fg="black")
    ida_ofertas.pack(side="left", padx=5, pady=5)

    text = (f"{ori} a {des}")
    viaje = tk.Label(barra_7, text=text , relief="flat", bg="white", fg="black")
    viaje.pack(side="left", padx=0, pady=8)

    #----Barra de ordenar por------
    barra_8 = tk.Frame(lienzo_4, bg="white", relief=tk.FLAT, highlightbackground="red", highlightthicknes=1)
    barra_8.pack(pady=0, padx=20, fill="x")

    #-------Barra para vuelos-------
    barra_9 = tk.Frame(lienzo_4, bg="white", relief=tk.FLAT, highlightbackground="red", highlightthicknes=1)
    barra_9.pack(pady=5, padx=20, fill="x")

    #------marco para los vuelos----
    marco_vuelos = tk.Frame(ventana_vuelos)
    marco_vuelos.pack(pady=20)

    vuelos = precios()
    
    for i in range(len(hora_s)):
        vuelo_frame = tk.Frame(marco_vuelos, relief=tk.RAISED, bg="white")
        vuelo_frame.pack(fill="x", pady=5)

        # Convertir las horas a objetos datetime
        hora_salida = datetime.strptime(hora_s[i], "%H:%M:%S")
        hora_llegada = datetime.strptime(hora_l[i], "%H:%M:%S")

        # Calcular la duración del vuelo
        duracion = hora_llegada - hora_salida
        minutos = duracion.seconds // 60  # Convertir la duración a minutos

        # Convertir los minutos a horas y minutos
        horas = minutos // 60
        minutos = minutos % 60

        destino = des[:3].upper() # .upper para pasarlo a mayusculas
        origen = ori[:3].upper() # .upper para pasarlo a mayusculas

        # detalles del vuelo
        if horas > 0:
            vuelo_title = tk.Label(vuelo_frame, text=f"""
    {hora_s[i]}________________ {hora_l[i]} 
    {origen}      {horas}h {minutos}m      {destino}
            """, bg="red", fg="white")
        else:
            vuelo_title = tk.Label(vuelo_frame, text=f"""
    {hora_s[i]}________________ {hora_l[i]} 
    {origen}        {minutos}m         {destino}
            """, bg="red", fg="white")
        vuelo_title.pack(side="left", padx=10)

        # Precio del vuelo
        vuelo_price = tk.Label(vuelo_frame, text=f"Desde COP {valormi[i]} hasta COP {valorma[i]}", font=("Arial", 12), bg="white", fg="black")
        vuelo_price.pack(fill="x", pady=10)

        # Botón de selección
        btn_seleccionar = tk.Button(vuelo_frame, text="Seleccionar", bg="red", fg="white", command=nueva_ventana_reserva)
        btn_seleccionar.pack(side="right", padx=10)

    btn_vol = tk.Button(ventana_vuelos, text="Atrás", bg="red", fg="white", command=volver_3)
    btn_vol.pack(pady=10, padx=30, side="bottom")

def volver_4():
    ventana_reserva.destroy()
    ventana_vuelos.deiconify()

def nueva_ventana_reserva():
    global ventana_reserva, paquete_text
    ventana_vuelos.withdraw() 

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

    viaje = tk.Label(barra_10, text="Detalles de compra:" , relief="flat", bg="white", fg="black")
    viaje.pack(side="left", padx=0, pady=8)

    barra_11 = tk.Frame(lienzo_5, bg="white", relief=tk.FLAT, highlightbackground='red', highlightthicknes=1)
    barra_11.pack(pady=0, padx=20, fill="x")

    # Mostrar el vuelo seleccionado
    vuelo_label = tk.Label(barra_11, text="Vuelo seleccionado:", bg="white")
    vuelo_label.pack(side="top", padx=0, pady=2)

    text = (f"{ori} a {des}")
    viaje = tk.Label(barra_11, text=text , relief="flat", bg="white", fg="black")
    viaje.pack(side="top", padx=0, pady=4)

    # Mostrar el paquete seleccionado
    paquete_label = tk.Label(barra_11, text="Paquete seleccionado:", bg="white")
    paquete_label.pack(side="top", padx=0, pady=4)

    texto = clase
    paquete_text = tk.Label(barra_11, text=texto, height=5, width=50, bg="white")
    paquete_text.pack(side="top", padx=0, pady=2)

    especifica = precio()
    espe = tk.Label(barra_11, text=especifica, height=5, width=50, bg="white")
    espe.pack(side="top", padx=0, pady=2)
    
    # Botón para continuar con el pago
    btn_continuar_pago = tk.Button(ventana_reserva, text="Continuar con el Pago", bg="red3", fg="white", command=nueva_ventana_tarjeta)
    btn_continuar_pago.pack(pady=20)

    btn_vol = tk.Button(ventana_reserva, text="Atrás", bg="red", fg="white", command=volver_4)
    btn_vol.pack(pady=20, padx= 5)

def precio():
    if clase == "Aluminio":
        aluminio = ("""
        1 artículo personal (bolso) (Debe caber debajo del asiento)
        1 equipaje de mano (10 kg)
        Equipaje de bodega (23 kg)
        Asiento Economy (Aleatoria-clasificado Aluminio)
        Cambios de vuelo (No es permitido)
        Reembolso (No es permitido)""")
        return aluminio
    elif clase == "Diamante":
        diamante = ("""
        1 artículo personal (bolso) (Debe caber debajo del asiento)
        1 equipaje de bodega (23 kg) (Debe caber en el compartimiento superior)
        1 equipaje de mano (10 kg) (Entrega el equipaje en el counter)
        Asiento Economy (Filas específicas disponibles de manera aleatoria)
        Cambios de vuelo (No es permitido)
        Reembolso (No es permitido)""")
        return diamante
    else:
        premium = ("""
        1 artículo personal (bolso) (Debe caber debajo del asiento)
        1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)
        1 equipaje de bodega (23 kg) (Entrega el equipaje en el counter)
        Asiento Plus (Sujeto a disponibilidad-clasificado Premium)
        Cambios de vuelo (Sin cargo por cambio, antes del vuelo)
        Reembolso (No es permitido)""")
        return premium
    
def volver_5():
    ventana_tarjeta.destroy()
    ventana_reserva.deiconify()

def nueva_ventana_tarjeta():
    global ventana_tarjeta
    ventana_reserva.withdraw() 

    ventana_tarjeta = tk.Toplevel(window)
    ventana_tarjeta.title("Sky-Voyage")
    ventana_tarjeta.geometry("800x400")
    ventana_tarjeta.iconbitmap("avion.ico")
    ventana_tarjeta.resizable(0, 0)

    #----Crear el cuadro para los datos de la tarjeta----
    tarjeta = tk.Frame(ventana_tarjeta, bg='white', relief=tk.FLAT, highlightbackground="red", highlightthicknes=1)
    tarjeta.pack(pady=20, padx=10, side="left")
    
    datos = tk.Label(tarjeta, text="Datos de la tarjeta" ,bg='white', relief=tk.FLAT)
    datos.pack(pady=5, padx=20, side="top")

    # Nombre del titular
    nombre_titular = tk.Label(tarjeta, text="Nombre del Titular:", bg="white")
    nombre_titular.pack(pady=5, padx=20, side="top")
    entrada_nombre = tk.Entry(tarjeta)
    entrada_nombre.pack(pady=5, padx=20, side="top")

    # Número de tarjeta
    lbl_numero_tarjeta = tk.Label(tarjeta, text="Número de Tarjeta:", bg="white")
    lbl_numero_tarjeta.pack(pady=5, padx=20, side="top")
    entrada_numero_tarjeta = tk.Entry(tarjeta)
    entrada_numero_tarjeta.pack(pady=5, padx=20, side="top")

    # Fecha de expiración
    lbl_fecha_expiracion = tk.Label(tarjeta, text="Fecha de Expiración:", bg="white")
    lbl_fecha_expiracion.pack(pady=5, padx=20, side="top")

    opciones_mes = ["Mes", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    entrada_mes = ttk.Combobox(tarjeta, values=opciones_mes)
    entrada_mes.current(0)
    entrada_mes.pack(pady=5, padx=5, side="left")

    opciones_anio = ["Año", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032"]
    entrada_anio = ttk.Combobox(tarjeta, values=opciones_anio)
    entrada_anio.current(0)
    entrada_anio.pack(pady=5, padx=5, side="left")

    # CVV
    cvv = tk.Label(tarjeta, text="CVV:", bg="white")
    cvv.pack(pady=5, padx=20, side="top")
    entrada_cvv = tk.Entry(tarjeta)
    entrada_cvv.pack(pady=5, padx=20, side="top")

    def validar_numero_tarjeta():
        numero_tarjeta = entrada_numero_tarjeta.get()
        if len(numero_tarjeta) != 16:
            messagebox.showwarning(title="Error", message="El número de tarjeta debe tener 16 dígitos")
            return False
        return True

    def validar_cvv():
        cvv = entrada_cvv.get()
        if len(cvv) != 3:
            messagebox.showwarning(title="Error", message="El CVV debe tener 3 dígitos")
            return False
        return True
    
    def calcular_total_pagar():
        global valor_paquete
        total_pagar = valor_paquete * int(cant)
        return total_pagar

    #----Crear el cuadro para los datos de la tarjeta----
    cuenta = tk.Frame(ventana_tarjeta, bg='white', relief=tk.FLAT, highlightbackground="red", highlightthicknes=1)
    cuenta.pack(pady=20, padx=10, side="left")

    # Mostrar el vuelo seleccionado
    vuelo_label = tk.Label(cuenta, text="Vuelo seleccionado:", bg="white")
    vuelo_label.pack(pady=5, padx=20, side="top")

    text = (f"{ori} a {des}")
    viaje = tk.Label(cuenta, text=text , relief="flat", bg="white", fg="black")
    viaje.pack(pady=5, padx=20, side="top")

    # Mostrar el número de personas
    personas_label = tk.Label(cuenta, text="Número de personas:", bg='white')
    personas_label.pack(pady=5, padx=20, side="top")

    textt = cant
    viaje = tk.Label(cuenta, text=textt , relief="flat", bg="white", fg="black")
    viaje.pack(pady=5, padx=20, side="top")

    # Mostrar el total a pagar
    total_label = tk.Label(cuenta, text="Valor unitario:", bg='white')
    total_label.pack(pady=5, padx=20, side="top")

    textto = valor_paquete
    viaje = tk.Label(cuenta, text=textto , relief="flat", bg="white", fg="black")
    viaje.pack(pady=5, padx=20, side="top")

    # Mostrar el total a pagar
    total_label = tk.Label(cuenta, text="Total a pagar:", bg='white')
    total_label.pack(pady=5, padx=20, side="top")

    texto = calcular_total_pagar(valor_paquete)
    viaje = tk.Label(cuenta, text=texto , relief="flat", bg="white", fg="black")
    viaje.pack(pady=5, padx=20, side="top")
    
    # Botón de pagar
    pagar_button = tk.Button(ventana_tarjeta, text="Pagar", bg='red3', fg='black', command=nueva_ventana_ticket)
    pagar_button.bind("<Button-1>", lambda event: validar_numero_tarjeta(), validar_cvv())
    pagar_button.pack(pady=5, padx=10, side="bottom")
    
    btn_vol = tk.Button(ventana_tarjeta, text="Atrás", bg="red", fg="white", command=volver_5)
    btn_vol.pack(pady=5, padx=10, side="bottom")

def crear_texto_rotado(canvas, texto, x, y, angulo, font=("Helvetica", 12, "bold"), fill="white"):
    # -------- Crear texto rotado ---------
    canvas.create_text(x, y, text=texto, angle=angulo, fill=fill, font=font, anchor="w")

def nueva_ventana_ticket():
    ventana_tarjeta.withdraw() 

    ventana_ticket = tk.Toplevel(window)  
    ventana_ticket.title("Sky-Voyage")
    ventana_ticket.geometry("700x280")
    ventana_ticket.config(bg="white")
    ventana_ticket.resizable(0, 0)

    # -------- lienzo --------------
    lienzo9 = tk.Frame(ventana_ticket, bg="white")
    lienzo9.pack(pady=10, padx=10)

    # -------- barra lateral --------------
    barra_lateral = tk.Frame(lienzo9, bg="red", width=80)
    barra_lateral.pack(side = "left", fill="y")
    
    # ---------- canvas en el lateral ----------
    canvas_lateral = tk.Canvas(barra_lateral, bg="red", width=80, height=280)
    canvas_lateral.pack()
    
    # ----------------- posicion del texto lateral ---------------------
    crear_texto_rotado(canvas_lateral, "Sky-Voyage", 40, 175, 90, font=("Helvetica", 12, "bold"), fill="white")

    # -------- barra superiro ------------
    encabezado = tk.Frame(lienzo9, bg="black", height=40)
    encabezado.pack(fill="x")
    tk.Label(encabezado, text="Pase de abordaje", bg="black", fg="white", font=("Helvetica", 12)).pack(pady=5)

    # ------------ Contenido principal ------------------
    contenido = tk.Frame(lienzo9, bg="white")
    contenido.pack(pady=10, padx=10, fill="both", expand=True)


    # Mostrar los valores de los campos de texto
    tk.Label(contenido, text="Nombre pasajero:", bg="white", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=5)
    tk.Label(contenido, text=f"{nom} {ape}", bg="white", font=("Helvetica", 12)).grid(row=0, column=1, sticky="w", pady=5)

    tk.Label(contenido, text="Origen:", bg="white", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", pady=5)
    tk.Label(contenido, text=ori, bg="white", font=("Helvetica", 12)).grid(row=1, column=1, sticky="w", pady=5)

    tk.Label(contenido, text="Destino:", bg="white", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", pady=5)
    tk.Label(contenido, text=des, bg="white", font=("Helvetica", 12)).grid(row=2, column=1, sticky="w", pady=5)

    tk.Label(contenido, text="Vuelo:", bg="white", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", pady=5)
    tk.Label(contenido, text=vuelo2, bg="white", font=("Helvetica", 12)).grid(row=3, column=1, sticky="w", pady=5)

    tk.Label(contenido, text="Fecha:", bg="white", font=("Helvetica", 12)).grid(row=1, column=2, sticky="w", padx=20)
    tk.Label(contenido, text=fech, bg="white", font=("Helvetica", 12)).grid(row=1, column=3, sticky="w", pady=5)

    tk.Label(contenido, text="Hora:", bg="white", font=("Helvetica", 12)).grid(row=2, column=2, sticky="w", padx=20)
    tk.Label(contenido, text=hora_s, bg="white", font=("Helvetica", 12)).grid(row=2, column=3, sticky="w", pady=5)


window.mainloop()
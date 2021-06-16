#-*- coding: UTF-8 -*-
#---------------------------------------
# Programa desarrollado por: C4P1T4N4Z0
# Breaksecurity - OBHE
# --------------------------------------
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter import ttk
from tkinter import *
import tkinter as tk

import pandas as pd
import sqlite3 



#------------------------------------------------------------------
# esto es de bufferoverflou 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#------------------------------------------------------------------

#lib de navegador
from selenium import webdriver
import os
import platform
from selenium.webdriver.common.action_chains import ActionChains
#---------------------------------------------------
# Agregado recien
from selenium.webdriver.common.keys import Keys 

#---------------------------------------------------


#lib tiempo
import time 

#---------------------------------------------------
# MI LIBRERIA
from cntrol import *
#from tecla import *
#---------------------------------------------------

#lib para compiar
#import pyperclip as clipboard

#Para verificar carga
#from bs4 import BeautifulSoup
#import requests

class Whatsend:

	db_name = 'database.db'

	def __init__(self,window):
		global entry
		#Configuracion de la ventana
		#Aplicando geometria
		

		#Actualizo la ventana
		window.update()

		#Menu 
		menu = Menu(window)
		window.config(menu = menu)
		#MENU 1
		subMenu = Menu(menu)
		menu.add_cascade(label = "Archivo",menu = subMenu)
		subMenu.add_command(label = "Cargar Excel", command = self.cargar_excel)

		subMenu.add_separator()
		subMenu.add_command(label = "Salir", command = self.fun_Cerrar)

		#MENU2
		subMenu2 = Menu(menu)
		menu.add_cascade(label = "Configurar", menu = subMenu2)
		subMenu2.add_command(label = "WhatsApp", command = self.Config_what)

		subMenu2.add_separator()
		subMenu2.add_command(label = "archivo", command = self.Config_adj)

		subMenu2.add_separator()
		subMenu2.add_command(label = "navegador", command = self.Config_nave)


		#MENU3
		subMenu3 = Menu(menu)
		menu.add_cascade(label = "Acerca", menu = subMenu3)
		subMenu3.add_command(label = "About", command = self.Texto_)





		# instancias de window 
		self.wind1 = Frame(window)
		self.wind1.pack(side = "left", anchor = "n", padx=2,pady=2,ipadx=2,ipady=2)

		#self.wind1.config(width = 100, height = 100)


		# Contenedor Frame
		frame1 = LabelFrame(self.wind1, text = 'Label 1 Botones')
		frame1.grid(row = 0, column = 0, columnspan =2, pady = 1)        #Grilla 


		frame2 = LabelFrame(self.wind1, text = 'label 2 Tabla')
		#frame2.config(width = 10, height = 100)
		frame2.grid(row = 1, column = 0, columnspan =2, pady = 1)        #Grilla 
		

		frame3 = LabelFrame(self.wind1, text = 'label 3 Archivo ')
		frame3.grid(row = 0, column = 2, columnspan =2, pady = 1)        #Grilla

		frame4 = LabelFrame(self.wind1, text = 'label 4 botones')
		frame4.grid(row = 0, column = 7, columnspan =2, pady = 1)        #Grilla

		# Crear caja de texto.
		#self.entry = ttk.Entry(frame3,width = 15,text = 'Mensaje: ').grid(row = 1, column = 3)
		
		# Posicionarla en la ventana.
		#self.entry.place(x=20, y=50)
		
		#Mensaje Input
		#Label(frame3,width = 15,text = 'Mensaje: ').grid(row = 1, column = 3)
		#self.text = tk.Entry(frame3)
		#self.text = Text(frame3)
		#self.text.config(width = 30, height = 3)
		


		#-------------------------------------------------------------
		#scr=Scrollbar(frame3, orient=VERTICAL, command=self.text.yview)
		#scr.grid(row=0, column=2, rowspan=15, columnspan=1, sticky=NS)
		#-------------------------------------------------------------

		'''
		label = Label(frame3, text="Nombre  del archivo")
		label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
		entry = Entry(frame3)
		entry.grid(row=0, column=1, padx=5, pady=5)
		entry.config(justify="right", state="normal")
		
		'''
		#self.text.grid(row=1, column=0)
		#self.text.config(yscrollcommand=scr.set, font=('Arial', 8, 'bold', 'italic'))
		#self.text.focus()
		#self.text.grid(row = 0,column=0, padx=5,pady=5,ipadx=5,ipady=1)


		#Button Excel
		boton1 = Button(frame1,width = 10, height = 5,text = 'Nuevo',command = self.get_dato).grid(row = 1,column = 1, columnspan = 1)
		boton2 = Button(frame1,width = 10, height = 5,text = 'Importar',command = self.cargar_excel).grid(row = 1,column =2, columnspan = 1)
		boton3 = Button(frame1,width = 10, height = 5,text = 'Exportar',command = self.cargar_excel).grid(row = 1,column =3, columnspan = 1)
		boton4 = Button(frame1,width = 10, height = 5,text = 'Limpiar',command = self.clear_table).grid(row = 1,column =4, columnspan = 1)
		boton5 = Button(frame1,width = 10, height = 5,text = 'Subir Imagen',command = self.F_archivo).grid(row = 1,column =5, columnspan = 1)

		#Button2
		#boton6 = Button(frame2,width = 10, height = 5, text = 'C2',command = self.cargar_excel).grid(row = 1,column = 0, columnspan = 2)
		
		#boton6 = Button(frame3,width = 15, height = 3,text = 'Nuevo Mensaje',command ='').grid(row = 1,column = 3, columnspan = 1)
		#boton7 = Button(frame3,width = 15, height = 3,text = 'Eliminar Mensaje',command = '').grid(row = 1,column =4, columnspan = 1)

		#boton8 = Button(frame4,width = 15, height = 5,text = 'Filtrar numeros',command = '').grid(row = 1,column =8, columnspan = 1)
		boton9 = Button(frame4,width = 15, height = 5,text = 'Numeros Validos',command = self.Numeros_validos).grid(row = 1,column =9, columnspan = 1)
		#boton10 = Button(frame4,width = 15, height = 5,text = 'Cuentas',command = self.cargar_excel).grid(row = 1,column =10, columnspan = 1)
		#boton11 = Button(frame4,width = 15, height = 5,text = 'Configuracion',command = self.cargar_excel).grid(row = 1,column =11, columnspan = 1)



		#Tabla
		self.title = Label(frame2,width = 35, text = "WhatsApp números", background = "#6ce52e", font=("Helvetica", 16)).grid(row = 2, column = 0)

		#Label(frame2, text = "WhatsApp números" , background = "#FFFFFF", font =("Arial", 12)).grid(row = 2, column = 0)
		
		self.tree = ttk.Treeview(frame2, height =28, columns =("ColName","ColTelf","ColEsta"))

		self.tree.grid(row = 3, column = 0, columnspan = 2)

		self.tree.heading('#0',text = 'Indice',anchor = 'w')
		self.tree.heading('ColName', text = 'Nombre',anchor = 'w')
		self.tree.heading('ColTelf', text = 'Telefono',anchor = 'w')
		self.tree.heading('ColEsta', text = 'Estado',anchor = 'w')

		self.tree.column('#0', minwidth = 50, width = 50, stretch = False)
		self.tree.column('ColName', minwidth = 150, width = 150, stretch = False)
		self.tree.column('ColTelf', minwidth = 100, width = 100, stretch = False)
		self.tree.column('ColEsta', minwidth = 100, width = 100, stretch = False)
		#Tabla


	

	'''
	-----------------------------------------------------
	-----		 Funciones de todo los eventos   --------
	-----------------------------------------------------
	'''
	def Texto_(self):		
		tex = entry.get()
		return tex

	def fun_Cerrar(self):
		if messagebox.askokcancel("Salir", "¿Quieres salir papú :( ?"):
			window.destroy()


	def about(self):
		messagebox.showinfo(message = "Primo, este programa te permitira llegar mas rapido a muchos clientes. \n Siguenos en facebook: BreakSecurity - OBHE", title = "Whatsend")

	'''
	-----------------------------------------------------
	-----		 Funciones de todo los metodos Excel  ---
	-----------------------------------------------------
	'''
	def cargar_excel(self):
		global archivo_excel

		fname = askopenfilename(filetypes=(("Solo archivos Excel","*.xlsx;*.csv"),
										   ("todo los archivos","*.*")))

		if fname:
			try:
				archivo_excel = pd.read_excel(str(fname))
				messagebox.showinfo(message = "Listo pariente ya se cargo el Excel", title = "Cargar Excel")
		
				self.show_datos()

			except:
				showerror("Problema al abrir Excel", "Fallo pariente al leer el archivo \n'%s"%fname)
			return	


	def F_archivo(self):
		global archi_vo
		farchi = askopenfilename(filetypes=(("Solo archivos ","*.gif;*.png;*.jpg;*.mp4;*.3gpp;*.quicktime"),
										   ("todo los archivos","*.*")))
		if farchi:
			try:
				archi_vo = str(farchi)
				print(archi_vo)
				messagebox.showinfo(message = "Listo pariente ya se cargo", title = "subir archivo")

			except:
				showerror("Problema al abrir archivo", "Fallo pariente al subir tu archivo \n'%s"%farchi)
			return

	'''
	---------------------------------------------------------
	-----		 Funciones de todo los metodos de tabla  ----
	---------------------------------------------------------
	'''
	def clear_table(self):
		#iniciando la tabla y limpiando los datos
		rec = self.tree.get_children()
		for elemento in rec:
			self.tree.delete(elemento)

	def show_datos(self):
		#iniciando la tabla y limpiando los datos
		rec = self.tree.get_children()
		for elemento in rec:
			self.tree.delete(elemento)

		#Insertando datos en tabla
		df = pd.DataFrame(archivo_excel)
		
		#print(len(df))
		#for x in range(len(df)):
		#	print(df.loc[x, df.columns[0]])
		#print(len(df.columns[0]))
		
		for i in range(len(df)):
		    
			self.tree.insert('', 0,text = str(i + 1) , value = (df.loc[i, df.columns[0]], df.loc[i, df.columns[1]], "Pendiente"))


			'''
			#guardo en la DataBase
			consulta = 'INSERT INTO Cliente VALUES (NULL,?,?,?)'
			parametros = (df.loc[i, df.columns[0]], str(df.loc[i, df.columns[1]]), "Pendiente")
			self.run_consulta(consulta, parametros)
			'''


	#conecion a la DB
	def run_consulta(self,consulta,parametros = ()):
		with sqlite3.connect(self.db_name) as conn:
			cursor = conn.cursor()   				#para saber en que posicion estoy en la DB
			resultado = cursor.execute(consulta,parametros)
			conn.commit()     #para ejecutar la funcion
		return resultado
		 
	def get_dato(self):
		#iniciando la tabla y limpiando los datos
		rec = self.tree.get_children()
		for elemento in rec:
			self.tree.delete(elemento)

		#consultando los datos
		consulta = 'SELECT * FROM Cliente'
		db_rows = self.run_consulta(consulta)
		

		# un ciclo para recorrer todos los datos de DB

		for row in db_rows:
			self.tree.insert('',0,text = row[0], value = (row [1],row[2], row[3]))



	'''
	---------------------------------------------------------
	-----		 Funciones de todas las configuraciones  ----
	---------------------------------------------------------
	'''
	def Config_what(self):
		Config_whatsapp()

	def Config_adj(self):
		Config_adjuntar()

	def Config_nave(self):
		self.options = webdriver.ChromeOptions()
		#Aqui hay que modificar para que ingrese por teclado 
		self.options.add_argument('--profile-directory=Profile 2')
		self.driver = webdriver.Chrome(chrome_options=self.options)
		self.driver.get('https://api.whatsapp.com/send/?phone=591')		
		Config_navegador()
		self.driver.close()
	'''
	---------------------------------------------------------
	-----		 Funciones de todo los metodos del envio ----
	---------------------------------------------------------
	'''

	def Numeros_validos(self):
		df = pd.DataFrame(archivo_excel)
		count = (len(df.columns[1]) -2) 
		print(count)
		#archivo_reporte = open('Numeros enviados.txt','w')
		archivo_reporte = open('reporte.csv','w')
		self.options = webdriver.ChromeOptions()
		#Aqui hay que modificar para que ingrese por teclado 
		self.options.add_argument('--profile-directory=Profile 2')
		self.driver = webdriver.Chrome(chrome_options=self.options)
		#self.driver.get('https://api.whatsapp.com/send/?phone=591')
		con_num = 0
		for i in range(len(df)):
			numero = df.loc[i,df.columns[1]]
			self.driver.get('https://api.whatsapp.com/send/?phone=591'+str(numero))
			print('https://api.whatsapp.com/send/?phone=591'+str(numero) + 'estado: Enviado')

			time.sleep(1)
			clik_url()
			time.sleep(2)
			#tecla_()	
			
			enviar_Imagen_sin_mensaje()		 
			time.sleep(1)
			pegar_mensaje()
			ir_navegador()
			con_num = con_num + 1 
			
			s = str(numero) + '=> mensaje enviado \n'
			archivo_reporte.write(s)
			s = ''
		self.driver.quit()
		archivo_reporte.close()
		messagebox.showinfo(message = "PARIENTE termine de enviar a  " + str(con_num)+ " numeros de WhatsApp", title = "Envio de mensajes PAPU ")
if __name__ == "__main__":
	window = Tk()
	window.title("WhatSend")
	aplication = Whatsend(window)
	window.geometry("1200x700") 
	window.resizable(0,0)
	window.mainloop()


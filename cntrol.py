from tkinter import messagebox as mb
import pyautogui
import time 


def enviar_Imagen_sin_mensaje():
    #----------------------------------------------------------------------------------
    # Habilitar para otros equipos
    #screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
    #print(pyautogui.size())


    #time.sleep(6)  
    #currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    #print(str(pyautogui.position()) +' posicion del mouse')
    #----------------------------------------------------------------------------------
    # (width=1920, height=1080) Tamaño de mi pantalla
    #      (x=668, y=986)       posicion del mouse, para el archivo de whatsapp
    #time.sleep(5)

    #pyautogui.click(668, 986)
    pyautogui.click(ejeX_adj, ejeY_adj)
    time.sleep(2)  
    #print(str(pyautogui.position()) +' posicion del mouse despues del click')
    #pyautogui.click(666, 899)
    pyautogui.click(ejeX_adj_archivo, ejeY_adj_archivo)

    #(x=666, y=899) posicion del mouse despues del click
 
    #pyautogui.write('team')
    
    pyautogui.write('img') # cambiar por el nombre de la imagen
    time.sleep(2)  
    pyautogui.press('enter')
    time.sleep(2)  

    # Aqui para el mensaje
    pyautogui.press('enter')



def enviar_Mensaje():
    pyautogui.write('memensaje sin salto de linea') 
    time.sleep(2)


def ir_navegador():
    pyautogui.click(ejeX_nav,ejeY_nav) 

def clik_url(): 
    pyautogui.click(ejeX_nav_url,ejeY_nav_url) 
    pyautogui.press('enter')
    #time.sleep(2)
    #pyautogui.click(ejeX_nav_url_open_what ,ejeY_nav_url_open_what)

def pegar_mensaje():
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v') # convinacion de teclas para salto de linea
    time.sleep(2)
    pyautogui.press('enter')




def Mensaje_Imagen():
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v') # convinacion de teclas para salto de linea
    time.sleep(2)

    pyautogui.click(668, 986)
    time.sleep(1)  
    #print(str(pyautogui.position()) +' posicion del mouse despues del click')
    pyautogui.click(666, 899)

    #(x=666, y=899) posicion del mouse despues del click
 
    #pyautogui.write('team')
    #pyautogui.write('Lucia') #prueba para lucia, cambiar por el nombre de la imagen
    pyautogui.write('img') #prueba para Sergio, cambiar por el nombre de la imagen
    time.sleep(1)  
    pyautogui.press('enter')
    time.sleep(2) 
    pyautogui.press('enter') # Para enviar todo




def Config_whatsapp():
    global ejeX 
    global ejeY
    mb.showinfo("Configuración WhatsApp", "Por favor posiciona el mouse sobre el icono de WhatsApp, hasta muestre resultado")

    time.sleep(6) 
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    mb.showinfo("Configuración", str(pyautogui.position()) +' posicion del icono de WhatsApp')
    ejeX = currentMouseX
    ejeY = currentMouseY


def Config_adjuntar():
    global ejeX_adj
    global ejeY_adj

    mb.showinfo("Configuración Adjuntar", "Por favor posiciona el mouse sobre adjuntar de whatsapp, hasta muestre resultado")

    time.sleep(6) 
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    mb.showinfo("Configuración", str(pyautogui.position()) +' posicion del icono de adjuntar')
    ejeX_adj = currentMouseX
    ejeY_adj = currentMouseY 


    global ejeX_adj_archivo
    global ejeY_adj_archivo
    mb.showinfo("Configuración Adjuntar", "Por favor posiciona el mouse sobre lo que quiera adjuntar: Foto, video, documento, hasta muestre resultado")
    time.sleep(6) 
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    mb.showinfo("Configuración", str(pyautogui.position()) +' posicion del icono a adjuntar')
    ejeX_adj_archivo = currentMouseX
    ejeY_adj_archivo = currentMouseY 

def Config_navegador():
    global ejeX_nav 
    global ejeY_nav
    mb.showinfo("Configuración Navegador", "Por favor posiciona el mouse sobre icono de chromiun, hasta muestre resultado")

    time.sleep(6) 
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    mb.showinfo("Configuración", str(pyautogui.position()) +' posicion del icono de WhatsApp')
    ejeX_nav = currentMouseX
    ejeY_nav = currentMouseY 


    global ejeX_nav_url 
    global ejeY_nav_url
    mb.showinfo("Configuración Navegador", "Por favor posiciona la url de chromiun, hasta muestre resultado")
    time.sleep(6) 
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    mb.showinfo("Configuración", str(pyautogui.position()) +' posicion del icono de WhatsApp')
    ejeX_nav_url = currentMouseX
    ejeY_nav_url = currentMouseY



    global ejeX_nav_url_open_what 
    global ejeY_nav_url_open_what
    mb.showinfo("Configuración Navegador", "Por favor posiciona el mouse sobre Abrir WhatsApp, hasta muestre resultado")
    time.sleep(6) 
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    mb.showinfo("Configuración", str(pyautogui.position()) +' posicion del Abrir con WhatsApp')
    ejeX_nav_url_open_what = currentMouseX
    ejeY_nav_url_open_what = currentMouseY  

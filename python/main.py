import mysql.connector
import tkinter
from tkinter import ttk
from tkinter import *
import tkinter as tk


# Conexion con la base de datos
try:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='contacts'
    )
    print('Conexion con la base de datos establecida')
except:
    print('Conexion fallida con la base de datos')

def main_page():
    window = tkinter.Tk()
    window.title('Registro de contactos')
    
    
    window.geometry('500x300')
    tkinter.Label(window, text='Registro de contactos').pack(pady=5)
    tkinter.Label(window, text='Introduce el nombre completo').pack(pady=5)
    inpt1 = tkinter.Entry(window)
    inpt1.pack(pady=5)
    tkinter.Label(window, text='Introduce el numero de telefono').pack(pady=5)
    inpt2 = tkinter.Entry(window)
    inpt2.pack(pady=5)
    def upload():
        name = inpt1.get()
        num = inpt2.get()
        user = cbox.get()
        if(len(name) > 50):
            alert.config(text='Error: El nombre contiene mas de 50 caracteres.')
        if(len(num) > 9):
            alert.config(text='Error: El numero contiene mas de 9 caracteres.')
            return()
        if(len(num) < 9):
            alert.config(text='Error: El numero contiene menos de 9 caracteres.')
            return()
        try:
            cursor.execute("INSERT INTO contacts (name, number, user) VALUES ('{}', '{}', '{}')".format(name, num, user))
            db.commit()
            alert.config(text='Contacto almacenado correctamente.')
        except:
            alert.config(text='El contacto ya esta registrado.')
    def delete():
        name = inpt1.get()
        num = inpt2.get()
        user = cbox.get()
        if(len(name) > 50):
            alert.config(text='Error: El nombre contiene mas de 50 caracteres.')
        if(len(num) > 9):
            alert.config(text='Error: El numero contiene mas de 9 caracteres.')
            return()
        if(len(num) < 9):
            alert.config(text='Error: El numero contiene menos de 9 caracteres.')
            return()
        try:
            cursor.execute("DELETE FROM contacts WHERE number='"+str(num)+"' AND user='"+str(user)+"'")
            db.commit()
            alert.config(text='Contacto eliminado correctamente.')
        except:
            alert.config(text='El contacto no esta registrado.')
    
    cbox = ttk.Combobox(window, state="readonly", values=["Nico", "Diego", "Adrian"])
    cbox.current(0)
    cbox.pack(pady=5)
    tkinter.Button(window, text='Crear contacto', command= upload).pack(pady=5)
    tkinter.Button(window, text='Borrar contacto', command= delete).pack(pady=5)
    alert = tk.Label(window, text='a')
    alert.pack()
    cursor = db.cursor()

    window.mainloop()
main_page()


import sys
from Tkinter import *
from numero_a_letras import *

def holamundo():
    n = int(var_campo.get())
    texto = to_word(n)
    etiqueta2 = Label(raiz, text=texto, fg="blue", font=("Helvetica", 16))
    etiqueta2.place(x = 250, y = 75, anchor = CENTER)

def salir():
    #m_salir = messagebox.askokcancel(titel="Salir", message="Esta seguro que desea salir.")
    #if m_salir > 0:
    #    raiz.destroy()
    #    return
    raiz.destroy()

raiz = Tk()
var_campo = StringVar()
raiz.geometry('500x200+200+200')
raiz.title("Convertir Numero a Letra")
etiqueta = Label(raiz, text="Escriba un numero")
boton = Button(raiz, text="Convetir a letra", command = holamundo)
campo = Entry(raiz, textvariable=var_campo)
b_salir = Button(raiz, text="Salir", command = salir)

etiqueta.place(x = 130, y= 12.5)
campo.place(x = 250, y= 10)
boton.place(x = 15, y= 150)
b_salir.place(x = 430, y= 150)
raiz.mainloop()

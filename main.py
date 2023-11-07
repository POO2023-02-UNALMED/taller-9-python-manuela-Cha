from tkinter import Label, Tk, Button, Entry

from numpy import char

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x257")


# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=80, padx=1, pady=1)

expresion_matematica = ""

def añadir(value):
    global expresion_matematica
    expresion_matematica += value
    pantalla.delete(0,'end')
    pantalla.insert(50, expresion_matematica)

def operacion():
    global expresion_matematica
    try:
        pantalla.delete(0,'end')
        pantalla.insert(0, eval(expresion_matematica))
        expresion_matematica = ""
    except:
        pantalla.delete(0,'end')
        pantalla.insert(0, "Error")
        expresion_matematica = ""




# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: añadir("1")).grid(row=1, column=0, padx=0.1, pady=0.5)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: añadir("2")).grid(row=1, column=1, padx=0.1, pady=0.5)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: añadir("3")).grid(row=1, column=2, padx=0.1, pady=0.5)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: añadir("4")).grid(row=2, column=0, padx=0.1, pady=0.5)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: añadir("5")).grid(row=2, column=1, padx=0.1, pady=0.5)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: añadir("6")).grid(row=2, column=2, padx=0.1, pady=0.5)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: añadir("7")).grid(row=3, column=0, padx=0.1, pady=0.5)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: añadir("8")).grid(row=3, column=1, padx=0.1, pady=0.5)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: añadir("9")).grid(row=3, column=2, padx=0.1, pady=0.5)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command = lambda: operacion()).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command = lambda: añadir(".")).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda: añadir("+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",  command = lambda: añadir("-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",  command = lambda: añadir("*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",  command = lambda: añadir("/")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()



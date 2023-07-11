#Este es mi primer proyecto en python
#Es una calculadora desarrollada en python
#Talvez para algunos puede no significar mucho pero para mi tiene mucho valor
#Ya que este sera mi primer paso como desarrollador 

import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora devoloped by Jorge Bernal")

resultado = 0

def multiplcar(a, b):
    return 

def dividir(a, b):
    return 

def restar():
    return

def sumar():
    global resultado
    valor_ingresado = int(entrada1.get())
    valor_ingresado2 = int(entrada2.get())
    resultado = valor_ingresado + valor_ingresado2
    etiqueta_resultado.config(text="Resultado: " + str(resultado) )

#Funcion obsoleta(no la incluire por ahora)
def elevar_al_cuadrado(a, b):
    return a**2

#Ingreso de datos del usuario

etiqueta_entrada = tk.Label(ventana, text="Ingrese aqui el primer numero:")
etiqueta_entrada.pack()

entrada1 = tk.Entry(ventana)
entrada1.pack()

etiqueta_entrada2 = tk.Label(ventana, text="Ingrese aqui el segundo numero:")
etiqueta_entrada2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

#Botones

sumar_numeros = tk.Button(ventana, text="sumar", command=sumar)
sumar_numeros.pack()

#Resultado

etiqueta_resultado = tk.Label(ventana, text="Resultado: " + str(resultado))
etiqueta_resultado.pack()


ventana.mainloop()

#El codigo aun no lo termino pero lo seguire mejorando

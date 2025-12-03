import tkinter as tk

# --- INTERFAZ ---
ventana = tk.Tk()
ventana.title("Calculadora con Funciones")
ventana.resizable(True, True)

entrada = tk.Entry(ventana, font=("Arial", 20), justify="right", width=15)
entrada.grid(row=0, column=0, columnspan=4, pady=10)

# Variables globales
numero_uno = None
operacion = None

# --- FUNCIONES BÁSICAS ---
def escribir(valor):
    """Escribe un valor numérico o símbolo en pantalla."""
    entrada.insert(tk.END, valor)

def limpiar():
    """Borra toda la entrada."""
    entrada.delete(0, tk.END)

def seccionar_operacion(op):
    """Guarda el primer número y la operación."""
    global numero_uno, operacion
    try:
        numero_uno = float(entrada.get())
        operacion = op
        entrada.delete(0, tk.END)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# --- FUNCIONES SOLICITADAS ---
def funcion_suma(a, b):
    return a + b

def funcion_potencia(a, b):
    return a ** b

def funcion_modulo(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a % b

# --- FUNCIONES EXTRA ---
def cambio_signo():
    try:
        valor = float(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(-valor))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def raiz():
    try:
        valor = float(entrada.get())
        if valor < 0:
            raise ValueError
        resultado = valor ** 0.5
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# --- FUNCIÓN RESULTADO ---
def calcular():
    global numero_uno, operacion
    try:
        numero_dos = float(entrada.get())
        entrada.delete(0, tk.END)

        if operacion == "+":
            resultado = funcion_suma(numero_uno, numero_dos)

        elif operacion == "-":
            resultado = numero_uno - numero_dos

        elif operacion == "*":
            resultado = numero_uno * numero_dos

        elif operacion == "/":
            if numero_dos == 0:
                raise ZeroDivisionError
            resultado = numero_uno / numero_dos

        elif operacion == "^":
            resultado = funcion_potencia(numero_uno, numero_dos)

        elif operacion == "%":
            resultado = funcion_modulo(numero_uno, numero_dos)

        else:
            resultado = "Error"

        entrada.insert(0, str(resultado))

    except Exception:
        entrada.insert(0, "Error")

# --- BOTONES NUMÉRICOS ---
numeros = [
    ("7",1,0),
    ("8",1,1),
    ("9",1,2),
    ("4",2,0),
    ("5",2,1),
    ("6",2,2),
    ("1",3,0),
    ("2",3,1),
    ("3",3,2),
    ("0",4,0),
]

for (texto, fila, col) in numeros:
    tk.Button(
        ventana,
        text=texto,
        width=5,
        height=2,
        font=("Arial", 16),
        command=lambda x=texto: escribir(x)
    ).grid(row=fila, column=col, padx=5, pady=5)

# --- BOTONES OPERACIONES ---
tk.Button(ventana, text="+", width=5, height=2, font=("Arial", 16),
          command=lambda: seccionar_operacion("+")).grid(row=1, column=3)

tk.Button(ventana, text="-", width=5, height=2, font=("Arial", 16),
          command=lambda: seccionar_operacion("-")).grid(row=2, column=3)

tk.Button(ventana, text="*", width=5, height=2, font=("Arial", 16),
          command=lambda: seccionar_operacion("*")).grid(row=3, column=3)

tk.Button(ventana, text="/", width=5, height=2, font=("Arial", 16),
          command=lambda: seccionar_operacion("/")).grid(row=4, column=3)

tk.Button(ventana, text="^", width=5, height=2, font=("Arial", 16),
          command=lambda: seccionar_operacion("^")).grid(row=5, column=0)

tk.Button(ventana, text="%", width=5, height=2, font=("Arial", 16),
          command=lambda: seccionar_operacion("%")).grid(row=5, column=1)

tk.Button(ventana, text="√", width=5, height=2, font=("Arial", 16),
          command=raiz).grid(row=5, column=2)

tk.Button(ventana, text="+/-", width=5, height=2, font=("Arial", 16),
          command=cambio_signo).grid(row=5, column=3)

# --- BOTONES ESPECIALES ---
tk.Button(ventana, text="=", width=5, height=2, font=("Arial", 16),
          command=calcular).grid(row=4, column=2)

tk.Button(ventana, text="C", width=5, height=2, font=("Arial", 16),
          command=limpiar).grid(row=4, column=1)

ventana.mainloop()

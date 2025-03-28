import tkinter as tk
from tkinter import messagebox

def elegir_palabra(palabra):
    return palabra

def mostrar_palabra(palabra, letras_adivinadas):
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)

def actualizar_ahorcado():
    ahorcado_label.config(text=estados_ahorcado[6 - intentos[0]])

def intentar_letra(letra):
    if letra in letras_adivinadas:
        return
    
    letras_adivinadas.add(letra)
    
    if letra not in palabra:
        intentos[0] -= 1
        actualizar_ahorcado()
        if intentos[0] == 0:
            messagebox.showinfo("Fin del Juego", f"¡Has perdido! La palabra era: {palabra}")
            root.quit()
    
    palabra_label.config(text=mostrar_palabra(palabra, letras_adivinadas))
    
    if set(palabra).issubset(letras_adivinadas):
        messagebox.showinfo("Fin del Juego", "¡Felicidades! Has adivinado la palabra!")
        root.quit()

def iniciar_juego():
    global palabra, intentos, letras_adivinadas
    palabra = elegir_palabra(entry_palabra.get().lower())
    intentos = [6]
    letras_adivinadas = set()
    actualizar_ahorcado()
    palabra_label.config(text=mostrar_palabra(palabra, letras_adivinadas))
    for btn in botones_letras:
        btn.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Ahorcado")

estados_ahorcado = [
    "\n +---+\n |   |\n     |\n     |\n     |\n     |\n=========",
    "\n +---+\n |   |\n O   |\n     |\n     |\n     |\n=========",
    "\n +---+\n |   |\n O   |\n |   |\n     |\n     |\n=========",
    "\n +---+\n |   |\n O   |\n/|   |\n     |\n     |\n=========",
    "\n +---+\n |   |\n O   |\n/|\\  |\n     |\n     |\n=========",
    "\n +---+\n |   |\n O   |\n/|\\  |\n/    |\n     |\n=========",
    "\n +---+\n |   |\n O   |\n/|\\  |\n/ \\  |\n     |\n========="
]

intentos = [6]
letras_adivinadas = set()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Ingresa la palabra a adivinar:").pack()
entry_palabra = tk.Entry(frame)
entry_palabra.pack()
btn_iniciar = tk.Button(frame, text="Iniciar Juego", command=iniciar_juego)
btn_iniciar.pack()

ahorcado_label = tk.Label(root, text=estados_ahorcado[0], font=("Courier", 14))
ahorcado_label.pack()

palabra_label = tk.Label(root, text="", font=("Courier", 16))
palabra_label.pack()

botones_letras = []
frame_letras = tk.Frame(root)
frame_letras.pack()
for letra in "abcdefghijklmnopqrstuvwxyz":
    btn = tk.Button(frame_letras, text=letra, command=lambda l=letra: intentar_letra(l), state=tk.DISABLED)
    btn.pack(side=tk.LEFT, padx=2, pady=2)
    botones_letras.append(btn)

root.mainloop()
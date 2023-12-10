import sys
import os
sys.path.append(os.path.abspath("./Tesseract"))
from pdfConv import pdf2txt
import tkinter as tk
from tkinter import filedialog
from collections import Counter

class ContadorPalabrasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Palabras")

        self.archivo_seleccionado = None

        # Botón para seleccionar el archivo
        self.btn_seleccionar = tk.Button(root, text="Seleccionar PDF", command=self.seleccionar_archivo)
        self.btn_seleccionar.pack(pady=10)

        # Botón para procesar el documento
        self.btn_procesar = tk.Button(root, text="Procesar documento", command=self.procesar_documento, state=tk.DISABLED)
        self.btn_procesar.pack(pady=10)

        # Mostrar resultados en la parte derecha
        self.resultados_label = tk.Label(root, text="Resultados:")
        self.resultados_label.pack()

        self.resultados_text = tk.Text(root, height=10, width=30)
        self.resultados_text.pack()

        # Asociar el cierre de la ventana con el método destroy
        root.protocol("WM_DELETE_WINDOW", root.destroy)

    def seleccionar_archivo(self):
        self.archivo_seleccionado = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf"),("Todos los archivos","*.*")], initialdir= "./Archivos PDF")
        if self.archivo_seleccionado:
            pdf2txt(self.archivo_seleccionado)
            self.btn_procesar["state"] = tk.NORMAL  # Habilitar el botón de procesar

    def procesar_documento(self):
            with open("./Tesseract/output/output.txt", "r") as file:
                contenido = file.read()
                palabras = contenido.split()
                contador_palabras = Counter(palabras)

                # Mostrar resultados en la interfaz
                self.mostrar_resultados(contador_palabras)

    def mostrar_resultados(self, contador_palabras):
        self.resultados_text.delete(1.0, tk.END)  # Limpiar el área de texto

        for palabra, frecuencia in contador_palabras.items():
            resultado = f"{palabra}: {frecuencia} veces\n"
            self.resultados_text.insert(tk.END, resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorPalabrasApp(root)
    root.mainloop()
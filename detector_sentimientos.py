import tkinter as tk
from tkinter import messagebox
from transformers import pipeline

    #Cargar el pipeline de la libreria transformres de analisis de sentimiento
sentimiento = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analizar_mensaje():
    mensaje = entry_texto.get()

    if not mensaje.strip():
        messagebox.showwarning("Advertencia", "Por favor escribe un mensaje.")
        return

    resultado = sentimiento(mensaje)[0]
    etiqueta = resultado['label']
    score = resultado['score']

        #Convertir estrellas a positivo / neutral / negativo
    if etiqueta in ["1 star", "2 stars"]:
        clasificacion = "Negativo"
    elif etiqueta == "3 stars":
        clasificacion = "Neutral"
    else:
        clasificacion = "Positivo"

        #Mostrar resultado
    resultado_label.config(
        text=f"Sentimiento: {clasificacion} (confianza: {score:.2f})"
    )

    #Crear ventana principal con Tkinter
ventana = tk.Tk()
ventana.title("Analizador de Sentimiento")
ventana.geometry("420x200")

    #Texto para ingresar el mensaje
label = tk.Label(ventana, text="Escribe un mensaje:")
label.pack(pady=5)

entry_texto = tk.Entry(ventana, width=50)
entry_texto.pack(pady=5)

    #Boton para analizar
boton = tk.Button(ventana, text="Analizar Sentimiento", command=analizar_mensaje)
boton.pack(pady=10)

    #Etiqueta para mostrar resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

    #Ejecutar la aplicacion
ventana.mainloop()
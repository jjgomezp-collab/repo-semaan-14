import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class AppEventos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Eventos")
        self.root.geometry("550x450")

        # =========================
        # HORA ACTUAL (ESQUINA)
        # =========================
        self.label_hora = tk.Label(root, font=("Arial", 12))
        self.label_hora.pack(anchor="ne", padx=10, pady=5)
        self.actualizar_hora()

        # =========================
        # FRAME LISTA
        # =========================
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        self.lista_eventos = tk.Listbox(frame_lista, width=70, height=10)
        self.lista_eventos.pack()

        # =========================
        # FRAME ENTRADA
        # =========================
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        tk.Label(frame_entrada, text="Evento:").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_evento = tk.Entry(frame_entrada, width=25)
        self.entrada_evento.grid(row=0, column=1, padx=5)

        tk.Label(frame_entrada, text="Fecha (dd/mm/aaaa):").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_fecha = tk.Entry(frame_entrada, width=25)
        self.entrada_fecha.grid(row=1, column=1, padx=5)

        # =========================
        # FRAME BOTONES
        # =========================
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)

    # =========================
    # FUNCIONES
    # =========================

    def actualizar_hora(self):
        """Actualiza la hora en tiempo real"""
        ahora = datetime.now().strftime("%H:%M:%S")
        self.label_hora.config(text="Hora actual: " + ahora)
        self.root.after(1000, self.actualizar_hora)

    def agregar_evento(self):
        """Agrega un evento con fecha y hora automática"""
        evento = self.entrada_evento.get()
        fecha = self.entrada_fecha.get()

        if evento == "" or fecha == "":
            messagebox.showwarning("Error", "Complete todos los campos")
            return

        # Hora automática
        hora_actual = datetime.now().strftime("%H:%M:%S")

        evento_completo = f"{evento} | Fecha: {fecha} | Hora: {hora_actual}"
        self.lista_eventos.insert(tk.END, evento_completo)

        # Limpiar campos
        self.entrada_evento.delete(0, tk.END)
        self.entrada_fecha.delete(0, tk.END)

    def eliminar_evento(self):
        """Elimina el evento seleccionado"""
        try:
            indice = self.lista_eventos.curselection()[0]
            self.lista_eventos.delete(indice)
        except IndexError:
            messagebox.showwarning("Error", "Seleccione un evento")

# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = AppEventos(root)
    root.mainloop()
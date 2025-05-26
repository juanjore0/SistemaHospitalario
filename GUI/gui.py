import tkinter as tk
from tkinter import ttk, messagebox
from controller.controller import create_hospital, search_by_dni

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Hospitalario")

        self.main_frame()

    def main_frame(self):
        self.clear_frame()
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Bienvenido al Sistema Hospitalario", font=("Arial", 14)).pack(pady=10)

        tk.Button(frame, text="Crear Hospital", command=self.create_hospital_frame, width=20).pack(pady=5)
        tk.Button(frame, text="Buscar por DNI", command=self.search_by_dni_frame, width=20).pack(pady=5)

    def create_hospital_frame(self):
        self.clear_frame()
        self.temporal_doctors = []

        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        # Doctor info
        tk.Label(frame, text="Nombre del Doctor:").grid(row=0, column=0, sticky="e")
        self.entry_doc_nombre = tk.Entry(frame)
        self.entry_doc_nombre.grid(row=0, column=1)

        tk.Label(frame, text="Especialidad:").grid(row=1, column=0, sticky="e")
        self.entry_doc_especialidad = tk.Entry(frame)
        self.entry_doc_especialidad.grid(row=1, column=1)

        tk.Label(frame, text="DNI:").grid(row=2, column=0, sticky="e")
        self.entry_doc_dni = tk.Entry(frame)
        self.entry_doc_dni.grid(row=2, column=1)

        # Nombre del hospital
        tk.Label(frame, text="Nombre del Hospital:").grid(row=4, column=0, sticky="e")
        self.entry_name_hospital = tk.Entry(frame)
        self.entry_name_hospital.grid(row=4, column=1)

        # Lista de doctores agregados
        tk.Button(frame, text="Agregar Doctor", command=self.append_doctor).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Label(frame, text="Doctores agregados:").grid(row=5, column=0, sticky="ne")
        self.combo_doctores = ttk.Combobox(frame, state="readonly", values=[])
        self.combo_doctores.grid(row=5, column=1, sticky="we")

        # Botones
        tk.Button(frame, text="Crear Hospital", command=self.create_hospital).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(frame, text="Volver", command=self.main_frame).grid(row=7, column=0, columnspan=2)

    def append_doctor(self):
        nombre = self.entry_doc_nombre.get()
        especialidad = self.entry_doc_especialidad.get()
        dni = self.entry_doc_dni.get()

        if not nombre or not especialidad or not dni:
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos del doctor.")
            return

        doctor = {"name": nombre, "speciality": especialidad, "dni": dni}
        self.temporal_doctors.append(doctor)

        self.combo_doctores['values'] = [f"{d['name']} ({d['speciality']})" for d in self.temporal_doctors]

        # Limpiar entradas
        self.entry_doc_nombre.delete(0, tk.END)
        self.entry_doc_especialidad.delete(0, tk.END)
        self.entry_doc_dni.delete(0, tk.END)

    def create_hospital(self):
        nombre = self.entry_name_hospital.get()
        if not nombre:
            messagebox.showwarning("Nombre vacío", "Debe ingresar un nombre para el hospital.")
            return
        if not self.temporal_doctors:
            messagebox.showwarning("Sin doctores", "Debe agregar al menos un doctor.")
            return

        create_hospital(nombre, self.temporal_doctors)
        messagebox.showinfo("Éxito", f"Hospital '{nombre}' creado correctamente.")

        self.main_frame()

    def search_by_dni_frame(self):
        self.clear_frame()
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Ingrese DNI del doctor:").grid(row=0, column=0)
        self.entry_search_dni = tk.Entry(frame)
        self.entry_search_dni.grid(row=0, column=1)

        tk.Button(frame, text="Buscar", command=self.buscar_dni).grid(row=1, column=0, columnspan=2, pady=5)

        self.tabla = ttk.Treeview(frame, columns=("Hospital", "Doctor", "Especialidad", "DNI"), show="headings")
        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)
        self.tabla.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(frame, text="Volver", command=self.main_frame).grid(row=3, column=0, columnspan=2)

    def buscar_dni(self):
        dni = self.entry_search_dni.get()
        resultado = search_by_dni(dni)
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        if resultado:
            self.tabla.insert("", "end", values=(
                resultado["Hospital"],
                resultado["Doctor"],
                resultado["Especialidad"],
                resultado["DNI"]
            ))
        else:
            messagebox.showwarning("No encontrado", "No se encontró ningún doctor con ese DNI.")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from logic import PurchaseLogic

class PurchaseGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NexusFlow - Lista de Compras Inteligente")
        self.geometry("1150x700")
        self.configure(bg="#FFFFFF")
        self.logic = PurchaseLogic()
        
        # Sugerencias predeterminadas al iniciar [cite: 51]
        self._load_suggestions()
        self.setup_ui()

    def _load_suggestions(self):
        # Articulos base para la lista 
        suggestions = [
            ("Leche", "Deslactosada 1L"),
            ("Pan", "Integral artesanal"),
            ("Huevos", "Cubeta x30 unidades"),
            ("Arroz", "Bolsa de 5kg")
        ]
        for name, desc in suggestions:
            self.logic.add_item(name, desc, "Sugerencias")

    def setup_ui(self):
        header = tk.Frame(self, bg="#FFFFFF", pady=20)
        header.pack(fill="x")
        tk.Label(header, text="Mi Lista de Compras", font=("Segoe UI", 20, "bold"), bg="#FFFFFF", fg="#1A202C").pack(padx=30, side="left")

        toolbar = tk.Frame(self, bg="#FFFFFF", padx=30)
        toolbar.pack(fill="x", pady=10)

        # Botones con colores de referencia [cite: 91, 139]
        tk.Button(toolbar, text="Agregar Urgente", bg="#E53E3E", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", padx=15, pady=8, command=lambda: self.ask_input(True)).pack(side="left", padx=5)
        tk.Button(toolbar, text="Agregar a Lista", bg="#4F67F0", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", padx=15, pady=8, command=lambda: self.ask_input(False)).pack(side="left", padx=5)
        tk.Button(toolbar, text="Eliminar Producto", bg="#718096", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", padx=15, pady=8, command=self.delete_item).pack(side="left", padx=5)

        self.board_view = tk.Frame(self, bg="#FFFFFF")
        self.board_view.pack(fill="both", expand=True, padx=25, pady=10)

        self.columns = {}
        # Columnas orientadas a compras [cite: 169]
        for name in ["Sugerencias", "En Carrito", "Comprado"]:
            f = tk.Frame(self.board_view, bg="#F7F8FA", highlightthickness=1, highlightbackground="#E2E6EA")
            f.pack(side="left", fill="both", expand=True, padx=8)
            tk.Label(f, text=name, font=("Segoe UI", 11, "bold"), bg="#F7F8FA", pady=12).pack()
            
            content = tk.Frame(f, bg="#F7F8FA")
            content.pack(fill="both", expand=True)
            self.columns[name] = content
        self.refresh_ui()

    def ask_input(self, to_front):
        name = simpledialog.askstring("Nuevo Articulo", "Nombre del producto:", parent=self)
        if name:
            desc = simpledialog.askstring("Detalles", f"Descripcion para '{name}':", parent=self)
            self.logic.add_item(name, desc if desc else "", "Sugerencias", to_front)
            self.refresh_ui()

    def refresh_ui(self):
        for c in self.columns.values():
            for w in c.winfo_children(): w.destroy()

        for item in self.logic.get_items():
            card = tk.Frame(self.columns[item.column], bg="#FFFFFF", padx=15, pady=15, highlightthickness=1, highlightbackground="#E2E6EA")
            card.pack(fill="x", padx=10, pady=8)
            
            tk.Label(card, text=item.name, font=("Segoe UI", 10, "bold"), bg="#FFFFFF").pack(anchor="w")
            tk.Label(card, text=item.detail, font=("Segoe UI", 9), bg="#FFFFFF", fg="#718096").pack(anchor="w", pady=(2, 8))

            btn_box = tk.Frame(card, bg="#FFFFFF")
            btn_box.pack(fill="x")
            
            # Flujo de compra [cite: 14, 37]
            if item.column == "Sugerencias":
                tk.Button(btn_box, text="Al Carrito", font=("Segoe UI", 8), bg="#EBF4FF", command=lambda n=item.name: self.move(n, "En Carrito")).pack(side="right")
            elif item.column == "En Carrito":
                tk.Button(btn_box, text="Comprar", font=("Segoe UI", 8), bg="#F0FFF4", command=lambda n=item.name: self.move(n, "Comprado")).pack(side="right")
            else:
                tk.Label(btn_box, text="En Despensa", font=("Segoe UI", 8, "italic"), fg="#38A169", bg="#FFFFFF").pack(side="right")

    def move(self, name, target):
        self.logic.change_status(name, target)
        self.refresh_ui()

    def delete_item(self):
        name = simpledialog.askstring("Eliminar", "Nombre del producto a quitar:", parent=self)
        if name and self.logic.remove_item(name):
            self.refresh_ui()
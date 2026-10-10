import tkinter as tk
from guiutils import ValidatedEntry, slug

root = tk.Tk()
root.title("Demo Reusables (Tkinter)")
root.geometry("450x250")
root.config(padx=15, pady=15)

# --- Componente Visual 1: Validación de Correo ---
lbl_email_title = tk.Label(root, text="Correo Electrónico (Regex Validation):", font=("Arial", 10, "bold"))
lbl_email_title.pack(anchor="w", pady=(0, 2))

email_pattern = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
email = ValidatedEntry(root, pattern=email_pattern, width=45)
email.pack(anchor="w", pady=(0, 4))

lbl_estado = tk.Label(root, text="Estado: Vacío", fg="gray")
lbl_estado.pack(anchor="w", pady=(0, 10))

def refresh_estado(*_):
    text = email.get()
    if not text:
        lbl_estado.config(text="Estado: Vacío", fg="gray")
    elif email.valid:
        lbl_estado.config(text="Estado: Válido (OK)", fg="green")
    else:
        lbl_estado.config(text="Estado: Inválido (ERROR)", fg="red")

email.bind("<KeyRelease>", refresh_estado)

# --- Componente Visual 2 con Utilitario No Visual (Slugifier) ---
lbl_slug_title = tk.Label(root, text="Texto para convertir a Slug:", font=("Arial", 10, "bold"))
lbl_slug_title.pack(anchor="w", pady=(0, 2))

entrada = ValidatedEntry(root, pattern=r".+", width=45)
entrada.pack(anchor="w", pady=(0, 4))

lbl_slug = tk.Label(root, text="Slug resultante: —", fg="blue")
lbl_slug.pack(anchor="w", pady=(0, 5))

def on_change(*_):
    current_text = entrada.get()
    generated_slug = slug(current_text)
    lbl_slug.config(text=f"Slug resultante: {generated_slug if generated_slug else '—'}")

entrada.bind("<KeyRelease>", on_change)

root.mainloop()
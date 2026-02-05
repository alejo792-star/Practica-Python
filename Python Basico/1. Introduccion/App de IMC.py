import tkinter as tk
from tkinter import ttk, messagebox

def parse_float(text: str) -> float:
    return float(text.strip().replace(",", "."))

def calcular():
    try:
        w = parse_float(peso_var.get())
        h = parse_float(altura_var.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos (puedes usar coma o punto).")
        return

    if w <= 0 or h <= 0:
        messagebox.showerror("Error", "Peso y altura deben ser mayores a 0.")
        return

    f = w / (h ** 2)

    # Condicionales EXACTAS de la imagen (mismos rangos y estructura de if)
    condicion = ""
    if (f < 18.5):
        condicion = "underweight"

    if (f >= 18.5 and f < 24.9):
        condicion = "normal"

    if (f >= 25 and f <= 29.9):
        condicion = "overweight"

    if (f >= 30 and f < 34.9):
        condicion = "obese"

    if (f > 35):
        condicion = "Extremly obese"

    # Caso borde: f == 35 no cae en ninguna por el último if (f > 35)
    if condicion == "":
        condicion = "sin clasificación (BMI = 35 exacto)"

    bmi_var.set(f"{f:.2f}")
    cond_var.set(condicion)

    # “Barra” simple según BMI (visual sin complicarse)
    val = max(0.0, min(40.0, f))
    progress["value"] = val

def limpiar():
    peso_var.set("")
    altura_var.set("")
    bmi_var.set("-")
    cond_var.set("-")
    progress["value"] = 0
    entry_peso.focus_set()

# ---------- UI ----------
root = tk.Tk()
root.title("Calculadora BMI")
root.geometry("520x360")
root.minsize(520, 360)

style = ttk.Style(root)
style.theme_use("clam")

# Estilos (suaves, “bonito” sin complicar)
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"))
style.configure("Sub.TLabel", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 11), padding=8)
style.configure("Card.TFrame", padding=16)
style.configure("Result.TLabel", font=("Segoe UI", 12, "bold"))

container = ttk.Frame(root, padding=18)
container.pack(fill="both", expand=True)

# Título
ttk.Label(container, text="Calculadora de BMI", style="Title.TLabel").pack(anchor="w")
ttk.Label(
    container,
    text="Ingresa peso y altura. Se aplican los rangos exactamente como en tu imagen.",
    style="Sub.TLabel"
).pack(anchor="w", pady=(4, 14))

# Card principal
card = ttk.Frame(container, style="Card.TFrame", relief="ridge")
card.pack(fill="x")

form = ttk.Frame(card)
form.pack(fill="x")

peso_var = tk.StringVar()
altura_var = tk.StringVar()
bmi_var = tk.StringVar(value="-")
cond_var = tk.StringVar(value="-")

# Grid bonito
form.columnconfigure(0, weight=1)
form.columnconfigure(1, weight=1)

ttk.Label(form, text="Peso (kg)").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=(0, 6))
ttk.Label(form, text="Altura (m)").grid(row=0, column=1, sticky="w", padx=(10, 0), pady=(0, 6))

entry_peso = ttk.Entry(form, textvariable=peso_var)
entry_altura = ttk.Entry(form, textvariable=altura_var)

entry_peso.grid(row=1, column=0, sticky="ew", padx=(0, 10))
entry_altura.grid(row=1, column=1, sticky="ew", padx=(10, 0))

# Botones
btns = ttk.Frame(card)
btns.pack(fill="x", pady=(12, 0))

btn_calc = ttk.Button(btns, text="Calcular", command=calcular)
btn_clear = ttk.Button(btns, text="Limpiar", command=limpiar)

btn_calc.pack(side="left")
btn_clear.pack(side="left", padx=10)

# Card de resultados
card2 = ttk.Frame(container, style="Card.TFrame", relief="ridge")
card2.pack(fill="both", expand=True, pady=(14, 0))

ttk.Label(card2, text="Resultado", style="Result.TLabel").pack(anchor="w")

res_grid = ttk.Frame(card2)
res_grid.pack(fill="x", pady=(10, 0))
res_grid.columnconfigure(0, weight=1)
res_grid.columnconfigure(1, weight=3)

ttk.Label(res_grid, text="BMI:").grid(row=0, column=0, sticky="w", pady=4)
ttk.Label(res_grid, textvariable=bmi_var, style="Result.TLabel").grid(row=0, column=1, sticky="w", pady=4)

ttk.Label(res_grid, text="Condición:").grid(row=1, column=0, sticky="w", pady=4)
ttk.Label(res_grid, textvariable=cond_var, style="Result.TLabel").grid(row=1, column=1, sticky="w", pady=4)

ttk.Label(card2, text="Indicador (0–40 aprox.)", style="Sub.TLabel").pack(anchor="w", pady=(14, 6))
progress = ttk.Progressbar(card2, orient="horizontal", mode="determinate", maximum=40)
progress.pack(fill="x")

# Enter para calcular
root.bind("<Return>", lambda e: calcular())

# Valores por defecto (puedes quitarlos)
peso_var.set("90")
altura_var.set("1.80")
entry_peso.focus_set()

root.mainloop()

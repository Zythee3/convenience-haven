from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel,PhotoImage
from tkcalendar import DateEntry
from gera_relatorio import *


def generate_report(start_date, end_date, category):
    if category == 'Todos': category = None
    
    start_date = datetime.strptime(str(start_date), '%Y-%m-%d')
    end_date = datetime.strptime(str(end_date), '%Y-%m-%d')
    report = manager.generate_report(start_date, end_date, category, 0)
    print(report)
    print()
    messagebox.showinfo("Relatório", f"Gerando relatório de {start_date} a {end_date} para a categoria {category}...")


def open_report_window():
    report_window = Toplevel()
    report_window.title("Gerar relatório")

    # Use padding and font options for a more modern look
    tk.Label(report_window, text="Data de início:", font=('Helvetica', 10, 'bold')).grid(row=0, column=0, padx=10, pady=10)
    start_date_entry = DateEntry(report_window)
    start_date_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(report_window, text="Data de fim:", font=('Helvetica', 10, 'bold')).grid(row=1, column=0, padx=10, pady=10)
    end_date_entry = DateEntry(report_window)
    end_date_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(report_window, text="Categoria:", font=('Helvetica', 10, 'bold')).grid(row=2, column=0, padx=10, pady=10)

    category_var = tk.StringVar()
    categories = ["Todos","Utensilio", "Acessorio", "Eletronico", "Vestuario", "Livro"]
        
    category_var.set(categories[0])  # set the default value

    category_entry = ttk.Combobox(report_window, textvariable=category_var, values=categories)
    category_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(report_window, text="Gerar relatório", command=lambda: generate_report(start_date_entry.get_date(), end_date_entry.get_date(), category_var.get())).grid(row=3, column=0, columnspan=2, padx=10, pady=10)


def main():
    width, height = 500, 500
    window = tk.Tk()
    window.title("Menu")
    window.geometry("500x500")
    window.resizable(False, False)

    canvas = tk.Canvas(window, width=width, height=height)
    canvas.pack(fill="both", expand=True)
    background = PhotoImage(file='background.png')
    canvas.create_image(0, 0, anchor = 'nw', image=background)

    button_style = ttk.Style()
    button_style.configure("TButton", relief="groove", padding=10, border=20)

    report_button = ttk.Button(window, text="Gerar relatório", command=open_report_window, style="TButton")
    canvas.create_window(250, 200, window=report_button)

    exit_button = ttk.Button(window, text="Sair", command=window.quit, style="TButton")
    canvas.create_window(250, 300, window=exit_button)

    window.mainloop()

if __name__ == '__main__':
    main()
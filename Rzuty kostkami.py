#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import ttk
import random

# Funkcje do rzucania kośćmi
def roll_die(sides):
    return random.randint(1, sides)

def roll_dice(die_type, num_rolls):
    return [roll_die(die_type) for _ in range(num_rolls)]

# Funkcje do operacji na wynikach rzutów
def sum_dice(rolls):
    return sum(rolls)

def max_die(rolls):
    return max(rolls)

def min_die(rolls):
    return min(rolls)

def drop_lowest(rolls):
    sorted_rolls = sorted(rolls)
    return sum(sorted_rolls[1:])  # Pomija najmniejszy wynik

# Funkcja do obsługi przycisku rzutu
def roll_button_clicked():
    try:
        die_type = int(die_type_var.get()[1:])
        num_rolls = int(num_rolls_var.get())
        bonus = int(bonus_var.get())
        operation = operation_var.get()
        
        rolls = roll_dice(die_type, num_rolls)
        max_value = die_type
        
        rolls_text.delete(1.0, tk.END)  # Czyszczenie widgetu Text
        
        for roll in rolls:
            if roll == 1:
                rolls_text.insert(tk.END, f"{roll} ", 'red')
            elif roll == max_value:
                rolls_text.insert(tk.END, f"{roll} ", 'green')
            else:
                rolls_text.insert(tk.END, f"{roll} ")
        
        if operation == 'Suma':
            result = sum_dice(rolls)
        elif operation == 'Największa':
            result = max_die(rolls)
        elif operation == 'Najmniejsza':
            result = min_die(rolls)
        elif operation == 'Odrzuć najmniejszą':
            result = drop_lowest(rolls)
        else:
            result = 'Błąd'
        
        result_with_bonus = result + bonus
        result_label.config(text=f'Wynik: {result} + {bonus} = {result_with_bonus}')
    except Exception as e:
        result_label.config(text=f'Błąd: {str(e)}')

# Konfiguracja GUI
root = tk.Tk()
root.title("Symulator rzutu kośćmi")

# Typ kości
ttk.Label(root, text="Typ kości:").grid(column=0, row=0, padx=5, pady=5)
die_type_var = tk.StringVar()
die_type_combobox = ttk.Combobox(root, textvariable=die_type_var)
die_type_combobox['values'] = ('k4', 'k6', 'k8', 'k10', 'k12', 'k20')
die_type_combobox.grid(column=1, row=0, padx=5, pady=5)
die_type_combobox.current(1)  # Domyślnie k6

# Liczba rzutów
ttk.Label(root, text="Liczba rzutów:").grid(column=0, row=1, padx=5, pady=5)
num_rolls_var = tk.StringVar()
num_rolls_entry = ttk.Entry(root, textvariable=num_rolls_var)
num_rolls_entry.grid(column=1, row=1, padx=5, pady=5)
num_rolls_entry.insert(0, "1")

# Bonus
ttk.Label(root, text="Bonus:").grid(column=0, row=2, padx=5, pady=5)
bonus_var = tk.StringVar()
bonus_entry = ttk.Entry(root, textvariable=bonus_var)
bonus_entry.grid(column=1, row=2, padx=5, pady=5)
bonus_entry.insert(0, "0")

# Operacja
ttk.Label(root, text="Operacja:").grid(column=0, row=3, padx=5, pady=5)
operation_var = tk.StringVar()
operation_combobox = ttk.Combobox(root, textvariable=operation_var)
operation_combobox['values'] = ('Suma', 'Największa', 'Najmniejsza', 'Odrzuć najmniejszą')
operation_combobox.grid(column=1, row=3, padx=5, pady=5)
operation_combobox.current(0)  # Domyślnie suma

# Przycisk rzutu
roll_button = ttk.Button(root, text="Rzuć", command=roll_button_clicked)
roll_button.grid(column=0, row=4, columnspan=2, padx=5, pady=5)

# Wyniki
ttk.Label(root, text="Rzuty:").grid(column=0, row=5, columnspan=2, padx=5, pady=5)
rolls_text = tk.Text(root, height=1, width=50)
rolls_text.grid(column=0, row=6, columnspan=2, padx=5, pady=5)
rolls_text.tag_configure('red', foreground='red')
rolls_text.tag_configure('green', foreground='green')

# Wynik
result_label = ttk.Label(root, text="Wynik:")
result_label.grid(column=0, row=7, columnspan=2, padx=5, pady=5)

root.mainloop()


# In[ ]:





# In[ ]:





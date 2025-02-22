import tkinter as tk
from tkinter import messagebox

def menu_inicial():
    window = tk.Tk()
    window.title('Conversor de Temperaturas')

    label = tk.Label(window, text='Conversor de Temperaturas')
    label.pack()

    options = [
        'Converter de Celsius [°C] para Fahrenheit [°F]',
        'Converter de Celsius [°C] para Kelvin [K]',
        'Converter de Fahrenheit [°F] para Celsius [°C]',
        'Converter de Fahrenheit [°F] para Kelvin [K]',
        'Converter de Kelvin [K] para Celsius [°C]',
        'Converter de Kelvin [K] para Fahrenheit [°F]'
    ]

    global selected_option
    selected_option = tk.StringVar(window)
    selected_option.set(options[0])

    option_menu = tk.OptionMenu(window, selected_option, *options)
    option_menu.pack()

    global entry
    entry = tk.Entry(window)
    entry.pack()

    convert_button = tk.Button(window, text='Converter', command=handle_selection)
    convert_button.pack()

    window.mainloop()

def handle_selection():
    temp = entry.get()
    if not temp:
        messagebox.showerror('Erro', 'Por favor, insira uma temperatura.')
        return

    try:
        temp = float(temp)
    except ValueError:
        messagebox.showerror('Erro', 'Por favor, insira um valor numérico válido.')
        return

    option = selected_option.get()
    if option == 'Converter de Celsius [°C] para Fahrenheit [°F]':
        celsius_fahrenheit(temp)
    elif option == 'Converter de Celsius [°C] para Kelvin [K]':
        celsius_kelvin(temp)
    elif option == 'Converter de Fahrenheit [°F] para Celsius [°C]':
        fahrenheit_celsius(temp)
    elif option == 'Converter de Fahrenheit [°F] para Kelvin [K]':
        fahrenheit_kelvin(temp)
    elif option == 'Converter de Kelvin [K] para Celsius [°C]':
        kelvin_celsius(temp)
    elif option == 'Converter de Kelvin [K] para Fahrenheit [°F]':
        kelvin_fahrenheit(temp)

def celsius_fahrenheit(C):
    F = C * (9 / 5) + 32
    messagebox.showinfo('Resultado', f'Temperatura convertida em Fahrenheit: {F}°F')

def celsius_kelvin(C):
    K = C + 273
    messagebox.showinfo('Resultado', f'Temperatura convertida em Kelvin: {K}K')

def fahrenheit_celsius(F):
    C = (F - 32) * (5 / 9)
    messagebox.showinfo('Resultado', f'Temperatura convertida em Celsius: {C}°C')

def fahrenheit_kelvin(F):
    K = (F - 32) * (5 / 9) + 273
    messagebox.showinfo('Resultado', f'Temperatura convertida em Kelvin: {K}K')

def kelvin_celsius(K):
    C = K - 273
    messagebox.showinfo('Resultado', f'Temperatura convertida em Celsius: {C}°C')

def kelvin_fahrenheit(K):
    F = (K - 273) * (9 / 5) + 32
    messagebox.showinfo('Resultado', f'Temperatura convertida em Fahrenheit: {F}°F')

if __name__ == '__main__':
    menu_inicial()
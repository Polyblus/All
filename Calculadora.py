import tkinter as tk
from tkinter import messagebox

class Calculator:
    
    def somar(self, n1: float, n2: float) -> float:
        return n1 + n2

    def subtrair(self, n1: float, n2: float) -> float:
        return n1 - n2

    def multiplicar(self, n1: float, n2: float) -> float:
        return n1 * n2

    def dividir(self, n1: float, n2: float) -> float:
        if n2 == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return n1 / n2

def menu_inicial():
    calc = Calculator()
    window = tk.Tk()
    window.title('Calculadora Simples')
    window.resizable(False, False)
    padding = {"padx": 8, "pady": 6}

    tk.Label(window, text='Número 1:').grid(row=0, column=0, **padding)
    entry_n1 = tk.Entry(window)
    entry_n1.grid(row=0, column=1, **padding)

    tk.Label(window, text='Número 2:').grid(row=1, column=0, **padding)
    entry_n2 = tk.Entry(window)
    entry_n2.grid(row=1, column=1, **padding)

    result_var = tk.StringVar(value='Resultado:')
    tk.Label(window, textvariable=result_var, width=30, anchor='w').grid(row=2, column=0, columnspan=2, **padding)

    def read_inputs():
        try:
            n1 = float(entry_n1.get())
            n2 = float(entry_n2.get())
            return n1, n2
        except ValueError:
            messagebox.showerror("Entrada inválida", "Informe dois números válidos (p.ex. 1.5 ou 3).")
            return None

    def operate(op: str):
        vals = read_inputs()
        if vals is None:
            return
        n1, n2 = vals
        try:
            if op == '+':
                res = calc.somar(n1, n2)
            elif op == '-':
                res = calc.subtrair(n1, n2)
            elif op == '*':
                res = calc.multiplicar(n1, n2)
            elif op == '/':
                res = calc.dividir(n1, n2)
            else:
                return
            result_var.set(f"Resultado: {res:.3f}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    btn_frame = tk.Frame(window)
    btn_frame.grid(row=3, column=0, columnspan=2, **padding)
    tk.Button(btn_frame, text='+', width=6, command=lambda: operate('+')).grid(row=0, column=0, padx=4)
    tk.Button(btn_frame, text='-', width=6, command=lambda: operate('-')).grid(row=0, column=1, padx=4)
    tk.Button(btn_frame, text='×', width=6, command=lambda: operate('*')).grid(row=0, column=2, padx=4)
    tk.Button(btn_frame, text='÷', width=6, command=lambda: operate('/')).grid(row=0, column=3, padx=4)

    window.mainloop()

if __name__ == "__main__":
    menu_inicial()

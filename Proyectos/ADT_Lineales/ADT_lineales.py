import tkinter as tk
from tkinter import ttk, messagebox
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib_venn import venn2, venn2_circles

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones de Conjuntos y Polinomios")
        self.root.geometry("800x600")
        
        # Configurar estilo para fuentes más grandes
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=('Arial', 12))
        
        # Crear pestañas
        self.tab_control = ttk.Notebook(root)
        
        # Pestaña de conjuntos
        self.tab_conjuntos = ttk.Frame(self.tab_control, padding=15)
        self.tab_control.add(self.tab_conjuntos, text='Conjuntos')
        self.setup_conjuntos_tab()
        
        # Pestaña de polinomios
        self.tab_polinomios = ttk.Frame(self.tab_control, padding=15)
        self.tab_control.add(self.tab_polinomios, text='Polinomios')
        self.setup_polinomios_tab()
        
        self.tab_control.pack(expand=1, fill='both')
        
        # Variable para almacenar el último resultado de operación
        self.last_poly_result = {}
    
    def create_large_label(self, parent, text):
        return tk.Label(parent, text=text, font=('Arial', 12))
    
    def create_large_entry(self, parent, width=40):
        return tk.Entry(parent, width=width, font=('Arial', 12))
    
    def create_large_button(self, parent, text, command, width=25):
        return tk.Button(parent, text=text, width=width, command=command, 
                        font=('Arial', 12), bg='#f0f0f0')
    
    def setup_conjuntos_tab(self):
        # Título
        title = tk.Label(self.tab_conjuntos, text="Operaciones con Conjuntos", 
                        font=('Arial', 14, 'bold'))
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Entradas para conjuntos
        self.create_large_label(self.tab_conjuntos, "Conjunto A (ej: 1,2,3):").grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        self.entry_set1 = self.create_large_entry(self.tab_conjuntos, 35)
        self.entry_set1.grid(row=1, column=1, padx=10, pady=10)
        
        self.create_large_label(self.tab_conjuntos, "Conjunto B (ej: 2,3,4):").grid(
            row=2, column=0, padx=10, pady=10, sticky='w')
        self.entry_set2 = self.create_large_entry(self.tab_conjuntos, 35)
        self.entry_set2.grid(row=2, column=1, padx=10, pady=10)
        
        # Frame para botones
        button_frame = tk.Frame(self.tab_conjuntos)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Botones de operaciones
        operations = ["Unión", "Intersección", "Diferencia (A-B)", "Diferencia (B-A)", "Diferencia Simétrica"]
        for i, op in enumerate(operations):
            btn = self.create_large_button(button_frame, op, lambda o=op: self.operar_conjuntos(o), 20)
            btn.grid(row=i//2, column=i%2, padx=10, pady=5)
        
        # Resultado
        self.create_large_label(self.tab_conjuntos, "Resultado:").grid(
            row=5, column=0, padx=10, pady=15, sticky='w')
        self.result_conjuntos = tk.StringVar()
        result_entry = self.create_large_entry(self.tab_conjuntos, 35)
        result_entry.config(state='readonly', textvariable=self.result_conjuntos)
        result_entry.grid(row=5, column=1, padx=10, pady=15)
    
    def setup_polinomios_tab(self):
        # Título
        title = tk.Label(self.tab_polinomios, text="Operaciones con Polinomios", 
                        font=('Arial', 14, 'bold'))
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Entradas para polinomios
        self.create_large_label(self.tab_polinomios, "Polinomio 1 (ej: 2x^2+3x+1):").grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        self.entry_poly1 = self.create_large_entry(self.tab_polinomios, 35)
        self.entry_poly1.grid(row=1, column=1, padx=10, pady=10)
        
        self.create_large_label(self.tab_polinomios, "Polinomio 2 (ej: x^2+2):").grid(
            row=2, column=0, padx=10, pady=10, sticky='w')
        self.entry_poly2 = self.create_large_entry(self.tab_polinomios, 35)
        self.entry_poly2.grid(row=2, column=1, padx=10, pady=10)
        
        # Entrada para evaluación
        self.create_large_label(self.tab_polinomios, "Valor de x (para evaluación):").grid(
            row=3, column=0, padx=10, pady=10, sticky='w')
        self.entry_x = self.create_large_entry(self.tab_polinomios, 35)
        self.entry_x.grid(row=3, column=1, padx=10, pady=10)
        
        # Frame para botones
        button_frame = tk.Frame(self.tab_polinomios)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Botones de operaciones
        operations = ["Suma", "Resta", "Multiplicación", "Evaluar"]
        for i, op in enumerate(operations):
            btn = self.create_large_button(button_frame, op, lambda o=op: self.operar_polinomios(o), 20)
            btn.grid(row=i//2, column=i%2, padx=10, pady=5)
        
        # Resultado
        self.create_large_label(self.tab_polinomios, "Resultado:").grid(
            row=5, column=0, padx=10, pady=15, sticky='w')
        self.result_polinomios = tk.StringVar()
        result_entry = self.create_large_entry(self.tab_polinomios, 35)
        result_entry.config(state='readonly', textvariable=self.result_polinomios)
        result_entry.grid(row=5, column=1, padx=10, pady=15)
    
    def get_conjuntos(self):
        try:
            set1_str = self.entry_set1.get()
            set2_str = self.entry_set2.get()
            
            if not set1_str or not set2_str:
                messagebox.showerror("Error", "Ambos conjuntos deben tener valores.")
                return None, None
            
            s1 = set(map(int, set1_str.split(',')))
            s2 = set(map(int, set2_str.split(',')))
            
            return s1, s2
        except ValueError:
            messagebox.showerror("Error", "Formato incorrecto. Use números separados por comas.")
            return None, None
    
    def mostrar_diagrama_venn(self, s1, s2, resultado, operacion):
        # Crear ventana emergente
        venn_window = tk.Toplevel(self.root)
        venn_window.title(f"Diagrama de Venn - {operacion}")
        venn_window.geometry("600x500")
        
        # Crear figura de matplotlib
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        fig.suptitle(f'Operación: {operacion}', fontsize=16)
        
        # Diagrama de Venn para los conjuntos originales
        venn2([s1, s2], ('Conjunto A', 'Conjunto B'), ax=ax1)
        ax1.set_title('Conjuntos Originales')
        
        # Diagrama de Venn para el resultado
        if operacion == "Unión":
            venn2([s1, s2], ('Conjunto A', 'Conjunto B'), ax=ax2)
            # Resaltar toda el área de unión
            for patch in ax2.patches:
                patch.set_alpha(0.5)
                patch.set_color('lightblue')
            ax2.set_title('Resultado: A ∪ B')
            
        elif operacion == "Intersección":
            venn2([s1, s2], ('Conjunto A', 'Conjunto B'), ax=ax2)
            # Resaltar solo la intersección
            if len(ax2.patches) >= 3:
                ax2.patches[0].set_alpha(0.3)  # Solo A
                ax2.patches[0].set_color('lightgray')
                ax2.patches[1].set_alpha(0.3)  # Solo B
                ax2.patches[1].set_color('lightgray')
                ax2.patches[2].set_alpha(0.7)  # Intersección
                ax2.patches[2].set_color('lightblue')
            ax2.set_title('Resultado: A ∩ B')
            
        elif operacion == "Diferencia (A-B)":
            venn2([s1, s2], ('Conjunto A', 'Conjunto B'), ax=ax2)
            # Resaltar solo A - B
            if len(ax2.patches) >= 3:
                ax2.patches[0].set_alpha(0.7)  # Solo A
                ax2.patches[0].set_color('lightblue')
                ax2.patches[1].set_alpha(0.3)  # Solo B
                ax2.patches[1].set_color('lightgray')
                ax2.patches[2].set_alpha(0.3)  # Intersección
                ax2.patches[2].set_color('lightgray')
            ax2.set_title('Resultado: A - B')
            
        elif operacion == "Diferencia (B-A)":
            venn2([s1, s2], ('Conjunto A', 'Conjunto B'), ax=ax2)
            # Resaltar solo B - A
            if len(ax2.patches) >= 3:
                ax2.patches[0].set_alpha(0.3)  # Solo A
                ax2.patches[0].set_color('lightgray')
                ax2.patches[1].set_alpha(0.7)  # Solo B
                ax2.patches[1].set_color('lightblue')
                ax2.patches[2].set_alpha(0.3)  # Intersección
                ax2.patches[2].set_color('lightgray')
            ax2.set_title('Resultado: B - A')
            
        elif operacion == "Diferencia Simétrica":
            venn2([s1, s2], ('Conjunto A', 'Conjunto B'), ax=ax2)
            # Resaltar diferencia simétrica (solo A y solo B)
            if len(ax2.patches) >= 3:
                ax2.patches[0].set_alpha(0.7)  # Solo A
                ax2.patches[0].set_color('lightblue')
                ax2.patches[1].set_alpha(0.7)  # Solo B
                ax2.patches[1].set_color('lightblue')
                ax2.patches[2].set_alpha(0.3)  # Intersección
                ax2.patches[2].set_color('lightgray')
            ax2.set_title('Resultado: A Δ B')
        
        # Ajustar diseño
        plt.tight_layout()
        
        # Mostrar información textual
        info_text = f"""
        Conjunto A: {sorted(s1)}
        Conjunto B: {sorted(s2)}
        Resultado ({operacion}): {sorted(resultado)}
        """
        
        info_label = tk.Label(venn_window, text=info_text, font=('Arial', 12), justify=tk.LEFT)
        info_label.pack(pady=10)
        
        # Embedder la figura en la ventana de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=venn_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Botón para cerrar
        close_btn = tk.Button(venn_window, text="Cerrar", command=venn_window.destroy, 
                             font=('Arial', 12), bg='#f0f0f0')
        close_btn.pack(pady=10)
    
    def operar_conjuntos(self, op):
        s1, s2 = self.get_conjuntos()
        if s1 is None or s2 is None:
            return
        
        if op == "Unión":
            res = s1 | s2
        elif op == "Intersección":
            res = s1 & s2
        elif op == "Diferencia (A-B)":
            res = s1 - s2
        elif op == "Diferencia (B-A)":
            res = s2 - s1
        elif op == "Diferencia Simétrica":
            res = s1 ^ s2
        else:
            res = set()
        
        self.result_conjuntos.set(str(sorted(res)))
        
        # Mostrar diagrama de Venn
        self.mostrar_diagrama_venn(s1, s2, res, op)
    
    def parse_poly(self, poly_str):
        if not poly_str:
            return {}
        
        # Limpiar la cadena
        poly_str = poly_str.replace(' ', '').replace('-', '+-')
        if poly_str.startswith('+'):
            poly_str = poly_str[1:]
        
        # Dividir en términos
        terms = poly_str.split('+')
        poly = {}
        
        for term in terms:
            if not term:
                continue
                
            # Manejar término constante
            if 'x' not in term:
                try:
                    coef = int(term)
                    poly[0] = poly.get(0, 0) + coef
                except ValueError:
                    continue
                continue
            
            # Separar coeficiente y exponente
            if 'x^' in term:
                parts = term.split('x^')
                exp_str = parts[1]
            else:
                parts = term.split('x')
                exp_str = '1' if len(parts) > 1 and not parts[1] else ''
            
            coef_str = parts[0]
            
            # Determinar coeficiente
            if not coef_str:
                coef = 1
            elif coef_str == '-':
                coef = -1
            else:
                try:
                    coef = int(coef_str)
                except ValueError:
                    continue
            
            # Determinar exponente
            if exp_str:
                try:
                    exp = int(exp_str)
                except ValueError:
                    exp = 1
            else:
                exp = 1
            
            poly[exp] = poly.get(exp, 0) + coef
        
        return poly
    
    def poly_to_str(self, poly):
        terms = []
        for exp in sorted(poly, reverse=True):
            coef = poly[exp]
            if coef == 0:
                continue
            
            sign = '+' if coef > 0 else '-'
            abs_coef = abs(coef)
            
            if exp == 0:
                terms.append(f"{sign} {abs_coef}")
            elif exp == 1:
                if abs_coef == 1:
                    terms.append(f"{sign} x")
                else:
                    terms.append(f"{sign} {abs_coef}x")
            else:
                if abs_coef == 1:
                    terms.append(f"{sign} x^{exp}")
                else:
                    terms.append(f"{sign} {abs_coef}x^{exp}")
        
        if not terms:
            return "0"
        
        # Construir la cadena resultante
        result = terms[0]
        if result.startswith('+ '):
            result = result[2:]
        elif result.startswith('- '):
            result = '-' + result[2:]
        
        for term in terms[1:]:
            result += f" {term}"
        
        return result
    
    def get_polinomios(self):
        try:
            p1_str = self.entry_poly1.get()
            p2_str = self.entry_poly2.get()
            
            if not p1_str:
                messagebox.showerror("Error", "El primer polinomio es requerido.")
                return None, None
            
            poly1 = self.parse_poly(p1_str)
            poly2 = self.parse_poly(p2_str) if p2_str else {}
            
            return poly1, poly2
        except Exception as e:
            messagebox.showerror("Error", f"Formato incorrecto de polinomio: {str(e)}")
            return None, None
    
    def operar_polinomios(self, op):
        if op == "Evaluar":
            try:
                # Si hay un resultado previo, evaluarlo
                if self.last_poly_result:
                    poly_to_evaluate = self.last_poly_result
                else:
                    # Si no, evaluar el primer polinomio
                    p1_str = self.entry_poly1.get()
                    if not p1_str:
                        messagebox.showerror("Error", "El polinomio es requerido para evaluación.")
                        return
                    poly_to_evaluate = self.parse_poly(p1_str)
                
                x_str = self.entry_x.get()
                if not x_str:
                    messagebox.showerror("Error", "El valor de x es requerido para evaluación.")
                    return
                
                x = float(x_str)
                res_val = 0
                for exp, coef in poly_to_evaluate.items():
                    res_val += coef * (x ** exp)
                
                self.result_polinomios.set(str(res_val))
                return
            except Exception as e:
                messagebox.showerror("Error", f"Error en evaluación: {str(e)}")
                return
        
        # Operaciones entre polinomios
        poly1, poly2 = self.get_polinomios()
        if poly1 is None or poly2 is None:
            return
        
        if op == "Suma":
            res = poly1.copy()
            for exp, coef in poly2.items():
                res[exp] = res.get(exp, 0) + coef
        elif op == "Resta":
            res = poly1.copy()
            for exp, coef in poly2.items():
                res[exp] = res.get(exp, 0) - coef
        elif op == "Multiplicación":
            res = {}
            for e1, c1 in poly1.items():
                for e2, c2 in poly2.items():
                    exp = e1 + e2
                    res[exp] = res.get(exp, 0) + c1 * c2
        
        # Guardar el resultado para posible evaluación posterior
        self.last_poly_result = res
        
        # Mostrar resultado
        self.result_polinomios.set(self.poly_to_str(res))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
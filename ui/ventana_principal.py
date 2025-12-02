import tkinter as tk
from tkinter import messagebox

class MainWindowDark:
    def __init__(self, root):
        self.root = root
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz gráfica del menú principal en modo oscuro"""
        self.configurar_ventana()
        self.crear_header()
        self.crear_botones_menu()
        self.crear_status_bar()
    
    def configurar_ventana(self):
        """Configura los parámetros de la ventana en modo oscuro"""
        self.root.title("Sistema de Gestión de Maratones - Menú Principal")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a1a1a")
        
        # Hacer que la ventana sea responsive
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
    
    def crear_header(self):
        """Crea el encabezado de la aplicación en modo oscuro"""
        # Frame del header
        header_frame = tk.Frame(self.root, bg='#0d1b2a', height=120)
        header_frame.grid(row=0, column=0, sticky='ew', padx=15, pady=15)
        header_frame.grid_propagate(False)
        
        # Título principal
        titulo = tk.Label(
            header_frame,
            text="SISTEMA DE GESTIÓN DE MARATONES",
            font=('Arial', 22, 'bold'),
            fg='#e0e1dd',
            bg='#0d1b2a'
        )
        titulo.pack(expand=True, pady=(20, 5))
        
        # Subtítulo
        subtitulo = tk.Label(
            header_frame,
            text="Menú Principal - Modo Oscuro",
            font=('Arial', 12, 'italic'),
            fg='#778da9',
            bg='#0d1b2a'
        )
        subtitulo.pack(pady=(0, 15))
    
    def crear_botones_menu(self):
        """Crea los botones del menú principal en modo oscuro"""
        # Frame principal para los botones
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.grid(row=1, column=0, sticky='nsew', padx=25, pady=20)
        
        # Configurar grid para centrar los botones
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Frame para contener los botones (centrado)
        botones_frame = tk.Frame(main_frame, bg='#1a1a1a')
        botones_frame.grid(row=0, column=0)
        
        # Lista de opciones del menú con colores oscuros
        opciones_menu = [
            {
                'texto': '1. 🏃 Gestión de Maratones',
                'comando': self.mostrar_gestion_maratones,
                'color': '#1b4332',
                'hover': '#2d6a4f'
            },
            {
                'texto': '2. 📊 Gestión de Problemas',
                'comando': self.mostrar_gestion_problemas,
                'color': '#741d1d',
                'hover': '#a53838'
            },
            {
                'texto': '3. 👥 Gestión de Equipos',
                'comando': self.mostrar_gestion_equipos,
                'color': '#1d3a4c',
                'hover': '#2a4d69'
            },
            {
                'texto': '4. 👤 Gestión de Participantes',
                'comando': self.mostrar_gestion_participantes,
                'color': '#5c4d1d',
                'hover': '#8a7a2a'
            },
            {
                'texto': '5. 🏆 Resultados de Maratones',
                'comando': self.mostrar_resultados_maratones,
                'color': '#3d1d5c',
                'hover': '#5a2a8a'
            },
            {
                'texto': '6. 🚪 Salir del Sistema',
                'comando': self.salir_sistema,
                'color': '#333333',
                'hover': '#555555'
            }
        ]
        
        # Crear botones
        for i, opcion in enumerate(opciones_menu):
            boton = tk.Button(
                botones_frame,
                text=opcion['texto'],
                font=('Arial', 13, 'bold'),
                bg=opcion['color'],
                fg='#e0e1dd',
                width=28,
                height=2,
                command=opcion['comando'],
                cursor='hand2',
                relief='flat',
                bd=0,
                activebackground=opcion['hover'],
                activeforeground='#ffffff'
            )
            boton.grid(row=i, column=0, pady=8, padx=20, sticky='ew')
            
            # Efectos hover mejorados
            boton.bind('<Enter>', lambda e, b=boton, h=opcion['hover']: 
                      self.on_enter(e, b, h))
            boton.bind('<Leave>', lambda e, b=boton, c=opcion['color']: 
                      self.on_leave(e, b, c))
    
    def on_enter(self, event, boton, color_hover):
        """Efecto cuando el mouse entra en el botón"""
        boton.configure(bg=color_hover)
    
    def on_leave(self, event, boton, color_original):
        """Efecto cuando el mouse sale del botón"""
        boton.configure(bg=color_original)
    
    def crear_status_bar(self):
        """Crea la barra de estado inferior en modo oscuro"""
        status_frame = tk.Frame(self.root, bg='#0d1b2a', height=35)
        status_frame.grid(row=2, column=0, sticky='ew', padx=15, pady=10)
        status_frame.grid_propagate(False)
        
        # Información de estado
        status_text = tk.Label(
            status_frame,
            text="🟢 Sistema listo - Seleccione una opción del menú",
            font=('Arial', 10),
            fg='#778da9',
            bg='#0d1b2a'
        )
        status_text.pack(side='left', padx=15)
        
        # Información del sistema
        sistema_status = tk.Label(
            status_frame,
            text="🌙 Modo Oscuro | v1.0",
            font=('Arial', 9),
            fg='#415a77',
            bg='#0d1b2a'
        )
        sistema_status.pack(side='right', padx=15)
    
    def mostrar_gestion_maratones(self):
        """Muestra la ventana de gestión de maratones"""
        messagebox.showinfo(
            "Gestión de Maratones", 
            "Abriendo módulo de Gestión de Maratones...",
            icon='info'
        )
    
    def mostrar_gestion_problemas(self):
        """Muestra la ventana de gestión de problemas"""
        messagebox.showinfo(
            "Gestión de Problemas", 
            "Abriendo módulo de Gestión de Problemas...",
            icon='info'
        )
    
    def mostrar_gestion_equipos(self):
        """Muestra la ventana de gestión de equipos"""
        messagebox.showinfo(
            "Gestión de Equipos", 
            "Abriendo módulo de Gestión de Equipos...",
            icon='info'
        )
    
    def mostrar_gestion_participantes(self):
        """Muestra la ventana de gestión de participantes"""
        messagebox.showinfo(
            "Gestión de Participantes", 
            "Abriendo módulo de Gestión de Participantes...",
            icon='info'
        )
    
    def mostrar_resultados_maratones(self):
        """Muestra la ventana de resultados de maratones"""
        messagebox.showinfo(
            "Resultados de Maratones", 
            "Abriendo módulo de Resultados de Maratones...",
            icon='info'
        )
    
    def salir_sistema(self):
        """Cierra la aplicación con confirmación"""
        respuesta = messagebox.askyesno(
            "Confirmar Salida",
            "¿Está seguro de que desea salir del sistema?",
            icon='question'
        )
        
        if respuesta:
            self.root.quit()


# Código para probar la pantalla en modo oscuro
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindowDark(root)
    root.mainloop()
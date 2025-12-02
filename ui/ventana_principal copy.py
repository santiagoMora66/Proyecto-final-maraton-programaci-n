import tkinter as tk

class Ventana_principal():
    def __init__(self):
        self.ventana = tk.Tk()
        self.crear_interfaz()
        self.ventana.mainloop()
        
    
    def crear_interfaz(self):
        """crea la interfaz grafica que se va a usar"""
        self.configurar_ventana()
        self.crear_encabezado()
        self.crear_cuerpo()
        
    
    def configurar_ventana(self):
        """configura los parametros de la ventana"""
        self.ventana.title("Menu principal")
        self.ventana.geometry("800x600")
        self.configurar_colores()
        self.ventana.configure(bg = self.colores["fondo_principal"])        
        self.configurar_grid()
        
    def configurar_colores(self):
        """Esquema minimalista que complementa #1a1a1a"""
        self.colores = {
            "fondo_principal": "#1a1a1a",        # Base
            
            "fondo_secundario": "#0d1b2a",       # Encabezado
            
            "acento_primario": "#6366f1",        # Índigo elegante
            "acento_secundario": "#8b5cf6",      # Púrpura
            
            "texto_primario": "#f3f4f6",
            "texto_secundario": "#d1d5db", 
            "texto_terciario": "#9ca3af",
            
            "borde": "#4b5563",
        }
        
    def configurar_grid(self):
        """configura los porcentajes de grid"""
        self.ventana.grid_rowconfigure(0, weight=1)    # 10%
        self.ventana.grid_rowconfigure(1, weight=9)    # 90%
        self.ventana.grid_columnconfigure(0, weight=1) # 100% ancho

    def crear_encabezado(self):
        """crear el encabezado de la aplicacion"""
        #contenedro
        contenedor_encabezado = tk.Frame(self.ventana, bg= self.colores["fondo_secundario"] )
        #disposicion
        contenedor_encabezado.grid(row=0, column=0, sticky="nsew", padx=40, pady= 30)
        
        #titulo
        titulo = tk.Label(
        contenedor_encabezado,
        text="Menu principal",  
        bg="#1e293b",      
        fg="white",        
        font=("Arial", 40) 
        )
        titulo.pack(pady=(10, 20))

    def crear_cuerpo(self):
        """crea el cuerpo de la pagina""" 
        contenedor_cuerpo = tk.Frame(self.ventana, bg=self.colores["fondo_principal"])
        contenedor_cuerpo.grid(row=1, column=0, sticky="nsew", padx=40, pady=(0,20))
        
        # Frame interno para centrar los botones
        frame_centro = tk.Frame(contenedor_cuerpo, bg="#2d3748")
        frame_centro.pack(expand=True)  # ← Esto centra verticalmente
        
        # Botones con estilo profesional
        boton_maratones = tk.Button(
            frame_centro,
            text="Gestión de Maratones",
            bg="#1b4332",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="raised",
            bd=2,
            padx=25,
            pady=12,
            width=20,
            cursor="hand2"
        )
        boton_maratones.pack(pady=8)

        boton_problemas = tk.Button(
            frame_centro,
            text="Gestión de Problemas", 
            bg="#059669",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="raised",
            bd=2,
            padx=25,
            pady=12,
            width=20,
            cursor="hand2"
        )
        boton_problemas.pack(pady=8)

        boton_equipos = tk.Button(
            frame_centro,
            text="Gestión de Equipos",
            bg="#7c3aed",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="raised",
            bd=2,
            padx=25,
            pady=12,
            width=20,
            cursor="hand2"
        )
        boton_equipos.pack(pady=8)

        boton_participantes = tk.Button(
            frame_centro,
            text="Gestión de Participantes",
            bg="#dc2626",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="raised",
            bd=2,
            padx=25,
            pady=12,
            width=20,
            cursor="hand2"
        )
        boton_participantes.pack(pady=8)



if __name__ == '__main__':
    app = Ventana_principal()

    
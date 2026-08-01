import customtkinter as ctk
import subprocess
import threading
import webbrowser
import sys
import os


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FlowMetricsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        
        self.title("FlowMetrics")
        self.geometry("400x500")
        self.resizable(False, False)

        self.streamlit_process = None

        self.criar_interface()

    def criar_interface(self):

        
        self.label_titulo = ctk.CTkLabel(
            self,
            text="FlowMetrics",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.label_titulo.pack(pady=20)

        self.label_subtitulo = ctk.CTkLabel(
            self,
            text="Análise automatizada de dados\ndo Google Analytics",
            font=ctk.CTkFont(size=13),
            text_color="gray"
        )
        self.label_subtitulo.pack(pady=5)

        
        self.divisor = ctk.CTkFrame(self, height=2, fg_color="gray")
        self.divisor.pack(fill="x", padx=20, pady=20)

        
        self.label_status = ctk.CTkLabel(
            self,
            text="Status: Aguardando...",
            font=ctk.CTkFont(size=13)
        )
        self.label_status.pack(pady=10)

        
        self.btn_iniciar = ctk.CTkButton(
            self,
            text="Iniciar FlowMetrics",
            command=self.iniciar_dashboard,
            width=200,
            height=45,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="green",
            hover_color="darkgreen"
        )
        self.btn_iniciar.pack(pady=10)

        
        self.btn_navegador = ctk.CTkButton(
            self,
            text="Abrir no Navegador",
            command=self.abrir_navegador,
            width=200,
            height=45,
            font=ctk.CTkFont(size=14),
            fg_color="blue",
            hover_color="darkblue",
            state="disabled"
        )
        self.btn_navegador.pack(pady=10)

        
        self.btn_parar = ctk.CTkButton(
            self,
            text="Parar FlowMetrics",
            command=self.parar_dashboard,
            width=200,
            height=45,
            font=ctk.CTkFont(size=14),
            fg_color="red",
            hover_color="darkred",
            state="disabled"
        )
        self.btn_parar.pack(pady=10)

        
        self.divisor2 = ctk.CTkFrame(self, height=2, fg_color="gray")
        self.divisor2.pack(fill="x", padx=20, pady=20)

        
        self.label_rodape = ctk.CTkLabel(
            self,
            text="FlowMetrics v1.0 • Python + MySQL + Google Analytics",
            font=ctk.CTkFont(size=10),
            text_color="gray"
        )
        self.label_rodape.pack(pady=5)

    def iniciar_dashboard(self):
        self.label_status.configure(text="🟡 Status: Iniciando...")
        self.btn_iniciar.configure(state="disabled")

        thread = threading.Thread(target=self._rodar_streamlit)
        thread.daemon = True
        thread.start()

    def _rodar_streamlit(self):
        self.streamlit_process = subprocess.Popen(
            [sys.executable, "-m", "streamlit", "run", "dashboard/app.py",
             "--server.headless", "true"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        import time
        time.sleep(3)

        self.label_status.configure(text="Status: Rodando!")
        self.btn_navegador.configure(state="normal")
        self.btn_parar.configure(state="normal")

    def abrir_navegador(self):
        webbrowser.open("http://localhost:8501")

    def parar_dashboard(self):
        if self.streamlit_process:
            self.streamlit_process.terminate()
            self.streamlit_process = None

        self.label_status.configure(text="Status: Parado!")
        self.btn_iniciar.configure(state="normal")
        self.btn_navegador.configure(state="disabled")
        self.btn_parar.configure(state="disabled")

if __name__ == "__main__":
    app = FlowMetricsApp()
    app.mainloop()
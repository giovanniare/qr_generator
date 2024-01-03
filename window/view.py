import tkinter as tk
from tkinter import font, filedialog
from qr_gen.generator import QrGenerator
from notification import exceptions as NT


class WindowMaker():
    def __init__(self, root) -> None:
        self.root = root

    def get_window_size(self) -> tuple:
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        return (screen_height, screen_width)

    def set_window_size(self) -> None:
        screen_height, screen_width = self.get_window_size()
        screen_size = f"{int(screen_width/2)}x{int(screen_height/2)}"

        self.root.geometry(screen_size)

    def set_header_title(self) -> None:
        header_frame = tk.Frame(self.root)
        header_frame.pack()
        header = "QR Generator"
        font_size = font.Font(size=20)
        header_label = tk.Label(header_frame, text=header, font=font_size)
        header_label.pack(padx=20, pady=20)

    def set_secundary_window_size(self, secundary_window) -> None:
        screen_height, screen_width = self.get_window_size()
        xside = int(screen_width/2)
        yside = int(screen_height/3)
        screen_size = f"{xside}x{yside}"

        secundary_window.geometry(screen_size)

    def build_single_url_qr(self, label, url, name):
        qr_gen = QrGenerator()
        qr_gen.initialize()

        try:
            qr_gen.build_single_url_qr(url, name)
            label.config(text="Todo cool!! QR listo!!", fg="#27A243")
        except NT.NoName as e:
            label.config(text=e.message, fg="orange")
        except NT.NoUrl as e:
            label.config(text=e.message, fg="orange")

    def single_qr_url_generator(self):
        window_pop = tk.Toplevel(self.root)
        window_pop.title("Single QR URL Gen")
        self.set_secundary_window_size(window_pop)

        options_frame = tk.Frame(window_pop)
        options_frame.pack()

        instruction = tk.Label(options_frame, text="Introduce el url para generar")
        instruction.pack()
        url = tk.Entry(options_frame)
        url.pack(pady=10)

        img_name = tk.Label(options_frame, text="Introduce el nombre para la imagen")
        img_name.pack()
        name = tk.Entry(options_frame)
        name.pack(pady=10)

        result_label = tk.Label(options_frame, text="")
        btn_send = tk.Button(options_frame, text="Send", command=lambda: self.build_single_url_qr(result_label, url, name))
        btn_send.pack(pady=10)
        result_label.pack(side="bottom", pady=(70, 10), anchor="center")

        btn_exit = tk.Button(window_pop, text="Close", command=window_pop.destroy)
        btn_exit.pack(side="bottom", pady=10, padx=10, anchor="se")

    def cargar_imagen(self, img_path):
        # Mostrar el cuadro de diálogo de apertura de archivos
        ruta_archivo = filedialog.askopenfilename()

        # Verificar si el usuario seleccionó un archivo
        if ruta_archivo:
            # Cargar la imagen seleccionada
            img_path.set(ruta_archivo)

    def build_url_qr_with_logo(self, label, logo, url, name):
        qr_gen = QrGenerator()
        qr_gen.initialize()

        try:
            qr_gen.build_url_qr_with_logo(logo, url, name)
            label.config(text="Todo cool!! QR listo!!", fg="#27A243")
        except NT.NoName as e:
            label.config(text=e.message, fg="orange")
        except NT.NoUrl as e:
            label.config(text=e.message, fg="orange")
        except NT.NoLogo as e:
            label.config(text=e.message, fg="orange")

    def logo_qr_url_generator(self):
        window_pop = tk.Toplevel(self.root)
        window_pop.title("Logo QR URL Gen")
        self.set_secundary_window_size(window_pop)

        options_frame = tk.Frame(window_pop)
        options_frame.pack()

        instruction = tk.Label(options_frame, text="Introduce el url para generar")
        instruction.pack()
        url = tk.Entry(options_frame)
        url.pack(pady=10)

        img_name = tk.Label(options_frame, text="Introduce el nombre para la imagen")
        img_name.pack()
        name = tk.Entry(options_frame)
        name.pack(pady=10)

        img_label = tk.Label(options_frame, text="Selecciona la imagen")
        img_label.pack()
        img_path = tk.StringVar()
        img_path.set("")
        boton_cargar = tk.Button(options_frame, text="Cargar Imagen", command=lambda: self.cargar_imagen(img_path))
        boton_cargar.pack(pady=10)

        result_label = tk.Label(options_frame, text="")
        btn_send = tk.Button(options_frame, text="Send", command=lambda: self.build_url_qr_with_logo(result_label, img_path, url, name))
        btn_send.pack(pady=10)
        result_label.pack(side="bottom", pady=(70, 10), anchor="center")

        btn_exit = tk.Button(window_pop, text="Close", command=window_pop.destroy)
        btn_exit.pack(side="bottom", pady=10, padx=10, anchor="se")

    def initialize(self):
        self.root.title("QR - GENERATOR")
        self.set_window_size()
        self.set_header_title()

        options_frame = tk.Frame(self.root)
        options_frame.pack()

        set_report_dates_btn = tk.Button(options_frame, text="Single QR url", command=self.single_qr_url_generator)
        set_report_dates_btn.pack(padx=25, pady=20, side="left")

        build_all_statements_btn = tk.Button(options_frame, text="QR url - Logo", command=self.logo_qr_url_generator)
        build_all_statements_btn.pack(padx=25, pady=20, side="left")

        close_btn = tk.Button(self.root, text="Close", command=self.root.destroy)
        close_btn.pack(side="bottom", pady=20, anchor="center")

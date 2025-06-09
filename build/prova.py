import tkinter as tk
from tkinter import Tk, Canvas, Button, PhotoImage

class CanvasFrame(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack()

        # Canvas
        self.canvas = tk.Canvas(self, width=469, height=531, bg='white',bd=0,highlightthickness=0,relief="ridge")
        self.canvas.pack()
        # Aggiungi qui altri elementi grafici sul canvas

        # Bottone
        self.button_image = PhotoImage(file="assets/button_1.png")
        self.button = tk.Button(
            self,
            image=self.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_click,  # Chiamata a una funzione per gestire il click
            relief="flat"
        )
        self.button.place(x=115, y=299, width=239, height=34)

        image_image_1 = PhotoImage(
        file="assets/image_1.png")
        image_1 = self.canvas.create_image(
            455.0,
            15.0,
            image=image_image_1
        )
        self.canvas.create_rectangle(
        58.0,
        144.0,
        408.0,
        184.0,
        fill="#BCD772",
        outline="")
        self.canvas.create_rectangle(
        58.0,
        227.0,
        408.0,
        267.0,
        fill="#BBD672",
        outline="")
        entry_image_1 = PhotoImage(
            file="assets/entry_1.png")
        entry_bg_1 = self.canvas.create_image(
            244.5,
            164.0,
            image=entry_image_1
        )
        entry_1 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=97.0,
            y=149.0,
            width=295.0,
            height=28.0
        )
        entry_image_2 = PhotoImage(
            file="assets/entry_2.png")
        entry_bg_2 = self.canvas.create_image(
            244.5,
            247.0,
            image=entry_image_2
        )
        entry_2 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=97.0,
            y=232.0,
            width=295.0,
            height=28.0
        )
        self.canvas.create_text(
        58.0,
        205.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
     )

        self.canvas.create_text(
            58.0,
            122.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Inter Bold", 16 * -1)
        )
        self.canvas.create_text(
        353.0,
        489.0,
        anchor="nw",
        text=" Nicolò Marotta",
        fill="#F7D9D9",
        font=("Inter", 16 * -1)
    )

        self.canvas.create_text(
        58.0,
        344.0,
        anchor="nw",
        text="Register \n",
        fill="#0DD567",
        font=("Inter BoldItalic", 16 * -1)
    )
    def button_click(self):
        # Inserisci qui il codice da eseguire quando il pulsante viene cliccato
        print("Pulsante premuto!")

# Creazione della finestra principale
root = tk.Tk()
root.title("Finestra con Canvas nel Frame")

# Inserimento del frame nella finestra principale
canvas_frame = CanvasFrame(root)
canvas_frame.pack()

# Avvio del mainloop
root.mainloop()

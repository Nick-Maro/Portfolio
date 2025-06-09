from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame

def create_login_frame(window):
    """Creates a login frame with organized widgets."""

    login_frame = Frame(window, bg="#FFFFFF")
    login_frame.pack(fill="both", expand=True)

    # Background canvas
    canvas = Canvas(login_frame, bg="#FFFFFF", height=511, width=469, bd=0, highlightthickness=0, relief="ridge")
    canvas.pack(fill="both", expand=True)

    # Green rectangles
    canvas.create_rectangle(58.0, 144.0, 408.0, 184.0, fill="#BCD772", outline="")
    canvas.create_rectangle(58.0, 227.0, 408.0, 267.0, fill="#BBD672", outline="")

    # Entry fields with background images
    entry_image_1 = PhotoImage(file=Path("assets/entry_1.png"))
    entry_bg_1 = canvas.create_image(244.5, 164.0, image=entry_image_1)
    entry_1 = Entry(login_frame, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_1.place(x=97.0, y=149.0, width=295.0, height=28.0)

    entry_image_2 = PhotoImage(file=Path("assets/entry_2.png"))
    entry_bg_2 = canvas.create_image(244.5, 247.0, image=entry_image_2)
    entry_2 = Entry(login_frame, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_2.place(x=97.0, y=232.0, width=295.0, height=28.0)

    # Image placements
    image_image_1 = PhotoImage(file=Path("assets/image_1.png"))
    canvas.create_image(455.0, 15.0, image=image_image_1)

    image_image_2 = PhotoImage(file=Path("assets/image_2.png"))
    canvas.create_image(79.0, 164.0, image=image_image_2)

    image_image_3 = PhotoImage(file=Path("assets/image_3.png"))
    canvas.create_image(79.0, 246.0, image=image_image_3)

    # Text labels
    canvas.create_text(58.0, 205.0, anchor="nw", text="Password", fill="#000000", font=("Inter Bold", -16))
    canvas.create_text(58.0, 122.0, anchor="nw", text="Username", fill="#000000", font=("Inter Bold", -16))

    # Button with background image
    button_image_1 = PhotoImage(file=Path("assets/button_1.png"))
    button_1 = Button(login_frame, image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
    button_1.place(x=115.0, y=299.0, width=239.0, height=34.0)

    # Text links (can be made into buttons)
    canvas.create_text(58.0, 344.0, anchor="nw", text="Register \n", fill="#0DD567", font=("Inter BoldItalic", -16))
    canvas.create_text(264.0, 344.0, anchor="nw", text="Recover password", fill="#0DD567", font=("Inter BoldItalic", -16))

if __name__ == "__main__":
    window = Tk()
    create_login_frame(window)
    window.mainloop()
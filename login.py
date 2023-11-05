
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x550")
window.configure(bg = "#EBEBC3")


canvas = Canvas(
    window,
    bg = "#EBEBC3",
    height = 550,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    87.0,
    fill="#F1C40F",
    outline="")

canvas.create_text(
    257.0,
    0.0,
    anchor="nw",
    text="Login",
    fill="#F5F5DC",
    font=("Righteous Regular", 70 * -1)
)

canvas.create_text(
    323.0,
    130.0,
    anchor="nw",
    text="Usuario:",
    fill="#E67E22",
    font=("Righteous Regular", 30 * -1)
)

canvas.create_text(
    305.0,
    280.0,
    anchor="nw",
    text="Contraseña:",
    fill="#E67E22",
    font=("Righteous Regular", 30 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    391.0,
    224.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F2DD88",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=219.0,
    y=189.0,
    width=344.0,
    height=69.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    391.0,
    360.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F2DD88",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=219.0,
    y=325.0,
    width=344.0,
    height=69.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("iniciar.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=281.0,
    y=431.0,
    width=202.0,
    height=58.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("user.png"))
image_1 = canvas.create_image(
    148.0,
    224.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("password.png"))
image_2 = canvas.create_image(
    148.0,
    357.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()

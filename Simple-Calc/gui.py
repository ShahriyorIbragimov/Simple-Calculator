from pathlib import Path
from customtkinter import CTk, END, CTkTextbox
from tkinter import Canvas, Button, PhotoImage


def num_click(symbol):
    entry_1.insert(END, symbol)


def clean():
    entry_1.delete('1.0', END)


def plus():
    num1 = entry_1.get('1.0', 'end-1c')
    entry_1.delete('1.0', END)
    global f_num
    global value
    value = 'addition'
    f_num = num1


def subtract():
    num1 = entry_1.get('1.0', 'end-1c')
    entry_1.delete('1.0', END)
    global f_num
    global value
    value = 'subtract'
    f_num = num1


def divide():
    num1 = entry_1.get('1.0', 'end-1c')
    entry_1.delete('1.0', END)
    global f_num
    global value
    value = 'division'
    f_num = num1


def multiply():
    num1 = entry_1.get('1.0', 'end-1c')
    entry_1.delete('1.0', END)
    global f_num
    global value
    value = 'multiplication'
    f_num = num1


def perc():
    num1 = entry_1.get('1.0', 'end-1c')
    entry_1.delete('1.0', END)
    global f_num
    global value
    value = 'percentage'
    f_num = num1


def radical():
    num1 = entry_1.get('1.0', 'end-1c')
    entry_1.delete('1.0', END)
    global f_num
    f_num = num1
    entry_1.insert('1.0', float(f_num) / float(f_num))


def equal():
    sec_num = entry_1.get('1.0', END)
    entry_1.delete('1.0', END)
    global result
    if value == 'addition':
        result = float(f_num) + float(sec_num)
        entry_1.insert('1.0', result)
    elif value == 'subtract':
        result = float(f_num) - float(sec_num)
        entry_1.insert('1.0', result)
    elif value == 'division':
        result = float(f_num) / float(sec_num)
        entry_1.insert('1.0', result)
    elif value == 'multiplication':
        result = float(f_num) * float(sec_num)
        entry_1.insert('1.0', result)
    elif value == 'percentage':
        result = float(f_num) % float(sec_num)
        entry_1.insert('1.0', result)
    else:
        entry_1.insert('1.0', 'ERROR!')


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = CTk()
window.title('Calculator')
window.geometry("338x453")
window.configure(bg = "#FFFFFF")
window.set_appearance_mode(mode_string='light')
window.iconbitmap(relative_to_assets('icon.ico'))

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 453,
    width = 338,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=multiply,
    relief="flat"
)
button_1.place(
    x=261.0,
    y=212.0,
    width=70.0,
    height=51.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=subtract,
    relief="flat"
)
button_2.place(
    x=261.0,
    y=273.0,
    width=70.0,
    height=51.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=plus,
    relief="flat"
)
button_3.place(
    x=261.0,
    y=334.0,
    width=70.0,
    height=112.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=equal,
    relief="flat"
)
button_4.place(
    x=176.0,
    y=395.0,
    width=70.0,
    height=51.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click('.'),
    relief="flat"
)
button_5.place(
    x=91.0,
    y=395.0,
    width=70.0,
    height=51.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click(0),
    relief="flat"
)
button_6.place(
    x=6.0,
    y=395.0,
    width=70.0,
    height=51.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click(3),
    relief="flat"
)
button_7.place(
    x=177.0,
    y=334.0,
    width=67.0,
    height=51.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click(2),
    relief="flat"
)
button_8.place(
    x=92.0,
    y=334.0,
    width=67.0,
    height=51.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click(1),
    relief="flat"
)
button_9.place(
    x=7.0,
    y=334.0,
    width=67.0,
    height=51.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click(6),
    relief="flat"
)
button_10.place(
    x=177.0,
    y=273.0,
    width=67.0,
    height=51.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click(5),
    relief="flat"
)
button_11.place(
    x=92.0,
    y=273.0,
    width=67.0,
    height=51.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click(4),
    relief="flat"
)
button_12.place(
    x=7.0,
    y=273.0,
    width=67.0,
    height=51.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click(9),
    relief="flat"
)
button_13.place(
    x=177.0,
    y=212.0,
    width=67.0,
    height=51.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click(8),
    relief="flat"
)
button_14.place(
    x=92.0,
    y=212.0,
    width=67.0,
    height=51.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: num_click(7),
    relief="flat"
)
button_15.place(
    x=7.0,
    y=212.0,
    width=67.0,
    height=51.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=divide,
    relief="flat"
)
button_16.place(
    x=261.0,
    y=151.0,
    width=70.0,
    height=51.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=176.0,
    y=151.0,
    width=70.0,
    height=51.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=91.0,
    y=151.0,
    width=70.0,
    height=51.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=6.0,
    y=151.0,
    width=70.0,
    height=51.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=window.quit,
    relief="flat"
)
button_20.place(
    x=271.0,
    y=96.0,
    width=60.0,
    height=45.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=radical,
    relief="flat"
)
button_21.place(
    x=205.0,
    y=96.0,
    width=60.0,
    height=45.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=perc,
    relief="flat"
)
button_22.place(
    x=139.0,
    y=96.0,
    width=60.0,
    height=45.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat"
)
button_23.place(
    x=73.0,
    y=96.0,
    width=60.0,
    height=45.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=clean,
    relief="flat"
)
button_24.place(
    x=7.0,
    y=96.0,
    width=60.0,
    height=45.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    169.0,
    43.0,
    image=entry_image_1
)
entry_1 = CTkTextbox(
    master=window,
    width=338,
    height=85,
    font=('JetBrains Mono', 25),
    fg_color='snow',
    text_color='black',
    corner_radius=0
)
entry_1.place(
    x=0.0,
    y=0.0,
)

window.resizable(False, False)
window.mainloop()

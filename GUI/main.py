import serial.tools.list_ports
import functools
from tkinter import *

TITLE = "Interface de commande du robot"
TITLE_PORTS_WINDOW = "Sélection du port série"
FONT_SIZE_TITLE = 18
FONT_SIZE = 12
FONT_SIZE_AUTHOR = 8

# Fenêtre principale
root = Tk()
root.title(TITLE)
root.geometry("800x600")
root.minsize(800, 600)


def open_ports_window():
    ports_window = Toplevel()
    ports_window.title(TITLE_PORTS_WINDOW)
    title_ports_window = Label(ports_window,
                               text=TITLE_PORTS_WINDOW,
                               font=("Helvetica", FONT_SIZE_TITLE))
    title_ports_window.grid(row=0, column=0)
    btn2 = Button(ports_window, text="Fermer", command=ports_window.destroy).grid(row=15, column=0)

    ports = serial.tools.list_ports.comports()
    serial_obj = serial.Serial()

    def init_com_port(index):
        current_port = str(ports[index])
        com_port_var = str(current_port.split(' ')[0])
        serial_obj.port = com_port_var
        serial_obj.baudrate = 9600
        serial_obj.open()
        serial_obj.write("1")

    for onePort in ports:
        com_button = Button(ports_window, text=onePort,
                            command=functools.partial(init_com_port, index=ports.index(onePort)))
        com_button.grid(row=ports.index(onePort) + 1, column=0)


btn = Button(root, text=TITLE_PORTS_WINDOW, command=open_ports_window).grid(row=5, column=0)

title = Label(root,
              text=TITLE,
              font=("Helvetica", FONT_SIZE_TITLE))
title.grid(row=0, column=0)

author = Label(root,
               text="Armand Wayoff - 2021",
               font=("Helvetica", FONT_SIZE_AUTHOR))
author.place(relx=0.0, rely=1.0, anchor='sw')

label_slider_air = Label(root,
                         text="Slider air",
                         font=("Helvetica", FONT_SIZE))
label_slider_air.grid(row=1, column=0)

slider_air = Scale(root,
                   from_=0,
                   to=100,
                   orient=HORIZONTAL)
slider_air.grid(row=1, column=1)

label_slider_camera = Label(root,
                            text="Slider camera",
                            font=("Helvetica", FONT_SIZE))
label_slider_camera.grid(row=2, column=0)

slider_camera = Scale(root,
                      from_=0,
                      to=100,
                      orient=HORIZONTAL)
slider_camera.grid(row=2, column=1)

root.mainloop()

import serial.tools.list_ports
import functools
from tkinter import *

FONT_FAMILY = "Helvetica"
TITLE = "Interface de commande du robot"
TITLE_PORTS_WINDOW = "Sélection du port série"
FONT_SIZE_TITLE = 18
FONT_SIZE = 12
FONT_SIZE_AUTHOR = 8

# Fenêtre principale
root = Tk()
root.title(TITLE)


def open_ports_window():
    ports_window = Toplevel()
    ports_window.title(TITLE_PORTS_WINDOW)
    # title_ports_window = Label(ports_window, text=TITLE_PORTS_WINDOW, font=(FONT_FAMILY, FONT_SIZE_TITLE))
    # title_ports_window.grid(row=0, column=0, padx=20, pady=10)

    ports = serial.tools.list_ports.comports()
    serial_obj = serial.Serial()

    def init_com_port(index):
        current_port = str(ports[index])
        com_port_var = str(current_port.split(' ')[0])
        serial_obj.port = com_port_var
        serial_obj.baudrate = 9600
        if not serial_obj.isOpen():
            serial_obj.open()

    if len(ports) > 0:
        for onePort in ports:
            com_button = Button(ports_window, text=onePort,
                                command=functools.partial(init_com_port, index=ports.index(onePort)))
            com_button.grid(row=ports.index(onePort) + 1, column=0, padx=10, pady=10)
    else:
        lb1 = Label(ports_window,
                    text="Aucun port série disponible",
                    font=(FONT_FAMILY, FONT_SIZE))
        lb1.grid(row=1, column=0)


btn = Button(root, text=TITLE_PORTS_WINDOW, command=open_ports_window)
btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

title = Label(root,
              text=TITLE,
              font=(FONT_FAMILY, FONT_SIZE_TITLE))
title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

author = Label(root,
               text="Armand Wayoff - 2021",
               font=(FONT_FAMILY, FONT_SIZE_AUTHOR))
author.grid(row=15, column=0, columnspan=2, pady=10)

label_scale_air = Label(root,
                         text="Slider air",
                         font=(FONT_FAMILY, FONT_SIZE))
label_scale_air.grid(row=2, column=0)

scale_air = Scale(root,
                   from_=0,
                   to=100,
                   orient=HORIZONTAL)
scale_air.grid(row=2, column=1)

label_scale_camera = Label(root,
                            text="Slider camera",
                            font=(FONT_FAMILY, FONT_SIZE))
label_scale_camera.grid(row=3, column=0)

scale_camera = Scale(root,
                      from_=0,
                      to=100,
                      orient=HORIZONTAL)
scale_camera.grid(row=3, column=1)

root.mainloop()

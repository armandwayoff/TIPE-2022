__author__ = "Armand Wayoff"
__email__ = "armandwayoff@lavabit.com"
__date__ = "Oct 2021"

import serial.tools.list_ports
import functools
from tkinter import *

FONT_FAMILY = "Helvetica"
TITLE = "Interface de commande du robot"
FONT_SIZE_TITLE = 12
FONT_SIZE = 10
FONT_SIZE_AUTHOR = 8
DELAY = 500  # ms

state_port = False

# Main window
root = Tk()
root.title(TITLE)

ports = serial.tools.list_ports.comports()


def open_ports_window():
    ports_window = Toplevel()
    ports_window.grab_set()
    ports_window.title("Sélectionner un port série")

    global serial_obj
    serial_obj = serial.Serial()

    def init_com_port(index):
        current_port = str(ports[index])
        com_port_var = str(current_port.split(' ')[0])
        serial_obj.port = com_port_var
        serial_obj.baudrate = 9600
        if not serial_obj.isOpen():
            serial_obj.open()

        global state_port
        state_port = True

        label_select_port.config(text="Port série sélectionné : " + com_port_var)
        button_select_port.config(text="Modifier")

        ports_window.destroy()

    if len(ports) > 0:
        for onePort in ports:
            com_button = Button(ports_window, text=onePort,
                                command=functools.partial(init_com_port, index=ports.index(onePort)))
            com_button.grid(row=ports.index(onePort) + 1, column=0, padx=10, pady=10)
    else:
        no_ports = Label(ports_window,
                         text="Aucun port série disponible",
                         font=(FONT_FAMILY, FONT_SIZE))
        no_ports.grid(row=1, column=0, padx=10, pady=10)


def send_data(serial_port):
    data = (str(scale_air.get()) + " " + str(scale_camera.get())).encode()
    serial_port.write(data)
    root.after(DELAY, send_data)


if state_port:
    root.after(DELAY, send_data)

# Widgets

label_select_port = Label(root,
                          text="Auncun port série sélectionné",
                          font=(FONT_FAMILY, FONT_SIZE))
label_select_port.grid(row=1, column=0, padx=10, pady=10)

button_select_port = Button(root,
                            text="Sélectionner un port série",
                            command=open_ports_window)
button_select_port.grid(row=1, column=1, padx=10, pady=10)

main_title = Label(root,
                   text=TITLE,
                   font=(FONT_FAMILY, FONT_SIZE_TITLE),
                   bg="white",
                   borderwidth=1,
                   relief="solid")
main_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10, ipadx=10, ipady=10)

label_scale_air = Label(root,
                        text="Débit d'air (%)",
                        font=(FONT_FAMILY, FONT_SIZE))
label_scale_air.grid(row=2, column=0)

scale_air = Scale(root,
                  from_=0,
                  to=100,
                  orient=HORIZONTAL)
scale_air.grid(row=2, column=1)

label_scale_camera = Label(root,
                           text="Vitesse du cable (%)",
                           font=(FONT_FAMILY, FONT_SIZE))
label_scale_camera.grid(row=3, column=0)

scale_camera = Scale(root,
                     from_=0,
                     to=100,
                     orient=HORIZONTAL)
scale_camera.grid(row=3, column=1)

author = Label(root,
               text="Armand Wayoff - 2021",
               font=(FONT_FAMILY, FONT_SIZE_AUTHOR),
               fg="grey")
author.grid(row=15, column=0, columnspan=2, pady=10)

root.mainloop()

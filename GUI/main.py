import serial.tools.list_ports
import functools
from tkinter import *

ports = serial.tools.list_ports.comports()
serialObj = serial.Serial()

TITLE = "Interface de commande du robot"
FONT_SIZE_TITLE = 18
FONT_SIZE = 12
FONT_SIZE_AUTHOR = 8

# Main window
root = Tk()
root.title(TITLE)
root.geometry("800x600")
root.minsize(800, 600)


def initComPort(index):
    currentPort = str(ports[index])
    comPortVar = str(currentPort.split(' ')[0])
    serialObj.port = comPortVar
    serialObj.baudrate = 9600
    serialObj.open()
    serialObj.write("1")


for onePort in ports:
    comButton = Button(root, text=onePort, command=functools.partial(initComPort, index=ports.index(onePort)))
    comButton.grid(row=ports.index(onePort), column=2)


author = Label(root, text="Armand Wayoff - 2021", font=("Helvetica", FONT_SIZE_AUTHOR)).place(relx=0.0,
                                                                                             rely=1.0,
                                                                                             anchor='sw')

title = Label(root, text=TITLE, fg="Black", font=("Helvetica", FONT_SIZE_TITLE)).grid(row=0, column=0)

label_slider_air = Label(root, text="Slider air", font=("Helvetica", FONT_SIZE)).grid(row=1, column=0)
slider_air = Scale(root, from_=0, to=100, orient=HORIZONTAL).grid(row=1, column=1)
label_slider_camera = Label(root, text="Slider camera", font=("Helvetica", FONT_SIZE)).grid(row=2, column=0)
slider_camera = Scale(root, from_=0, to=100, orient=HORIZONTAL).grid(row=2, column=1)

root.mainloop()

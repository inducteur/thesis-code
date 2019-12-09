import tkinter as tkinter
import matplotlib as matplotlib
from matplotlib import pyplot as plt
import numpy as np
import control as control
from tkinter import ttk
from tkinter import *

plt.style.use('classic')
def plot():
    numerator_tf_arg = numerator.get().split(" ")
    denominator_tf_arg = denominator.get().split(" ")

    numerator_tf_arg = [float(zeroes) for zeroes in numerator_tf_arg]
    denominator_tf_arg = [float(poles) for poles in denominator_tf_arg]
    rlist, klist = control.root_locus(control.TransferFunction(numerator_tf_arg, denominator_tf_arg), kvect=np.linspace(100.0, -100.0, num=1000))
    try:
        plt.show()
    except:
        pass

# setup unchanging GUI stuff
master_window = tkinter.Tk()
master_window.title("Root Locus Explorer") # window name

center_frame = tkinter.ttk.Frame(master_window, padding='20 20 20 20') # frame widget
#center_frame = tkinter.ttk.Frame(master_window, width=500, height=500, padding='20 20 20 20') # frame widget
center_frame.grid(column=0, row=0, sticky=('N, W, E, S'))

master_window.columnconfigure(0, weight=1)
master_window.rowconfigure(0, weight=1)

# bind entry variables
numerator = StringVar()
denominator = StringVar()

sys_numerator_entry = tkinter.ttk.Entry(center_frame, width=10, textvariable=numerator) # width controls the entry box size
sys_denominator_entry = tkinter.ttk.Entry(center_frame, width=10, textvariable=denominator)


# define placement of grids for bound vars
sys_numerator_entry.grid(column=2, row=4, sticky=(W, E))
sys_denominator_entry.grid(column=2, row=8, sticky=(W, E))

# configure entry button. this button executes whatever function "command" is
test_button = tkinter.ttk.Button(center_frame, text='Plot Root Locus', command=plot)
test_button.grid(column=14, row=1, sticky=W)

ttk.Label(center_frame, text="Input transfer function, separated by spaces\n\n").grid(column=1, row=1, sticky=E)
ttk.Label(center_frame, text="numerator").grid(column=3, row=4, sticky=W)
ttk.Label(center_frame, text="denominator").grid(column=3, row=8, sticky=W)


master_window.mainloop()
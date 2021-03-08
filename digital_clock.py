from tkinter import *
from tkinter.ttk import *

#(strftime) to convert date and time to their string representation
from time import strftime

#to create UI
#root-is the root window in which all other widgets go
root = Tk()

#to create title
root.title("Digital Clock")

#defining a function to get time
#string  to strore time in timeformat
def time():
    string = strftime('%H:%M:%S %p') 
    label.config(text=string)
    label.after(1000,time)

#label to store all the widgets parameter
# using custom fonts here from ds_digital  
label =Label(root, font=("ds-digital",50),background = "black",foreground = "red")

#pack- geomatry manager ehich organizes widgets in blocks
#anchor -to define position of text relative to refrence point
label.pack(anchor='center')

time() #calling time funtion

mainloop()
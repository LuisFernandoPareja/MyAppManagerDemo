import customtkinter
from tkinter import *
from tkinter import filedialog
import os


# Set theme and color options
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


def openFile():
    filepath = filedialog.askopenfilename()
    print(filepath)

# Size of Window
root = customtkinter.CTk()
root.geometry('500x350')

frame1 = customtkinter.CTkFrame(master=root)

top_segmented_button = customtkinter.CTkSegmentedButton(master=root, values=['File', 'Datenbank', 'Database'], corner_radius=0)
top_segmented_button.pack()


CRUD_segmented_button = customtkinter.CTkSegmentedButton(master=root, values=['Select', 'Update', 'Insert', 'Delete'])
CRUD_segmented_button.pack(pady=20)

openFile_button = customtkinter.CTkButton(master=root, text='open file', command=openFile)
openFile_button.pack()




root.mainloop()






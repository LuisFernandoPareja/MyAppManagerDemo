import customtkinter
import os
from PIL import Image
from tkinter import filedialog


# list_files = os.listdir(filedialog.askdirectory())
list_files = []

class MyScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text=item)
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
        self.checkbox_list.append(checkbox)

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTkScrollableFrame example")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)



        # create scrollable checkbox frame
        self.scrollable_checkbox_frame = MyScrollableFrame(master=self, width=200, command=self.checkbox_frame_event, item_list=list_files)

        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")

    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")





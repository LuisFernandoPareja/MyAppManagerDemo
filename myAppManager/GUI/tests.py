from tkinter import filedialog
import customtkinter
import os
from PIL import Image
import MyScrollableFrame
from DB import db_operations

CATALOGS_FILEPATH = "C:\\Users\\Fernando Bernal\\Desktop\\Catalogs"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("My App Manager")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hula-hoop.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")),
                                                       size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "open-folder.png")),
                                                       size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  My App Manager",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="",
                                                                   image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_open_file = customtkinter.CTkButton(self.home_frame, text="Open Catalogs",
                                                                   image=self.image_icon_image, compound="right",
                                                                   command=self.get_catalogs)
        self.home_frame_button_open_file.grid(row=2, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="",
                                                                     image=self.large_test_image)

        self.second_frame_large_image_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.option_menu = customtkinter.CTkOptionMenu(self.second_frame, values=["Artist Name", "Song Name"])
        self.option_menu.grid(row=3, column=0, padx=20, pady=10)

        self.second_frame_entry = customtkinter.CTkEntry(self.second_frame, placeholder_text="Search")
        self.second_frame_entry.grid(row=4, column=0)

        self.second_frame_search_button = customtkinter.CTkButton(self.second_frame, text="Search",
                                                              image=self.image_icon_image, compound="right",
                                                              command=self.search_inquiry)

        self.second_frame_search_button.grid(row=5, column=0, pady=10)

        self.second_frame_textbox = customtkinter.CTkTextbox(self.second_frame)
        self.second_frame_textbox.insert("0.0", "Results Here\n" * 5)
        self.second_frame_textbox.configure(state="disabled")  # configure textbox to be read-only
        self.second_frame_textbox.grid(row=6, column=0)



        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def get_catalogs(self):
        # filepath = filedialog.askopenfilename()
        list_files = os.listdir(CATALOGS_FILEPATH)
        print(CATALOGS_FILEPATH)
        scrollable_checkbox_home_frame = MyScrollableFrame.MyScrollableFrame(master=self.home_frame, width=200,
                                                                             command=None,
                                                                             item_list=list_files)
        scrollable_checkbox_home_frame.grid(row=4, column=0, padx=20, pady=10)

    def option_menu_callback(self, choice):
        print("option_menu dropdown clicked:", choice)

    def search_inquiry(self):
        if self.option_menu.get() == 'Song Name':
            print('Searching Artist By SongName')

        else:
            print('Searching Song By ArtistName')
            all_songs = db_operations.all_songs(self.second_frame_entry.get())
            print(type(all_songs))
            self.second_frame_textbox.configure(state="normal")
            self.second_frame_textbox.delete('0.0', 'end')
            for i in all_songs:
                self.second_frame_textbox.insert("0.0", ''.join(i)+'\n')
            self.second_frame_textbox.configure(state="disabled")


app = App()
app.mainloop()

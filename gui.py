from customtkinter import filedialog, CTkLabel, CTkButton, CTkImage
from utils import translate, get_paragraphs, build_document
from PIL import Image
from getpass import getuser
import subprocess

SUPPORTED_LANGUAGES = {
    "EN": "en",
    "ES": "es"
}

def populate_main_window(master):
    STATE = {
        "file": "",
        "from": SUPPORTED_LANGUAGES["EN"],
        "to": SUPPORTED_LANGUAGES["ES"],
        "listener": False
    }

    def toggle_language():
        if STATE["from"] == SUPPORTED_LANGUAGES["EN"]:
            STATE["from"] = SUPPORTED_LANGUAGES["ES"]
            STATE["to"] = SUPPORTED_LANGUAGES["EN"]
        elif STATE["from"] == SUPPORTED_LANGUAGES["ES"]:
            STATE["from"] = SUPPORTED_LANGUAGES["EN"]
            STATE["to"] = SUPPORTED_LANGUAGES["ES"]
        
        lbl_language.configure(require_redraw=True, text=f"{STATE['to']}")

    def toggle_listener(): 
        STATE["listener"] = not STATE["listener"]

    def get_translation():
        doc = get_paragraphs(STATE["file"])
        STATE["file"] = build_document(translate(STATE["from"], STATE["to"], doc), f"new_file_{STATE['to']}")
        toggle_listener()
        btn_handling.configure(text="Open file", command=open_file)

    open_file = lambda: subprocess.Popen(f"start {STATE['file']}", shell=True)
    exit_app = lambda: master.destroy()

    img_language = CTkImage(Image.open(fp="images/traducir.png"))
    btn_handling = CTkButton(master, text="Translate", command=get_translation, corner_radius=20)
    btn_exit = CTkButton(master, text="Exit", command=exit_app, corner_radius=20, fg_color="red", hover_color="darkred")

    def set_path():
        STATE["file"] = filedialog.askopenfilename(
                initialdir=f"C:/Users/{getuser()}/", 
                title="Select a file", 
                filetypes=[("Word documents", "*.docx")]
            )
        if STATE["file"] != "":
            if STATE["listener"]:
                btn_handling.configure(text="Translate", command=get_translation)
                toggle_listener()
            else:
                btn_handling.place(relx=.5, rely=.6, anchor="center")
                btn_exit.place(relx=.5, rely=.7, anchor="center")

    lbl_title = CTkLabel(master, text="Welcome!", font=("Helvetica bold", 26))
    lbl_language = CTkLabel(master, text=f"{STATE['to']}", font=("Helvetica bold", 12))
    btn_language = CTkButton(master, image=img_language, text="", command=toggle_language, width=7, corner_radius=5, fg_color="#FEC", hover_color="#EDB")
    btn_set_file = CTkButton(master, text="Select a file", command=set_path, corner_radius=20)
	
    lbl_title.place(relx=.5, rely=.3, anchor="center")
    lbl_language.place(relx=.8, rely=.1, anchor="center")
    btn_language.place(relx=.9, rely=.1, anchor="center")
    btn_set_file.place(relx=.5, rely=.5, anchor="center")
    btn_exit.place(relx=.5, rely=.6, anchor="center")
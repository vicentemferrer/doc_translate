from customtkinter import CTk
from gui import populate_main_window

def main():
	app = CTk()
	# gui = App(master=app)
	
	app.geometry("300x300")
	app.wm_title("DocTranslate")
	populate_main_window(app)

	app.mainloop()

if __name__ == "__main__":
	main()

# class App:
# 	def __init__(self, master: CTk):
# 		self.master = master
# 		self.master.geometry("300x300")
# 		self.master.wm_title("DocTranslate")

# 		self.doc_path = ""

# 		self.lbl_title = CTkLabel(self.master, text="Welcome!", font=("Helvetica bold", 26))
# 		self.btn_set_file = CTkButton(self.master, text="Select a file", command=self.set_path, corner_radius=20)
# 		self.btn_translate = CTkButton(self.master, text="Translate", command=self.get_translation, corner_radius=20)
# 		self.btn_open_file = CTkButton(self.master, text="Open file", command=self.open_file, corner_radius=20)
# 		self.btn_exit = CTkButton(self.master, text="Exit", command=self.exit, corner_radius=20, fg_color="red", hover_color="red")

# 		self.lbl_title.place(relx=.5, rely=.3, anchor="center")
# 		self.btn_set_file.place(relx=.5, rely=.5, anchor="center")
# 		self.btn_exit.place(relx=.5, rely=.6, anchor="center")
	
# 	def set_path(self):
# 		self.doc_path = filedialog.askopenfilename(
# 			initialdir=f"C:/Users/{getuser()}/", 
# 			title="Select a file", 
# 			filetypes=[("Word documents", "*.docx")]
# 		)
		
# 		if self.doc_path != "":
# 			self.btn_translate.place(relx=.5, rely=.6, anchor="center")
# 			self.btn_exit.place(relx=.5, rely=.7, anchor="center")

# 	def get_translation(self):
# 		doc = get_paragraphs(self.doc_path)
# 		self.doc_path = build_document(translate(doc), "new_file")
# 		self.btn_translate.destroy()
# 		self.btn_open_file.place(relx=.5, rely=.6, anchor="center")
	
# 	def open_file(self):
# 		subprocess.Popen(f"start {self.doc_path}", shell=True)

# 	def exit(self):
# 		self.master.destroy()
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import sys
from tkinter.ttk import *
import anavarin
# import _imaging
# import Image

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
window = Tk()
window.resizable(None, None)

height = 530
width = 600
x = (window.winfo_screenwidth()//2)-(width//2)
y = (window.winfo_screenheight()//2)-(height//2)
window.geometry("{}x{}+{}+{}".format(width, height, x, y))
window.wm_attributes("-topmost", True)

# -------- Remove Title Bar------
window.overrideredirect(True)
window.config(background="#1B2430")

exit_button = customtkinter.CTkButton(window, text="X", text_font=("yu gothic ui", 15, "bold"),
                                      command=lambda: exit_window(), width=5, height=5, fg_color="#1B2430",
                                      hover_color="#1B2430")
exit_button.place(x=550, y=0)

welcome_label = customtkinter.CTkLabel(window, text="Anavarin Cipher", text_font=("yu gothic ui", 30, "bold"))
welcome_label.place(x=160, y=20)

hour_img = Image.open("hour1.png")
hour_photo = ImageTk.PhotoImage(hour_img.resize((380, 350), Image.LANCZOS))
hour_label = customtkinter.CTkLabel(window, image=hour_photo)
hour_label.place(x=115, y=90)

progress_label = customtkinter.CTkLabel(window, text="Please Wait... ", text_font=("yu gothic ui", 20, "bold"))
progress_label.place(x=165, y=410)

progress = Progressbar(window, length=500)
progress.place(x=50, y=480)

i = 0


def load():
    global i
    if i <= 10:
        load_txt = f"Please Wait... {10 * i}%"
        progress_label.configure(text=load_txt)
        progress_label.after(1000, load)
        progress["value"] = 10 * i
        i += 1
    else:
        top()


load()


def exit_window():
    sys.exit(window.destroy())


def top():
    win = Toplevel()
    anavarin.LinkPage(win)
    window.withdraw()
    win.deiconify()


window.mainloop()

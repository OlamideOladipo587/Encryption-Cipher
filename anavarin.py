from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import PyPDF2
from tkinter import filedialog, messagebox
from tkinter.simpledialog import askstring
import smtplib
import random
import json
# from DigitalPersona import *
# from DigitalPersona.Registration import *
# from DigitalPersona.Auth import *
# customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"


class LinkPage:
    def __init__(self, window):
        self.window = window

        window.title("Anavarin Cipher")
        window.geometry("1366x750")
        window.state("zoomed")
        window.resizable(0, 0)
        window.config(padx=0, pady=0)

        # CIPHER DETAILS
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
                    '4', '5', '6', '7', '8', '9', ' ', '+', '-', '@', '!', '#', '$', '%', '^', '&', '*', '(', ')',
                    '_', '=', '{', '}', '|', '/', '"', ';', ':', ',', '.', '?', '>', '<']

        usernames = []

        # --------- LOGIN PAGE ---------
        loginpage = Frame(window, width=1366, height=768, bg="#1B2430", highlightthickness=0, border=0)
        login_canvas = Canvas(loginpage, width=1366, height=750, highlightthickness=0)
        bg_frame = Image.open("cipher_img.jpg")
        photo = ImageTk.PhotoImage(bg_frame.resize((1366, 750), Image.LANCZOS))
        login_canvas.create_image(683, 365, image=photo)
        login_canvas.image = photo
        login_canvas.place(x=0, y=0)

        login_frame = Frame(loginpage, bg="#1B2430", width=950, height=600)
        login_frame.place(x=170, y=60)

        txt = "Welcome To Anavarin!"
        heading = Label(login_frame, text=txt, font=("yu gothic ui", 25, "bold"), bg="#1B2430",
                        fg="white")
        heading.place(x=45, y=30, width=350, height=30)

        txt_line = Canvas(login_frame, width=100, height=2.0, bg="white", highlightthickness=0)
        txt_line.place(x=56, y=80)

        txt2 = "Login!"
        heading2 = Label(login_frame, text=txt2, font=("yu gothic ui", 20, "bold"), bg="#1B2430",
                         fg="white")
        heading2.place(x=590, y=265, width=350, height=45)

        # ----------LEFT SIDE IMAGE----------
        left_img = Image.open("loginn.png")
        photo = ImageTk.PhotoImage(left_img.resize((400, 300), Image.LANCZOS))
        left_img_label = Label(login_frame, image=photo, bg="#1B2430")
        left_img_label.image = photo
        left_img_label.place(x=5, y=190)

        # ----------Login Image----------
        login_img = Image.open("login3.png")
        photo = ImageTk.PhotoImage(login_img.resize((160, 185), Image.LANCZOS))
        login_img = Label(login_frame, image=photo, bg="#1B2430")
        login_img.image = photo
        login_img.place(x=690, y=80)

        # ----------Username----------
        username = Label(login_frame, text="Username:", font=("yu gothic ui", 15, "bold"), bg="#1B2430",
                         fg="white")
        username.place(x=470, y=320, width=150, height=45)

        password_label = Label(login_frame, text="Password:", font=("yu gothic ui", 15, "bold"), bg="#1B2430",
                         fg="white")
        password_label.place(x=470, y=380, width=150, height=45)

        username_entry = customtkinter.CTkEntry(login_frame, width=300, height=35, border_width=2,
                                                corner_radius=12, fg_color="white", bg_color="#1B2430",
                                                text_color="#1B2430")
        username_entry.focus()
        username_entry.place(x=620, y=330)
        password_entry = customtkinter.CTkEntry(login_frame, width=300, height=35, border_width=2,
                                                corner_radius=12, fg_color="white", bg_color="#1B2430",
                                                text_color="#1B2430")
        password_entry.place(x=620, y=380)


        # ----------Finger Print----------
        fingerprint = Label(login_frame, text="Fingerprint:", font=("yu gothic ui", 15, "bold"),
                            bg="#1B2430", fg="white")
        fingerprint.place(x=470, y=470, width=150, height=45)

        fingerprint_img = Image.open("finger1.png")
        photo = ImageTk.PhotoImage(fingerprint_img.resize((200, 130), Image.LANCZOS))
        fingerprint_img = Label(login_frame, image=photo, bg="#1B2430")
        fingerprint_img.image = photo
        fingerprint_img.place(x=660, y=420)

        # def login():
        #     login_username = username_entry
        #     for i in usernames:
        #         if i == login_username:
        #         # Initialize a new DigitalPersona Authentication object
        #             auth = DigitalPersonaAuth()
        #
        #         # Set the fingerprint reader to use
        #             reader_name = "DigitalPersona U.are.U 4500 Fingerprint Reader"
        #             auth.set_reader(reader_name)
        #
        #         # Prompt the user to swipe their finger
        #             print("Please swipe your finger on the fingerprint reader.")
        #             finger_data = auth.capture()
        #
        #         # Authenticate the user's fingerprint
        #             if auth.authenticate(finger_data):
        #                 print("Authentication successful!")
        #                 return True
        #             else:
        #                 print("Authentication failed.")
        #         else:
        #             messagebox.showerror(title="Authentication Error", message="Invalid Username. Try again.")

        def login():
            login_username = username_entry.get()
            login_password = password_entry.get()
            try:
                with open("user.json") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                print("no data file")
            else:
                if login_username in data and data[login_username] == login_password:
                    messagebox.showinfo(title="Authentication", message="Authentication Successful")
                    return True

        # ----------Login Button----------
        login_button = customtkinter.CTkButton(master=login_frame, text="Login", corner_radius=20,
                                               height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                               width=120, text_font=("yu gothic ui", 12, "bold"), cursor="hand2",
                                               command=lambda: show_frame(page2) if(login()) else(messagebox.showinfo(
                                                    title="Authentication Error", message="Invalid Username & or Password. Please Try again.")))
        login_button.place(x=620, y=550)
        fingerprint_login_button = customtkinter.CTkButton(master=login_frame, text="Fingerprint", corner_radius=20,
                                               height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                               width=150, text_font=("yu gothic ui", 12, "bold"), cursor="hand2",)
        fingerprint_login_button.place(x=750, y=550)
        account_button = customtkinter.CTkButton(master=login_frame, text="New User", corner_radius=20,
                                               height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                               width=150, text_font=("yu gothic ui", 12, "bold"), cursor="hand2",
                                               command=lambda: show_frame(createaccountpage))
        account_button.place(x=60, y=550)
        admin_button = customtkinter.CTkButton(master=login_frame, text="Admin", corner_radius=20,
                                                 height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                                 width=150, text_font=("yu gothic ui", 12, "bold"), cursor="hand2",
                                                 command=lambda: show_frame(adminpage))
        admin_button.place(x=240, y=550)

        # CREATE ACCOUNT PAGE
        createaccountpage = Frame(window, width=1366, height=768, bg="#1B2430", highlightthickness=0, border=0)
        createaccount_canvas = Canvas(createaccountpage, width=1366, height=750, highlightthickness=0)
        bg_frame = Image.open("cipher_img.jpg")
        photo = ImageTk.PhotoImage(bg_frame.resize((1366, 750), Image.LANCZOS))
        createaccount_canvas.create_image(683, 365, image=photo)
        createaccount_canvas.image = photo
        createaccount_canvas.place(x=0, y=0)

        createaccountframe = Frame(createaccountpage, bg="#1B2430", width=950, height=600)
        createaccountframe.place(x=170, y=60)

        txt = "Welcome To Anavarin!"
        heading = Label(createaccountframe, text=txt, font=("yu gothic ui", 25, "bold"), bg="#1B2430",
                        fg="white")
        heading.place(x=45, y=30, width=350, height=30)

        txt_line2 = Canvas(createaccountframe, width=100, height=2.0, bg="white", highlightthickness=0)
        txt_line2.place(x=56, y=80)

        txt2 = "Create Account"
        heading3 = Label(createaccountframe, text=txt2, font=("yu gothic ui", 20, "bold"), bg="#1B2430",
                         fg="white")
        heading3.place(x=590, y=265, width=350, height=45)

        # ----------LEFT SIDE IMAGE----------
        left_img2 = Image.open("loginn.png")
        photo = ImageTk.PhotoImage(left_img2.resize((400, 300), Image.LANCZOS))
        left_img_label2 = Label(createaccountframe, image=photo, bg="#1B2430")
        left_img_label2.image = photo
        left_img_label2.place(x=5, y=190)

        # ----------Login Image----------
        login_img2 = Image.open("login3.png")
        photo = ImageTk.PhotoImage(login_img2.resize((160, 185), Image.LANCZOS))
        login_img2 = Label(createaccountframe, image=photo, bg="#1B2430")
        login_img2.image = photo
        login_img2.place(x=690, y=80)

        # ----------Username----------
        username2 = Label(createaccountframe, text="Username:", font=("yu gothic ui", 15, "bold"), bg="#1B2430",
                         fg="white")
        username2.place(x=470, y=320, width=150, height=45)

        username2_entry = customtkinter.CTkEntry(createaccountframe, width=300, height=35, border_width=2,
                                                corner_radius=12, fg_color="white", bg_color="#1B2430",
                                                text_color="#1B2430")
        username2_entry.focus()
        username2_entry.place(x=620, y=330)

        password2 = Label(createaccountframe, text="Password:", font=("yu gothic ui", 15, "bold"), bg="#1B2430",
                          fg="white")
        password2.place(x=470, y=370, width=150, height=45)

        password2_entry = customtkinter.CTkEntry(createaccountframe, width=300, height=35, border_width=2,
                                                 corner_radius=12, fg_color="white", bg_color="#1B2430",
                                                 text_color="#1B2430")
        password2_entry.place(x=620, y=380)



        # ----------Finger Print----------
        fingerprint2 = Label(createaccountframe, text="Fingerprint:", font=("yu gothic ui", 15, "bold"),
                            bg="#1B2430", fg="white")
        fingerprint2.place(x=470, y=420, width=150, height=45)

        fingerprint2_img = Image.open("finger1.png")
        photo = ImageTk.PhotoImage(fingerprint2_img.resize((200, 130), Image.LANCZOS))
        fingerprint2_img = Label(createaccountframe, image=photo, bg="#1B2430")
        fingerprint2_img.image = photo
        fingerprint2_img.place(x=660, y=420)

        # def register():
        #     register_username = username2_entry.get()
        #     usernames.append(register_username)
        #     # Initialize a new DigitalPersona Registration object
        #     registration = DigitalPersonaRegistration()
        #
        #     # Set the fingerprint reader to use
        #     reader_name = "DigitalPersona U.are.U 4500 Fingerprint Reader"
        #     registration.set_reader(reader_name)
        #
        #     # Prompt the user to enroll their finger
        #     print("Please place your finger on the fingerprint reader to enroll.")
        #     finger_data = registration.capture()
        #
        #     # Register the user's fingerprint
        #     if registration.enroll(finger_data):
        #         messagebox.showinfo(title="Successful", message="Registration Successful")
        #         return True
        #     else:
        #         # messagebox.showerror(title="Error", message="Error registering account. Try again")
        #         print("Fingerprint enrollment failed.")

        def register():
            username1 = username2_entry.get()
            password = password2_entry.get()
            new_data1 = {
                username1: password
            }
            try:
                with open("user.json", "r") as data1_file:
                    # Reading old data
                    data1 = json.load(data1_file)
            except FileNotFoundError:
                with open("user.json", "w") as data_file:
                    json.dump(new_data1, data1_file, indent=4)
            except Exception as e:
                print(e)
            else:
                # Updating old data with new data
                data1.update(new_data1)


                with open("user.json", "w") as data1_file:
                    # Saving updated data
                    json.dump(data1, data1_file, indent=4)
                    messagebox.showinfo(title="Authentiation", message="Registration Successful")
                    return True

        # ----------Login Button----------
        createaccount_button = customtkinter.CTkButton(master=createaccountframe, text="Create", corner_radius=20,
                                               height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                               width=150, text_font=("yu gothic ui", 12, "bold"), cursor="hand2",
                                                       command=lambda: show_frame(loginpage) if (register()) else (
                                                       messagebox.showinfo(
                                                           title="Error", message="Error Registering Account. Try Agian."))
                                                       )
        createaccount_button.place(x=620, y=540)
        backtologin_button = customtkinter.CTkButton(master=createaccountframe, text="Login",
                                                       corner_radius=20,
                                                       height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                                       width=150, text_font=("yu gothic ui", 12, "bold"),
                                                       cursor="hand2",
                                                       command=lambda: show_frame(loginpage)
                                                       )
        backtologin_button.place(x=770, y=540)

        # ADMIN LOGIN PAGE
        adminpage = Frame(window, width=1366, height=768, bg="#1B2430", highlightthickness=0, border=0)
        admin_canvas = Canvas(adminpage, width=1366, height=750, highlightthickness=0)
        bg1_frame = Image.open("cipher_img.jpg")
        photo = ImageTk.PhotoImage(bg1_frame.resize((1366, 750), Image.LANCZOS))
        admin_canvas.create_image(683, 365, image=photo)
        admin_canvas.image = photo
        admin_canvas.place(x=0, y=0)

        adminframe = Frame(adminpage, bg="#1B2430", width=950, height=600)
        adminframe.place(x=170, y=60)

        txt1 = "Welcome Admin!"
        heading1 = Label(adminframe, text=txt1, font=("yu gothic ui", 25, "bold"), bg="#1B2430",
                        fg="white")
        heading1.place(x=20, y=30, width=350, height=30)

        txt_line3 = Canvas(adminframe, width=100, height=2.0, bg="white", highlightthickness=0)
        txt_line3.place(x=56, y=80)

        txt3 = "Login"
        heading4 = Label(adminframe, text=txt3, font=("yu gothic ui", 20, "bold"), bg="#1B2430",
                         fg="white")
        heading4.place(x=590, y=265, width=350, height=45)

        # ----------LEFT SIDE IMAGE----------
        left_img3 = Image.open("loginn.png")
        photo = ImageTk.PhotoImage(left_img3.resize((400, 300), Image.LANCZOS))
        left_img_label3 = Label(adminframe, image=photo, bg="#1B2430")
        left_img_label3.image = photo
        left_img_label3.place(x=5, y=190)

        # ----------Login Image----------
        login_img3 = Image.open("login3.png")
        photo = ImageTk.PhotoImage(login_img3.resize((160, 185), Image.LANCZOS))
        login_img3 = Label(adminframe, image=photo, bg="#1B2430")
        login_img3.image = photo
        login_img3.place(x=690, y=80)

        # ----------Username----------
        admin_username = Label(adminframe, text="Username:", font=("yu gothic ui", 15, "bold"), bg="#1B2430",
                          fg="white")
        admin_username.place(x=470, y=320, width=150, height=45)

        adminusername_entry = customtkinter.CTkEntry(adminframe, width=300, height=35, border_width=2,
                                                 corner_radius=12, fg_color="white", bg_color="#1B2430",
                                                 text_color="#1B2430")
        adminusername_entry.focus()
        adminusername_entry.place(x=620, y=330)

        admin_password = Label(adminframe, text="Password:", font=("yu gothic ui", 15, "bold"), bg="#1B2430",
                          fg="white")
        admin_password.place(x=470, y=370, width=150, height=45)

        adminpassword_entry = customtkinter.CTkEntry(adminframe, width=300, height=35, border_width=2,
                                                 corner_radius=12, fg_color="white", bg_color="#1B2430",
                                                 text_color="#1B2430")
        adminpassword_entry.place(x=620, y=380)

        # ----------Finger Print----------
        admin_fingerprint = Label(adminframe, text="Fingerprint:", font=("yu gothic ui", 15, "bold"),
                             bg="#1B2430", fg="white")
        admin_fingerprint.place(x=470, y=420, width=150, height=45)

        fingerprint3_img = Image.open("finger1.png")
        photo = ImageTk.PhotoImage(fingerprint3_img.resize((200, 130), Image.LANCZOS))
        fingerprint3_img = Label(adminframe, image=photo, bg="#1B2430")
        fingerprint3_img.image = photo
        fingerprint3_img.place(x=660, y=420)

        def admin():
            username3 = adminusername_entry.get()
            password3 = adminpassword_entry.get()
            try:
                with open("admin.json") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                print("no data file")
            else:
                if username3 in data and data[username3] == password3:
                    messagebox.showinfo(title="Authentication", message="Authentication Successful")
                    return True

        # ----------Login Button----------
        adminlogin_button = customtkinter.CTkButton(master=adminframe, text="Login", corner_radius=20,
                                                       height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                                       width=150, text_font=("yu gothic ui", 12, "bold"),
                                                       cursor="hand2",
                                                       command=lambda: show_frame(adminpage2) if (admin()) else (
                                                           messagebox.showinfo(
                                                               title="Error",
                                                               message="Invalid Username and or Password. Try Again."))
                                                       )
        adminlogin_button.place(x=620, y=540)
        back_button = customtkinter.CTkButton(master=adminframe, text="Back",
                                                     corner_radius=20,
                                                     height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                                     width=150, text_font=("yu gothic ui", 12, "bold"),
                                                     cursor="hand2",
                                                     command=lambda: show_frame(loginpage)
                                                     )
        back_button.place(x=770, y=540)

        # ADMIN PAGE
        adminpage2 = Frame(window, width=1366, height=768, bg="#1B2430", highlightthickness=0, border=0)
        admin2_canvas = Canvas(adminpage2, width=1366, height=750, highlightthickness=0)
        bg2_frame = Image.open("cipher_img.jpg")
        photo = ImageTk.PhotoImage(bg2_frame.resize((1366, 750), Image.LANCZOS))
        admin2_canvas.create_image(683, 365, image=photo)
        admin2_canvas.image = photo
        admin2_canvas.place(x=0, y=0)

        adminframe2 = Frame(adminpage2, bg="#1B2430", width=950, height=600)
        adminframe2.place(x=170, y=60)

        txt2 = "Welcome Admin!"
        heading2 = Label(adminframe2, text=txt2, font=("yu gothic ui", 25, "bold"), bg="#1B2430",
                         fg="white")
        heading2.place(x=20, y=30, width=350, height=30)

        txt_line4 = Canvas(adminframe2, width=100, height=2.0, bg="white", highlightthickness=0)
        txt_line4.place(x=56, y=80)

        txt4 = "Update"
        heading5 = Label(adminframe2, text=txt4, font=("yu gothic ui", 20, "bold"), bg="#1B2430",
                         fg="white")
        heading5.place(x=590, y=265, width=350, height=45)

        # ----------LEFT SIDE IMAGE----------
        left_img4 = Image.open("loginn.png")
        photo = ImageTk.PhotoImage(left_img4.resize((400, 300), Image.LANCZOS))
        left_img_label4 = Label(adminframe2, image=photo, bg="#1B2430")
        left_img_label4.image = photo
        left_img_label4.place(x=5, y=190)

        # ----------Login Image----------
        login_img4 = Image.open("login3.png")
        photo = ImageTk.PhotoImage(login_img4.resize((160, 185), Image.LANCZOS))
        login_img4 = Label(adminframe2, image=photo, bg="#1B2430")
        login_img4.image = photo
        login_img4.place(x=690, y=80)

        # ----------Username----------
        user_account = Label(adminframe2, text="Username:", font=("yu gothic ui", 15, "bold"), bg="#1B2430",
                               fg="white")
        user_account.place(x=470, y=320, width=150, height=45)

        useraccount_entry = customtkinter.CTkEntry(adminframe2, width=300, height=35, border_width=2,
                                                     corner_radius=12, fg_color="white", bg_color="#1B2430",
                                                     text_color="#1B2430")
        useraccount_entry.place(x=620, y=330)

        user_password = Label(adminframe2, text="Password:", font=("yu gothic ui", 15, "bold"), bg="#1B2430",
                               fg="white")
        user_password.place(x=470, y=370, width=150, height=45)

        userpassword_entry = customtkinter.CTkEntry(adminframe2, width=300, height=35, border_width=2,
                                                     corner_radius=12, fg_color="white", bg_color="#1B2430",
                                                     text_color="#1B2430")
        userpassword_entry.place(x=620, y=380)

        # ----------Finger Print----------
        # admin2_fingerprint = Label(adminframe2, text="Fingerprint:", font=("yu gothic ui", 15, "bold"),
        #                           bg="#1B2430", fg="white")
        # admin2_fingerprint.place(x=470, y=420, width=150, height=45)
        #
        # fingerprint4_img = Image.open("finger1.png")
        # photo = ImageTk.PhotoImage(fingerprint4_img.resize((200, 130), Image.LANCZOS))
        # fingerprint4_img = Label(adminframe2, image=photo, bg="#1B2430")
        # fingerprint4_img.image = photo
        # fingerprint4_img.place(x=660, y=420)

        def delete():
            username3 = useraccount_entry.get()
            try:
                with open("user.json") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                print("no data file")
            else:
                del data[username3]  # or iterate through entries to find matching name
                with open("user.json", "w") as data_file:
                    json.dump(data, data_file)
                    return True

        # ----------Login Button----------
        add_button = customtkinter.CTkButton(master=adminframe2, text="Add", corner_radius=20,
                                                    height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                                    width=150, text_font=("yu gothic ui", 12, "bold"),
                                                    cursor="hand2",
                                                    command=lambda: messagebox.showinfo(title="Add User",
                                                                                         message="User Added Successfully") if (
                                                         register()) else (
                                                         messagebox.showinfo(
                                                             title="Error",
                                                             message="Unable to add user."))
                                                    )
        add_button.place(x=620, y=440)
        delete_button = customtkinter.CTkButton(master=adminframe2, text="Delete",
                                              corner_radius=20,
                                              height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                              width=150, text_font=("yu gothic ui", 12, "bold"),
                                              cursor="hand2",
                                              command=lambda: messagebox.showinfo(title="Delete", message="User Deleted Successfully") if (delete()) else (
                                                  messagebox.showinfo(
                                                    title="Error",
                                                    message="User not found. Try Again."))
                                              )
        delete_button.place(x=770, y=440)

        back2_button = customtkinter.CTkButton(master=adminframe2, text="Logout",
                                                corner_radius=20,
                                                height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                                width=300, text_font=("yu gothic ui", 12, "bold"),
                                                cursor="hand2",
                                                command=lambda: show_frame(loginpage)
                                                )
        back2_button.place(x=620, y=540)

        # ---------- ABOUT/SECOND PAGE ----------
        page2 = Frame(window)

        # -------- Left Side----------
        cipher_img = Image.open("cipher_img.jpg")
        photo = ImageTk.PhotoImage(cipher_img.resize((790, 768), Image.LANCZOS))

        canvas = Canvas(page2, width=700, height=768, highlightthickness=0)
        canvas.create_image(360, 365, image=photo)
        canvas.image = photo
        canvas.create_text(180, 130, text="About Anavarin", font=("yu gothic ui", 25, "bold"),
                           fill="white")
        # -------- Left Side(About Text)---------
        canvas.create_text(300, 390,
                           text="Welcome to our encryption cipher, where we\nstrive "
                                "to provide the most secure and reliable\nmeans of data "
                                "encryption. Our team of experts\nis dedicated to ensure "
                                "that your information is\nprotected from prying eyes and "
                                "malicious third parties.\n\nWe understand the ever-growing"
                                "threat to information\nsecurity, and that's why we have"
                                "developed cutting-edge\nencryption algorithms"
                                "that utilize the latest technology to\nprovide the highest level of protection for your data.", font=("yu gothic ui", 15, "bold"),
                                fill="white")
        canvas.place(x=0, y=0)
        about_line = Canvas(canvas, width=2.0, height=200, bg="white", highlightthickness=0)
        about_line.place(x=30, y=300)

        # --------- Right Side--------
        frame2 = Frame(page2, bg="white", width=750, height=768, highlightthickness=0)
        frame2.place(x=650, y=0)

        txt1 = "Get Started!"
        heading1 = Label(frame2, text=txt1, font=("yu gothic ui", 25, "bold"), bg="white",
                         fg="#1B2430")
        heading1.place(x=170, y=70, width=350, height=30)

        # ------- Encrypt Button --------
        encrypt_button = customtkinter.CTkButton(master=frame2, text="Encrypt", corner_radius=20,
                                                 height=40, fg_color="#1B2430", border_width=2, text_color="white",
                                                 width=300, text_font=("yu gothic ui", 12, "bold"), cursor="hand2",
                                                 command=lambda: show_frame(page3))

        encrypt_button.place(x=200, y=220)

        # ------- Decrypt Button --------
        decrypt_button = customtkinter.CTkButton(master=frame2, text="Decrypt", corner_radius=20,
                                                 height=40, fg_color="#1B2430", border_width=2, text_color="white",
                                                 width=300, text_font=("yu gothic ui", 12, "bold"), cursor="hand2",
                                                 command=lambda: show_frame(page4))
        decrypt_button.place(x=200, y=320)

        # # ------- How It Works Button --------
        # how_button = customtkinter.CTkButton(master=frame2, text="How It Works", corner_radius=20,
        #                                      height=40, fg_color="#1B2430", border_width=2, text_color="white",
        #                                      width=300, text_font=("yu gothic ui", 12, "bold"), cursor="hand2")
        # how_button.place(x=200, y=420)

        # ------- ABOUT/SECOND PAGE(Logout Button) --------
        logout = customtkinter.CTkButton(master=frame2, text="Logout", corner_radius=20,
                                         height=40, fg_color="#1B2430", border_width=2, text_color="white",
                                         width=300, text_font=("yu gothic ui", 12, "bold"), cursor="hand2", command=lambda: show_frame(loginpage))
        logout.place(x=200, y=420)

        # ----------- ENCRYPT/THIRD PAGE------------
        page3 = Frame(window)

        # ------- ENCRYPT PAGE(Enter Plain Text Box) --------
        type_frame = Frame(page3, width=690, height=700, highlightthickness=0, bg="#1B2430")

        enter_text_label = Label(type_frame, font=("yu gothic ui", 20, "bold"), bg="#1B2430",
                                 fg="white", text="Enter Plain Text Below:")
        enter_text_label.place(x=50, y=10)
        plain_text_box1 = Text(type_frame, width=60, height=23, bg="#1B2430", font=("yu gothic ui", 12, "bold"),
                               fg="white",
                               highlightthickness=0, border=5)
        plain_text_box1.focus()
        plain_text_box1.config(padx=10, pady=10)
        plain_text_box1.place(x=40, y=70)

        # ENCRYPTION FUNCTION
        def encrypt():
            encrypted_text_box1.delete(1.0, END)
            shift = askstring("Key", "Kindly enter your secret key.")
            random.shuffle(alphabet)
            new_alphabet = []
            for a in alphabet:
                new_alphabet.append(a)
            for a in alphabet:
                new_alphabet.append(a)
            new_data = {
                shift: new_alphabet
            }
            text = plain_text_box1.get(1.0, END)
            if len(shift) == 10:
                shift_1 = int(shift[0:5])
                shift_2 = int(shift[5:])
                new_shift1 = shift_1 % 59
                new_shift2 = shift_2 % 59
                try:
                    with open("data.json", "r") as data_file:
                        # Reading old data
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    # Updating old data with new data
                    data.update(new_data)

                    with open("data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)
                cipher_text = ""
                text_length = len(text)
                text1_length = int(text_length / 2)
                text1 = text[0:text1_length]
                text2 = text[text1_length:]
                for i in text1:
                    if i in new_alphabet:
                        position1 = new_alphabet.index(i)
                        new_position1 = position1 - new_shift1
                        cipher_text += new_alphabet[new_position1]
                    else:
                        cipher_text += i

                for j in text2:
                    if j in new_alphabet:
                        position2 = new_alphabet.index(j)
                        new_position2 = position2 + new_shift2
                        cipher_text += new_alphabet[new_position2]
                    else:
                        cipher_text += j

                encrypted_text_box1.insert(1.0, cipher_text)
            else:
                messagebox.showerror("Key error", "Error: Your encryption key must be a 10 digit key.")

        # -------- Encrypt Now Button --------
        encrypt_now_button = customtkinter.CTkButton(master=type_frame, text="Encrypt Now!", corner_radius=20,
                                                     height=40, fg_color="white", border_width=2, text_color="#1B2430",
                                                     width=300, text_font=("yu gothic ui", 12, "bold"), cursor="hand2", command=encrypt)
        encrypt_now_button.place(x=190, y=630)
        type_frame.place(x=0, y=0)

        # ------- ENCRYPT PAGE(Encrypted Text Box Picture) --------
        text_img = Image.open("textbox1.png")
        photo = ImageTk.PhotoImage(text_img.resize((600, 570), Image.LANCZOS))
        textbox_canvas = Canvas(page3, width=700, height=768, highlightthickness=0, bg="white")
        textbox_canvas.create_image(320, 330, image=photo)
        textbox_canvas.image = photo
        encrypted_text_label = Label(textbox_canvas, font=("yu gothic ui", 20, "bold"), fg="#1B2430",
                                     bg="white", text="Encrypted Text:")
        encrypted_text_label.place(x=75, y=10)
        textbox_canvas.place(x=650, y=0)

        # ------- ENCRYPT PAGE(Encrypted Text Actual Box) --------
        encrypted_text_box1 = Text(textbox_canvas, width=50, height=18, bg="white", font=("yu gothic ui", 12, "bold"),
                                   fg="#1B2430",
                                   highlightthickness=0, border=0)
        encrypted_text_box1.focus()
        encrypted_text_box1.config(padx=10, pady=10)
        encrypted_text_box1.place(x=100, y=120)

        # OPEN PDF FUNCTION
        import PyPDF2

        def open_pdf():

            my_file = filedialog.askopenfilename(title="Open file",
                                                 filetypes=(("PDF Files", ".pdf"), ("Allfiles", "*.*")))
            my_entry = askstring("Page number", "Please enter the page number you want to open")
            try:
                pdf_file = PyPDF2.PdfReader(my_file)
                number_of_pages = len(pdf_file.pages)
                page1 = pdf_file.pages[int(my_entry)]
                content = page1.extract_text()
                plain_text_box1.delete(1.0, END)
                plain_text_box1.insert(1.0, content)

            except Exception as e:
                messagebox.showerror("Whoa!", f"There was a problem! {e}")

        # ------- PDF Button --------
        pdf_button = customtkinter.CTkButton(master=type_frame, text="Open PDF", corner_radius=20,
                                               height=40, fg_color="#fff", border_width=2, text_color="#1B2430",
                                               width=100, text_font=("yu gothic ui", 12, "bold"),
                                               cursor="hand2", command=open_pdf)
        pdf_button.place(x=450, y=20)

        # EMAIL FUNCTION

        def send_email():
            msg = encrypted_text_box1.get(1.0, END)
            user_email = askstring("Email", "Please enter the email you want to send it to")
            MY_EMAIL = "enter your email"
            MY_PASSWORD = "enter your password"
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    connection.login(MY_EMAIL, MY_PASSWORD)
                    message = f"""Subject: My Encrypted Message\n\n {msg}"""
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=user_email,
                        msg=message
                    )
                    connection.close()
            except Exception as b:
                messagebox.showerror("Whoa!", f"There was a problem! {b}")
                print(b)

        # ------- Email Button --------
        email_button = customtkinter.CTkButton(master=textbox_canvas, text="Send Email", corner_radius=20,
                                               height=40, fg_color="#1B2430", border_width=2, text_color="#fff",
                                               width=100, text_font=("yu gothic ui", 12, "bold"),
                                               hover_color="#1B2430", cursor="hand2", command=send_email)
        email_button.place(x=450, y=20)

        # ------- ENCRYPT PAGE(Logout Button) --------

        encrypt_logout_button = customtkinter.CTkButton(master=textbox_canvas, text="Logout", corner_radius=20,
                                                        height=40, fg_color="#1B2430", border_width=2,
                                                        text_color="white",
                                                        width=300, text_font=("yu gothic ui", 12, "bold"), cursor="hand2",
                                                        command=lambda: show_frame(loginpage))
        encrypt_logout_button.place(x=190, y=630)

        # ----------- DECRYPT/FOURTH PAGE --------
        page4 = Frame(window)

        # ------- Decrypted Text Box --------
        type_frame2 = Frame(page4, width=690, height=700, highlightthickness=0, bg="#1B2430")

        enter_text_label2 = Label(type_frame2, font=("yu gothic ui", 20, "bold"), bg="#1B2430",
                                  fg="white", text="Decoded Text:")
        enter_text_label2.place(x=50, y=10)
        plain_text_box2 = Text(type_frame2, width=60, height=24, bg="#1B2430", font=("yu gothic ui", 12, "bold"),
                               fg="white",
                               highlightthickness=0, border=5)
        plain_text_box2.focus()
        plain_text_box2.config(padx=10, pady=10)
        plain_text_box2.place(x=60, y=70)
        type_frame2.place(x=620, y=0)

        # ------- DECRYPT PAGE(Logout Button) --------
        logout_button3 = customtkinter.CTkButton(master=type_frame2, text="Logout", corner_radius=20,
                                                 height=40, fg_color="white", border_width=2, text_color="#1B2430",
                                                 width=300, text_font=("yu gothic ui", 12, "bold"), cursor="hand2",
                                                 command=lambda: show_frame(loginpage))
        logout_button3.place(x=190, y=630)

        # ------- DECRYPT PAGE(Encrypted Text Box Picture) --------
        text_img = Image.open("textbox1.png")
        photo = ImageTk.PhotoImage(text_img.resize((600, 570), Image.LANCZOS))
        textbox_canvas2 = Canvas(page4, width=650, height=768, highlightthickness=0, bg="white")
        textbox_canvas2.create_image(320, 330, image=photo)
        textbox_canvas2.image = photo
        encrypted_text_label2 = Label(textbox_canvas2, font=("yu gothic ui", 20, "bold"), fg="#1B2430",
                                      bg="white", text="Enter Encrypted Text Below:")
        encrypted_text_label2.place(x=75, y=10)

        # ------- DECRYPT PAGE(Encrypted Text Actual Box) --------
        encrypted_text_box2 = Text(textbox_canvas2, width=50, height=18, bg="white", font=("yu gothic ui", 12, "bold"),
                                   fg="#1B2430",
                                   highlightthickness=0, border=0)
        encrypted_text_box2.focus()
        encrypted_text_box2.config(padx=10, pady=10)
        encrypted_text_box2.place(x=100, y=120)

        def decode():
            plain_text_box2.delete(1.0, END)
            shift = askstring("Key", "Kindly enter your secret key.")

            text = encrypted_text_box2.get(1.0, END)
            try:
                with open("data.json") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                print("no data file")
            else:
                if shift in data:
                    shift_1 = int(shift[0:5])
                    shift_2 = int(shift[5:])
                    new_shift1 = shift_1 % 59
                    new_shift2 = shift_2 % 59
                    new_alphabet = data[shift]
                    plain_text = ""
                    text_length = len(text)
                    text1_length = text_length // 2
                    text1 = text[0:text1_length]
                    text2 = text[text1_length:]
                    for k in text1:
                        if k in new_alphabet:
                            position1 = new_alphabet.index(k)
                            new_position1 = position1 + new_shift1
                            plain_text += new_alphabet[new_position1]
                        else:
                            plain_text += k
                    for m in text2:
                        if m in new_alphabet:
                            position2 = new_alphabet.index(m)
                            new_position2 = position2 - new_shift2
                            plain_text += new_alphabet[new_position2]
                        else:
                            plain_text += m

                    plain_text_box2.insert(1.0, plain_text)

                    try:
                        with open("data.json") as data_file:
                            data = json.load(data_file)
                    except FileNotFoundError:
                        print("no data file")
                    else:
                        del data[shift]  # or iterate through entries to find matching name
                        with open("data.json", "w") as data_file:
                            json.dump(data, data_file)
                else:
                    print("no key")
                    messagebox.showerror("Key error", "Error: The key you entered is wrong")

        # -------- Decrypt Now Button -------
        decrypt_button = customtkinter.CTkButton(master=textbox_canvas2, text="Decrypt Now!", corner_radius=20,
                                                        height=40, fg_color="#1B2430", border_width=2,
                                                        text_color="white",
                                                        width=300, text_font=("yu gothic ui", 12, "bold"), cursor="hand2", command=decode)
        decrypt_button.place(x=190, y=630)
        textbox_canvas2.place(x=0, y=0)

        # --------- Looping All The Pages Together ------
        for frame in (loginpage, createaccountpage, adminpage, adminpage2, page2, page3, page4):
            frame.grid(row=0, column=0, sticky="nsew")

        # -------- Showing Each Frame --------
        def show_frame(frames):
            window.after(500, frames.tkraise())

        # --------- Dummy Login Authentication -----
        # def login():
        #     r = True
        #     if r:
        #         return True

        show_frame(loginpage)

# --------- Creating The Frame ----------


def page():
    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    window = customtkinter.CTk()
    LinkPage(window)
    window.mainloop()


if __name__ == "__main__":
    page()

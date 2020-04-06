from tkinter import *
import tkinter as tk
from selenium import webdriver
import time
from datetime import date
from Data_refactor import encoder
from Data_refactor import decoder

window = tk.Tk()
window.iconbitmap("icon/Sociamatic.ico")
log_pass_code = StringVar()


class ButtonActions:

    def __init__(self):
        pass

    def login(self):

        window.title("Sociamatic Login")
        window.geometry('700x300')
        window.configure(background="#1C1C1C")
        window.resizable(0, 0)
        # window.overrideredirect(0)

        w = Label(window, text="Enter Passcode", cursor="dotbox", font=('Calibri', 12, "normal"), fg="White", bg="#1C1C1C")
        w.place(x=250, y=90)

        passEntered = Entry(window, width=20, cursor="dotbox", highlightthickness=0,
                            fg="white", relief="flat", bg="#505050", font=('Calibri', 12, "normal"), show="**", textvariable=log_pass_code)
        passEntered.place(x=250, y=120)
        passEntered.delete(first=0, last=22)  # For emptying the entry space

        log_label = Label(window, text=" Press Enter to  داخل", relief=FLAT, width=20,
                          font=('Calibri', 12, "bold"), background="#FF9500", cursor="dotbox", foreground="white")
        log_label.place(x=250, y=160)
        window.bind('<Return>', self.checker)
        window.mainloop()

    def checker(self, call):
        if self.pass_Check() == 1:
            window.destroy()
            self.mainPage()

        else:
            self.login()

    def pass_Check(self):
        code = log_pass_code.get()
        if code != "" and code == "4811":
            return 1
        else:
            return 0

    def mainPage(self):
        top = tk.Tk()
        top.title("Sociamatic v1.0 (beta)")
        top.iconbitmap("icon/Sociamatic.ico")
        top.geometry('800x400')
        top.resizable(0, 0)
        today = date.today()
        today = today.strftime("%d-%b-%Y")

        top.configure(background="black")

        heading = tk.Label(top, text=f"{today}", foreground="#737373", background="black",
                           font=('Calibri', 12, "bold"))
        heading.place(x=700, y=15)

        heading = tk.Label(top, text="Welcome To Sociamatic v1.0", foreground="White", cursor="dotbox", background="black",
                           font=('Calibri', 26, "bold"))
        heading.place(x=240, y=10)
        heading = tk.Label(top, text="By MUHAMMAD TALHA TARIQ", foreground="White", cursor="dotbox", background="black",
                           font=('Calibri', 12, "normal"))
        heading.place(x=300, y=55)

        fontsize = 12

        socialbtn = Button(top, text="Edit Credentials !", relief=FLAT,
                           font=('Calibri', fontsize, "bold"), background="#9A001F", cursor="dotbox", foreground="white",
                           command=self.credential)
        socialbtn.place(x=20, y=18)

        socialbtn = Button(top, text="Facebook Login", relief=FLAT, padx=10, pady=0.5,
                           font=('Calibri', fontsize, "bold"), background="#1778F2", cursor="dotbox", foreground="white",
                           command=self.faceBook)
        socialbtn.place(x=320, y=160)

        socialbtn = Button(top, text="Instagram Login", relief=FLAT, padx=10, pady=0.5,
                           font=('Calibri', fontsize, "bold"), background="#DD2A7B", cursor="dotbox", foreground="white",
                           command=self.insta)
        socialbtn.place(x=320, y=220)

        socialbtn = Button(top, text="WhatsApp Web", relief=FLAT, padx=10, pady=0.5,
                           font=('Calibri', fontsize, "bold"), background="#4FCE5D", cursor="dotbox", foreground="white",
                           command=self.whatsApp)
        socialbtn.place(x=320, y=280)
        top.mainloop()

    def credential(self):
        cred_window = tk.Tk()
        cred_window.title("Credentials")
        cred_window.iconbitmap("icon/Sociamatic.ico")
        cred_window.geometry('800x500')
        cred_window.resizable(0, 0)
        cred_window.configure(background="black")

        heading = tk.Label(cred_window, text="Credential Editor", foreground="White", cursor="dotbox", background="black",
                           font=('Calibri', 26, "bold"))
        heading.place(x=240, y=10)

        w = Label(cred_window, text="Enter Facebook Email", font=('Calibri', 12, "normal"), foreground="White", background="black")
        w.place(x=200, y=100)
        faceMail_entry = Entry(cred_window, width=40, cursor="dotbox", highlightthickness=0, font=('Calibri', 14),
                               fg="white", relief="flat", bg="#505050")
        faceMail_entry.place(x=200, y=130)

        w = Label(cred_window, text="Enter Facebook Password", font=('Calibri', 12, "normal"), foreground="White", background="black")
        w.place(x=200, y=170)
        facePass_entry = Entry(cred_window, width=40, cursor="dotbox", highlightthickness=0, font=('Calibri', 14),
                               fg="white", relief="flat", bg="#505050", show="**")
        facePass_entry.place(x=200, y=200)

        w = Label(cred_window, text="Enter Instagram Id", font=('Calibri', 12, "normal"), foreground="White", background="black")
        w.place(x=200, y=240)
        instaId_entry = Entry(cred_window, width=40, cursor="dotbox", highlightthickness=0, font=('Calibri', 14),
                              fg="white", relief="flat", bg="#505050")
        instaId_entry.place(x=200, y=270)

        w = Label(cred_window, text="Enter Instagram Password", font=('Calibri', 12, "normal"), foreground="White", background="black")
        w.place(x=200, y=310)
        instaPass_entry = Entry(cred_window, width=40, cursor="dotbox", highlightthickness=0, font=('Calibri', 14),
                                fg="white", relief="flat", bg="#505050", show="**")
        instaPass_entry.place(x=200, y=340)

        def closer():
            cred_window.destroy()

        def clearer():
            faceMail_entry.delete(first=0, last=100)
            facePass_entry.delete(first=0, last=100)
            instaId_entry.delete(first=0, last=100)
            instaPass_entry.delete(first=0, last=100)

        def storing():

            if len(faceMail_entry.get()) != 0:
                file1 = open("text/data1.txt", "w")
                passage_1 = encoder(faceMail_entry.get())
                file1.writelines(passage_1)
                file1.close()

            if len(facePass_entry.get()) != 0:
                file2 = open("text/data2.txt", "w")
                passage_2 = encoder(facePass_entry.get())
                file2.writelines(passage_2)
                file2.close()

            if len(instaId_entry.get()) != 0:
                file3 = open("text/data3.txt", "w")
                passage_3 = encoder(instaId_entry.get())
                file3.writelines(passage_3)
                file3.close()

            if len(instaPass_entry.get()) != 0:
                file4 = open("text/data4.txt", "w")
                passage_4 = encoder(instaPass_entry.get())
                file4.writelines(passage_4)
                file4.close()
            cred_window.destroy()
        btnHeight = 380
        close = Button(cred_window, text="Close", relief=FLAT, width="10",
                       font=('Calibri', 12, "bold"), background="#fe4747", foreground="white", cursor="dotbox", command=lambda: closer())
        close.place(x=200, y=btnHeight)

        clear = Button(cred_window, text="Clear", relief=FLAT, width="10",
                       font=('Calibri', 12, "bold"), background="#47bffe", foreground="white", cursor="dotbox", command=lambda: clearer())
        clear.place(x=350, y=btnHeight)

        store = Button(cred_window, text="Save", relief=FLAT, width="10",
                       font=('Calibri', 12, "bold"), background="#47fe83", foreground="white", cursor="dotbox", command=lambda: storing())
        store.place(x=495, y=btnHeight)

    def faceBook(self):
        read_data1 = open("text/data1.txt", "r")
        read_data2 = open("text/data2.txt", "r")

        email = decoder(read_data1.readline())          # decoding data-1(email)
        fbpass = decoder(read_data2.readline())         # decoding data-2(password)

        driver = webdriver.Chrome('ChromeAutomationDriver/chromedriver')  # path of chrome driver .exe file
        driver.get("https://www.facebook.com/")
        time.sleep(5)
        mailbox = driver.find_element_by_id('email')
        mailbox.send_keys(f"{email}")

        fbpassbox = driver.find_element_by_id('pass')
        fbpassbox.send_keys(f"{fbpass}")
        time.sleep(3)
        fbloginbtn = driver.find_element_by_id('loginbutton')
        fbloginbtn.click()  # login btn Click

    def insta(self):

        read_data3 = open("text/data3.txt", "r")
        read_data4 = open("text/data4.txt", "r")

        instaUser = decoder(read_data3.readline())  # decoding data-3(email)
        instapass = decoder(read_data4.readline())  # decoding data-4(password)

        driver = webdriver.Chrome('ChromeAutomationDriver/chromedriver')  # path of chrome driver .exe file
        driver.get("https://www.instagram.com/?hl=en")
        time.sleep(5)
        userbox = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        userbox.send_keys(f"{instaUser}")  # Username Entry

        passbox = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        passbox.send_keys(f"{instapass}")  # Password Entry

        instaloginbtn = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
        instaloginbtn.click()  # login btn Click

    def whatsApp(self):
        driver = webdriver.Chrome('ChromeAutomationDriver/chromedriver')  # path of chrome driver .exe file
        driver.get("https://web.whatsapp.com/")


btn = ButtonActions()

btn.login()

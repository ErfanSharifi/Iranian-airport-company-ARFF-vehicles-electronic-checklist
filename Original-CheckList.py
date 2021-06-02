from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import jdatetime
import sqlite3
import string
import Form_Tamirat as sa
import Admin as ad
import ClientUI as cl
import Logbook as lb


class exam():

    def __init__(self, root):

        self.root = root

        self.btn_client = Button(root, text="چک لیست",
                                 width=10, height=2, command=self.Client)
        self.btn_client.grid(row=0, column=0, padx=20, pady=20)

        self.btn_admin = Button(root, text="مسِئول",
                                width=10, height=2, command=self.Admin)
        self.btn_admin.grid(row=0, column=1, padx=20, pady=20)

        self.btn_client = Button(
            root, text="فرم‌ تعمیرات خودرو", width=15, height=2, command=self.Tamir)
        self.btn_client.grid(row=1, column=0, padx=20, pady=20)

        self.btn_client = Button(
            root, text="لاگ‌‌بوک", width=10, height=2, command=self.Ledger)
        self.btn_client.grid(row=1, column=1, padx=20, pady=20)

        self.btn_client = Button(
            root, text="خروج", width=20, height=2, command=self.Exit)
        self.btn_client.grid(row=2, columnspan=2, padx=10)

    def Admin(self):

        obj = ad.AdminUI()
        obj.Masool(self.root)

    def Client(self):

        obj = cl.ClientUI()
        obj.Client(self.root)

    def Tamir(self):

        obj = sa.Tamirat()
        obj.test(self.root)

    def Ledger(self):

        obj = lb.Log()
        obj.Book(self.root)

    def Exit(self):

        self.root.destroy()


def main():

    root = Tk()
    root.overrideredirect(1)
    # root.title('                      شرکت فرودگاهها و ناوبری هوایی')
    # root.attributes('-fullscreen', True)
    root.geometry("400x350+550+200")

    imge = Image.open('C:\\Users\\ErfanSharifi\\OneDrive\\Documents\\Projects\\Check-List-Test\\Codes\\sd.jpg')
    photo = ImageTk.PhotoImage(imge)

    lab = Label(image=photo)
    lab.pack()

    root.after(1000, root.destroy)

    root.mainloop()

    root = Tk()
    root.geometry("290x210+550+200")
    root.title("                       وقت بخیر")
    root.resizable(0, 0)
    obj = exam(root)
    root.mainloop()

main()
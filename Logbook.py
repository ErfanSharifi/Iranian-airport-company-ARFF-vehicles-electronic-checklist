from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import jdatetime
import sqlite3
import string
import Keyboard as kb

class Log:


    def __init__(self):

        pass


    def Keb(self):

        obj = kb.Keyb()
        obj.Key(self.root)


    def lal(self, txt):

        # V = self.txt_matn.get("1.0", END)
        # print (V)
        # print (txt)
        # self.txt_matn.insert(END, txt)
        self.txt_Date.get()

    def Book(self, root):

        self.root =root
        top = Toplevel(self.root)
        top.geometry("820x800+300+20")
        top.resizable(0,0)


        frn1 =LabelFrame(top, text = "لاگ‌بوک" ,width=820, height=800, relief=GROOVE, bd =4)
        frn1.grid_propagate(False)
        frn1.grid(row = 0, columnspan = 2,sticky=NSEW,padx =1, pady =1)


        self.lbl_Day = Label(frn1, text = "روز:")
        self.lbl_Day.grid(row = 0, column = 0,padx = 30, pady= 10)
        self.Day = StringVar()
        self.cmb_Day= ttk.Combobox(frn1, textvariable= self.Day, values=("شنبه","یکشنبه","دوشنبه","سه‌شنبه","چهارشنبه","پنجشنبه","جمعه"))
        self.cmb_Day.grid(row = 0, column = 1, padx = 30)


        self.btn_Date =Button(frn1, text ="تاریخ", width =20, height =2)
        self.btn_Date.grid(row = 0, column= 2,padx = 30, pady= 10)
        self.txt_Date =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_Date.grid(row =0, column = 3, padx = 30)


        self.lbl_Car = Label(frn1, text = "انتخاب خودرو:")
        self.lbl_Car.grid(row = 1, column = 0, padx = 30, pady= 10)
        self.Car = StringVar()
        self.cmb_Car = ttk.Combobox(frn1, textvariable= self.Car, values=("برف‌روب","تانکر","آذر-4","آذر-3","آذر-2","آذر1"))
        self.cmb_Car.grid(row = 1, column = 1, padx =30)      


        self.lbl_firstdriver = Label(frn1, text = "نفر اول:")
        self.lbl_firstdriver.grid(row = 2, column = 0,padx = 30, pady= 10)
        self.firstdriver = StringVar()
        self.cmb_firstdriver = ttk.Combobox(frn1, textvariable= self.firstdriver, values=("مجتبی‌خان‌احمدلو","بهلول‌حبیبی","مجید‌قاسمی","جلال‌سلطانی","امیر‌هدایتی","عرفان‌شریفی","بهزاد‌سعیدی","رسول‌قاسمی","وحید‌علیزاده","مسعود‌خان‌احمدلو"))
        self.cmb_firstdriver.grid(row = 3, column = 0, padx = 30) 


        self.lbl_seconddriver = Label(frn1, text = "نفر دوم:")
        self.lbl_seconddriver.grid(row = 2, column = 1,padx = 30, pady= 10)
        self.seconddriver = StringVar()
        self.cmb_seconddriver = ttk.Combobox(frn1, textvariable= self.seconddriver, values=("مجتبی‌خان‌احمدلو","بهلول‌حبیبی","مجید‌قاسمی","جلال‌سلطانی","امیر‌هدایتی","عرفان‌شریفی","بهزاد‌سعیدی","رسول‌قاسمی","وحید‌علیزاده","مسعود‌خان‌احمدلو"))
        self.cmb_seconddriver.grid(row = 3, column = 1, padx = 30, pady = 10) 


        self.lbl_thirddriver = Label(frn1, text = "نفر سوم:")
        self.lbl_thirddriver.grid(row = 2, column = 2,padx = 30, pady= 10)
        self.thirddriver = StringVar()
        self.cmb_thirddriver = ttk.Combobox(frn1, textvariable= self.thirddriver, values=("مجتبی‌خان‌احمدلو","بهلول‌حبیبی","مجید‌قاسمی","جلال‌سلطانی","امیر‌هدایتی","عرفان‌شریفی","بهزاد‌سعیدی","رسول‌قاسمی","وحید‌علیزاده","مسعود‌خان‌احمدلو"))
        self.cmb_thirddriver.grid(row = 3, column = 2, padx = 30) 


        self.lbl_marshaler = Label(frn1, text = "مارشالر:")
        self.lbl_marshaler.grid(row = 2, column = 3,padx = 30, pady= 10)
        self.marshaler = StringVar()
        self.cmb_marshaler = ttk.Combobox(frn1, textvariable= self.marshaler, values=("مجتبی‌خان‌احمدلو","بهلول‌حبیبی","مجید‌قاسمی","جلال‌سلطانی","امیر‌هدایتی","عرفان‌شریفی","بهزاد‌سعیدی","رسول‌قاسمی","وحید‌علیزاده","مسعود‌خان‌احمدلو"))
        self.cmb_marshaler.grid(row = 3, column = 3, padx = 30)


        self.lbl_mojtaba = Label(frn1, text = "مجتبی خان‌احمدلو:")
        self.lbl_mojtaba.grid(row = 4, column = 0,padx = 30, pady= 10)
        self.txt_mojtaba =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_mojtaba.grid(row =4, column =1 , padx = 30, pady = 10)
        self.mojtaba = StringVar()
        self.rdb_mojtaba =Radiobutton (frn1, text = "مرخصی", variable = self.mojtaba, value = "مرخصی")
        self.rdb_mojtaba.grid(row = 4, column = 2, padx = 30,pady =10)
        self.rdb_mojtaba =Radiobutton(frn1, text = "Off", variable = self.mojtaba, value = "Off")
        self.rdb_mojtaba.grid(row =4 , column = 3, padx =30, pady =10)


        self.lbl_bohlool = Label(frn1, text = "بهلول حبیبی:")
        self.lbl_bohlool.grid(row =5 , column = 0,padx = 30, pady= 10)
        self.txt_bohlool =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_bohlool.grid(row =5, column =1 , padx = 30, pady = 10)
        self.bohlool = StringVar()
        self.rdb_bohlool =Radiobutton (frn1, text = "مرخصی", variable = self.bohlool, value = "مرخصی")
        self.rdb_bohlool.grid(row = 5, column = 2, padx = 30,pady =10)
        self.rdb_bohlool =Radiobutton(frn1, text = "Off", variable = self.bohlool, value = "Off")
        self.rdb_bohlool.grid(row = 5, column = 3, padx =30, pady =10)


        self.lbl_jalal = Label(frn1, text = "جلال سلطانی:")
        self.lbl_jalal.grid(row = 6, column = 0 ,padx = 30, pady= 10)
        self.txt_jalal =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_jalal.grid(row = 6, column = 1, padx = 30, pady = 10)
        self.jalal = StringVar()
        self.rdb_jalal =Radiobutton (frn1, text = "مرخصی", variable = self.jalal, value = "مرخصی")
        self.rdb_jalal.grid(row = 6, column = 2, padx = 30,pady =10)
        self.rdb_jalal =Radiobutton(frn1, text = "Off", variable = self.jalal, value = "Off")
        self.rdb_jalal.grid(row =6 , column = 3, padx =30, pady =10)


        self.lbl_majid = Label(frn1, text = "مجید قاسمی:")
        self.lbl_majid.grid(row =7 , column =0 ,padx = 30, pady= 10)
        self.txt_majid =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_majid.grid(row =7, column =1 , padx = 30, pady = 10)
        self.majid = StringVar()
        self.rdb_majid =Radiobutton (frn1, text = "مرخصی", variable = self.majid, value = "مرخصی")
        self.rdb_majid.grid(row = 7, column = 2, padx = 30,pady =10)
        self.rdb_majid =Radiobutton(frn1, text = "Off", variable = self.majid, value = "Off")
        self.rdb_majid.grid(row = 7, column = 3, padx =30, pady =10)


        self.lbl_masood = Label(frn1, text = "مسعود خان‌احمدلو:")
        self.lbl_masood.grid(row = 8, column =0 ,padx = 30, pady= 10)
        self.txt_masood =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_masood.grid(row =8, column =1, padx = 30, pady = 10)
        self.masood = StringVar()
        self.rdb_masood =Radiobutton (frn1, text = "مرخصی", variable = self.masood, value = "مرخصی")
        self.rdb_masood.grid(row = 8, column = 2, padx = 30,pady =10)
        self.rdb_masood =Radiobutton(frn1, text = "Off", variable = self.masood, value = "Off")
        self.rdb_masood.grid(row =8 , column = 3, padx =30, pady =10)


        self.lbl_amir = Label(frn1, text = "امیر هدایتی:")
        self.lbl_amir.grid(row = 9, column = 0,padx = 30, pady= 10)
        self.txt_amir =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_amir.grid(row =9, column = 1, padx = 30, pady = 10)
        self.amir = StringVar()
        self.rdb_amir =Radiobutton (frn1, text = "مرخصی", variable = self.amir, value = "مرخصی")
        self.rdb_amir.grid(row = 9, column = 2, padx = 30,pady =10)
        self.rdb_amir =Radiobutton(frn1, text = "Off", variable = self.amir, value = "Off")
        self.rdb_amir.grid(row = 9, column = 3, padx =30, pady =10)


        self.lbl_behzad = Label(frn1, text = "بهزاد سعیدی:")
        self.lbl_behzad.grid(row = 10, column = 0,padx = 30, pady= 10)
        self.txt_behzad =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_behzad.grid(row =10, column = 1, padx = 30, pady = 10)
        self.behzad = StringVar()
        self.rdb_behzad =Radiobutton (frn1, text = "مرخصی", variable = self.behzad, value = "مرخصی")
        self.rdb_behzad.grid(row = 10, column = 2, padx = 30,pady =10)
        self.rdb_behzad =Radiobutton(frn1, text = "Off", variable = self.behzad, value = "Off")
        self.rdb_behzad.grid(row = 10, column = 3, padx =30, pady =10)


        self.lbl_vahid = Label(frn1, text = "وحید علیزاده:")
        self.lbl_vahid.grid(row = 11, column = 0,padx = 30, pady= 10)
        self.txt_vahid =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_vahid.grid(row = 11, column = 1, padx = 30, pady = 10)
        self.vahid = StringVar()
        self.rdb_vahid =Radiobutton (frn1, text = "مرخصی", variable = self.vahid, value = "مرخصی")
        self.rdb_vahid.grid(row = 11, column = 2, padx = 30,pady =10)
        self.rdb_vahid =Radiobutton(frn1, text = "Off", variable = self.vahid, value = "Off")
        self.rdb_vahid.grid(row = 11, column = 3, padx =30, pady =10)


        self.lbl_rasool = Label(frn1, text = "رسول قاسمی:")
        self.lbl_rasool.grid(row = 12, column = 0,padx = 30, pady= 10)
        self.txt_rasool =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_rasool.grid(row =12, column = 1, padx = 30, pady = 10)
        self.rasool = StringVar()
        self.rdb_rasool =Radiobutton (frn1, text = "مرخصی", variable = self.rasool, value = "مرخصی")
        self.rdb_rasool.grid(row = 12, column = 2, padx = 30,pady =10)
        self.rdb_rasool =Radiobutton(frn1, text = "Off", variable = self.rasool, value = "Off")
        self.rdb_rasool.grid(row = 12, column = 3, padx =30, pady =10)


        self.lbl_erfan = Label(frn1, text = "عرفان شریفی:")
        self.lbl_erfan.grid(row = 13, column = 0,padx = 30, pady= 10)
        self.txt_erfan =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_erfan.grid(row =13, column = 1, padx = 30, pady = 10)
        self.erfan = StringVar()
        self.rdb_erfan =Radiobutton (frn1, text = "مرخصی", variable = self.erfan, value = "مرخصی")
        self.rdb_erfan.grid(row = 13, column = 2, padx = 30,pady =10)
        self.rdb_erfan =Radiobutton(frn1, text = "Off", variable = self.erfan, value = "Off")
        self.rdb_erfan.grid(row =13 , column = 3, padx =30, pady =10)


        self.lbl_baiat = Label(frn1, text = "محمد حسین بیات:")
        self.lbl_baiat.grid(row = 14, column = 0,padx = 30, pady= 10)
        self.txt_baiat =Text(frn1, width =15, height =1, relief=SOLID,bd=1)
        self.txt_baiat.grid(row =14, column = 1, padx = 30, pady = 10)
        self.baiat = StringVar()
        self.rdb_baiat =Radiobutton (frn1, text = "مرخصی", variable = self.baiat, value = "مرخصی")
        self.rdb_baiat.grid(row = 14, column = 2, padx = 30,pady =10)
        self.rdb_baiat =Radiobutton(frn1, text = "Off", variable = self.baiat, value = "Off")
        self.rdb_baiat.grid(row = 14, column = 3, padx =30, pady =10)


        self.txt_matn =Text(frn1, width =50, height =5, relief=SOLID, bd=1)
        self.txt_matn.grid(row =15, columnspan = 2, padx = 10)
        V = self.txt_matn.get("1.0", END)
        print (V)


        self.btn_keyboard =Button(frn1, text ="کیبورد", width =10, height =2, command = self.Keb)
        self.btn_keyboard.grid(row = 15, column= 3)
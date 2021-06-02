from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import jdatetime
import sqlite3
import string



class Tamirat:

    def __init__(self):

        pass

    def test(self, root):

        self.root = root

        
        top = Toplevel(self.root)
        top.geometry("800x490+300+100")
        top.title("                                                                                                         موارد بازدید و تعویض")
        top.resizable(0,0)

        frn1 =LabelFrame(top, text = "موارد بازدید و تعویض" ,width=800, height=490, relief=GROOVE, bd =4)
        frn1.grid_propagate(False)
        frn1.grid(row = 0, columnspan = 2,sticky=NSEW,padx =1, pady =1)



        self.lbl_Car = Label(frn1, text = "انتخاب خودرو:")
        self.lbl_Car.grid(row = 0, column = 0, padx = 30, pady= 10, sticky = W)
        self.Car = StringVar()
        self.cmb_Car = ttk.Combobox(frn1, textvariable= self.Car, values=("برف‌روب","تانکر","آذر-4","آذر-3","آذر-2","آذر1"))
        self.cmb_Car.grid(row = 0, column = 1)


        self.btn_Date =Button(frn1, text ="تاریخ", width =20, height =2)
        self.btn_Date.grid(row = 0, column= 2,padx = 30)
        self.txt_Date =Text(frn1, width =20, height =1, relief=SOLID,bd=1)
        self.txt_Date.grid(row =0, column = 3, columnspan =4, padx =30, pady =50)


        self.lbl_oilmotor = Label(frn1, text = "روغن موتور:")
        self.lbl_oilmotor.grid(row = 1, column = 0, padx= 30, pady = 10, sticky = W)
        self.oilmotor = StringVar()
        self.cmb_oilmotor = ttk.Combobox(frn1, textvariable= self.oilmotor , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_oilmotor.grid(row =1 , column =1 ,padx = 30)


        self.lbl_oilfilter = Label(frn1, text = " فیلتر روغن:")
        self.lbl_oilfilter.grid(row =2 , column = 0, padx= 30, pady = 10, sticky = W)
        self.oilfilter = StringVar()
        self.cmb_oilfilter = ttk.Combobox(frn1, textvariable=self.oilfilter  , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_oilfilter.grid(row = 2, column =1 ,padx = 30)


        self.lbl_filtergasoil = Label(frn1, text = "فیلتر گازوییل:")
        self.lbl_filtergasoil.grid(row =3 , column =0 , padx= 30, pady = 10, sticky = W)
        self.filtergasoil = StringVar()
        self.cmb_filtergasoil = ttk.Combobox(frn1, textvariable=self.filtergasoil  , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_filtergasoil.grid(row =3 , column =1 ,padx = 30)


        self.lbl_havafilter = Label(frn1, text = "فیلتر هوا:")
        self.lbl_havafilter.grid(row =4 , column = 0, padx= 30, pady = 10, sticky = W)
        self.havafilter = StringVar()
        self.cmb_havafilter = ttk.Combobox(frn1, textvariable=self.havafilter  , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_havafilter.grid(row =4 , column =1 ,padx = 30)


        self.lbl_gearvasgasin = Label(frn1, text = "واسگازین گیربکس:")
        self.lbl_gearvasgasin.grid(row = 5, column = 0, padx= 30, pady = 10, sticky = W)
        self.gearvasgasin = StringVar()
        self.cmb_gearvasgasin = ttk.Combobox(frn1, textvariable=self.gearvasgasin  , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_gearvasgasin.grid(row = 5, column = 1,padx = 30)



        self.lbl_difvasgasin = Label(frn1, text = " واسگازین دیفرانسیل:")
        self.lbl_difvasgasin.grid(row =6 , column =0 , padx= 30, pady = 10, sticky = W)
        self.difvasgasin = StringVar()
        self.cmb_difvasgasin = ttk.Combobox(frn1, textvariable=self.difvasgasin  , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_difvasgasin.grid(row =6 , column =1 ,padx = 30)


        self.lbl_roghanfarman = Label(frn1, text = "روغن هیدرولیک فرمان:")
        self.lbl_roghanfarman.grid(row =7 , column = 0, padx= 30, pady = 10, sticky = W)
        self.roghanfarman = StringVar()
        self.cmb_roghanfarman = ttk.Combobox(frn1, textvariable= self.roghanfarman  , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_roghanfarman.grid(row =7 , column =1 ,padx = 30)


        self.lbl_kelachoil = Label(frn1, text = "روغن پمپ کلاچ:")
        self.lbl_kelachoil .grid(row =8 , column = 0, padx= 30, pady = 10, sticky = W)
        self.kelachoil  = StringVar()
        self.cmb_kelachoil  = ttk.Combobox(frn1, textvariable= self.kelachoil  , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_kelachoil .grid(row =8 , column =1 ,padx = 30)


        self.lbl_griskaricar = Label(frn1, text = "گریسکاری زیر خودرو:")
        self.lbl_griskaricar.grid(row =1 , column = 2, padx= 30, pady = 10, sticky = W)
        self.griskaricar = StringVar()
        self.cmb_griskaricar = ttk.Combobox(frn1, textvariable= self.griskaricar  , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_griskaricar.grid(row =1 , column = 3,padx = 30)


        self.lbl_griskariatash = Label(frn1, text = "گریسکاری سیستم آتش‌نشانی:")
        self.lbl_griskariatash.grid(row =2 , column = 2, padx= 30, pady = 10, sticky = W)
        self.griskariatash = StringVar()
        self.cmb_griskariatash = ttk.Combobox(frn1, textvariable= self.griskariatash , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_griskariatash.grid(row = 2, column = 3,padx = 30)


        self.lbl_griskarigardan = Label(frn1, text = "گریسکاری گاردان:")
        self.lbl_griskarigardan.grid(row =3 , column =2 , padx= 30, pady = 10, sticky = W)
        self.griskarigardan = StringVar()
        self.cmb_griskarigardan = ttk.Combobox(frn1, textvariable= self.griskarigardan , values=("بازدید گردید", "تعویض گردید"))
        self.cmb_griskarigardan.grid(row = 3, column = 3,padx = 30)


        self.btn_register =Button(frn1, text ="ثبت", width =50, height =2)
        self.btn_register.grid(row = 8, column= 2, columnspan= 3 ,padx = 30)







from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import jdatetime
import sqlite3
import string
import Form_Tamirat as sa




class ClientUI:

    def __init__(self):

        pass

    def Client(self, root):
 

        
        self.root = root
        root.title("                                                                                                                                                                                                       برنامه چک لیست فرودگاه زنجان")
        
        top = Toplevel(self.root)
        top.geometry("1410x880+55+0")
        top.resizable(0,0)

        #########################################################################################################
        ##################################             Frame Config           ###################################
        #########################################################################################################


        frn1 =LabelFrame(top, text = "راننده" ,width=400, height=80, relief=GROOVE, bd =4)
        frn2 =LabelFrame(top, text = "تجهیزات", width=752, height=360, relief=GROOVE, bd = 4)
        frn3 =LabelFrame(top, text = "کابین راننده", width=650, height=320, relief=GROOVE, bd = 4)
        frn4 =LabelFrame(top, text ="وضعیت بدنه", width=650, height=270, relief=GROOVE, bd = 4)
        frn5 =LabelFrame(top, text = "" ,width=1000, height=100, relief=GROOVE, bd =4) 
         

        frn1.grid_propagate(False)
        frn1.grid(row = 0, columnspan = 2,sticky=NSEW,padx =2, pady =2)


        frn2.grid_propagate(False)
        frn2.grid(row = 1, column = 0,sticky=NSEW,padx =2, pady =2)


        frn3.grid_propagate(False)
        frn3.grid(row = 1, column = 1,sticky=NSEW, padx =2, pady =2)

        
        frn4.grid_propagate(False)
        frn4.grid(row =2 , columnspan = 2,sticky=NSEW,padx =2, pady =2)


        frn5.grid_propagate(False)
        frn5.grid(row = 3, columnspan = 2,sticky=NSEW,padx =2, pady =2)



        #########################################################################################################
        ##################################                  راننده                ###############################
        #########################################################################################################

        self.lbl_Select = Label(frn1, text = "انتخاب راننده::")
        self.lbl_Select.grid(row = 0, column = 0, padx = 10, pady= 10, sticky = W)
        self.Select = StringVar()
        self.cmb_Select = ttk.Combobox(frn1, textvariable= self.Select, values=("مجتبی‌خان‌احمدلو","بهلول‌حبیبی","مجید‌قاسمی","جلال‌سلطانی","امیر‌هدایتی","عرفان‌شریفی","بهزاد‌سعیدی","رسول‌قاسمی","وحید‌علیزاده","مسعود‌خان‌احمدلو"))
        self.cmb_Select.grid(row = 0, column = 1, padx = 30)


        self.lbl_Car = Label(frn1, text = "انتخاب خودرو:")
        self.lbl_Car.grid(row = 0, column = 2, padx = 50, pady= 10, sticky = W)
        self.Car = StringVar()
        self.cmb_Car = ttk.Combobox(frn1, textvariable= self.Car, values=("برف‌روب","تانکر","آذر-4","آذر-3","آذر-2","آذر1"))
        self.cmb_Car.grid(row = 0, column = 3,padx = 10, sticky = E)


        self.btn_Date =Button(frn1, text ="تاریخ", width =20, height =2, command = self.date)
        self.btn_Date.grid(row = 0, column= 4, padx = 100)


        self.txt_Date =Text(frn1, width =10, height =1, relief=SOLID,bd=2)
        self.txt_Date.config(state = DISABLED)
        self.txt_Date.grid(row =0, column = 5, columnspan =4, padx =20)


        #########################################################################################################
        ##################################                  بازدید تجهیزات       ###############################
        #########################################################################################################


        self.lbl_khamooshDasti = Label(frn2, text = "خاموش کننده دستی:")
        self.lbl_khamooshDasti.grid(row = 2, column = 0, padx = 10, pady= 10, sticky = W)
        self.Khamoosh = StringVar()
        self.cmb_Khamoosh = ttk.Combobox(frn2, textvariable= self.Khamoosh, values=("1","2","3","4","5","ندارد"))
        self.cmb_Khamoosh.grid(row = 2, column = 2,columnspan = 4, padx = 400)



        self.lbl_FireClothes = Label(frn2, text = "لباس آتش‌نشانی:")
        self.lbl_FireClothes.grid(row = 3, column = 0, padx = 10, pady= 10, sticky = W)
        self.Clothes = StringVar()
        self.cmb_Clothes = ttk.Combobox(frn2, textvariable= self.Clothes, values=("1","2","3","4","5","ندارد"))
        self.cmb_Clothes.grid(row = 3, column = 2,columnspan = 4, padx = 400)


        self.lbl_Oxygen = Label(frn2, text = "دستگاه تنفسی:")
        self.lbl_Oxygen.grid(row = 4, column = 0, padx = 10, pady= 10, sticky = W)
        self.Oxygen = StringVar()
        self.cmb_Oxygen = ttk.Combobox(frn2, textvariable= self.Oxygen, values=("1","2","3","4","5","ندارد"))
        self.cmb_Oxygen.grid(row = 4, column = 2,columnspan = 4, padx = 400)


        self.lbl_Robe = Label(frn2, text = "طناب نجات:")
        self.lbl_Robe.grid(row = 5, column = 0, padx = 10, pady= 10, sticky = W)
        self.Robe = StringVar()
        self.cmb_Robe = ttk.Combobox(frn2, textvariable= self.Robe, values=("1","2","3","4","5","ندارد"))
        self.cmb_Robe.grid(row = 5, column = 2,columnspan = 4, padx = 400)



        self.lbl_Brankadr = Label(frn2, text = "بارنکادر:")
        self.lbl_Brankadr.grid(row = 6, column = 0, padx = 10, pady= 10, sticky = W)
        self.Brankadr = StringVar()
        self.cmb_Brankadr = ttk.Combobox(frn2, textvariable= self.Brankadr, values=("1","2","3","4","5","ندارد"))
        self.cmb_Brankadr.grid(row = 6, column = 2,columnspan = 4, padx = 400)



        self.lbl_Raw = Label(frn2, text = "آره موتوری:")
        self.lbl_Raw.grid(row = 7, column = 0, padx = 10, pady= 10, sticky = W)
        self.Raw = StringVar()
        self.cmb_Raw = ttk.Combobox(frn2, textvariable= self.Raw, values=("1","2","3","4","5","ندارد"))
        self.cmb_Raw.grid(row = 7, column = 2,columnspan = 4, padx = 400)



        self.lbl_Hidrolic = Label(frn2, text = "ست هیدرولیک:")
        self.lbl_Hidrolic.grid(row = 8, column = 0, padx = 10, pady= 10, sticky = W)
        self.Hidrolic = StringVar()
        self.cmb_Hidrolic = ttk.Combobox(frn2, textvariable= self.Hidrolic, values=("1","2","3","4","5","ندارد"))
        self.cmb_Hidrolic.grid(row = 8, column = 2,columnspan = 4, padx = 400)



        self.lbl_Loole = Label(frn2, text = "لوله آتش‌نشانی:")
        self.lbl_Loole.grid(row = 9, column = 0, padx = 10, pady= 10, sticky = W)
        self.Loole = StringVar()
        self.cmb_Loole = ttk.Combobox(frn2, textvariable= self.Loole, values=("1","2","3","4","5","6","7","8","9","ندارد"))
        self.cmb_Loole.grid(row = 9, column = 2,columnspan = 4, padx = 400)


        #########################################################################################################
        ##################################                   کابین راننده        ###############################
        #########################################################################################################


        self.lbl_Radio = Label(frn3, text = "دستگاه رادیویی:")
        self.lbl_Radio.grid(row = 2, column = 0, padx = 10, pady= 10, sticky = W)
        self.Radio = StringVar()
        self.cmb_Radio = ttk.Combobox(frn3, textvariable= self.Radio, values=("مطلوب", "نامطلوب"))
        self.cmb_Radio.grid(row = 2, column = 1,columnspan = 4, padx = 350)



        self.lbl_Alarm = Label(frn3, text = "آژیر و چراغ گردان:")
        self.lbl_Alarm.grid(row = 3, column = 0, padx = 10, pady= 10, sticky = W)
        self.Alarm = StringVar()
        self.cmb_Alarm = ttk.Combobox(frn3, textvariable= self.Alarm, values=("مطلوب", "نامطلوب"))
        self.cmb_Alarm.grid(row = 3, column = 1,columnspan = 4, padx = 350)



        self.lbl_TableControl = Label(frn3, text = "تابلو کنترل:")
        self.lbl_TableControl.grid(row = 4, column = 0, padx = 10, pady= 10, sticky = W)
        self.Table = StringVar()
        self.cmb_Table = ttk.Combobox(frn3, textvariable= self.Table, values=("مطلوب", "نامطلوب"))
        self.cmb_Table.grid(row =4 , column = 1,columnspan = 4, padx = 350)


        
        self.lbl_Etfa = Label(frn3, text = "سیستم اطفا:")
        self.lbl_Etfa.grid(row = 5, column = 0, padx = 10, pady= 10, sticky = W)
        self.Etfa = StringVar()
        self.cmb_Etfa = ttk.Combobox(frn3, textvariable= self.Etfa, values=("مطلوب", "نامطلوب"))
        self.cmb_Etfa.grid(row = 5, column = 1,columnspan = 4, padx = 350)



        self.lbl_PoshtAmper = Label(frn3, text = "نشانگر پشت آمپر:")
        self.lbl_PoshtAmper.grid(row = 6, column = 0, padx = 10, pady= 10, sticky = W)
        self.Posht = StringVar()
        self.cmb_Posht = ttk.Combobox(frn3, textvariable= self.Posht, values=("مطلوب", "نامطلوب"))
        self.cmb_Posht.grid(row = 6, column = 1,columnspan = 4, padx = 350)



        self.lbl_Snow = Label(frn3, text = "برف پک‌کن:")
        self.lbl_Snow.grid(row = 7, column = 0, padx = 10, pady= 10, sticky = W)
        self.Snow = StringVar()
        self.cmb_Snow = ttk.Combobox(frn3, textvariable= self.Snow, values=("مطلوب", "نامطلوب"))
        self.cmb_Snow.grid(row =7 , column = 1,columnspan = 4, padx = 350)

        

        self.lbl_Abpash = Label(frn3, text = "آب‌پاش شیشه:")
        self.lbl_Abpash.grid(row = 8, column = 0, padx = 10, pady= 10, sticky = W)
        self.Abpash = StringVar()
        self.cmb_Abpash = ttk.Combobox(frn3, textvariable= self.Abpash, values=("مطلوب", "نامطلوب"))
        self.cmb_Abpash.grid(row =8 , column = 1,columnspan = 4, padx = 350)



        self.lbl_Map = Label(frn3, text = "نقشه:")
        self.lbl_Map.grid(row = 9, column = 0, padx = 10, pady= 10, sticky = W)    
        self.Map = StringVar()
        self.cmb_Map = ttk.Combobox(frn3, textvariable= self.Map, values=("دارد", "ندارد"))
        self.cmb_Map.grid(row =9 , column = 1,columnspan = 4, padx = 350)


        #########################################################################################################
        ##################################                  وضعیت بدنه           ###############################
        #########################################################################################################
        

        self.lbl_Kapoot = Label(frn4, text = "کاپوت:")
        self.lbl_Kapoot.grid(row = 2, column = 0, padx = 10, pady= 10, sticky = W)
        self.kapoot = StringVar()
        self.cmb_kapoot= ttk.Combobox(frn4, textvariable= self.kapoot, values=("مطلوب", "نامطلوب"))
        self.cmb_kapoot.grid(row = 2, column = 0, padx = 100)


        self.lbl_DriverDoor = Label(frn4, text = "درب  راننده:")
        self.lbl_DriverDoor.grid(row = 3, column = 0, padx = 10, pady= 10, sticky = W)
        self.driverdoor = StringVar()
        self.cmb_driverdoor = ttk.Combobox(frn4, textvariable= self.driverdoor, values=("مطلوب", "نامطلوب"))
        self.cmb_driverdoor.grid(row =3 , column = 0, padx = 100)


        self.lbl_ShagerdDoor = Label(frn4, text = "درب  شاگرد:")
        self.lbl_ShagerdDoor.grid(row = 4, column = 0, padx = 10, pady= 10, sticky = W)
        self.shagerd = StringVar()
        self.cmb_shagerd = ttk.Combobox(frn4, textvariable= self.shagerd, values=("مطلوب", "نامطلوب"))
        self.cmb_shagerd.grid(row = 4, column = 0, padx = 100)


        self.lbl_Mirror = Label(frn4, text = " آیینه‌ها:")
        self.lbl_Mirror.grid(row = 5, column = 0, padx = 10, pady= 10, sticky = W)
        self.mirror = StringVar()
        self.cmb_mirror = ttk.Combobox(frn4, textvariable= self.mirror, values=("مطلوب", "نامطلوب"))
        self.cmb_mirror.grid(row =5 , column = 0, padx = 100)


        self.lbl_BackLight = Label(frn4, text = "چراغ‌های  عقب:")
        self.lbl_BackLight.grid(row = 6, column = 0, padx = 10, pady= 10, sticky = W)
        self.backlight = StringVar()
        self.cmb_backlight = ttk.Combobox(frn4, textvariable= self.backlight, values=("مطلوب", "نامطلوب"))
        self.cmb_backlight.grid(row = 6, column = 0, padx = 100)


        self.lbl_FrontLight = Label(frn4, text = "چراغ‌های جلو:")
        self.lbl_FrontLight.grid(row = 2, column = 3, padx = 10, pady= 10, sticky = W)
        self.frontlight = StringVar()
        self.cmb_frontlight = ttk.Combobox(frn4, textvariable= self.frontlight, values=("مطلوب", "نامطلوب"))
        self.cmb_frontlight.grid(row =2 , column = 3, padx = 100)


        self.lbl_Cabin = Label(frn4, text = " اتاق عقب:")
        self.lbl_Cabin.grid(row = 3, column = 3, padx = 10, pady= 10, sticky = W)
        self.cabin = StringVar()
        self.cmb_cabin = ttk.Combobox(frn4, textvariable= self.cabin, values=("مطلوب", "نامطلوب"))
        self.cmb_cabin.grid(row =3, column = 3, padx = 100)


        self.lbl_Vinch = Label(frn4, text = "وینچ:")
        self.lbl_Vinch.grid(row = 4, column = 3, padx = 10, pady= 10, sticky = W)
        self.vinch = StringVar()
        self.cmb_vinch = ttk.Combobox(frn4, textvariable= self.vinch, values=("مطلوب", "نامطلوب"))
        self.cmb_vinch.grid(row =4 , column = 3,padx = 100)


        self.lbl_Radiator = Label(frn4, text = " آب رادیاتور:")
        self.lbl_Radiator.grid(row = 5, column = 3, padx = 10, pady= 10, sticky = W)
        self.radiator = StringVar()
        self.cmb_radiator = ttk.Combobox(frn4, textvariable= self.radiator, values=("مطلوب", "نامطلوب"))
        self.cmb_radiator.grid(row =5 , column = 3, padx = 100)


        self.lbl_OilHidrolic = Label(frn4, text = "روغن هدرولیک:")
        self.lbl_OilHidrolic.grid(row = 6, column = 3, padx = 10, pady= 10, sticky = W)
        self.oilhid = StringVar()
        self.cmb_oilhid = ttk.Combobox(frn4, textvariable= self.oilhid, values=("مطلوب", "نامطلوب"))
        self.cmb_oilhid.grid(row =6 , column = 3, padx = 100)


        self.lbl_OilKelach = Label(frn4, text = "روغن پمپ کلاچ:")
        self.lbl_OilKelach.grid(row = 2, column = 4, padx = 20, pady= 10, sticky = W)
        self.kelach = StringVar()
        self.cmb_kelach = ttk.Combobox(frn4, textvariable= self.kelach, values=("مطلوب", "نامطلوب"))
        self.cmb_kelach.grid(row =2 , column = 5, padx =50)


        self.lbl_OilMotor = Label(frn4, text = "روغن موتور:")
        self.lbl_OilMotor.grid(row = 3, column = 4, padx = 10, pady= 10, sticky = W)
        self.oilmotor = StringVar()
        self.cmb_oilmotor = ttk.Combobox(frn4, textvariable= self.oilmotor, values=("مطلوب", "نامطلوب"))
        self.cmb_oilmotor.grid(row =3 , column = 5, padx = 50)


        self.lbl_Tasmeh = Label(frn4, text = "وضعیت تسمه‌ها:")
        self.lbl_Tasmeh.grid(row = 4, column = 4, padx = 10, pady= 10, sticky = W)
        self.tasmeh = StringVar()
        self.cmb_tasmeh = ttk.Combobox(frn4, textvariable= self.tasmeh, values=("مطلوب", "نامطلوب"))
        self.cmb_tasmeh.grid(row =4 , column =5 , padx = 50)


        self.lbl_Batteries = Label(frn4, text = "وضعیت باطری‌ها:")
        self.lbl_Batteries.grid(row = 5, column = 4, padx = 10, pady= 10, sticky = W)  
        self.batteries = StringVar()
        self.cmb_batteries = ttk.Combobox(frn4, textvariable= self.batteries, values=("مطلوب", "نامطلوب"))
        self.cmb_batteries.grid(row = 5, column = 5, padx = 50)


        self.lbl_Fom = Label(frn4, text = "سطح آب و فم:")
        self.lbl_Fom.grid(row = 6, column = 4, padx = 10, pady= 10, sticky = W) 
        self.fom = StringVar()
        self.cmb_fom = ttk.Combobox(frn4, textvariable= self.fom, values=("مطلوب", "نامطلوب"))
        self.cmb_fom.grid(row =6 , column = 5, padx =50)


        self.lbl_Monitor = Label(frn4, text = "وضعیت مانیتور:")
        self.lbl_Monitor.grid(row = 2, column = 6, padx = 10, pady= 10, sticky = W)     
        self.monitor = StringVar()
        self.cmb_monitor = ttk.Combobox(frn4, textvariable= self.monitor, values=("مطلوب", "نامطلوب"))
        self.cmb_monitor.grid(row = 2, column = 7, padx = 50)



        ######################################################################################################### 
        ##################################                  Accept                ###############################
        #########################################################################################################
        

        self.choose = BooleanVar()
        self.chk_term = Checkbutton(frn5, text ="آیا تمام گزینه‌ها را چک کردین؟", variable =self.choose, onvalue = True, offvalue = False)
        self.chk_term.config(command = self.CheckTerm)
        self.chk_term.grid(row =0, column = 0)


        self.btn_clear =Button(frn5, text ="پاک کردن", width =50, height =2, command = self.Pak)
        self.btn_clear.grid(row =1, columnspan =2, sticky =NSEW,padx =20, pady = 12)


        self.btn_register =Button(frn5, text ="ثبت", width =50, height =2, command = self.Accept)
        self.btn_register.config(state = DISABLED)
        self.btn_register.grid(row = 1, column= 6, sticky =E, padx = 615, pady = 12)



        ######################################################################################################### 
        ##################################                                        ###############################
        #########################################################################################################

    def CheckTerm(self):

        if self.choose.get() == True:
            self.btn_register.config(state = NORMAL)

    def clk(self):

        messagebox.showinfo(title="اخطار",message="لطفا تمام فیلدها را پر کنید")

    def save(self):

        messagebox.showinfo(title="اطلاع",message="اطلاعات با موفقیت ثبت شد")


    #########################################################################################################
    ##################################             تابع ثبت              ###################################
    #########################################################################################################


    def Accept(self):




        if (self.Car.get() == "" or
            self.Car.get() == "" or
            self.Select.get() == "" or
            self.Loole.get() == "" or
            self.Hidrolic.get() == "" or
            self.Raw.get() == "" or
            self.Brankadr.get() == "" or
            self.Robe.get() == "" or
            self.Oxygen.get() == "" or
            self.Clothes.get() == "" or
            self.Khamoosh.get() == "" or
            self.Map.get() == "" or
            self.cmb_Abpash.get() == "" or
            self.Snow.get() == "" or
            self.Posht.get() == "" or
            self.Etfa.get() == "" or
            self.Table.get() == "" or
            self.Alarm.get() == "" or
            self.Radio.get() == "" or
            self.fom.get() == "" or
            self.monitor.get() == "" or
            self.batteries.get() == "" or
            self.tasmeh.get() == "" or
            self.oilmotor.get() == ""  or
            self.kelach.get() == "" or
            self.oilhid.get() == "" or
            self.radiator.get() == "" or
            self.vinch.get() == "" or
            self.cabin.get() == "" or
            self.frontlight.get() == "" or
            self.backlight.get() == "" or
            self.mirror.get() == "" or
            self.shagerd.get() == "" or
            self.driverdoor.get() == "" or
            self.kapoot.get() == ""):

            messagebox.showinfo(title="اخطار",message="لطفا تمام فیلدها را پر کنید")

        else:



    #########################################################################################################
    ##################################             fetch info             ###################################
    #########################################################################################################
     
            # database = ("E:\DataBase_Checklist/Check_list2.db")
            database = ("C:\DataBase/Check_list2.db")
            con = sqlite3.connect(database)
            cur = con.cursor()
            cur.execute("select id from fetch_tb")
            rows = cur.fetchall()
            rows = str(rows)
            rows = rows.replace("u", "")
            rows = rows.replace("(", "")
            rows = rows.replace(")", "")
            rows = rows.replace(",", "")
            rows = rows.replace("'", "")
            rows = rows.replace("[", "")
            rows = rows.replace("]", "")
            rows =list(rows)
            
            if rows == []:
                rows.append(1)

                rows = str(rows)
                rows = rows.replace("[", "")
                rows = rows.replace("]", "")
                x = int(rows)
                # database = ("E:\DataBase_Checklist/Check_list2.db")
                database = ("C:\DataBase/Check_list2.db")
                con = sqlite3.connect(database)
                cur = con.cursor()


                mashin = self.Car.get()
                ranande = self.Select.get()

                tarikh = self.txt_Date.get("1.0", END)
                tarikh = tarikh.replace("-", "")
                tarikh = int(tarikh)

                loole = self.Loole.get()
                hidrolic = self.Hidrolic.get()
                raw = self.Raw.get()
                brankadr = self.Brankadr.get()
                robe = self.Robe.get()
                oxygen = self.Oxygen.get()
                clothes = self.Clothes.get()
                khamoosh = self.Khamoosh.get()
                naghshe = self.Map.get()
                abpash = self.cmb_Abpash.get()
                snow = self.Snow.get()
                posht = self.Posht.get()
                etfa = self.Etfa.get()
                tabl = self.Table.get()
                alarm = self.Alarm.get()
                radio = self.Radio.get()
                fom = self.fom.get() 
                monitor = self.monitor.get()
                batteries = self.batteries.get()
                tasmeh = self.tasmeh.get()
                oilmotor = self.oilmotor.get()
                kelach = self.kelach.get()
                oilhid = self.oilhid.get()
                radiator = self.radiator.get()
                vinch = self.vinch.get()
                cabin = self.cabin.get()
                frontlight = self.frontlight.get()
                backlight = self.backlight.get()
                mirror = self.mirror.get()
                shagerd = self.shagerd.get()
                drivedoor = self.driverdoor.get()
                kapoot = self.kapoot.get()


                query = ("INSERT INTO fetch_tb (id, car, driver, date, khamoosh, clothes, oxygen, robe, brankadr, raw, hidrolic, loole, radio, alarm, tabl, etfa, posht, snow, abpash, naghshe, kapoot, driverdoor, shagerd, mirror, backlight, frontlight, cabin, vinch, radiator, oilhid, kelach, oilmotor, tasmeh, batteries, monitor, fom) VALUES({0:d}, '{1:s}', '{2:s}', {3:d}, '{4:s}', '{5:s}', '{6:s}', '{7:s}', '{8:s}', '{9:s}', '{10:s}', '{11:s}', '{12:s}', '{13:s}', '{14:s}', '{15:s}', '{16:s}', '{17:s}', '{18:s}', '{19:s}', '{20:s}', '{21:s}', '{22:s}', '{23:s}', '{24:s}', '{25:s}', '{26:s}', '{27:s}', '{28:s}', '{29:s}', '{30:s}', '{31:s}', '{32:s}', '{33:s}', '{34:s}', '{35:s}')".format(x, ranande, mashin, tarikh, khamoosh, clothes, oxygen, robe, brankadr, raw, hidrolic, loole, radio, alarm, tabl, etfa, posht, snow, abpash, naghshe, kapoot, drivedoor, shagerd, mirror, backlight, frontlight, cabin, vinch, radiator, oilhid, kelach, oilmotor, tasmeh, batteries, monitor, fom))

                cur.execute(query)
                con.commit()

            else:


                x = rows[-1]
                x = int(x)
                x = x+1

                mashin = self.Car.get() 
                ranande = self.Select.get()


                tarikh = self.txt_Date.get("1.0", END)
                tarikh = tarikh.replace("-", "")
                tarikh = int(tarikh)
 

                loole = self.Loole.get()
                hidrolic = self.Hidrolic.get()
                raw = self.Raw.get()
                brankadr = self.Brankadr.get()
                robe = self.Robe.get()
                oxygen = self.Oxygen.get()
                clothes = self.Clothes.get()
                khamoosh = self.Khamoosh.get()
                naghshe = self.Map.get()
                abpash = self.cmb_Abpash.get()
                snow = self.Snow.get()
                posht = self.Posht.get()
                etfa = self.Etfa.get()
                tabl = self.Table.get()
                alarm = self.Alarm.get()
                radio = self.Radio.get()
                fom = self.fom.get() 
                monitor = self.monitor.get()
                batteries = self.batteries.get()
                tasmeh = self.tasmeh.get()
                oilmotor = self.oilmotor.get()
                kelach = self.kelach.get()
                oilhid = self.oilhid.get()
                radiator = self.radiator.get()
                vinch = self.vinch.get()
                cabin = self.cabin.get()
                frontlight = self.frontlight.get()
                backlight = self.backlight.get()
                mirror = self.mirror.get()
                shagerd = self.shagerd.get()
                drivedoor = self.driverdoor.get()
                kapoot = self.kapoot.get()


                query = ("INSERT INTO fetch_tb (id, car, driver, date, khamoosh, clothes, oxygen, robe, brankadr, raw, hidrolic, loole, radio, alarm, tabl, etfa, posht, snow, abpash, naghshe, kapoot, driverdoor, shagerd, mirror, backlight, frontlight, cabin, vinch, radiator, oilhid, kelach, oilmotor, tasmeh, batteries, monitor, fom) VALUES({0:d}, '{1:s}', '{2:s}', {3:d}, '{4:s}', '{5:s}', '{6:s}', '{7:s}', '{8:s}', '{9:s}', '{10:s}', '{11:s}', '{12:s}', '{13:s}', '{14:s}', '{15:s}', '{16:s}', '{17:s}', '{18:s}', '{19:s}', '{20:s}', '{21:s}', '{22:s}', '{23:s}', '{24:s}', '{25:s}', '{26:s}', '{27:s}', '{28:s}', '{29:s}', '{30:s}', '{31:s}', '{32:s}', '{33:s}', '{34:s}', '{35:s}')".format(x,mashin , ranande, tarikh, khamoosh, clothes, oxygen, robe, brankadr, raw, hidrolic, loole, radio, alarm, tabl, etfa, posht, snow, abpash, naghshe, kapoot, drivedoor, shagerd, mirror, backlight, frontlight, cabin, vinch, radiator, oilhid, kelach, oilmotor, tasmeh, batteries, monitor, fom))


                cur.execute(query)
                con.commit()
                messagebox.showinfo(title="اطلاع",message="اطلاعات با موفقیت ثبت شد")






    def Pak(self):

        
        res = messagebox.askyesno(title="اخطار",message="آیا مطمئن هستید؟??") # True/ False

        if (res == True):

            self.Car.set('')
            self.cmb_Select.set('')
            self.cmb_Khamoosh.set('')
            self.cmb_Clothes.set('')
            self.cmb_Oxygen.set('')
            self.cmb_Robe.set('')
            self.cmb_Brankadr.set('')
            self.cmb_Raw.set('')
            self.cmb_Hidrolic.set('')
            self.cmb_Loole.set('')
            self.cmb_Radio.set('')
            self.cmb_Alarm.set('')
            self.cmb_Table.set('')
            self.cmb_Etfa.set('')
            self.cmb_Posht.set('')
            self.cmb_Snow.set('')
            self.cmb_Abpash.set('')
            self.cmb_Map.set('')
            self.cmb_kapoot.set('')
            self.cmb_driverdoor.set('')
            self.cmb_shagerd.set('')
            self.cmb_mirror.set('')
            self.cmb_backlight.set('')
            self.cmb_frontlight.set('')
            self.cmb_cabin.set('')
            self.cmb_vinch.set('')
            self.cmb_radiator.set('')
            self.cmb_oilhid.set('')
            self.cmb_kelach.set('')
            self.cmb_oilmotor.set('')
            self.cmb_tasmeh.set('')
            self.cmb_batteries.set('')
            self.cmb_fom.set('')
            self.cmb_monitor.set('')
            self.txt_Date.delete("1.0", END)
            self.txt_Date.config(state = DISABLED)

    def date(self):


        Calendar = jdatetime.datetime.today()


        a = str(Calendar)
        b = a.split()


        d = b[0]
        c = b[1]
        c = c.split(".")


        self.txt_Date.config(state = NORMAL)
        self.txt_Date.insert("1.0", d)
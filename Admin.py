from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import jdatetime
import sqlite3
import string



class AdminUI:

    def __init__(self):

        pass


    def Masool(self,root):

        
        self.root = root
        top = Toplevel(self.root)
        top.geometry("400x250+500+300")
        root.title('                      پنل مسئول  ')
        top.resizable(0,0)


        self.lbl_Car = Label(top, text = "انتخاب خودرو:")
        self.lbl_Car.grid(row = 0, column = 0, padx = 50, pady= 10, sticky = W)
        self.Car = StringVar()
        self.cmb_Car = ttk.Combobox(top, textvariable= self.Car, values=("فرم‌تعمیرات خودروها","لاگ‌بوک","چک‌لیست"))
        self.cmb_Car.grid(row = 0, column = 1,padx = 10, sticky = E)
 


        self.lbl_Car = Label(top, text = "تاریخ:")
        self.lbl_Car.grid(row = 1, column = 0, padx = 50, pady= 10, sticky = W)
        self.txt_Date =Text(top, width =10, height =1, relief=SOLID,bd=1)
        self.txt_Date.grid(row =1, column = 1, padx =20, pady =50)


        self.btn_Fetch =Button(top, text ="فراخوانی", width =20, height =2, command =self.fetch)
        self.btn_Fetch.grid(row = 2, column= 0,columnspan= 2, padx = 40,pady = 10)



    def fetch(self):


        if (self.Car.get() == "چک‌لیست"):

            # database = ("E:\DataBase_Checklist/Check_list2.db")
            database = ("C:\DataBase/Check_list2.db")
            con = sqlite3.connect(database)
            cur = con.cursor()

            
            c = self.txt_Date.get("1.0", END)
            c = c.replace("\n", "")
            c = c.replace("-", "")


            cur.execute("select date from fetch_tb WHERE date = (%s)" %(c))
            rows = cur.fetchall()


            rows = str(rows)
            rows = rows.replace("u", "")
            rows = rows.replace("(", "")
            rows = rows.replace(")", "")
            rows = rows.replace(",", "")
            rows = rows.replace("[", "")
            rows = rows.replace("]", "")
            rows = rows.replace("/n", "")
            rows = rows.replace("'", "")
            rows = rows.replace(" ", ",")
            rows = rows.split(",")


            for i in range(len(rows)):

                if (c == rows[i]):


                #########################################################################################################
                ##################################                  فراخوانی   دیتا      ###############################
                #########################################################################################################




                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select car from fetch_tb WHERE date = (%s)" %(c))
                    car = cur.fetchall()
                    car = str(car) 
                    car = car.replace("u", "")
                    car = car.replace("(", "")
                    car = car.replace(")", "")
                    car = car.replace("'", "")
                    car = car.replace("[", "")
                    car = car.replace("]", "")
                    car = car.replace(",", "")
                    car = car.split()




                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select driver from fetch_tb WHERE date = (%s)" %(c))
                    driver = cur.fetchall()
                    driver = str(driver) 
                    driver = driver.replace("u", "")
                    driver = driver.replace("(", "")
                    driver = driver.replace(")", "")
                    driver = driver.replace("'", "")
                    driver = driver.replace("[", "")
                    driver = driver.replace("]", "")
                    driver = driver.replace(",", "")
                    driver = driver.replace("\\200c", "") 
                    driver = driver.split()




                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select date from fetch_tb WHERE date = (%s)" %(c))
                    date = cur.fetchall()
                    date = str(date) 
                    date = date.replace("(", "")
                    date= date.replace(")", "")
                    date= date.replace("'", "")
                    date= date.replace("[", "")
                    date= date.replace("]", "")
                    date= date.replace(",", "")
                    date= date.split()


                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select khamoosh from fetch_tb WHERE date = (%s)" %(c))
                    kham = cur.fetchall()
                    kham = str(kham) 
                    kham = kham.replace("(", "")
                    kham= kham.replace(")", "")
                    kham= kham.replace("'", "")
                    kham= kham.replace("[", "")
                    kham= kham.replace("]", "")
                    kham= kham.replace(",", "")
                    kham= kham.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select clothes from fetch_tb WHERE date = (%s)" %(c))
                    cloth = cur.fetchall()
                    cloth = str(cloth) 
                    cloth = cloth.replace("u", "")
                    cloth = cloth.replace("(", "")
                    cloth = cloth.replace(")", "")
                    cloth = cloth.replace("'", "")
                    cloth = cloth.replace("[", "")
                    cloth = cloth.replace("]", "")
                    cloth = cloth.replace(",", "")
                    cloth = cloth.split()



                    
                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select oxygen from fetch_tb WHERE date = (%s)" %(c))
                    oxy = cur.fetchall()
                    oxy = str(oxy) 
                    oxy = oxy.replace("u", "")
                    oxy = oxy.replace("(", "")
                    oxy = oxy.replace(")", "")
                    oxy = oxy.replace("'", "")
                    oxy = oxy.replace("[", "")
                    oxy = oxy.replace("]", "")
                    oxy = oxy.replace(",", "")
                    oxy=  oxy.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select robe from fetch_tb WHERE date = (%s)" %(c))
                    robe= cur.fetchall()
                    robe= str(robe) 
                    robe= robe.replace("u", "")
                    robe= robe.replace("(", "")
                    robe= robe.replace(")", "")
                    robe= robe.replace("'", "")
                    robe= robe.replace("[", "")
                    robe= robe.replace("]", "")
                    robe= robe.replace(",", "")
                    robe= robe.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select brankadr from fetch_tb WHERE date = (%s)" %(c))
                    bran = cur.fetchall()
                    bran= str(bran) 
                    bran= bran.replace("u", "")
                    bran= bran.replace("(", "")
                    bran= bran.replace(")", "")
                    bran= bran.replace("'", "")
                    bran= bran.replace("[", "")
                    bran= bran.replace("]", "")
                    bran= bran.replace(",", "")
                    bran= bran.split()


                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select raw from fetch_tb WHERE date = (%s)" %(c))
                    raw= cur.fetchall()
                    raw= str(raw) 
                    raw= raw.replace("u", "")
                    raw= raw.replace("(", "")
                    raw= raw.replace(")", "")
                    raw= raw.replace("'", "")
                    raw= raw.replace("[", "")
                    raw= raw.replace("]", "")
                    raw= raw.replace(",", "")
                    raw= raw.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select hidrolic from fetch_tb WHERE date = (%s)" %(c))
                    hidro= cur.fetchall()
                    hidro= str(hidro) 
                    hidro= hidro.replace("u", "")
                    hidro= hidro.replace("(", "")
                    hidro= hidro.replace(")", "")
                    hidro= hidro.replace("'", "")
                    hidro= hidro.replace("[", "")
                    hidro= hidro.replace("]", "")
                    hidro= hidro.replace(",", "")
                    hidro= hidro.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select loole from fetch_tb WHERE date = (%s)" %(c))
                    lool= cur.fetchall()
                    lool= str(lool) 
                    lool= lool.replace("u", "")
                    lool= lool.replace("(", "")
                    lool= lool.replace(")", "")
                    lool= lool.replace("'", "")
                    lool= lool.replace("[", "")
                    lool= lool.replace("]", "")
                    lool= lool.replace(",", "")
                    lool= lool.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select radio from fetch_tb WHERE date = (%s)" %(c))
                    radio= cur.fetchall()
                    radio= str(radio) 
                    radio= radio.replace("u", "")
                    radio= radio.replace("(", "")
                    radio= radio.replace(")", "")
                    radio= radio.replace("'", "")
                    radio= radio.replace("[", "")
                    radio= radio.replace("]", "")
                    radio= radio.replace(",", "")
                    radio= radio.split()


                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select alarm from fetch_tb WHERE date = (%s)" %(c))
                    alarm= cur.fetchall()
                    alarm= str(alarm) 
                    alarm= alarm.replace("u", "")
                    alarm= alarm.replace("(", "")
                    alarm= alarm.replace(")", "")
                    alarm= alarm.replace("'", "")
                    alarm= alarm.replace("[", "")
                    alarm= alarm.replace("]", "")
                    alarm= alarm.replace(",", "")
                    alarm= alarm.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select tabl from fetch_tb WHERE date = (%s)" %(c))
                    tabl= cur.fetchall()
                    tabl= str(tabl) 
                    tabl= tabl.replace("u", "")
                    tabl= tabl.replace("(", "")
                    tabl= tabl.replace(")", "")
                    tabl= tabl.replace("'", "")
                    tabl= tabl.replace("[", "")
                    tabl= tabl.replace("]", "")
                    tabl= tabl.replace(",", "")
                    tabl= tabl.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select etfa from fetch_tb WHERE date = (%s)" %(c))
                    etfa = cur.fetchall()
                    etfa= str(etfa) 
                    etfa= etfa.replace("u", "")
                    etfa= etfa.replace("(", "")
                    etfa= etfa.replace(")", "")
                    etfa= etfa.replace("'", "")
                    etfa= etfa.replace("[", "")
                    etfa= etfa.replace("]", "")
                    etfa= etfa.replace(",", "")
                    etfa= etfa.split()


                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select posht from fetch_tb WHERE date = (%s)" %(c))
                    posht= cur.fetchall()
                    posht= str(posht) 
                    posht= posht.replace("u", "")
                    posht= posht.replace("(", "")
                    posht= posht.replace(")", "")
                    posht= posht.replace("'", "")
                    posht= posht.replace("[", "")
                    posht= posht.replace("]", "")
                    posht= posht.replace(",", "")
                    posht= posht.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select snow from fetch_tb WHERE date = (%s)" %(c))
                    snow= cur.fetchall()
                    snow= str(snow) 
                    snow= snow.replace("u", "")
                    snow= snow.replace("(", "")
                    snow= snow.replace(")", "")
                    snow= snow.replace("'", "")
                    snow= snow.replace("[", "")
                    snow= snow.replace("]", "")
                    snow= snow.replace(",", "")
                    snow= snow.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select abpash from fetch_tb WHERE date = (%s)" %(c))
                    abpash= cur.fetchall()
                    abpash= str(abpash) 
                    abpash= abpash.replace("u", "")
                    abpash= abpash.replace("(", "")
                    abpash= abpash.replace(")", "")
                    abpash= abpash.replace("'", "")
                    abpash= abpash.replace("[", "")
                    abpash= abpash.replace("]", "")
                    abpash= abpash.replace(",", "")
                    abpash= abpash.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select naghshe from fetch_tb WHERE date = (%s)" %(c))
                    naghshe= cur.fetchall()
                    naghshe= str(naghshe) 
                    naghshe= naghshe.replace("u", "")
                    naghshe= naghshe.replace("(", "")
                    naghshe= naghshe.replace(")", "")
                    naghshe= naghshe.replace("'", "")
                    naghshe= naghshe.replace("[", "")
                    naghshe= naghshe.replace("]", "")
                    naghshe= naghshe.replace(",", "")
                    naghshe= naghshe.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select kapoot from fetch_tb WHERE date = (%s)" %(c))
                    kapoot= cur.fetchall()
                    kapoot= str(kapoot) 
                    kapoot= kapoot.replace("u", "")
                    kapoot= kapoot.replace("(", "")
                    kapoot= kapoot.replace(")", "")
                    kapoot= kapoot.replace("'", "")
                    kapoot= kapoot.replace("[", "")
                    kapoot= kapoot.replace("]", "")
                    kapoot= kapoot.replace(",", "")
                    kapoot= kapoot.split()




                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select driverdoor from fetch_tb WHERE date = (%s)" %(c))
                    drivedoor= cur.fetchall()
                    drivedoor= str(drivedoor)  
                    drivedoor= drivedoor.replace("u", "")
                    drivedoor= drivedoor.replace("(", "")
                    drivedoor= drivedoor.replace(")", "")
                    drivedoor= drivedoor.replace("'", "")
                    drivedoor= drivedoor.replace("[", "")
                    drivedoor= drivedoor.replace("]", "")
                    drivedoor= drivedoor.replace(",", "")
                    drivedoor= drivedoor.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select shagerd from fetch_tb WHERE date = (%s)" %(c))
                    shagerd= cur.fetchall()
                    shagerd= str(shagerd) 
                    shagerd= shagerd.replace("u", "")
                    shagerd= shagerd.replace("(", "")
                    shagerd= shagerd.replace(")", "")
                    shagerd= shagerd.replace("'", "")
                    shagerd= shagerd.replace("[", "")
                    shagerd= shagerd.replace("]", "")
                    shagerd= shagerd.replace(",", "")
                    shagerd= shagerd.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select mirror from fetch_tb WHERE date = (%s)" %(c))
                    mirror= cur.fetchall()
                    mirror= str(mirror) 
                    mirror= mirror.replace("u", "")
                    mirror= mirror.replace("(", "")
                    mirror= mirror.replace(")", "")
                    mirror= mirror.replace("'", "")
                    mirror= mirror.replace("[", "")
                    mirror= mirror.replace("]", "")
                    mirror= mirror.replace(",", "")
                    mirror= mirror.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select backlight from fetch_tb WHERE date = (%s)" %(c))
                    backlight= cur.fetchall()
                    backlight= str(backlight) 
                    backlight= backlight.replace("u", "")
                    backlight= backlight.replace("(", "")
                    backlight= backlight.replace(")", "")
                    backlight= backlight.replace("'", "")
                    backlight= backlight.replace("[", "")
                    backlight= backlight.replace("]", "")
                    backlight= backlight.replace(",", "")
                    backlight= backlight.split()




                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select frontlight from fetch_tb WHERE date = (%s)" %(c))
                    frontlight= cur.fetchall()
                    frontlight= str(frontlight) 
                    frontlight= frontlight.replace("u", "")
                    frontlight= frontlight.replace("(", "")
                    frontlight= frontlight.replace(")", "")
                    frontlight= frontlight.replace("'", "")
                    frontlight= frontlight.replace("[", "")
                    frontlight= frontlight.replace("]", "")
                    frontlight= frontlight.replace(",", "")
                    frontlight= frontlight.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select cabin from fetch_tb WHERE date = (%s)" %(c))
                    cabin= cur.fetchall()
                    cabin= str(cabin) 
                    cabin= cabin.replace("u", "")
                    cabin= cabin.replace("(", "")
                    cabin= cabin.replace(")", "")
                    cabin= cabin.replace("'", "")
                    cabin= cabin.replace("[", "")
                    cabin= cabin.replace("]", "")
                    cabin= cabin.replace(",", "")
                    cabin= cabin.split()




                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select vinch from fetch_tb WHERE date = (%s)" %(c))
                    vinch= cur.fetchall()
                    vinch= str(vinch) 
                    vinch= vinch.replace("u", "")
                    vinch= vinch.replace("(", "")
                    vinch= vinch.replace(")", "")
                    vinch= vinch.replace("'", "")
                    vinch= vinch.replace("[", "")
                    vinch= vinch.replace("]", "")
                    vinch= vinch.replace(",", "")
                    vinch= vinch.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select radiator from fetch_tb WHERE date = (%s)" %(c))
                    radiator= cur.fetchall()
                    radiator= str(radiator) 
                    radiator= radiator.replace("u", "")
                    radiator= radiator.replace("(", "")
                    radiator= radiator.replace(")", "")
                    radiator= radiator.replace("'", "")
                    radiator= radiator.replace("[", "")
                    radiator= radiator.replace("]", "")
                    radiator= radiator.replace(",", "")
                    radiator= radiator.split()


                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select oilhid from fetch_tb WHERE date = (%s)" %(c))
                    oilhid= cur.fetchall()
                    oilhid= str(oilhid) 
                    oilhid= oilhid.replace("u", "")
                    oilhid= oilhid.replace("(", "")
                    oilhid= oilhid.replace(")", "")
                    oilhid= oilhid.replace("'", "")
                    oilhid= oilhid.replace("[", "")
                    oilhid= oilhid.replace("]", "")
                    oilhid= oilhid.replace(",", "")
                    oilhid= oilhid.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select kelach from fetch_tb WHERE date = (%s)" %(c))
                    kelach= cur.fetchall()
                    kelach= str(kelach) 
                    kelach= kelach.replace("u", "")
                    kelach= kelach.replace("(", "")
                    kelach= kelach.replace(")", "")
                    kelach= kelach.replace("'", "")
                    kelach= kelach.replace("[", "")
                    kelach= kelach.replace("]", "")
                    kelach= kelach.replace(",", "")
                    kelach= kelach.split()




                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select oilmotor from fetch_tb WHERE date = (%s)" %(c))
                    oilmotor= cur.fetchall()
                    oilmotor= str(oilmotor) 
                    oilmotor= oilmotor.replace("u", "")
                    oilmotor= oilmotor.replace("(", "")
                    oilmotor= oilmotor.replace(")", "")
                    oilmotor= oilmotor.replace("'", "")
                    oilmotor= oilmotor.replace("[", "")
                    oilmotor= oilmotor.replace("]", "")
                    oilmotor= oilmotor.replace(",", "")
                    oilmotor= oilmotor.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select tasmeh from fetch_tb WHERE date = (%s)" %(c))
                    tasmeh= cur.fetchall()
                    tasmeh= str(tasmeh) 
                    tasmeh= tasmeh.replace("u", "")
                    tasmeh= tasmeh.replace("(", "")
                    tasmeh= tasmeh.replace(")", "")
                    tasmeh= tasmeh.replace("'", "")
                    tasmeh= tasmeh.replace("[", "")
                    tasmeh= tasmeh.replace("]", "")
                    tasmeh= tasmeh.replace(",", "")
                    tasmeh= tasmeh.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select batteries from fetch_tb WHERE date = (%s)" %(c))
                    batteries= cur.fetchall()
                    batteries= str(batteries) 
                    batteries= batteries.replace("u", "")
                    batteries= batteries.replace("(", "")
                    batteries= batteries.replace(")", "")
                    batteries= batteries.replace("'", "")
                    batteries= batteries.replace("[", "")
                    batteries= batteries.replace("]", "")
                    batteries= batteries.replace(",", "")
                    batteries= batteries.split()




                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select monitor from fetch_tb WHERE date = (%s)" %(c))
                    monitor= cur.fetchall()
                    monitor= str(monitor) 
                    monitor= monitor.replace("u", "")
                    monitor= monitor.replace("(", "")
                    monitor= monitor.replace(")", "")
                    monitor= monitor.replace("'", "")
                    monitor= monitor.replace("[", "")
                    monitor= monitor.replace("]", "")
                    monitor= monitor.replace(",", "")
                    monitor= monitor.split()



                    # database = ("E:\DataBase_Checklist/Check_list2.db")
                    database = ("C:\DataBase/Check_list2.db")
                    con = sqlite3.connect(database)
                    cur = con.cursor()
                    cur.execute("select fom from fetch_tb WHERE date = (%s)" %(c))
                    fom= cur.fetchall()
                    fom= str(fom) 
                    fom= fom.replace("u", "")
                    fom= fom.replace("(", "")
                    fom= fom.replace(")", "")
                    fom= fom.replace("'", "")
                    fom= fom.replace("[", "")
                    fom= fom.replace("]", "")
                    fom= fom.replace(",", "")
                    fom= fom.split()



                    #########################################################################################################
                    ##################################                  پنجره فراخوانی       ###############################
                    #########################################################################################################




                    top = Toplevel(self.root)
                    top.geometry("1410x880+55+0")
                    top.title("                                                                                                                                                                                                       نتیجه")
                    top.resizable(0,0)
                    
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



                    self.lbl_Select = Label(frn1, text = " راننده:")
                    self.lbl_Select.grid(row = 0, column = 0, padx = 10, pady= 10, sticky = W)

                    self.txt_Select =Text(frn1, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_Select.config(state=NORMAL)
                    self.txt_Select.insert(END, driver[i])
                    self.txt_Select.config(state = DISABLED)
                    self.txt_Select.grid(row =0, column = 1, padx = 50)
                    


                    self.lbl_Car = Label(frn1, text = " خودرو:")
                    self.lbl_Car.grid(row = 0, column = 2, padx = 50, pady= 10, sticky = W)
                    self.txt_Car =Text(frn1, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_Car.insert(END, car[i])
                    self.txt_Car.config(state = DISABLED)
                    self.txt_Car.grid(row =0, column = 3, padx =50)
                

                    self.lbl_Date =Label(frn1, text ="تاریخ")
                    self.lbl_Date.grid(row = 0, column= 4, padx = 100)
                    self.txt_Date =Text(frn1, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_Date.insert(END, date[i])
                    self.txt_Date.config(state = DISABLED)
                    self.txt_Date.grid(row =0, column = 5, columnspan =4, padx =20)



                    #########################################################################################################
                    ##################################                  بازدید تجهیزات       ###############################
                    #########################################################################################################


                    self.lbl_khamooshDasti = Label(frn2, text = "خاموش کننده دستی:")
                    self.lbl_khamooshDasti.grid(row = 2, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_khamoosh =Text(frn2, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_khamoosh.insert(END, kham[i])
                    self.txt_khamoosh.config(state = DISABLED)
                    self.txt_khamoosh.grid(row =2, column = 2, columnspan =4, padx =400)





                    self.lbl_FireClothes = Label(frn2, text = "لباس آتش‌نشانی:")
                    self.lbl_FireClothes.grid(row = 3, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_clothes =Text(frn2, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_clothes.insert(END, cloth[i])
                    self.txt_clothes.config(state = DISABLED)
                    self.txt_clothes.grid(row =3, column = 2, columnspan =4, padx =400)



                    self.lbl_Oxygen = Label(frn2, text = "دستگاه تنفسی:")
                    self.lbl_Oxygen.grid(row = 4, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_oxygen =Text(frn2, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_oxygen.insert(END, oxy[i])
                    self.txt_oxygen.config(state = DISABLED)
                    self.txt_oxygen.grid(row =4, column =2 , columnspan =4, padx =400)


                    self.lbl_Robe = Label(frn2, text = "طناب نجات:")
                    self.lbl_Robe.grid(row = 5, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_robe =Text(frn2, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_robe.insert(END, robe[i])
                    self.txt_robe.config(state = DISABLED)
                    self.txt_robe.grid(row =5, column =2 , columnspan =4, padx =400)



                    self.lbl_Brankadr = Label(frn2, text = "بارنکادر:")
                    self.lbl_Brankadr.grid(row = 6, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_brankadr =Text(frn2, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_brankadr.insert(END, bran[i])
                    self.txt_brankadr.config(state = DISABLED)
                    self.txt_brankadr.grid(row =6, column = 2, columnspan =4, padx =400)



                    self.lbl_Raw = Label(frn2, text = "آره موتوری:")
                    self.lbl_Raw.grid(row = 7, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_raw =Text(frn2, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_raw.insert(END, raw[i])
                    self.txt_raw.config(state = DISABLED)
                    self.txt_raw.grid(row =7, column =2 , columnspan =4, padx =400)


                    self.lbl_Hidrolic = Label(frn2, text = "ست هیدرولیک:")
                    self.lbl_Hidrolic.grid(row = 8, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_hidrolic =Text(frn2, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_hidrolic.insert(END, hidro[i])
                    self.txt_hidrolic.config(state = DISABLED)
                    self.txt_hidrolic.grid(row =8, column =2 , columnspan =4, padx =400)


                    self.lbl_Loole = Label(frn2, text = "لوله آتش‌نشانی:")
                    self.lbl_Loole.grid(row = 9, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_loole =Text(frn2, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_loole.insert(END, lool[i])
                    self.txt_loole.config(state = DISABLED)
                    self.txt_loole.grid(row =9, column = 2, columnspan =4, padx =400)


                    #########################################################################################################
                    ##################################                   کابین راننده        ###############################
                    #########################################################################################################


                    self.lbl_Radio = Label(frn3, text = "دستگاه رادیویی:")
                    self.lbl_Radio.grid(row = 2, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_radio =Text(frn3, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_radio.insert(END, radio[i])
                    self.txt_radio.config(state = DISABLED)
                    self.txt_radio.grid(row =2, column =1 , columnspan =4, padx =400)




                    self.lbl_Alarm = Label(frn3, text = "آژیر و چراغ گردان:")
                    self.lbl_Alarm.grid(row = 3, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_alarm =Text(frn3, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_alarm.insert(END, alarm[i])
                    self.txt_alarm.config(state = DISABLED)
                    self.txt_alarm.grid(row =3, column =1 , columnspan =4, padx =400)



                    self.lbl_TableControl = Label(frn3, text = "تابلو کنترل:")
                    self.lbl_TableControl.grid(row = 4, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_table =Text(frn3, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_table.insert(END, tabl[i])
                    self.txt_table.config(state = DISABLED)
                    self.txt_table.grid(row =4, column = 1, columnspan =4, padx =400)


                    
                    self.lbl_Etfa = Label(frn3, text = "سیستم اطفا:")
                    self.lbl_Etfa.grid(row = 5, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_etfa =Text(frn3, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_etfa.insert(END, etfa[i])
                    self.txt_etfa.config(state = DISABLED)
                    self.txt_etfa.grid(row =5, column =1 , columnspan =4, padx =400)


                    self.lbl_PoshtAmper = Label(frn3, text = "نشانگر پشت آمپر:")
                    self.lbl_PoshtAmper.grid(row = 6, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_posht =Text(frn3, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_posht.insert(END, posht[i])
                    self.txt_posht.config(state = DISABLED)
                    self.txt_posht.grid(row =6, column =1 , columnspan =4, padx =400)



                    self.lbl_Snow = Label(frn3, text = "برف پک‌کن:")
                    self.lbl_Snow.grid(row = 7, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_snow =Text(frn3, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_snow.insert(END, snow[i])
                    self.txt_snow.config(state = DISABLED)
                    self.txt_snow.grid(row =7, column =1 , columnspan =4, padx =400)

                    

                    self.lbl_Abpash = Label(frn3, text = "آب‌پاش شیشه:")
                    self.lbl_Abpash.grid(row = 8, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_abpash =Text(frn3, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_abpash.insert(END, abpash[i])
                    self.txt_abpash.config(state = DISABLED)
                    self.txt_abpash.grid(row =8, column =1 , columnspan =4, padx =400)



                    self.lbl_Map = Label(frn3, text = "نقشه:")
                    self.lbl_Map.grid(row = 9, column = 0, padx = 10, pady= 10, sticky = W)   
                    self.txt_map =Text(frn3, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_map.insert(END, naghshe[i])
                    self.txt_map.config(state = DISABLED)
                    self.txt_map.grid(row =9, column =1 , columnspan =4, padx =400)

                    #########################################################################################################
                    ##################################                  وضعیت بدنه           ###############################
                    #########################################################################################################
                    

                    self.lbl_Kapoot = Label(frn4, text = "کاپوت:")
                    self.lbl_Kapoot.grid(row = 2, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_kapoot =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_kapoot.insert(END, kapoot[i])
                    self.txt_kapoot.config(state = DISABLED)
                    self.txt_kapoot.grid(row =2, column =0 , padx =100)



                    


                    self.lbl_DriverDoor = Label(frn4, text = "درب  راننده:")
                    self.lbl_DriverDoor.grid(row = 3, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_driverdoor =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_driverdoor.insert(END, drivedoor[i])
                    self.txt_driverdoor.config(state = DISABLED)
                    self.txt_driverdoor.grid(row =3, column = 0,padx =100)



                    self.lbl_ShagerdDoor = Label(frn4, text = "درب  شاگرد:")
                    self.lbl_ShagerdDoor.grid(row = 4, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_shagerd =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_shagerd.insert(END, shagerd[i])
                    self.txt_shagerd.config(state = DISABLED)
                    self.txt_shagerd.grid(row =4, column =0 ,padx =100)


                    self.lbl_Mirror = Label(frn4, text = " آیینه‌ها:")
                    self.lbl_Mirror.grid(row = 5, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_mirror =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_mirror.insert(END, mirror[i])
                    self.txt_mirror.config(state = DISABLED)
                    self.txt_mirror.grid(row =5, column = 0, padx =100)
                    

                    self.lbl_BackLight = Label(frn4, text = "چراغ‌های  عقب:")
                    self.lbl_BackLight.grid(row = 6, column = 0, padx = 10, pady= 10, sticky = W)
                    self.txt_backlight =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_backlight.insert(END, backlight[i])
                    self.txt_backlight.config(state = DISABLED)
                    self.txt_backlight.grid(row =6, column =0 , padx =100)


                    self.lbl_FrontLight = Label(frn4, text = "چراغ‌های جلو:")
                    self.lbl_FrontLight.grid(row = 2, column = 3, padx = 10, pady= 10, sticky = W)
                    self.txt_frontlight =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_frontlight.insert(END, frontlight[i])
                    self.txt_frontlight.config(state = DISABLED)
                    self.txt_frontlight.grid(row =2, column =3 ,padx =100)
                    


                    self.lbl_Cabin = Label(frn4, text = " اتاق عقب:")
                    self.lbl_Cabin.grid(row = 3, column = 3, padx = 10, pady= 10, sticky = W)
                    self.txt_cabin =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_cabin.insert(END, cabin[i])
                    self.txt_cabin.config(state = DISABLED)
                    self.txt_cabin.grid(row =3, column =3 ,  padx =100)

                    


                    self.lbl_Vinch = Label(frn4, text = "وینچ:")
                    self.lbl_Vinch.grid(row = 4, column = 3, padx = 10, pady= 10, sticky = W)
                    self.txt_vinch =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_vinch.insert(END, vinch[i])
                    self.txt_vinch.config(state = DISABLED)
                    self.txt_vinch.grid(row =4, column =3 ,  padx =100)
            


                    self.lbl_Radiator = Label(frn4, text = " آب رادیاتور:")
                    self.lbl_Radiator.grid(row = 5, column = 3, padx = 10, pady= 10, sticky = W)
                    self.txt_radiator =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_radiator.insert(END, radiator[i])
                    self.txt_radiator.config(state = DISABLED)
                    self.txt_radiator.grid(row =5, column =3 ,  padx =100)


                    self.lbl_OilHidrolic = Label(frn4, text = "روغن هدرولیک:")
                    self.lbl_OilHidrolic.grid(row = 6, column = 3, padx = 10, pady= 10, sticky = W)
                    self.txt_oilhidrolic =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_oilhidrolic.insert(END, oilhid[i])
                    self.txt_oilhidrolic.config(state = DISABLED)
                    self.txt_oilhidrolic.grid(row =6, column =3 ,  padx =100)
                    


                    self.lbl_OilKelach = Label(frn4, text = "روغن پمپ کلاچ:")
                    self.lbl_OilKelach.grid(row = 2, column = 4, padx = 20, pady= 10, sticky = W)
                    self.txt_oilkelach =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_oilkelach.insert(END, kelach[i])
                    self.txt_oilkelach.config(state = DISABLED)
                    self.txt_oilkelach.grid(row =2, column =5 ,  padx =100)
                


                    self.lbl_OilMotor = Label(frn4, text = "روغن موتور:")
                    self.lbl_OilMotor.grid(row = 3, column = 4, padx = 10, pady= 10, sticky = W)
                    self.txt_oilmotor =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_oilmotor.insert(END, oilmotor[i])
                    self.txt_oilmotor.config(state = DISABLED)
                    self.txt_oilmotor.grid(row =3, column =5 ,  padx =100)
                    


                    self.lbl_Tasmeh = Label(frn4, text = "وضعیت تسمه‌ها:")
                    self.lbl_Tasmeh.grid(row = 4, column = 4, padx = 10, pady= 10, sticky = W)
                    self.txt_tasmeh =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_tasmeh.insert(END, tasmeh[i])
                    self.txt_tasmeh.config(state = DISABLED)
                    self.txt_tasmeh.grid(row =4, column =5 ,  padx =100)
                


                    self.lbl_Batteries = Label(frn4, text = "وضعیت باطری‌ها:")
                    self.lbl_Batteries.grid(row = 5, column = 4, padx = 10, pady= 10, sticky = W) 
                    self.txt_batteries =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_batteries.insert(END, batteries[i])
                    self.txt_batteries.config(state = DISABLED)
                    self.txt_batteries.grid(row =5, column =5 ,  padx =100)


                    self.lbl_Fom = Label(frn4, text = "سطح آب و فم:")
                    self.lbl_Fom.grid(row = 6, column = 4, padx = 10, pady= 10, sticky = W) 
                    self.txt_fom =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_fom.insert(END, fom[i])
                    self.txt_fom.config(state = DISABLED)
                    self.txt_fom.grid(row =6, column =5 ,  padx =100)


                    self.lbl_Monitor = Label(frn4, text = "وضعیت مانیتور:")
                    self.lbl_Monitor.grid(row = 2, column = 6, padx = 10, pady= 10, sticky = W)    
                    self.txt_monitor =Text(frn4, width =10, height =1, relief=SOLID,bd=2)
                    self.txt_monitor.insert(END, monitor[i])
                    self.txt_monitor.config(state = DISABLED)
                    self.txt_monitor.grid(row =2, column =7 ,  padx =100)

        elif (self.Car.get() == "لاگ‌بوک"):

            print ("لاگ‌بوک")

        elif (self.Car.get() == "فرم‌تعمیرات خودروها"):

            top = Toplevel(self.root)
            top.geometry("800x490+300+100")
            top.title("                                                                                                         موارد بازدید و تعویض")
            top.resizable(0,0)

            frn1 =LabelFrame(top, text = "موارد بازدید و تعویض" ,width=800, height=490, relief=GROOVE, bd =4)
            frn1.grid_propagate(False)
            frn1.grid(row = 0, columnspan = 2,sticky=NSEW,padx =1, pady =1)


            self.lbl_Car = Label(frn1, text = " خودرو:")
            self.lbl_Car.grid(row = 0, column = 0, padx = 30, pady= 10, sticky = W)
            self.txt_Car =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_Car.grid(row =0, column =1 , padx =10, pady =50)
           

            self.lbl_Car = Label(frn1, text = "تاریخ:")
            self.lbl_Car.grid(row = 0, column = 2, padx = 30)
            self.txt_Date =Text(frn1, width =20, height =1, relief=SOLID,bd=1)
            self.txt_Date.grid(row =0, column = 3, columnspan =4, padx =30, pady =50)


            self.lbl_oilmotor = Label(frn1, text = "روغن موتور:")
            self.lbl_oilmotor.grid(row = 1, column = 0, padx= 30, pady = 10, sticky = W)
            self.txt_oilmotor =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_oilmotor.grid(row =1, column =1 , padx =30)
            

            self.lbl_oilfilter = Label(frn1, text = " فیلتر روغن:")
            self.lbl_oilfilter.grid(row =2 , column = 0, padx= 30, pady = 10, sticky = W)            
            self.txt_oilfilter =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_oilfilter.grid(row =2, column = 1, padx =30)
            

            self.lbl_filtergasoil = Label(frn1, text = "فیلتر گازوییل:")
            self.lbl_filtergasoil.grid(row =3 , column =0 , padx= 30, pady = 10, sticky = W)            
            self.txt_filtergasoil =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_filtergasoil.grid(row =3, column =1 , padx =30)
            

            self.lbl_havafilter = Label(frn1, text = "فیلتر هوا:")
            self.lbl_havafilter.grid(row =4 , column = 0, padx= 30, pady = 10, sticky = W)            
            self.txt_havafilter =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_havafilter.grid(row =4, column = 1, padx =30)
            

            self.lbl_gearvasgasin = Label(frn1, text = "واسگازین گیربکس:")
            self.lbl_gearvasgasin.grid(row = 5, column = 0, padx= 30, pady = 10, sticky = W)            
            self.txt_gearvasgasin =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_gearvasgasin.grid(row =5, column =1 , padx =30)
            

            self.lbl_difvasgasin = Label(frn1, text = " واسگازین دیفرانسیل:")
            self.lbl_difvasgasin.grid(row =6 , column =0 , padx= 30, pady = 10, sticky = W)
            self.txt_difvasgasin =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_difvasgasin.grid(row =6, column =1 , padx =30)
            
            
            self.lbl_roghanfarman = Label(frn1, text = "روغن هیدرولیک فرمان:")
            self.lbl_roghanfarman.grid(row =7 , column = 0, padx= 30, pady = 10, sticky = W)
            self.txt_roghanfarman =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_roghanfarman.grid(row =7, column =1 , padx =30)
            

            self.lbl_kelachoil = Label(frn1, text = "روغن پمپ کلاچ:")
            self.lbl_kelachoil .grid(row =8 , column = 0, padx= 30, pady = 10, sticky = W)
            self.txt_kelachoil =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_kelachoil.grid(row =8, column =1 , padx =30)
            

            self.lbl_griskaricar = Label(frn1, text = "گریسکاری زیر خودرو:")
            self.lbl_griskaricar.grid(row =1 , column = 2, padx= 30, pady = 10, sticky = W)
            self.txt_griskaricar =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_griskaricar.grid(row =1, column =3 , padx =30)
           

            self.lbl_griskariatash = Label(frn1, text = "گریسکاری سیستم آتش‌نشانی:")
            self.lbl_griskariatash.grid(row =2 , column = 2, padx= 30, pady = 10, sticky = W)
            self.txt_griskariatash =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_griskariatash.grid(row =2, column =3 , padx =30)
            

            self.lbl_griskarigardan = Label(frn1, text = "گریسکاری گاردان:")
            self.lbl_griskarigardan.grid(row =3 , column =2 , padx= 30, pady = 10, sticky = W)
            self.txt_griskarigardan =Text(frn1, width =10, height =1, relief=SOLID,bd=1)
            self.txt_griskarigardan.grid(row =3, column =3 , padx =30)
            

        else:

            messagebox.showwarning(title="اخطار",message="لطفا یکی از گزینه‌ها را انتخاب کنین")
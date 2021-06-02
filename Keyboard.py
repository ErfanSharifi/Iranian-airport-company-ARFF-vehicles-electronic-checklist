
from sqlite3.dbapi2 import SQLITE_ALTER_TABLE
from tkinter import *
import tkinter as tk
from tkinter import ttk
import Logbook as bv


class Keyb:

    def __init__(self):


        pass


    def Key(self, root):


        self.root = root
        top = Toplevel(self.root)
        top.geometry('1010x250')
        top.title('کیبورد')
        top.configure(bg = 'white')        
        top.maxsize(width=1010, height=250)      
        top.minsize(width= 1010 , height = 250)


        self.exp = " "


        self.equation = tk.StringVar()
        Dis_entry = ttk.Entry(top,state= 'readonly',textvariable = self.equation)
        Dis_entry.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)




        q = ttk.Button(top,text =  'ض' , width = 6, command = lambda : self.press('ض'))
        q.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)

        w = ttk.Button(top,text = 'ص' , width = 6, command = lambda : self.press('ص'))
        w.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)

        E = ttk.Button(top,text = 'ث' , width = 6, command = lambda : self.press('ث'))
        E.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)

        R = ttk.Button(top,text = 'ق' , width = 6, command = lambda : self.press('ق'))
        R.grid(row = 1 , column = 3, ipadx = 6 , ipady = 10)

        T = ttk.Button(top,text = 'ف' , width = 6, command = lambda : self.press('ف'))
        T.grid(row = 1 , column = 4, ipadx = 6 , ipady = 10)

        Y = ttk.Button(top,text = 'غ' , width = 6, command = lambda : self.press('غ'))
        Y.grid(row = 1 , column = 5, ipadx = 6 , ipady = 10)

        U = ttk.Button(top,text = 'ع' , width = 6, command = lambda : self.press('ع'))
        U.grid(row = 1 , column = 6, ipadx = 6 , ipady = 10)

        I = ttk.Button(top,text = 'ه' , width = 6, command = lambda : self.press('ه'))
        I.grid(row = 1 , column = 7, ipadx = 6 , ipady = 10)

        O = ttk.Button(top,text = 'خ' , width = 6, command = lambda : self.press('خ'))
        O.grid(row = 1 , column = 8, ipadx = 6 , ipady = 10)

        P = ttk.Button(top,text = 'ح' , width = 6, command = lambda : self.press('ح'))
        P.grid(row = 1 , column = 9, ipadx = 6 , ipady = 10)

        cur = ttk.Button(top,text = 'ج' , width = 6, command = lambda : self.press('ج'))
        cur.grid(row = 1 , column = 10 , ipadx = 6 , ipady = 10)

        cur_c = ttk.Button(top,text = 'چ' , width = 6, command = lambda : self.press('چ'))
        cur_c.grid(row = 1 , column = 11, ipadx = 6 , ipady = 10)

        back_slash = ttk.Button(top,text = 'پ' , width = 6, command = lambda : self.press('پ'))
        back_slash.grid(row = 1 , column = 12, ipadx = 6 , ipady = 10)


        clear = ttk.Button(top,text = 'Clear' , width = 6, command = self.clear)
        clear.grid(row = 1 , column = 13, ipadx = 20 , ipady = 10)


        # Second Line Button



        A = ttk.Button(top,text = 'ش' , width = 6, command = lambda : self.press('ش'))
        A.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)


        S = ttk.Button(top,text = 'س' , width = 6, command = lambda : self.press('س'))
        S.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)


        D = ttk.Button(top,text = 'ی' , width = 6, command = lambda : self.press('ی'))
        D.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)


        F = ttk.Button(top,text = 'ب' , width = 6, command = lambda : self.press('ب'))
        F.grid(row = 2 , column = 3, ipadx = 6 , ipady = 10)


        G = ttk.Button(top,text = 'ل' , width = 6, command = lambda : self.press('ل'))
        G.grid(row = 2 , column = 4, ipadx = 6 , ipady = 10)


        H = ttk.Button(top,text = 'ا' , width = 6, command = lambda : self.press('ا'))
        H.grid(row = 2 , column = 5, ipadx = 6 , ipady = 10)


        J = ttk.Button(top,text = 'ت' , width = 6, command = lambda : self.press('ت'))
        J.grid(row = 2 , column = 6, ipadx = 6 , ipady = 10)


        K = ttk.Button(top,text = 'ن' , width = 6, command = lambda : self.press('ن'))
        K.grid(row = 2 , column = 7, ipadx = 6 , ipady = 10)

        L = ttk.Button(top,text = 'م' , width = 6, command = lambda : self.press('م'))
        L.grid(row = 2 , column = 8, ipadx = 6 , ipady = 10)


        semi_co = ttk.Button(top,text = 'ک' , width = 6, command = lambda : self.press('ک'))
        semi_co.grid(row = 2 , column = 9, ipadx = 6 , ipady = 10)


        d_colon = ttk.Button(top,text = 'گ' , width = 6, command = lambda : self.press('گ'))
        d_colon.grid(row = 2 , column = 10, ipadx = 6 , ipady = 10)


        enter = ttk.Button(top,text = 'Enter' , width = 6, command = self.action)
        enter.grid(row = 2 , columnspan = 75, ipadx = 85 , ipady = 10)


        # third line Button


        Z = ttk.Button(top,text = 'ظ' , width = 6, command = lambda : self.press('ظ'))
        Z.grid(row = 3 , column = 0, ipadx = 6 , ipady = 10)


        X = ttk.Button(top,text = 'ط' , width = 6, command = lambda : self.press('ط'))
        X.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)


        C = ttk.Button(top,text = 'ز' , width = 6, command = lambda : self.press('ز'))
        C.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)


        V = ttk.Button(top,text = 'ر' , width = 6, command = lambda : self.press('ر'))
        V.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)

        B = ttk.Button(top, text= 'ذ' , width = 6 , command = lambda : self.press('ذ'))
        B.grid(row = 3 , column = 4 , ipadx = 6 ,ipady = 10)


        N = ttk.Button(top,text = 'د' , width = 6, command = lambda : self.press('د'))
        N.grid(row = 3 , column = 5, ipadx = 6 , ipady = 10)


        M = ttk.Button(top,text = 'ئ' , width = 6, command = lambda : self.press('ئ'))
        M.grid(row = 3 , column = 6, ipadx = 6 , ipady = 10)


        left = ttk.Button(top,text = 'و' , width = 6, command = lambda : self.press('و'))
        left.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)


        right = ttk.Button(top,text = '.' , width = 6, command = lambda : self.press('.'))
        right.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)


        slas = ttk.Button(top,text = 'ژ' , width = 6, command = lambda : self.press('ژ'))
        slas.grid(row = 3 , column = 9, ipadx = 6 , ipady = 10)


        q_mark = ttk.Button(top,text = '?' , width = 6, command = lambda : self.press('?'))
        q_mark.grid(row = 3 , column = 10, ipadx = 6 , ipady = 10)


        coma = ttk.Button(top,text = ',' , width = 6, command = lambda : self.press(','))
        coma.grid(row = 3 , column = 11, ipadx = 6 , ipady = 10)

        dot = ttk.Button(top,text = '.' , width = 6, command = lambda : self.press('.'))
        dot.grid(row = 3 , column = 12, ipadx = 6 , ipady = 10)

        shift = ttk.Button(top,text = 'Shift' , width = 6, command = lambda : self.press('Shift'))
        shift.grid(row = 3 , column = 13, ipadx = 20 , ipady = 10)


        #Fourth Line Button


        ctrl = ttk.Button(top,text = 'Ctrl' , width = 6, command = lambda : self.press('Ctrl'))
        ctrl.grid(row = 4 , column = 0, ipadx = 6 , ipady = 10)


        Fn = ttk.Button(top,text = 'Fn' , width = 6, command = lambda : self.press('Fn'))
        Fn.grid(row = 4 , column = 1, ipadx = 6 , ipady = 10)


        window = ttk.Button(top,text = 'Window' , width = 6, command = lambda : self.press('Window'))
        window.grid(row = 4 , column = 2 , ipadx = 6 , ipady = 10)

        Alt = ttk.Button(top,text = 'Alt' , width = 6, command = lambda : self.press('Alt'))
        Alt.grid(row = 4 , column = 3 , ipadx = 6 , ipady = 10)

        space = ttk.Button(top,text = 'Space' , width = 6, command = lambda : self.press(' '))
        space.grid(row = 4 , columnspan = 14 , ipadx = 160 , ipady = 10)

        Alt_gr = ttk.Button(top,text = 'Alt Gr' , width = 6, command = lambda : self.press('Alt Gr'))
        Alt_gr.grid(row = 4 , column = 10 , ipadx = 6 , ipady = 10)

        open_b = ttk.Button(top,text = '(' , width = 6, command = lambda : self.press('('))
        open_b.grid(row = 4 , column = 11 , ipadx = 6 , ipady = 10)

        close_b = ttk.Button(top,text = ')' , width = 6, command = lambda : self.press(')'))
        close_b.grid(row = 4 , column = 12 , ipadx = 6 , ipady = 10)


        tap = ttk.Button(top,text = 'Tab' , width = 6, command = self.Tab)
        tap.grid(row = 4 , column = 13 , ipadx = 20 , ipady = 10)



    def press(self, num):


        self.num = num
        self.exp = self.exp + str(self.num)
        self.equation.set(self.exp)



    def clear(self):


        self.exp = " "
        self.equation.set(self.exp)


    def action(self):


        b = self.equation.get()
        # print (b)
        self.equation.set(self.exp)

        obj = bv.Log()
        obj.lal(b)

   
    def Tab(self):


        self.exp = " TAB : "
        self.equation.set(self.exp)
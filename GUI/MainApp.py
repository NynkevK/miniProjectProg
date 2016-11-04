# Geschreven door Mark


import tkinter as tk
from GUI import BillingDutch
from GUI import StartpageDutch
from GUI import StartpageEnglish
from GUI import PayDutch
from GUI import TicketDutch
from GUI import BillingEnglish
from GUI import PayEnglish
from GUI import TicketEnglish


class MainApplication(tk.Tk):


    def __init__(self, *args, **kwargs):
        """initialiseert de main applicatie objecten"""
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Betaalautomaat Kruisstraat")
        tk.Tk.resizable(self, False, False)
        tk.Tk.wm_geometry(self, '1000x600')

        container = tk.Frame(self)
        container.pack()

        self.frames = {}

        for F in (StartpageDutch.StartPageDutch, StartpageEnglish.StartPageEnglish, TicketDutch.TicketDutch, TicketEnglish.TicketEnglish,
                  PayDutch.PayDutch, PayEnglish.PayEnglish, BillingDutch.BillingDutch, BillingEnglish.BillingEnglish):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0)

        self.show_frame("StartPageDutch")


    def show_frame(self, page_name, Data = None):
        """laat het actieve frame zien"""
        frame = self.frames[page_name]
        frame.tkraise()
        frame.Update(Data)


    def Update(self,data):
        print("test")

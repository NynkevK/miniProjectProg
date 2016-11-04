# Geschreven door Mark


import tkinter as tk


class StartPageDutch(tk.Frame):

    def __init__(self, parent, controller):
        """laadt de pagina objecten"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.StartPageView(controller)


    def StartPageView(self, controller):
        """Organiseert het gezicht van de startpagina"""
        self.controller = controller

        frameLeft = tk.Frame(self, bg="#313D4B")
        frameLeft.pack(side="left", fill="both", ipady="240", ipadx="10")

        frameRight = tk.Frame(self, bg="#FF554F", bd="1")
        frameRight.pack(side="right", fill="both", ipady="240", ipadx="40")

        buttonTicket = tk.Button(frameRight, text="Ik wil een uitrijkaart", bg="white", width="24", height="6",
                                 command=lambda: controller.show_frame("TicketDutch"))
        buttonTicket.pack(padx="20", pady="24")

        buttonPay = tk.Button(frameRight, text="Ik wil betalen", bg="white", width="24", height="6",
                              command=lambda: controller.show_frame("PayDutch"))
        buttonPay.pack(padx="26", pady="24")

        languageDutch = tk.Button(frameRight, text="Nederlands", bg="white", width="24", height="2",
                                  command=lambda: controller.show_frame("StartPageDutch"))
        languageDutch.pack(side="top", padx="26", pady="4")

        languageEnglish = tk.Button(frameRight, text="English", bg="white", width="24", height="2",
                                    command=lambda: controller.show_frame("StartPageEnglish"))
        languageEnglish.pack( padx="26", pady="4")

        WelcomeText = tk.Label(frameLeft, text="WELKOM \n"
                                                "BIJ PARKEERGARAGE\n"
                                                "KRUISSTRAAT UTRECHT",
                                   font=("Helvetica", 22), bg="white", fg="#313D4B", height="15", width="42")
        WelcomeText.pack(side="top", pady="10")

        informationText = tk.Label(frameLeft, text="Tarief: 3 euro per uur\n"
                                                   "Open 24/7\n",
                                   font=("Helvetica", 18), bg="#313D4B", fg="white", height="3", width="20")
        informationText.pack(side="top")


    def Update(self,data):
        pass

# Geschreven door Mark


import tkinter as tk
from Database import Database
from GUI import Input
from Billing import Billing


class PayEnglish(tk.Frame):


    def __init__(self, parent, controller):
        """laadt de pagina objecten"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.payViewEnglish(controller)


    def payViewEnglish(self, controller):
        "laat de pagina objecten zien en krijgt veld info op wat de gebruiker in heeft gevoerd"
        self.controller = controller

        frameLeft = tk.Frame(self, bg="white")
        frameLeft.pack(side="left", fill="both", ipady="240", ipadx="114")

        frameRight = tk.Frame(self, bg="#FF554F", bd="1")
        frameRight.pack(side="right", fill="both", ipady="240", ipadx="50")

        informatieLabel = tk.Label(frameLeft, text="Enter you license plate in\n to pay",
                                   font="Helvetica, 14", bg="#313D4B", fg="white")
        informatieLabel.pack(pady="100", ipady="10", ipadx="140")

        frameLeftInput = tk.Frame(frameLeft, bg="#313D4B")
        frameLeftInput.pack(pady="48")


        def pay_format():
            """maakt één invoer veld aan"""
            licensePlateOutput = []

            frame = tk.Frame(frameLeftInput, width="42", bg="white")
            frame.pack(padx="115", pady="80", ipadx="10")

            entry = tk.Entry(frame, width="45", bg="white", fg="#313D4B", relief="flat")
            entry.pack(side="right")

            licensePlateOutput.append(entry)

            return licensePlateOutput

        entries = pay_format()
        sendButton = tk.Button(frameLeftInput, text="SEND", width="40", height="2", bg="#ff554f", fg="white",
                               font="Helvetica, 10", command=(lambda: self.ProcessLicensePlate(entries)))
        sendButton.pack(side="bottom", pady="10")

        sendButton.bind('<Return>', (lambda event: self.ProcessLicensePlate(entries)))

        buttonHome = tk.Button(frameRight, text="Next \n customer", width="24", height="6", bg="white",
                                       command=(lambda: controller.show_frame("StartPageEnglish")))
        buttonHome.pack(padx="10", pady="10")


    def ProcessLicensePlate(self,entries):
        """Database informatie"""
        licensePlate = Input.Input.get(Input.Input, entries)

        if not licensePlate[0]:
            return

        license = Database.Query("SELECT Car.RecordGuid,Is_allowed, Name,Lastname,Email,Account_number FROM Car LEFT JOIN Customer ON Car.RecordGuid = Customer.ref_Car WHERE Car.License_plate = ?",licensePlate[0])

        if not any(license):
            return

        license = license[0]

        if license is not None:
            name = license["name"]
            lastName = license["lastname"]
            email = license["email"]
            accountNumber = license["account_number"]

            if not name or lastName or email or accountNumber:
                #opent billing pagina

                self.controller.show_frame("BillingEnglish",license)

            else:
                print("You will be forwarded!")
                print(Billing.Billing.parkedTime(str(licensePlate)))
        else:
            #error message license plate bestaat niet.
            pass


    def Update(self,data):
        pass

# Geschreven door Mark


import tkinter as tk
from GUI import Input
from  Database import  Database
from Billing import Billing
from tkinter import BOTH, END, LEFT
import uuid
from Email import Document
from Email import Email


class BillingEnglish(tk.Frame):
    _emailInput = None
    _nameInput = None
    _lastNameInput = None
    _billingAccount = None
    #de license plate die geedit word
    _licenseGuid = None
    _informationLabel = None


    def __init__(self, parent, controller):
        """laadt de pagina objecten"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.billingViewEnglish(controller)


    def billingViewEnglish(self, controller):
        """laadt de pagina objecten en ontvangt de entry input"""
        self.controller = controller

        frameLeft = tk.Frame(self, bg="white")
        frameLeft.pack(side="left", fill="both", ipady="240", ipadx="114")

        frameRight = tk.Frame(self, bg="#FF554F", bd="1")
        frameRight.pack(side="right", fill="both", ipady="240", ipadx="50")

        self._informationLabel = tk.Label(frameLeft, text="Fill in your data\n"
                                                   "for automatic facturation ",
                                   font="Helvetica, 14", bg="#313D4B", fg="white")
        self._informationLabel.pack(pady="57", ipady="10", ipadx="120")

        frameLeftInput = tk.Frame(frameLeft, bg="#313D4B")
        frameLeftInput.pack(pady="98")


        def billing_format():
            """format voor de billing invoer velden"""
            billingInput = ["Name:", "Lastname", "E-mail:", "Account Number:"]

            billingOutput = []

            for field in billingInput:
                frame = tk.Frame(frameLeftInput, width="42", bg="white")
                frame.pack(padx="100", pady="10", ipadx="10")

                label = tk.Label(frame, text=field, anchor="w", width="16", bg="white", fg="#313D4B")
                label.pack(side="left")

                entry = tk.Entry(frame, width="30", bg="white", fg="#313D4B", relief="flat")
                entry.pack(side="right")

                billingOutput.append(entry)

            self._nameInput = billingOutput[0]
            self._lastNameInput = billingOutput[1]
            self._emailInput = billingOutput[2]
            self._billingAccount = billingOutput[3]
            return billingOutput


        entries = billing_format()

        sendButton = tk.Button(frameLeftInput, text="SEND", width="40", height="2", bg="#ff554f", fg="white",
                               font="Helvetica, 10", command=(lambda: self.Send(entries)))
        sendButton.pack(side="bottom", pady="10")

        sendButton.bind('<Return>', (lambda event: self.Send(entries)))

        buttonHome = tk.Button(frameRight, text="Next \n customer", width="24", height="6", bg="white",
                                       command=(lambda: controller.show_frame("StartPageEnglish")))
        buttonHome.pack(padx="10", pady="20")


    def Send(self,entries):
        "haalt de text op"
        # TODO iban valideren

        values = Input.Input.get(Input.Input,entries)

        for item in values:
            if not item:
                self.ShowMessage("One or more field \nare incomplete")
                return

        name = self.CreateEmptyIfNone(values[0])
        lastname = self.CreateEmptyIfNone(values[1])
        emailAddress = self.CreateEmptyIfNone(values[2])
        accountnumber = self.CreateEmptyIfNone(values[3])
        recordguid = Database.ParseRecordGuid(self._licenseGuid)
        licenseplate = self.GetLicensePlate(recordguid)

        exists = Database.Query("SELECT RecordGuid FROM Customer WHERE ref_Car = ?",recordguid)

        if any(exists):
            Database.Insert("UPDATE Customer set [Name] = ?, [Lastname] = ?, [Email] = ?, [Account_number] = ? where ref_Car =  ?" , name, lastname, emailAddress, accountnumber, recordguid)
        else:
            Database.Insert("INSERT INTO Customer (Name,Lastname,Email,Account_number,ref_Car) VALUES (?,?,?,?,?)",
                name, lastname, emailAddress, accountnumber, recordguid)
        # self.controller.show_frame("StartPageDutch")
        items = Database.Query("SELECT RecordGuid FROM Park_times WHERE Arrival IS NOT NULL AND Departure IS NOT NULL AND Is_send = 0")

        if not any(items):
            return

        #     factudingesen
        self.ShowMessage("An e-mail will be send!")
        billing = Billing.Billing()
        payment = billing.parkedTime(recordguid)
        print(payment)
        document = Document.EmailDocument()
        documentName = document.CreateDocument(name, licenseplate, payment[1], 3.0, payment[0])
        #TODO Document toevoegen (werkt nog niet helemaal)
        email = Email.SendEmail()
        email.SetSubject("Automatic invoice")
        email.AppendEmail(emailAddress)
        email.SetMessage("In the attachments you will find your invoice")
        email.Send(documentName)

    def CreateEmptyIfNone(self,s):
        if s is None:
            return ''
        return str(s)

    def ShowMessage(self,message):
        if not self._informationLabel:
            return
        if not message:
            return

        self._informationLabel.config(text=message)


    def TryParse(self,value,type):
        try:
            value = type(value)
            return True
        except:
            return False


    def Update(self,data):
        """..."""
        if data is None:
            self.controller.show_frame("PayEnglish")
            return
        self._licenseGuid = self.CreateEmptyIfNone(data["recordguid"])
        self._billingAccount.delete(0,END)
        self._billingAccount.insert(0, self.CreateEmptyIfNone(data["account_number"]))
        self._emailInput.delete(0, END)
        self._emailInput.insert(0, self.CreateEmptyIfNone(data["email"]))
        self._nameInput.delete(0, END)
        self._nameInput.insert(0, self.CreateEmptyIfNone(data["name"]))
        self._lastNameInput.delete(0, END)
        self._lastNameInput.insert(0,self.CreateEmptyIfNone( data["lastname"]))

    def GetLicensePlate(self,recordGuid):
        query = Database.Query("SELECT License_plate FROM Car WHERE RecordGuid = ?",recordGuid)

        if not any(query):
            return None
        # TODO Scalar
        query = query[0]
        return query["license_plate"]
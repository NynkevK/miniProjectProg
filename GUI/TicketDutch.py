import tkinter as tk
from Database import Database
from API import Client
from GUI import Input

class TicketDutch(tk.Frame):
    _informationLabel = None

    def __init__(self, parent, controller):
        """load the page objects"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.TicketViewDutch(controller)

    def TicketViewDutch(self, controller):
        """display the page objects and retrieve entry input"""
        self.controller = controller

        frameLeft = tk.Frame(self, bg="white")
        frameLeft.pack(side="left", fill="both", ipady="240", ipadx="114")

        frameRight = tk.Frame(self, bg="#FF554F", bd="1")
        frameRight.pack(side="right", fill="both", ipady="240", ipadx="50")

        self._informationLabel = tk.Label(frameLeft, text="Vul hier uw kenteken in\n voor een uitrijkaart",
                                   font="Helvetica, 14", bg="#313D4B", fg="white")
        self._informationLabel.pack(pady="100", ipady="10", ipadx="140")

        frameLeftInput = tk.Frame(frameLeft, bg="#313D4B")
        frameLeftInput.pack(pady="53")

        def pay_format():
            """formatteer invoerveld"""
            licensePlateOutput = []

            frame = tk.Frame(frameLeftInput, width="42", bg="white")
            frame.pack(padx="115", pady="80", ipadx="10")

            entry = tk.Entry(frame, width="45", bg="white", fg="#313D4B", relief="flat")
            entry.pack(side="right")

            licensePlateOutput.append(entry)

            return licensePlateOutput

        entries = pay_format()
        sendButton = tk.Button(frameLeftInput, text="VERZEND", width="40", height="2", bg="#ff554f", fg="white",
                               font="Helvetica, 10", command=(lambda: self.ProcessLicensePlate(entries)))
        sendButton.pack(side="bottom", pady="5")

        sendButton.bind('<Return>', (lambda event: self.ProcessLicensePlate(entries)))

        buttonHome = tk.Button(frameRight, text="Volgende \n klant", width="24", height="6", bg="white",
                               command=(lambda: controller.show_frame("StartPageDutch")))
        buttonHome.pack(padx="10", pady="20")

    def ProcessLicensePlate(self,entries):
        """Database informatie"""
        licensePlateValues = Input.Input.get(Input.Input, entries)
        licensePlate = licensePlateValues[0]
        if not licensePlate:
            return

        request = Client.ClientRequest()

        licenseData = request.GetPlateData(licensePlate)

        if licenseData is None:
            return

        if str(licenseData.Fuel).lower().strip() == "diesel":
            if licenseData.DateFirstEntry.year >= 2001:
                self.HandleEntry(licensePlate)
            else:
                self.ShowMessage("Uw auto is niet toegestaan")
        else:
            self.HandleEntry(licensePlate)

    def HandleEntry(self,licensePlate):
        """Check of de auto in de database zit"""
        if not licensePlate:
            return

        query = Database.Query("SELECT Park_times.RecordGuid FROM Park_times INNER JOIN Car ON Car.RecordGuid = Park_times.ref_Car WHERE  Car.License_plate = ? AND Departure is null",licensePlate)
        if any(query):
            Database.Insert(
                "UPDATE Park_times SET Departure = GETDATE() WHERE ref_Car = (SELECT RecordGuid FROM Car WHERE License_plate = ?) AND Departure IS NULL AND Arrival IS NOT NULL",
                licensePlate)
            self.ShowMessage("U bent uitgereden! \n U kunt nu betalen!")
            pass
        else:
            exists = Database.Query("SELECT RecordGuid FROM Car WHERE License_plate = ?",licensePlate)

            if not any(exists):
                Database.Insert("INSERT INTO Car (License_plate,Is_allowed) VALUES (?,1)",licensePlate)
            Database.Insert("INSERT INTO Park_times (Arrival,ref_Car) VALUES (GETDATE(),(SELECT RecordGuid FROM Car WHERE License_plate = ?))",licensePlate)

            self.ShowMessage("U bent ingereden! \n Welkom!")
            pass


    def ShowMessage(self,message):
        """Verander labeltekst"""
        if not self._informationLabel:
            return
        if not message:
            return

        self._informationLabel.config(text=message)


    def Update(self, data):
        """Update frame"""
        pass
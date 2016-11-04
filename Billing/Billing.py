import datetime
from Database import Database


class Billing:
    # Deze functie bepaald het aantal kwartieren dat er geparkeerd is.
    def parkedTime(self, recordGuid):
        query1 = Database.Query('SELECT  Arrival,Departure, Bill FROM dbo.Park_times INNER JOIN dbo.Car ON Car.RecordGuid = Park_times.ref_Car WHERE Car.RecordGuid = ?',recordGuid)

        if not any(query1):
            return

        # todo dit omgezeten naar scalar
        query1 = query1[0]

        if query1["arrival"] == " ":
            arrival = datetime.datetime.strptime("2016-01-01 00:00:00", "%Y-%m-%d %H:%M:%S.%f")
            if query1["departure"] == " ":
                departure = datetime.datetime.strptime("2016-01-01 00:00:00", "%Y-%m-%d %H:%M:%S.%f")
        else:
            arrival = datetime.datetime.strptime(query1["arrival"], "%Y-%m-%d %H:%M:%S.%f")
            departure = datetime.datetime.strptime(query1["departure"], "%Y-%m-%d %H:%M:%S.%f")

        ParkedTime = (str(departure - arrival).split(':'))

        TotalQuarters = (int(ParkedTime[0]) * 4) + (int(ParkedTime[1]) / 15)

        # Hier wordt het te betalen bedrag bepaald.
        if TotalQuarters == 0:
            bill = round(0, 2)
            return bill,(departure - arrival)
        elif TotalQuarters >= 1 and TotalQuarters < 36:
            bill = round(TotalQuarters * 0.75, 2)
            return bill,(departure - arrival)
        elif TotalQuarters > 36:
            bill = round((TotalQuarters * 0.75) + 7.5, 2)   # De bill moet dan uiteindelijk ook worden gewrite naar het CSV file
            return bill,(departure - arrival)


    # Hier wordt de info over de autogebruiker opgehaald uit te database,
    def DriverInfo(self, license_plate):
        query1 = Database.Query('SELECT Name, Lastname, Email FROM CUSTOMER INNER JOIN dbo.Car ON Car.RecordGuid = Customer.ref_Car WHERE Car.License_plate = ?', license_plate)

        # Als er geen data in staat is de query leeg en gebeurt er dus niets mee.
        if not any(query1):
            return

        # todo dit omgezeten naar scalar
        query1 = query1[0]

        name = query1['name'] + " " + query1['lastname']
        email = query1['email']

        return name, email


B = Billing()

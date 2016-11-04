# Geschreven door Mark


from GUI import MainApp
#96-xzf-4
from Database import DatabaseCsv
from API import Client


client = Client
database = DatabaseCsv.Database()


if __name__ == "__main__":
    app = MainApp.MainApplication()
    app.mainloop()

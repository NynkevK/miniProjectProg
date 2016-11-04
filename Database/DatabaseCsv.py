# Omdat database niet werkt (door porten die geblokkeerd zijn)
# Geschreven door Robin


import csv


class Database:


    Data = {}
    _fileName = "Database.csv"
    _columCount = 0
    _colums = []


    def __init__(self,database = "..//Database.csv"):
        "Initieert de database file (colum count etc)"
        self._fileName = database

        with open(self._fileName, "r") as file:
            try:
                self.Data = list(csv.DictReader(file))
            except ValueError:
                pass

        with open(self._fileName, "r") as file:
            try:
                reader = csv.reader(file)
                for item in reader:
                    self._colums = item
                    break
            except ValueError:
                pass


    def Save(self):
        with open(self._fileName, "w") as file:
            writer = csv.DictWriter(file, self._colums)
            writer.writeheader()
            print(self.Data)

            for item in self.Data:
                writer.writerow(item)


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Save()


    def Append(self,data):
        if len(data) < self._columCount:
            return False

        index = self.GetIndex(int(data["Id"]))

        if index is None:
            self.Data.append(self.AppendEmptyValues(data))
            return True

        return False


    #todo dit omzetten naar lamda
    def Delete(self,id):
        index = self.GetIndex(id)

        if index != None:
            self.Data.pop(index)
            return True
        return False


    def Where(self,key,value):
        try:
            for item in self.Data:
                if item[key] == value:
                    return item

        except:
            return None


    def ReadAll(self):
        return self.Data


    #todo dit omzetten naar lamda
    def Read(self,id):
        for item in self.Data:
            if item["Id"] == id:
                return item


    def Update(self,data):
        if len(data) < self._columCount:
            return False

        id = int(data["Id"])
        index = self.GetIndex(id)

        if index is None:
            return False

        newData = self.Data[index]

        for key, value in data.items():
            if key in data:
                newData[key] = value

        self.Data[index] = newData

        return True


    def GetIndex(self,id):
        index = None

        for item in range(0, len(self.Data)):
            if int(self.Data[item]["Id"]) == id:
                index = item
                break

        return index


    def AppendEmptyValues(self,data):
        for key in self._colums:
            if key not in data:
                data[key] = ""

        return data

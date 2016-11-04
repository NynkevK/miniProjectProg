#Robin
import pypyodbc as sql
from Database import ValueParser

#Database connection variables
_driverName = "{SQL Server}"
#Mijn ip niet ddosen plz :)
_HostServer = "84.105.26.219\SQLEXPRESS,1433"
_HostProvider = "ROBIN-DESKTOP\SQLEXPRESS"
_databaseName = 'Project'
_loginName = 'hu'
_loginPassword = 'SuperVeilig!'
_connectionString = str.format('Driver={};Data Source={};Server={};Database={};UID={};PWD={};',_driverName, _HostProvider,_HostServer,_databaseName,_loginName,_loginPassword)

def Query(query,*paramaters):
    "Data word mee gegeven als data = ?"
    # Injection save :)
    con = None


    try:
        #Connect met de database en haalt de data op
        global _connectionString
        con = sql.connect(_connectionString)
        cur = con.cursor()
        cur.execute(query,paramaters)
        data = cur.fetchall()
        #geen data gevonden return
        if data is None:
            return
        # Haalt colum names op
        names = list(map(lambda x: x[0], cur.description))
        #geen namen gevonden return
        if names is None:
            return
        sortedData = []
        #Maakt een list met dictronaries aan met columname:data
        for i in range(0,len(data)):
            value = data[i]
            sorted = {}
            for x in range(0,len(names)):
                name = names[x]
                columValue = value[x]
                sorted[name] = str(columValue).strip()
            sortedData.append(sorted)

        return sortedData
    except ValueError:
        print(ValueError)
    finally:
        #sluit de connectie weer omdat je geen database connectie open heb willen staan
        if con:
            con.close()
    #Wanneer er iets niet goed is gegaan return null
    return None
def Scalar(query,*paramaters):
    "Data word mee gegeven als data = ?"
    # Injection save :)
    con = None
    try:
        #Connect met de database en haalt de data op
        global _connectionString
        con = sql.connect(_connectionString)
        cur = con.cursor()
        cur.execute(query,paramaters)
        data = cur.fetchone()
        #geen data gevonden return
        if data is None:
            return
        # Haalt colum names op
        names = list(map(lambda x: x[0], cur.description))
        #geen namen gevonden return
        if names is None:
            return
        sortedData = []
        #Maakt een list met dictronaries aan met columname:data
        for i in range(0,len(data)):
            value = data[i]
            sorted = {}
            for x in range(0,len(names)):
                name = names[x]
                columValue = value[x]
                sorted[name] = str(columValue).strip()
            sortedData.append(sorted)

        return sortedData[0]
    except ValueError:
        print(ValueError)
    finally:
        #sluit de connectie weer omdat je geen database connectie open heb willen staan
        if con:
            con.close()
    #Wanneer er iets niet goed is gegaan return null
    return None

def Insert(query,*paramaters):
    "Data word mee gegeven als data = ?"
    #Injection save :)
    con = None
    try:
        #Connect met de database en haalt de data op
        global _connectionString
        con = sql.connect(_connectionString)
        cur = con.cursor()
        cur.execute(query,paramaters)
        cur.commit()
    except ValueError:
        print(ValueError)
    finally:
        #sluit de connectie weer omdat je geen database connectie open heb willen staan
        if con:
            con.close()
    #Wanneer er iets niet goed is gegaan return null
    return None


def NonQuery(query):
    "Execure query zonder return value"
    con = None
    try:
        # Connect met de database en haalt de data op
        global _connectionString
        con = sql.connect(_connectionString)
        cur = con.cursor()
        cur.execute(query)
    except ValueError:
        print(ValueError)
    finally:
        # sluit de connectie weer omdat je geen database connectie open heb willen staan
        if con:
            con.close()
    # Wanneer er iets niet goed is gegaan return null
    return None
def ParseRecordGuid(value):
    recordGuid = str(value).replace("'", "").replace("b", "")
    return str(recordGuid)
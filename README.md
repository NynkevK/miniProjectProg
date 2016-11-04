Betaalautomaat Parkeergarage Kruisstraat		Versie 1.0.0 		04-11-2016


--------------------------------------------------------------------------------------------------------------------------------


AUTHORS
Nynke van Koningsveld - 1710479
Esmée Zandvliet - 1683655 
Mark Lanser - 1658950
Robin Tempert - 1698199


--------------------------------------------------------------------------------------------------------------------------------


WHAT IS IT?
Deze applicatie is een simulatie van de parkeergarage aan de Kruisstraat te Utrecht. Auto’s kunnen in- en uitrijden en de bestuurders kunnen hun gegevens invullen voor bijvoorbeeld automatische facturatie. Er zitten een aantal verplichte features in, maar we hebben ook wat extraatjes eraan toegevoegd.


--------------------------------------------------------------------------------------------------------------------------------


FEATURES
Verplicht:
Auto’s herkennen aan hun kenteken bij vertrek en aankomst uit de parkeergarage.
Kentekens opslaan in de database.
Met het kenteken bij het RDW ophalen of de auto hier wel mag parkeren (milieubeleid).
Extra keuze:
Facturatiegegevens klant invoeren en koppelen aan het kenteken, zodat na het parkeren meteen een factuur verstuurd kan worden.


In onze applicatie:
In onze applicatie hebben wij bijna al het bovenstaande kunnen verwerken. Het herkennen van de kentekens moest met een bepaalde module die niemand (zelfs de docenten) werkend kon krijgen. Hiervoor hebben wij dan ook een vrijstelling gekregen en hebben die nu met de hand ingevoerd.
Daarnaast hebben wij gebruik gemaakt van een Microsoft SQL Server database. Hieruit kun je door middel van queries al je info lezen. Als er nog geen gegevens van de klant in de database staan, kan dit erin worden gezet. Je kunt de database dus volledig gebruiken. Dit stond niet in de oorspronkelijke opdracht, maar dit wilden wij toch toevoegen.
Het automatisch factureren werkt ook. Hier is nog iets anders aan verbonden, namelijk het automatisch versturen van een email met onder andere de duur van het parkeren en de kosten. Deze wordt dan naar het emailadres van de klant, zoals deze bij ons in de database bekend is, verstuurd.


--------------------------------------------------------------------------------------------------------------------------------


BUGS
Er is geen failsafe
Nog niet echt andere apartheden kunnen vinden. Naar onze mening werkt de applicatie naar onze tevredenheid.


--------------------------------------------------------------------------------------------------------------------------------


INSTALLS
Wij maken gebruik van een aantal libraries die geïnstalleerd moeten worden zodat de applicatie op een juiste manier werkt.
Requests library (https://github.com/kennethreitz/requests). Deze kan je door middel van een pip-install installeren. Als je deze installeert werkt meteen alles.
SMTP4dev programma (https://smtp4dev.codeplex.com/downloads/get/269147). Met dit programma wordt gebruikt omdat we geen e-mail server hebben en de e-mails alleen lokaal verstuurd kunnen worden. SMTP4dev onderschept deze en laat deze zien.
pypyodbc library (https://github.com/jiangwen365/pypyodbc). Als je dit installeert kan je een connectie maken met een Microsoft SQL Server database, dus werkt onze database connectie.


--------------------------------------------------------------------------------------------------------------------------------

MANUAL
Om de applicatie te starten, moet MainGUI.py gerund worden. Als u de screencast kijkt weet u wel hoe het werkt.


--------------------------------------------------------------------------------------------------------------------------------


MOCK DATA
Er zijn een aantal kentekens die wij zelf in de database hebben moeten zetten, omdat het inlezen niet werkt. U komt vanzelf achter welke bekend zijn en niet. Het gaat om de volgende kentekens:
96-ZXF-4
DB-FB-26
17-TX-FH 
09-TJV-5 
36-TN-HJ
92-HRB-4
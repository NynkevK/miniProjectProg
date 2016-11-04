import time


class EmailDocument:
	# functie pmaken van e-mail
	def CreateDocument(self,name, licensePlate, hours, rate, total):
		fileName = "output.txt"
		text_file = open(fileName, "w")
		text_file.write("Hartelijk dank voor het gebruikmaken van de "
	                    "parkeergarage aan de Kruisstraat.\n")
		text_file.write('{:17}{:10}'.format("\nNaam: ", name))
		text_file.write('{:17}{:10}'.format("\nKenteken: ", licensePlate))
		text_file.write('{:17}{:10}'.format("\nDatum: ", time.strftime('%A %d %B %Y %H:%M', time.localtime())))
		text_file.write("\n")
		text_file.write('\nDuur: {}'.format(hours))
		text_file.write('{:10}{:10}{:1}'.format("\nTarief: ", rate, " euro"))
		text_file.write("\n" + "-"*25)
		text_file.write('{:10}{:10}{:1}'.format("\nTotaal: ", total, " euro"))
		text_file.write("\n")
		text_file.write("\nGelieve dit bedrag binnen 5 werkdagen over te maken op NL16TEST03112016.\n "
		                "\nFijne dag en tot ziens!")
		text_file.close()
		return fileName
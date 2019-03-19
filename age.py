from datetime import date

def calculAage(annee_naissance):	
	date_jour = date.today().year
	age = date_jour - annee_naissance
	return age

def main():
	annee_naissance = input("Enter votre annee de naissance : ")	
	print("{} est {} {}".format("votre age ", calculAage(int(annee_naissance)), "ans"))

main()			
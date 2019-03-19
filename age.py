from datetime import date

def get_age(annee_naissance):	
	date_jour = date.today().year
	age = date_jour - annee_naissance
	return age

def main():
	annee_naissance = input("Enter votre annee de naissance : ")	
	print("{} est {}".format("votre age ", get_age(int(annee_naissance))))

main()			
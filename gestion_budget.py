from tinydb import TinyDB, Query
db = TinyDB('gestion_budget.json')
la_depense = Query() 
le_revenu = Query()
ecart = Query()
# donnons la depense
def la_depense(montant, la_depense):
    la_depense.montant = db.insert(la_depense)
    print("la depense ajoutée avec montant{la_depense.montant}")
    result = db.search(la_depense = [])
    print(result)
    print("la dépense est ajoutées", montant)
    la_depense()
    
   
# donnons le revenu 
def le_revenu(montant, le_revenu):
    le_revenu.montant = db.insert(le_revenu)
    print("le revenu est ajouté avec montant{le_revenu.montant}")
    result = db.search(le_revenu = [])
    print(result)
    print("le revenu est vérifié:", montant)
    le_revenu()
    
#liste  

# donnons la différence qui existe
def ecart(la_depense, le_revenu):
    depense_totale = sum[la_depense]
    revenu_totale = sum[le_revenu]
    ecart = revenu_totale-depense_totale
    results = db.search(ecart = revenu_totale-depense_totale)
    print(results)
    print("la depense totale est:", depense_totale)
    print("le revenu total est :", revenu_totale)
    print("l'ecart est:", ecart)
    return ecart()
   
while True:
    print("       Bonjour comment vous allez ?      ")
    print("                                         ")
    print("   A) Remplissez la dépense")
    print("   C) Consulter le revenu")
    print("   E) Vérifier la difference entre la dépense et le revenu")
    print("   0) quitter l'application")
    choix = input("quel est votre désire:\n")
    if choix == "A" or choix == "a":
        montant = float(input("donnez le montant:"))
        print("la depense est :", montant)
    elif choix == "C" or choix == "c":
        montant = float(input("donnez le montant:"))
        print("le revenu est :", montant)
    elif choix == "E" or choix == "e":
        print("ecart qui existe est de:", la_depense, le_revenu)
        exit()
    elif choix == "0":
        print("Quitter")
        exit()
    else:
        print("votre choix n'est pas reconnu" )
        print(db.all())

            
import model

def izpis_igre(igra):
    tekst = """ 
Število preostalih poskusov: {0} 
Neuspeli poskusi: {1}
    """.format(
        igra.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        igra.stevilo_napak() 
    )
    return tekst

def izpis_zmage(igra):
    tekst = """
###### BRAVO! Uganil si geslo '{0}'######
    """.format(
        igra.geslo
    ) 
    return tekst

def izpis_poraza(igra):
    tekst = """
!!!!!! JOOOOJ! POrabil si vse poskuse. Geslo je '{}' !!!!!!
    """.format(
        igra.geslo
    )

    return tekst

def zahtevaj_vnos():
    return input("Vnesi črko: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        crka = zahtevaj_vnos()
        if len(crka) != 1:
            print(" Ne ne ******")
            continue 

########

igra = model.nova_igra()
print(izpis_igre(igra))
print(izpis_zmage(igra))
print(izpis_poraza(igra))
import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = ' + '
PONOVLJENA_CRKA = ' o '
NAPACNA_CRKA = ' - '
ZMAGA = ' W '
PORAZ = ' X '

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = [] if crke == None else crke

    def napacne_crke(self):
        napacna = []
        for crka in crka:
            if crka not in self.geslo:
                napacna.append(crka)
        return napacna
            
    def pravilne_crke(self):
        pravilna = []
        for crka in crka:
            if crka in self.geslo:
                pravilna.append(crka)
        return pravilna
    
    def stevilo_napak(self):
        return len(napacna)

    def zmaga(self):
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                return True 

    def poraz(self):
        if stevilo_napak() >= 10:
            return True 
        else:
            return False

    def pravilni_del_gesla(self):
        nova_beseda = " "
        for crka in self.geslo:
            if crka in self.crka():
                nova_beseda += crka + " "
            else:
                nova_beseda += " _ "
        return nova_beseda

    def nepravilni_ugibi(self):
        nepravilni_ugibi = " "
        for crka in self.crke:
            if crka in self.napacne_crke():
                nepravilni_ugibi += crka +  " "
        return nepravilni_ugibi
    
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka not in self.geslo:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
        else:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
            
bazen_besed = []
with open('besede.txt', 'r', encoding=' utf-8 ') as f: 
    for vrstica in f:
        bazen_besed.append(vrstica)

def nova_igra():
    return Igra(random.choice(bazen_besed))
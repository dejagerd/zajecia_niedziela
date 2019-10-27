class Czlowiek:
    gatunek = 'human'

    # Konstruktor:
    def __init__(self, imie, nazwisko):
        print("Narodziny nowego czlowieka")
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print("Mam na imie {}".format(self.imie))


marcin = Czlowiek("marcin", "nowak")
marcin.przedstaw_sie()

ania = Czlowiek("Anna", "nowak")
ania.przedstaw_sie()
ania.imie = "Marzena"
ania.przedstaw_sie()




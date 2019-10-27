# Tworzymy nową klasę (szablon)
class Rodzic:
    # atrybuty klasy
    gatunek = 'human'
    kolor_oczu = 'zielone'
 
    # Konstruktor
    # Specjalna metoda, która jest wykonywana w momencie
    # inicjalizacji obiektu (odrysowywania z szablonu)
    # np. marcin = Czlowiek()
    def __init__(self, imie_zadane):
        print("Konstruktor uruchomił się")
        # Moje imię to bedzie to zadane imie
        self.imie = imie_zadane
    def zabawa(self):
        print("Upiłem się")
 
class Dziecko(Rodzic):
    def zabawa(self):
        print('ale fajowo, juhuu!!!')
 
marcin=Rodzic('marcin')
natalia = Rodzic('natalia')
przemus= Dziecko('Przemuś')



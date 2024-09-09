class Film:
    def __init__(self):
        self._tytul=""
        self._lista_wypozyczen=0
    def set_tytul(self, tytul):
        if len(tytul)<=20:
            self._tytul = tytul
        else:
            print("Tytuł nie może mieć więcej niż 20 znaków")
    def get_tytul(self):
        return self._tytul
    
    def get_lista_wypozyczen(self):
        return self._lista_wypozyczen

    def increment_list_wypozyczen(self):
        self._lista_wypozyczen+=1
film=Film()
print("Początkowy tytuł: ", film.get_tytul())
print("Początkow=a liczba zamówień: ", film.get_lista_wypozyczen())
film.set_tytul("Bobobbobob")
print("Tytuł filmu: ",film.get_tytul())

lista_przed = film.get_lista_wypozyczen()
print("Przed wypozyczeniem: ",lista_przed)

film.increment_list_wypozyczen()
liczba_wypozyczeniem_po=film.get_lista_wypozyczen()
print("Po wypoRZyczeniu: ", liczba_wypozyczeniem_po)
# _ =  protected
# __ = private

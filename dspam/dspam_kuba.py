def otworzplik(tekst):
    zawartosc = open(tekst, "r")
    return zawartosc.read()


def dspam_confidence(tekst):
    zawartosc = otworzplik(tekst)
    usun = ["\n", ","]
    for i in zawartosc:
        if i in usun:
            zawartosc = zawartosc.replace(i, " ")

    zawartosc = zawartosc.split(" ")

    print(zawartosc)

    tablica_danych = []

    for i in zawartosc:
        if i == "X-DSPAM-Confidence:":
            indeks = zawartosc.index(i)
            tablica_danych.append(float(zawartosc[(indeks + 1)]))
            zawartosc.pop(indeks)

    print(tablica_danych)

    wynik = (sum(tablica_danych) / len(tablica_danych))

    return round(wynik, 6)


print(dspam_confidence("mejle.txt"))

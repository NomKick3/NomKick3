import time

def plus(tal1, tal2):
    resultat = tal1 + tal2
    return resultat

tal1 = input("Vad är ditt första tal? ")
tal2 = input("Och ditt andra tal? ")

print(plus(float(tal1), float(tal2)))

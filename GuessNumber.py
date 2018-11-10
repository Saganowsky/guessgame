import random

attempt_number = 0 # liczba prob

print("Przedstaw się")
name = input()

computer_number = random.randint(1,20) # generuje losowa liczbe, ktora user bedzie zgadywal
computer_number = int(computer_number)

print("Witaj " + name + ", komputer wylosował Ci liczbę z zakresu 1 - 20. Spróbuj ją odgadnąć")

for attempt_number in range(6): # 6 prob dopoki user nie zgadnie wartosci
    guess_attempt = int(input())

    if guess_attempt > computer_number:
        print("Twoja liczba jest za duża")

    if guess_attempt < computer_number:
        print("Twoja liczba jest za mała")

    if guess_attempt == computer_number:
        print("Trafiłeś")
        break
if guess_attempt == computer_number:
    ("WIN!")
    attempt_number = str(attempt_number + 1)
    print("Udało Ci się po " + attempt_number + " próbach")
else:
    print("Przegrałeś")
    print("Szukana przez Ciebie liczba to " + str(computer_number))

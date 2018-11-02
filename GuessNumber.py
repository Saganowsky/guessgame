import random

attempt_number = 0 # liczba prob

print("Przedstaw się")
name = input()

computer_number = random.randint(1,20) # generuje losowa liczbe, ktora user bedzie zgadywal


print("Witaj " + name + "wybrałem liczbę z zakresu 1 - 20")

for attempt_number in range(6): # 6 prob dopoki user nie zgadnie wartosci
    print("Spróbuj odgadnąć wartość")
    guess_attempt = input()
    

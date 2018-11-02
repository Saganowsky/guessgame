import random

attempt_number = 0

print("Przedstaw się")
name = input()

computer_number = random.randint(1,20)


print("Witaj " + name + "wybrałem liczbę z zakresu 1 - 20")

for attempt_number in range(6):
    print("Spróbuj odgadnąć wartość")
    guess_attempt = input()
    

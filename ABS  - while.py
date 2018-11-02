# value = 0
#
# while value <= 10 :
#     print(str(value) + " dupeczek")
#     value += 1
#

name = input("Podaj Twoje ulubione imię")

while name != "Kasia":
    print("Podano złe imię, próbuj jeszcze raz")
    name = input()

print("W końcu")
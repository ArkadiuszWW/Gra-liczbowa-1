import random
randomNumber = str (random.randint(100,999))
myNumber = input("Wprowadź liczbę od 100 do 999 \n") 
while randomNumber !=997:
    if (randomNumber[0] == myNumber[0]):
      print("HOT")
    elif myNumber[0] in randomNumber:
      print("WARM")
    else:
      print("COLD")

    if (randomNumber[1] == myNumber[1]):
      print("HOT")
    elif myNumber[0] in randomNumber:
      print("WARM")
    else:
      print("COLD")

    if (randomNumber[2] == myNumber[2]):
      print("HOT")
    elif myNumber[0] in randomNumber:
      print("WARM")
    else:
      print("COLD")
    myNumber = input("Wprowadź liczbę od 100 do 999 \n")

#setups
import time
import os
stop1 = False
stop2 = False
life = (3)
score = int(0)


#intro
os.system('clear')
name = input("Hello, user what is your name? ")
print("\n Welcome", name, "to this 5 question quiz about the capital city's of countries around the world")
time.sleep(10)
os.system('clear')

#Question 1
q1 = input("Question 1: What is the capital of Turkey? \n a:Ankara \n b:Istanbul \n c:Izmir \n Your answer: \n")
if q1.upper () == "A":
  print("Well done! " + q1 + " is correct!")
  score = score + 1
  print("Your current score is ", score , " out of 5")
elif q1.upper() == "B" or "C":
  print("Sorry but that answer was wrong")
else:
  print("Sorry I didn't understand that input.")
print("----------------------------------------------------")

#Question 2
q2 = input("Question 2: What is the capital of Poland? \n a:Krakow \n b:Warsaw \n c:Gdansk \n Your answer: \n")
if q2.upper () == "B":
  print("Well done you are correct!")
  score = score + 1
  print("Your current score is ", score , " out of 5")
else:
  print("Sorry but that answer was wrong")
print("----------------------------------------------------")

#Question 3
q2 = input("Question 3: What is the capital of Germany? \n a:Hamburg \n b:Berlin \n c:Köln \n Your answer: \n")
if q2.upper () == "B":
  print("Well done you are correct!")
  score = score + 1
  print("Your current score is ", score , " out of 5")
else:
  print("Sorry but that answer was wrong")
print("----------------------------------------------------")

#Question 4
q3 = input("Question 4: What is the capital of italy? \n a:Moscow \n b:Rome \n c:Berlin \n Your answer: \n")
if q3.upper() == "B":
  print("Well done you are correct!")
  score = score + 1
  print("Your current score is ", score , " out of 5")
else:
  print("Sorry but that answer was wrong")
print("----------------------------------------------------")


#Question 5
while stop2 == False:
  q5 = input("Question 5: What's the capital of the United Kingdom? \n a: London \n b:Portsmouth \n c:Southampton \n  your awnser: \n")
  if q5.upper() == "A":
    print("Well done you are correct!")
    score = score + 1
    print("Your current score is ", score , " out of 5")
    stop2 = True

  elif life == 0 :
    print("Sorry but that answer was wrong")
    stop2 = True

  elif life >1:
    life = life - 1
    print("Sorry but that answer was wrong you have", life ,"reaming")
print("----------------------------------------------------")

#Total
print("\n \n Congratulations", name, "your score", score ,"out of 5")

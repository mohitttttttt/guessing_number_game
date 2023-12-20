import random

def number_checker(guess, number, turns):
  if guess > number:
    print ("Too high")
    return turns - 1
  elif guess < number:
    print ("Too low")
    return turns - 1
  else:
    print (f"You got it. The number was {number}")
    

def set_dificulty():
  if input("Choose difficuty: hard or easy: ")=="hard":
    return 5
  else:
    return 10

def game():
  number_inp = random.randint(1,100)
  print ("Welcome to the guessing game ")
  print("I am thinking of a number between 1 and 100")
  #print (number_inp)
  
  turns = set_dificulty()
  
  guess_inp = 0 
  while guess_inp != number_inp :
    print(f"You have {turns} guesses")
    guess_inp= int(input("Guess a number: "))
    turns = number_checker(guess_inp, number_inp, turns )
    if turns == 0:
      print ("You run out of guesses. You lose")
      return
  
game()
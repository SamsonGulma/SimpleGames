# -*- A Number Positioning Game--: Guessing a Four digit exact Number and Position of those four
# digit number Opponent Player
name = input("Enter your Name: ")
print("While you are playing, Your name will be " + name.upper())
print(" ")
print("Hello" + " " + name.upper() + ", Welcome to Number Position!")
print(""" Before playing, Lets talk about the Rules and the Points""")
print("""    'Rule is first ;-)' -Samson GT
       1. Your input character should be a positive integer not other character like -ve integer, symbols, letters,...!
       2. Your your single digit number to guess should be 1-9 which doesn't include 0 and 10!
          Example: First digit should be 1-9, Tenth digit'ld be 1-9, hundredth digit'ld be 1-9, thousandth'ld be 1-9
       3. The Number that you guess should be 4 digit number 
     Points  
       1. Your point will be handled as per you are correct on guessing the exact number and its position in the digit. 
       2. If you lose the exact number and its position you will lose your points too.
""")
print('''So now let's get into it! :-)
''')

Number = ('3157')
usersGuess = input("Guess a Number: ")

if type(int) == type(usersGuess):
 if Number[0] == usersGuess[0] or Number[0] == usersGuess[1] or Number[0] == usersGuess[2] or Number[0] == usersGuess[3]:
  print("You rock! " + name + "You Guess 1 correct Number and keep guessing, don't lose!")

 elif Number[1] == usersGuess[1] or Number[1] == usersGuess[2] or Number[1] == usersGuess[3]:
  print("You rock! " + name + "You Guess 2 correct number and keep guessing, don't lose!")
 else:
  print("Guess Again!")
else:
    print("Game Over, your input character is not correct. Read the rules again, " + name + " !!!")




import random
name=input("Enter your name: ")
print("Good luck! ",name)
words=['hello','chemistry','rainbow','temple',
       'basket','flowers','ran','house',
       'water','boat','leave','office']
word=random.choice(words)
print("Guess the character")
guesses=''
turns=12
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed+=1
    if failed==0:
        print("you win")
        print("The word is: ", word)
    
    print()
    guess=input("Guess a character:")
    guesses += guess
    if guess not in word:
        turns=turns-1
        print("wrong")
        print("you have",+ turns,'More guesses')
        if turns == 0:
            print("you loose")
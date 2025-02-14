import random
def guess(x):
    random_number=random.randint(1, x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"guess a number between 1 and {x}:"))
        if guess<random_number:
            print("your guess is too low")
        elif guess>random_number:
            print("your guess is too high")
    print(f"yayy!your guess is correct{random_number}")
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low, high)
        else:
            guess=low
        feedback=input(f'is {guess} too high(H) or too low(L) or correct(C)').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"yayyyy! the computer guessed your number,{guess},correctly")
computer_guess(100)
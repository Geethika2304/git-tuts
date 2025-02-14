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
guess(40)
import random
print("welcome to password generator")
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_.,1234567890"
number=input("enter amount of password:")
number=int(number)
length=input("enter the length of password:")
length=int(length)
for i in range(number):
    passwords=''
    for c in range(length):
        passwords+=random.choice(chars)
    print(passwords)

import random

print("welcome to your password generator")

num_of_passwords=int(input("how many passwords do you want to generate:"))

length=int(input("how many charactemrs do you want in your password?:"))
characters="aqwertyuiopsdfghjklzxcvbnQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*_"

print("here are your passwords")
def generatepasswords():
    for pwd in range(num_of_passwords):
        passwords=""
        for security in range(length):
            passwords=passwords+random.choice(characters)

        print(passwords)
        
generatepasswords()


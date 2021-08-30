secret_word = "word"
guess=""
guess_count=0

print("WELCOME TO THE GUESSING GAME,LET US SEE IF YOU CAN GUESS THE WORD OR NOT")
print("hint: try to find the word in the intro of the game. it is known as meaningful combination of alphabets")

while guess != secret_word:
    guess=input("enter the secret word:")
    guess_count=guess_count + 1

if guess == secret_word:
    print("you win")

if guess_count<=5:
    print("it seems like you are really good at this game")

elif guess_count>5:
    print("hmm.. seems like you just need to practice more")    

print("you took " + str(guess_count) + " trial(s) to guess the word")


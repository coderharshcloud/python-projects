print("welcome to the giraffe language translator")



phrase=input("enter a phrase to translate:")

def translate():
    translation=""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            if letter.isupper():
                translation=translation + "G"
            else:     
                translation=translation + "g"
    
        else:
            translation=translation+letter   
            
    return translation


print(translate())
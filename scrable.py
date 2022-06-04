SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
          "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for letter in word:
        total += SCORES[letter]
    return total

w = input("\nType in the word: ")
result = scrabble_score(w)

pl = input("\nAre there any premium letter points? yes/no ")
if pl == "yes":
    anwser = input("double or tripple? ")
    if anwser =="double":
        letters = input("\nType in the letters that should be doubled: ")
        result += scrabble_score(letters)
    elif anwser == "tripple":
        letters = input("\nType in the letters that should be trippled: ")
        result += 2*scrabble_score(letters)

pw = input ("\nAre there any premium word points? yes/no ")
if pw == "yes":
    anwser = input("double or tripple? ")
    if anwser =="double":
        result = 2*result
    elif anwser == "tripple":
        result = 3*result

print("\nTotal number of points for that word is",result,"\n")
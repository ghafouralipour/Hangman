import random
import string

def load_words(file_name):
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    c=0
    for i in lettersGuessed:
        if i in secretWord:
            c+=1
    if c==len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    s=[]
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans=''
    for i in secretWord:
        if i in s:
            ans+=i
        else:
            ans+='_ '
    return ans



def getAvailableLetters(lettersGuessed):

    ans=list(string.ascii_lowercase)
    for i in lettersGuessed:
        ans.remove(i)
    return ''.join(ans)

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long.")
    
    global lettersGuessed
    mistakeMade=0
    lettersGuessed=[]
    
    while 8 - mistakeMade > 0:
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        else:
            print("-------------")
            print("You have",8-mistakeMade,"guesses left.")
            print("Available letters:",getAvailableLetters(lettersGuessed))
            guess=str(input("Please guess a letter: ")).lower()
            
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
                
            elif guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
                
            else:
                lettersGuessed.append(guess)
                mistakeMade += 1
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed))
                
        if 8 - mistakeMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.",secretWord)
            break
        
        else:
            continue


                

if __name__ == "__main__":
    word_list = load_words("words.txt")
    hidden_word = choose_word(word_list).lower()
#     print(hidden_word)
    hangman(hidden_word)

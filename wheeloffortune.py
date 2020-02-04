import random

def prettyprintlist(letterlist): #pretty prints the guessed consonants and vowels
    pretty=""
    for i in letterlist:
        pretty+=i
        pretty+=" "
    return pretty

def randomphrase(PhraseBank): #determines the random phrase and category
    phraseindex=random.randint(0,99)
    phrase=PhraseBank[phraseindex]
    return phrase

def category(PhraseBank,storedphrase): #determines the category given the phrase
    phraseposition=PhraseBank.index(storedphrase)
    if 0<= phraseposition<19:
        category='Before and After'
    elif 20<= phraseposition<39:
        category='Song Lyrics'
    elif 40<= phraseposition<59:
        category='Around the House'
    elif 60<= phraseposition<79:
        category='Food and Drink'
    else:
        category='Same Name'
    return category

def hiddenphrase(storedphrase): #stores phrase hidden from the user
    hidden=""
    for i in storedphrase:
        if i.isalpha():
            hidden+="_"
        if i.isspace():
            hidden+=" "
    return hidden

def isvowel(letter): #boolean test to check if a inputted letter is a vowel)
    if letter.isalpha():
        letter.upper()
        if letter=="A" or letter=="E" or letter=="I" or letter=="O" or letter=="U":
            return True #returns true if the letter is a vowel and false if it is not
        else:
            return False
    else:
        return False

def isconsonant(letter): #boolean test to check if a inputted letter is a consonant
    if letter.isalpha() and len(letter)==1:
        letter=letter.lower()
        if letter!="a" and letter!="e" and letter!="i" and letter!="o" and letter!="u":
            return True #returns true if the letter is a consonant and false if not
        else:
            return False
    else:
        return False

def newphrase(guessedconsonants,guessedvowels,storedphrase,displayedphrase): #this function allows the phrase to be printed with the letters guessed and underscores and spaces appropriately
    index=0
    position=0
    hiddenconsonants=list(storedphrase)
    hiddenvowels=list(storedphrase)
    newdisplayedlist=list(hiddenphrase(storedphrase))
    newdisplayed=""
    if len(guessedconsonants)>0: #uses list of guessedconsonants to check each letter in the storedphrase
        for i in storedphrase:
            while index<len(guessedconsonants):#if the letter is a guessed consonant, it is stored in the list as the consonant, else it is stored as either a space or underscore(unguessed consonant)
                if i.isspace():
                    hiddenconsonants[position]==i
                elif i.isalpha() and guessedconsonants[index]!=i:
                    hiddenconsonants[position]=displayedphrase[position]
                elif guessedconsonants[index]==i:
                    hiddenconsonants[position]=i
                else:
                    hiddenconsonants[position]="_" #note: this list only checks for consonants and not vowels
                index+=1
            index=0
            position+=1
    else:
        hiddenconsonants=hiddenphrase(storedphrase)#if there are no guessed consonants, it returns a list of all spaces and underscores
    position=0
    if len(guessedvowels)>0:#uses list of vowels to check if their are vowels in the storedphrase
        for i in storedphrase:
            while index<len(guessedvowels):#if the letter is a guessed vowel, then it is stored as that vowel in the list, else it is stored as a underscore or space
                if i.isspace():
                    hiddenvowels[position]==i
                elif i.isalpha() and guessedvowels[index]!=i:
                    hiddenvowels[position]=displayedphrase[position]
                elif guessedvowels[index]==i:
                    hiddenvowels[position]=i
                else:
                    hiddenvowels[position]="_"
                index+=1
            index=0
            position+=1
    else:
        hiddenvowels=list(hiddenphrase(storedphrase))
    position=0
    while index<len(newdisplayedlist):#this loop prints the phrase properly with spaces, characters, and underscores
        if isvowel(hiddenvowels[index]): #Since a vowel and consonant can't be in the same list, it selects whatever is present at the position and stores it in the newphrase
            newdisplayedlist[index]=hiddenvowels[index]
        elif isconsonant(hiddenconsonants[index]):
            newdisplayedlist[index]=hiddenconsonants[index]
        elif hiddenvowels[index]== " ":#if the position of the index is a space or there are no consonants or vowels, it stores it as a space or underscore.
            newdisplayedlist[index]=hiddenvowels[index]
        else:
            newdisplayedlist[index]=hiddenvowels[index]
        index+=1
    for letter in newdisplayedlist:
        newdisplayed+=letter
    return newdisplayed

def spinTheWheel(Winnings,storedphrase): #spins the wheel, assigns a letter value, asks input from the user, and gives added winnings
    wheeloutput=[]
    again=True
    consonantcount=0
    uppercasephrase=storedphrase.upper()
    spin=random.randint(1,24)
    if spin==1:#random wheel value according to spin
        wheelvalue=50
    elif 2 <= spin <= 7:
        wheelvalue=100
    elif 8 <= spin <=11:
        wheelvalue=200
    elif 12 <= spin <=14:
        wheelvalue=250
    elif 15 <= spin <=16:
        wheelvalue=500
    elif 17 <= spin <=18:
        wheelvalue=750
    elif spin==19:
        wheelvalue=1000
    elif spin==20:
        wheelvalue=2000
    elif spin==21:
        wheelvalue=5000
    elif spin==22:
        wheelvalue=10000
    else:
        if Winnings<0:# if spin is 23 or 24 Bankrupt and checks if winnings>=0
            wheeloutput+=[""]
            wheeloutput+=[Winnings]
            print("")
            print("You spun a Bankrupt! Your deficit will stay the same")
            print("")
            return wheeloutput
        else:
            wheeloutput+=[""]
            wheeloutput+=[0]
            print("")
            print("You spun a Bankrupt! Your winnings will be reset")
            print("Your turn has ended")
            print("")
            return wheeloutput
    if spin<23: #guessing consonant for wheel value
        print("")
        print("You spun a value of: ",wheelvalue)
        while again:
            letter=input("Guess a consonant: ")
            print("")
            uppercaseletter=letter.upper()
            if isconsonant(letter):
                wheeloutput+=[uppercaseletter]
                for guess in uppercasephrase:
                    if guess==uppercaseletter:
                        consonantcount+=1
                if consonantcount>0:#if the guessed consonant if in the phrase, calculate winnings else subtract winnings
                    addedwinnings=consonantcount*wheelvalue
                    totalwinnings=Winnings+addedwinnings
                    wheeloutput+=[totalwinnings]
                    print(letter.upper(), "appeared",consonantcount,"times in the phrase!")
                    print("You won: $",addedwinnings)
                    print("")
                    again=False
                else:
                    newwinnings=Winnings-wheelvalue
                    wheeloutput+=[newwinnings]
                    print("Sorry...",letter.upper(), "is not in the phrase")
                    print("You lost $",wheelvalue)
                    print("")
                    again=False
            else:
                print(letter.upper(), "is not a consonant")
                print("Please type a single alphabetical character that is not a, e, i, o, or u")
                print("")
    return wheeloutput

def buyAVowel(Winnings, storedphrase): #checks winnings and guessed vowel, then returns new winnings and vowel to add later to list of guessed vowels
    voweloutput=[]
    uppercasephrase=storedphrase.upper()
    vowelcount=0
    moreinput=True
    if Winnings<250:
        voweloutput.append("")
        voweloutput.append(Winnings)
        return voweloutput
    else:
        Winnings-=250
        print("")
        print("$250 dollars have been subtracted from your winnings")
        print("")
        vowel=input("Enter a vowel: ")
        uppervowel=vowel.upper()
        while moreinput:
            if isvowel(uppervowel): #if vowel is in add to list and return true and if the letter is not in the phrase do the converse
                for letter in uppercasephrase:
                    if letter==uppervowel:
                        vowelcount+=1
                vowel.upper()
                if vowelcount>0:
                    print("")
                    print(vowel,"appears in the phrase", vowelcount, "times!")
                    print("")
                else:
                    print("")
                    print(uppervowel,"does not appear in the phrase")
                voweloutput.append(uppervowel)
                voweloutput.append(Winnings)
                moreinput=False
            else:#checks for incorrect input
                print("")
                print(uppervowel, "is not a vowel, please enter a vowel")
                print("Enter a, e, i, o, or u")
                print("")
                vowel=input("Enter a vowel: ")
                uppervowel=vowel.upper()
    return voweloutput

def uppercasenospace(phrase): #takes a phrase and returns a phrase with all characters uppercase and no space
    correctedphrase=""
    upperphrase=phrase.upper()
    for letter in upperphrase:
        if letter.isalpha():
            correctedphrase+=letter
    return correctedphrase

def solveThePuzzle(storedphrase, Winnings):
    response=input("What is the phrase?: ")
    solveoutput=[]
    correctedresponse=uppercasenospace(response)#correctedreponse is the phrase given by user while the storedphrase is the correct phrase stored by the system
    correctedstoredphrase=uppercasenospace(storedphrase)
    if correctedresponse==correctedstoredphrase:#if the phrase is correct return either the amount they won or 0 if the total is less than 0
        print("")
        print("You are correct!")
        Trueanswer=True
        if Winnings>0:
            solveoutput.append(Trueanswer)
            solveoutput.append(Winnings)
        else:
            Winnings=0
            solveoutput.append(Trueanswer)
            solveoutput.append(Winnings)
        return solveoutput
    elif Winnings>=0:# if the guess is wrong, then either reset the winnings to zero or keep it the same if the winnings is negative
        print("")
        print("Sorry that is not correct. Your Winnings will be reset to zero.")
        Winnings=0
        Trueanswer=False
        solveoutput.append(Trueanswer)
        solveoutput.append(Winnings)
        return solveoutput
    else:
        print("")
        print("Sorry that is not correct. Your Winnings will still be $",Winnings)
        Trueanswer=False
        solveoutput.append(Trueanswer)
        solveoutput.append(Winnings)
        return solveoutput

def main():
    print("")
    print("Welcome to the Wheel of Fortune!")
    print("")
    Winnings=0
    PhraseBank= open("phrasebank.txt").read().splitlines() #indexed from 0-99
    storedphrase=randomphrase(PhraseBank) #Correct Phrase hidden from user
    displayedphrase=hiddenphrase(storedphrase)
    displayedcategory=category(PhraseBank,storedphrase)
    stillsolving=True #checks to see if the user is still inputting data when all the letters in the hidden phrase have been guessed
    Gameover=False
    continueturn=True#boolean test for if a user is still inputting an action for the turn while the puzzle is still unsolved
    vowelguesses=0
    consonantguesses=0
    guessedconsonants=[]
    guessedvowels=[]
    correctguess=False
    while Gameover==False:
        print("The Phrase is: ",displayedphrase) #this function displays the status of the round to the user after every action.
        print("The Category is: ",displayedcategory)
        print("")
        print("Consonants Guessed:", prettyprintlist(guessedconsonants))
        print("Vowels Guessed:", prettyprintlist(guessedvowels))
        print("Your current winnings are: $", Winnings)
        print("")
        print(storedphrase)
        if displayedphrase==storedphrase:
            vowelguesses=5
            consonantguesses=21
            if correctguess:
                stillsolving=False
            else:
                print("")
                print("To end the game, you must solve")
                print("")
        action=input("Would you like to spin the Wheel (type 'spin'), Buy a Vowel (type 'vowel'), or  Solve the Puzzle (type 'solve')? ")
        action=uppercasenospace(action)
        while continueturn:
            if action=='SPIN':
                if consonantguesses<21:
                    Displayvalues=spinTheWheel(Winnings, storedphrase)
                    if Displayvalues[0]=="":
                        Winnings=Diplayvalues[1]
                    if Displayvalues[0]!="":
                        guessedconsonants.append(Displayvalues[0])
                        displayedphrase=newphrase(guessedconsonants,guessedvowels,storedphrase,displayedphrase)
                        Winnings=Displayvalues[1]
                        consonantguesses+=1
                    continueturn=False
                elif stillsolving:
                    print("")
                    print("Solve the puzzle")
                    print("")
                    continueturn=False
                else:
                    print("")
                    print("You have guessed all the consonants, either buy a vowel or solve")
                    print("")
                    action=input("Would you like to spin the Wheel (type 'spin'), Buy a Vowel (type 'vowel'), or  Solve the Puzzle (type 'solve')? ")
                    action=uppercasenospace(action)
            elif action=='VOWEL':
                if vowelguesses<5:
                        Displayvalues=buyAVowel(Winnings, storedphrase)
                        if Displayvalues[0]=="":
                            print("")
                            print("You don't have enough money to buy a vowel, please select another action" )
                            print("")
                        if Displayvalues[0]!="":
                            Winnings=Displayvalues[1]
                            guessedvowels.append(Displayvalues[0])
                            displayedphrase=newphrase(guessedconsonants,guessedvowels,storedphrase,displayedphrase)
                            vowelguesses+=1
                        continueturn=False
                elif stillsolving:
                    print("")
                    print("Solve the puzzle")
                    print("")
                    continueturn=False
                else:
                    print("")
                    print("You have guessed all the vowels, either spin the wheel or solve")
                    print("")
                    action=input("Would you like to spin the Wheel (type 'spin'), Buy a Vowel (type 'vowel'), or  Solve the Puzzle (type 'solve')? ")
                    action=uppercasenospace(action)
            elif action=='SOLVE':
                print("")
                Displayvalues=solveThePuzzle(storedphrase, Winnings)
                Winnings=Displayvalues[1]
                if Displayvalues[0]==True:
                    correctguess=True
                continueturn=False
            else:
                print("")
                print("Sorry that is not a valid response, please try again")
                print("")
                action=input("Would you like to spin the Wheel (type 'spin'), Buy a Vowel (type 'vowel'), or  Solve the Puzzle (type 'solve')? ")
                action=uppercasenospace(action)
                print("")
        if correctguess:
            stillsolving=False
        if consonantguesses==21 and vowelguesses==5 and Winnings<=0: #If all the letters have been guessed and the winnings is still less than zero.
            print("Sorry, you have guessed all the letters")
            print("Your Total Winnings for the game is $0")
            print("")
            Gameover=True
        elif consonantguesses==21 and Winnings<=0:
            print("Sorry, you lost")
            print("Your Total Winnings for the game is $0")
            print("")
        elif correctguess and stillsolving==False:#user must solve the puzzel before they end the game, if they spell the phrase wrong, they lose the game
            if Winnings>=0:
                print("Congrats, you have won!!!")
                print("Your Total Winnings for the game is:", Winnings)
                print("Thanks for Playing!")
                print("")
            else:
                print("Congrats, you have guessed the puzzle!!!")
                print("Your Total Winnings for the game is: 0")
                print("Thanks for Playing!")
                print("")
            Gameover=True
        continueturn=True

if __name__ == '__main__':
    main()

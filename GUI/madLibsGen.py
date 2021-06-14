'''
    Mad libs generator with Python gui using tkinter
'''
from tkinter import *
import random

#to display story
def displayStory():
    global win1
    quit(win)
    win1 = Tk()
    win1.title("YOUR STORY")
    frame1 = Frame(win1)
    frame1.pack()
    story = StringVar()
    randomInt = random.randint(1,10)
    story = getStory(str(randomInt))
    L1 = Label(frame1, text = story)
    L1.grid(row=0, column=0, sticky=W)

    submitButton1 = Button(frame1, text="Do It Again!!", width=10, command=switchWindow)
    submitButton1.grid(row=2, column=1, sticky=W)
    win1.mainloop()

#returns random story
def getStory(storyNo):
    noun1Txt = noun1.get()
    nounPTxt = nounP.get()
    noun2Txt = noun2.get()
    noun3Txt = noun3.get()
    placeTxt = place.get()
    adjectiveTxt = adjective.get()
    return {
        '1':  "Be kind to your "+noun1Txt+" -footed "+nounPTxt+"\n For a duck may be somebody`s "+noun2Txt+" \n Be "+ noun3Txt +" to your Legs in "+ placeTxt +" Where the weather is always " + adjectiveTxt + "\n You may think that this is the Knee Brace, Well it is" ,
        '2' : "Be random to your "+noun1Txt+" -footed "+nounPTxt+"\n For a rat may be somebody`s "+noun2Txt+" \n Be "+ noun3Txt +" to your Legs in "+ placeTxt +" Where the weather is not always " + adjectiveTxt + "\n You may think that this is the Knee Brace, Well it is" ,
        '3':  "Be clear to your "+noun1Txt+" -footed "+nounPTxt+"\n For a mice may be somebody`s "+noun2Txt+" \n Be "+ noun3Txt +" to your Legs in "+ placeTxt +" Where the weather is many times " + adjectiveTxt + "\n You may think that this is the Knee Brace, Well it is" ,
        '4' : "Be killer to your "+noun1Txt+" -footed "+nounPTxt+"\n For a goat may be somebody`s "+noun2Txt+" \n Be "+ noun3Txt +" to your Legs in "+ placeTxt +" Where the weather is closly  " + adjectiveTxt + "\n You may think that this is the Knee Brace, Well it is" ,
        '5':  "Be cool to your "+noun1Txt+" -footed "+nounPTxt+"\n For a fort may be somebody`s "+noun2Txt+" \n Be "+ noun3Txt +" to your Legs in "+ placeTxt +" Where the weather is about " + adjectiveTxt + "\n You may think that this is the Knee Brace, Well it is" ,
        '6' : "Be smart to your "+noun1Txt+" -footed "+nounPTxt+"\n For a god may be somebody`s "+noun2Txt+" \n Be "+ noun3Txt +" to your Legs in "+ placeTxt +" Where the weather is slow " + adjectiveTxt + "\n You may think that this is the Knee Brace, Well it is" ,
        '7': "Be free to your "+noun1Txt+" -footed "+nounPTxt+"\n For a creature may be somebody`s "+noun2Txt+" \n Be "+ noun3Txt +" to your Legs in "+ placeTxt +" Where the weather is always " + adjectiveTxt + "\n You may think that this is the Knee Brace, Well it is" ,
        '8' : "Be tough to your "+noun1Txt+" -footed "+nounPTxt+"\n For a animal may be somebody`s "+noun2Txt+" \n Be "+ noun3Txt +" to your Legs in "+ placeTxt +" Where the weather is very well " + adjectiveTxt + "\n You may think that this is the Knee Brace, Well it is" ,
        '9':  "Be Sad to your "+noun1Txt+" -footed "+nounPTxt+"\n For a crow may be somebody`s "+noun2Txt+" \n Be "+ noun3Txt +" to your Legs in "+ placeTxt +" Where the weather is not well " + adjectiveTxt + "\n You may think that this is the Knee Brace, Well it is" ,
        '10' :"Be Happy to your "+noun1Txt+" -footed "+nounPTxt+"\n For a cat may be somebody`s "+noun2Txt+" \n Be "+ noun3Txt +" to your Legs in "+ placeTxt +" Where the weather  may be  " + adjectiveTxt + "\n You may think that this is the Knee Brace, Well it is" ,
    }[storyNo]

def quit(win):
    win.destroy()

def switchWindow():
    quit(win1)
    displayGetWordsScreen()

def switchWindow():
    quit(win1)
    displayGetWordsScreen()

def quit(win):
    win.destroy()

def getRandomNoun(number):
    return {
        '1': 'people'  ,
        '2': 'history' ,
        '3': 'way' ,
        '4': 'art',
        '5': 'world' ,
        '6': 'information',
        '7': 'map' ,
        '8': 'two',
        '9': 'family' ,
        '10': 'government',
    }[number]

def getRandomNounP(number):
    return {
        '1': 'bacteria'  ,
        '2': 'brothers' ,
        '3': 'children' ,
        '4': 'elves',
        '5': 'confetti' ,
        '6': 'phenomena',
        '7': 'tuna' ,
        '8': 'Ninja',
        '9': 'Goods' ,
        '10': 'Pens',
    }[number]

def getRandomPlce(number):
    return {
        '1':'CapeTown' ,
        '2':'Pune',
        '3':'London',
        '4':'Canada',
        '5':'US',
        '6':'Manmad',
        '7':'Chennai',
        '8':'Banglore',
        '9':'Hydrabad',
        '10':'Delhi',
    }[number]

def getRandomAdjective(number):
    return {
        '1':'active',
        '2':'better',
        '3':'junior',
        '4':'nocturnal',
        '5':'precious',
        '6':'plastic',
        '7':'rotten',
        '8':'sympathetic',
        '9':'wrong',
        '10':'webbed',
    }[number]


def resetText():
    randomInt = random.randint(1,10)
    clearEntry(E2)
    E2.insert(0, getRandomNoun(str(randomInt)))
    clearEntry(E3)
    E3.insert(0, getRandomNounP(str(random.randint(1,10))))
    clearEntry(E4)
    E4.insert(0, getRandomNoun(str(random.randint(1,10))))
    clearEntry(E5)
    E5.insert(0, getRandomPlce(str(randomInt)))
    clearEntry(E6)
    E6.insert(0, getRandomAdjective(str(randomInt)))
    clearEntry(E7)
    E7.insert(0, getRandomNoun(str(random.randint(1,10))))

def clearEntry(Entry):
    Entry.delete(0, 'end')

def displayGetWordsScreen():
    global noun1, noun2, nounP, place, noun3, adjective, win, E2, E3, E4, E5, E6, E7
    win = Tk()
    win.title("MAD LIBS")

    frame = Frame(win)
    frame.pack()

    L1 = Label(frame, text="Mad Libs Game")
    L1.grid(row=0, column=0, sticky=W)
    
    L2 = Label(frame, text="NOUN")
    L2.grid(row=1, column=0, sticky=W)
    noun1 = StringVar()
    E2 = Entry(frame, textvariable=noun1)
    E2.grid(row=1, column=1, sticky=W)

    L3 = Label(frame, text="NOUN(PLURAL)")
    L3.grid(row=2, column=0, sticky=W)
    nounP = StringVar()
    E3 = Entry(frame, textvariable=nounP)
    E3.grid(row=2, column=1, sticky=W)

    L4 = Label(frame, text="NOUN")
    L4.grid(row=3, column=0, sticky=W)
    noun2 = StringVar()
    E4 = Entry(frame, textvariable=noun2)
    E4.grid(row=3, column=1, sticky=W)

    L5 = Label(frame, text="PLACE")
    L5.grid(row=4, column=0, sticky=W)
    place = StringVar()
    E5 = Entry(frame, textvariable=place)
    E5.grid(row=4, column=1, sticky=W)

    L6 = Label(frame, text="ADJECTIVE")
    L6.grid(row=5, column=0, sticky=W)
    adjective = StringVar()
    E6 = Entry(frame, textvariable=adjective)
    E6.grid(row=5, column=1, sticky=W)

    L7 = Label(frame, text="NOUN")
    L7.grid(row=6, column=0, sticky=W)
    noun3 = StringVar()
    E7 = Entry(frame, textvariable=noun3)
    E7.grid(row=6, column=1, sticky=W)

    submitButton1 = Button(frame, text="Go Mad!", width=10, command=displayStory)
    submitButton1.grid(row=7, column=1, sticky=W)
    randomButton = Button(frame, text="Totally Random", width= 10, command=resetText)
    randomButton.grid(row=7, column=2, sticky=W)

    win.mainloop()

displayGetWordsScreen()
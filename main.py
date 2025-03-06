##############
# Final project Submition 2
######
### code
## imports
import pygame
import random as r
import pyhelperfunctions as a
import drawmu as d

## defining functions
# choosing invironament
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# sound function
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

# randomly choosing color
def color2():
    list2 = [r.randint(0,255),r.randint(0,255),r.randint(0,255)]
    return list2

# learn function
def learn(wordnumber):
    part = 0
    wordelem = objectlist[0:11]
    for i in range (int(wordnumber)):
        canvas = a.getWhiteImage(400,300)
        photo = a.getImage("images/" + wordelem[part] + ".png")
        d.drawItem(canvas, photo, r.randint(0,100), r.randint(0,100))
        a.showImage(canvas)
        sound = playSound(wordelem[part], ENV)
        input(str(part+1)+ ".Press Enter to continue...")
        part += 1
    return wordnumber

# the play function
def play(choice_number):
    print("PLAY")
    print("This is a seek and find game. You will hear a word.\nCount how many of that item you find!")
    num_rounds = int(input("How many rounds would you like to play? "))
    # create a challenge list of 3 words that the user learned
    # use the random.shuffle() for no repeated words
    # ask how many can they see
    objectlistlearned = objectlist[0:choice_number]
    for n in range(0,num_rounds):
        input("press enter to continue")
        num_item = r.randint(1,4)
        r.shuffle(objectlistlearned)
        item1 = objectlistlearned[0]
        canvasT = a.getWhiteImage(400,300)
        a.showImage(canvasT)
        imgT = a.getImage("images/" + item1 + ".png")
        # do color and mirror here
        colorT = color2()
        imgT = d.recolorImage(imgT,colorT)
        minimum_random = r.randint(0,1)
        if minimum_random != 1:
            imgT = d.minify(imgT)
            imgT = d.mirror(imgT)
        rec = d.distributeItems(canvasT,imgT,num_item)
        a.showImage(rec)
        itemlist2 = objectlistlearned[1:choice_number]
        for it in itemlist2:
            num_items = r.randint(1,4)
            colorT2 = color2()
            imgT2 = a.getImage("images/" + it + ".png")
            # do color and mirror here
            imgT2 = d.recolorImage(imgT2,colorT2)
            minimum_random2 = minimum_random
            if minimum_random2 != 1:
                imgT2 = d.minify(imgT2)
                imgT2 = d.mirror(imgT2)
            rec2 = d.distributeItems(canvasT,imgT2,num_items)
            a.showImage(rec2)
        # display sound (call playSound)
        sound = playSound(item1,ENV)
        # ask the user
        num_ans = int(input("Listen to the word. How many of them can you find? "))
        if num_ans == num_item:
            print("Right! Press Enter to continue.")
        else:
            print("Sorry, your answer is worng. Good luck next time.")


## reading the excel file
file = open("blackfoot.csv")
unneeded_header = file.readline()

# construct list here
objectlist = []
for line in file:
    object_data = line.strip("\n").split(",")
    items = object_data[0]
    objectlist += [object_data[0]]

## starting the program
ENV = initEnv()
mini_ran = [0,1,2,3,4,5,6,7,8,9,10]
app = 0
playn = 0
settingreply = 3
while app == 0:
    # inserting menu
    main_menu = ["1. Learn - Word Flashcards","2. Play - Seek and Find Game","3. Settings - Change difficulty","4. exit"]
    print("\nMAIN MENU")
    for main in main_menu:
        print(main)
    choice = input(str(("choose an option: ")))

    if choice == "1":
        learn(settingreply)

    # instructions for the game
    if choice == "2":
        while playn == 0:
            play(settingreply)
            #play(3)
            playn += 1

    if choice == "3":
        settingreply = int(input("How many words would you like to learn (3-12)?"))
        if settingreply <3 or settingreply >12:
            print("Sorry, that's not a valid number. Resetting to 3 words.")
            settingreply = 3

    if choice == "4":
        app += 1
        print("Goodbye")
# the end of the app


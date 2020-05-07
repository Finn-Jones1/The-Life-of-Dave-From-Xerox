# Importing dependencies 
import time, sys, pygame, random, os
from pygame import mixer

# Variables
lphaseCount = 0
health = 100
lhealth = 100
ans = ''

# This is defining a flexable path so that code won't break when used on other computers
FlexyPath = os.path.dirname(os.path.abspath(__file__))

# This is loading any saves
f=open(FlexyPath + "/data.txt", "r")
contents = f.read()
f.close()
Scontents = contents.split()
if contents != "0 0":
    lphaseCount = Scontents[0]
    lhealth = Scontents[1]
else:
    f = open(FlexyPath + '/data.txt','w')
    f.write("0 100")
    f.close()
powerUP = 0


# Initalising pygame mixer and defining sounds and music
mixer.init()
music = pygame.mixer.music.load(FlexyPath + "/ThemeSong.wav")

# sad = pygame.mixer.Sound(FlexyPath+ "/asd.wav")
alarm = pygame.mixer.Sound(FlexyPath+ "/Alarm.wav")
musicBattle = pygame.mixer.Sound(FlexyPath + "/Battle.wav")
musicBossBattle = pygame.mixer.Sound(FlexyPath + "/FinalBossFight.wav")

# Setting music volume and playing main theme song
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# Functions

# This function simulates typing so that the text on screen looks semi natural and more interesting
def GameText(text):
    for letter in (text):
        rand = random.uniform(0.001, 0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(rand)
    print("")

# Prints Game Over in slow red text also resets saves
def GameOver():
    for letter in (u"\u001b[31mGame Over\u001b[0m"):
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    f = open(FlexyPath + '/data.txt','w')
    f.write("0 100")
    f.close()
    exit()

# Prints You Died in slow red text also resets saves
def YouDied():
    for letter in (u"\u001b[31mYou Died\u001b[0m"):
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    f = open(FlexyPath + '/data.txt','w')
    f.write("0 100")
    f.close()
    exit()

# This function saves your progress during the game (AutoSave)
def save():
    f = open(FlexyPath + '/data.txt','w')
    f.write(str(lphaseCount)+ " " + str(lhealth))

# This function creates a little loading animation
def loading():
    print ("Loading...")
    for i in range(0, 100):
        time.sleep(0.05)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    
# This function is used to change the health value depending on what the damage value is set to
def healthUpdate(damage):
    global lhealth
    lhealth = int(lhealth) + int(damage)
    save()
    GameText(u"\u001b[32mYour health is now "+  str(lhealth)+ " HP\u001b[0m")
    
    if lhealth <= 0:
        save()
        YouDied()
        

# This function clears the console
def clear():
    os.system('clear')

# This function is the shop where you can get upgrades
def shop():
    buy = ''
    loopS = 1
    global powerUP
    powerUP = 0
    while loopS == 1:
        GameText(u"\u001b[35mShop\u001b[0m")
        GameText(u"\u001b[33m1. Rewind\u001b[0m")
        GameText(u"\u001b[24m2. Wrench\u001b[0m")
        GameText(u"\u001b[36;1m3. Potato\u001b[0;0m")
        GameText(u"\u001b[35m1, 2, 3 or exit:")
        buy = input("\u001b[0m")

        if buy == "1":
            GameText(u"\u001b[35mYou Now Have Rewind\u001b[0m")
            GameText(u"\u001b[35mDescription: At the end of a scene you can choose if you want to restart the phase or not.\u001b[0m")

            
            powerUP = 1
            time.sleep(2)
            loopS = 2
        elif buy == "2":
            GameText(u"\u001b[35mYou Now Have Wrench\u001b[0m")
            GameText(u"\u001b[35mDescription: If you use the wrench in a copier battle, you will get one extra copy giving you the advantage and also any tiebreaker will go your way.\u001b[0m")

            powerUP = 2
            time.sleep(2)
            loopS = 2
        elif buy == "3":
            GameText(u"\u001b[35mYou now have a Potato\u001b[0m")
            GameText(u"\u001b[35mDescription: The potato falls onto the ground and grows into a potato plant\u001b[0m")
            GameText(u"\u001b[35mDescription: The potato thanks you for letting it grow and gives you 20HP\u001b[0m")
            healthUpdate(20)

            powerUP = 3
            time.sleep(2)
            loopS = 2
        elif buy == "exit":
            loopS = 2
    
    clear()
    return powerUP

# This function will find out how many copies your opponent will make in the printer battle
def chalengerPBattle(ChallengerSpeed, copyTime):
    global ls
    ls = []
    loopPB = 1
    randCSpeed1 = 0
    while loopPB == 1:
        L = ChallengerSpeed - 1
        H = ChallengerSpeed + 1
        randCSpeed = random.uniform(L, H)
        randCSpeed1 = randCSpeed1 + randCSpeed
        ls.append(randCSpeed)
        if randCSpeed1 > copyTime:
            loopPB = 0

# This is where printer battles can be created. You can change the amount of time you get to copy the opponents copy speed and the name of the opponent all in this function
def Printerbattle(copyTime, ChallengerName, ChallengerSpeed):

    copyCount = 0
    loopa = 1
    
    chalengerPBattle(ChallengerSpeed, copyTime)
    # Checking For Powerful
    if powerUP == 2:
        GameText(u"\u001b[32mWould You like to use your wrench (Y/N)\u001b[0m")
        ans = input("")
        ans = ans.lower()
        if ans == "y":
            copyCount = copyCount + 1

    GameText(u"\u001b[32m3\u001b[0m")
    time.sleep(1)
    GameText(u"\u001b[32m2\u001b[0m")
    time.sleep(1)
    GameText(u"\u001b[32m1\u001b[0m")
    time.sleep(1)
    print(u"\u001b[32mGO!\u001b[0m")
    start = time.time()
    clear()
    while loopa == 1:
        
        # Starting Game
        update = time.time()
        if update - start < copyTime:
            print(u"\u001b[32mTime Elapsed: "+ str("%.2f" %(time.time() - start)) +"\u001b[0m")
            typeTimeS = time.time()
            copy = input("")
            copy = copy.lower()

            if copy != 'copy':
                GameText(u"\u001b[32mPaper Jam\u001b[0m")
                loading()
                print("")
                clear()
            else:
                copyCount = copyCount + 1
                typeTimeE = time.time()
                
                print(u"\u001b[32mSpeed: "+ str("%.2f" %(typeTimeE - typeTimeS)) +"\u001b[0m")
                clear()
        else:
            loopa = 0


    lenLS = 0
    lenLS = len(ls)
    # Tie Breaker
    if len(ls) == copyCount:
        if ans == "y":
            copyCount = copyCount + 1
        else:
            ran = random.randint(2, 5)
            if ran == 3:
                lenLS = lenLS - 1
            elif ran == 4:
                lenLS = lenLS + 1

    # Who Is The Winner?
    time.sleep(3)
    print("")
    global winner
    GameText(u"\u001b[35mThe Scores Are In\u001b[0m")
    GameText(u"\u001b[35m" + ChallengerName +" Made "+ str(lenLS) +" Copies\u001b[0m")
    GameText(u"\u001b[35mYou Made "+ str(copyCount) +" Copies\u001b[0m")
    if lenLS > copyCount:
        winner = "challenger"
        GameText(u"\u001b[33m" + ChallengerName + " Wins\u001b[0m")
    if lenLS < copyCount:
        winner = "you"
        GameText(u"\u001b[33mYou Win\u001b[0m")




# How To Play

def H2P():
    GameText(u"\u001b[32mThis is\u001b[0m")
    GameText(u"\u001b[32mLife of Dave from Xerox\u001b[0m")
    GameText(u"\u001b[32mYou Start with 100HP\u001b[0m")
    GameText(u"\u001b[32mThis game is about a guy who is down on his luck and is trying to get through life\u001b[0m")
    GameText(u"\u001b[32mThe aim of the game is to make your way from Janitor to Ceo at Xerox by defeating people in copier battles without letting your HP get to 0\u001b[0m")
    GameText(u"\u001b[32mIf you quit the game you will lose your powerups and need to get them back from the shop\u001b[0m")
    GameText(u"\u001b[32mPress Enter To Start\u001b[0m")
    input("")
    clear()
    
# The first part of the game 
def phase1():
    clear()
    global lphaseCount
    lphaseCount = 1
    global powerUP
    save()
    alarm.play()
    GameText(u"\u001b[32mYou wake up to the sound you have grown to hate\u001b[0m")
    GameText(u"\u001b[32mThe alarm clock\u001b[0m")
    clear()
    
    ans = ''
    while ans != "punch" or ans != "wake":
        GameText(u"\u001b[32mDo you (Punch) the alarm clock or do you (Wake) up:\u001b[0m")
        ans = input()
        ans = ans.lower()
        if ans == "punch":
            clear()
            GameText(u"\u001b[32mYou get electrocuted\u001b[0m")
            healthUpdate(-50)
            clear()
            GameText(u"\u001b[32mYou say 'Screw This!' and you go back to bed\u001b[0m")
            GameText(u"\u001b[32mYou wake up to the sound of your phone ringing\u001b[0m")
            GameText(u"\u001b[32mYou pick up the phone it's your boss. It is your fourth time you have forgotten to come into work and your boss says...\u001b[0m")
            GameText(u"\u001b[32mDAVE YOU ARE SUCH AN IDIOT! DON'T COME INTO XEROX EVER AGAIN!\u001b[0m")
            GameText(u"\u001b[32mThen suddenly you feel a strong pain coming from your chest. The electricity has caused your heart beat to become irregular.\u001b[0m")
            GameText(u"\u001b[32mYour bosses sudden yelling has caused you to go into cardiac arrest\u001b[0m")
            GameText(u"\u001b[32mThen suddenly your heart stops.\u001b[0m")
            print("")
            if powerUP == 1:
                clear()
                powerUP = 0
                GameText(u"\u001b[32mWould You like to use rewind Y/N\u001b[0m")
                ans = input("")
                ans = ans.lower()
                if ans == "y":
                    GameText(u"\u001b[32mRewinding Please Wait\u001b[0m")
                    loading()
                    clear()
                    f = open(FlexyPath + '/data.txt','w')
                    f.write("1 100")
                    f.close()
                    phase1()
            YouDied()
        elif ans == "wake":
            clear()
            rand = random.randrange(5, 9)
            GameText(u"\u001b[32mYou wake up and check the time your watch reads "+ str(rand) +":00\u001b[0m")
            if rand > 7:
                while ans != "breakfast" or ans != "leave":
                    GameText(u"\u001b[32mYou are running late, should you eat (Breakfast) or (Leave) without breakfast?\u001b[0m")
                    ans = input("")
                    ans = ans.lower()
                    if ans == "breakfast":
                        clear()
                        GameText(u"\u001b[32mYou eat breakfast and gain 20 health but you are now running 20 minutes late\u001b[0m")
                        healthUpdate(20)
                        GameText(u"\u001b[32mWhen you get to work you look at the time and you are 40 minutes late\u001b[0m")
                        GameText(u"\u001b[32mYour boss walks up to you and says 'I have never seen a more idiotic, indifferent worker in my life. You are FIRED'\u001b[0m")
                        GameOver()
                    elif ans == "leave":
                        clear()
                        GameText(u"\u001b[32mYou skip breakfast and go straight to work and you just make it on time.\u001b[0m")
                        GameText(u"\u001b[32mYou grab your mop and start cleaning\u001b[0m")
                        GameText(u"\u001b[32mYou finish your work at 5:00pm and you go home and flop onto your bed.\u001b[0m")
                        phase1()
            else:
                clear()
                while ans != "breakfast" or ans != "leave":
                    GameText(u"\u001b[32mYou are on schedule. Should you eat (Breakfast) or (Leave) without breakfast?\u001b[0m")
                    ans = input("")
                    ans = ans.lower()
                    if ans == "breakfast":
                        clear()
                        GameText(u"\u001b[32mYou eat breakfast and gain 20 health and you get to work on time\u001b[0m")
                        healthUpdate(20)
                        
                        GameText(u"\u001b[32mYou grab your mop and start cleaning\u001b[0m")
                        GameText(u"\u001b[32mYou finish your work at 5:30 and you go home and flop onto your bed.\u001b[0m")
                        phase1()
                    elif ans == "leave":
                        clear()
                        GameText(u"\u001b[32mYou skip breakfast and go straight to work. You are early by 10 minutes which makes a good impression on your boss.\u001b[0m")
                        GameText(u"\u001b[32mI like to see a dedicated worker, have you ever done printer maintenance before?\u001b[0m")
                        GameText(u"\u001b[32mYou respond with 'I am fairly handy and printers can't be too hard'\u001b[0m")
                        GameText(u"\u001b[32mOk then it's settled. You will challenge Josh in an hour for the job of printer maintenance with a copier battle!\u001b[0m")
                        time.sleep(2)
                        GameText(u"\u001b[32mAn hour passes.\u001b[0m")
                        GameText(u"\u001b[32mYou are extremely nervous as you approach the photo copier\u001b[0m")
                        GameText(u"\u001b[32mYour boss says 'You will need to make as many copies as possible by typing the word (copy) and pressing enter in 20 seconds'\u001b[0m")
                        time.sleep(2)
                        # Battle start and battle music start
                        pygame.mixer.music.stop()
                        musicBattle.play(-1)
                        Printerbattle(20, "Josh", 3)
                        pygame.mixer.pause()
                        pygame.mixer.music.set_volume(0.3)
                        pygame.mixer.music.play(-1)

                        if winner == "you":
                            time.sleep(1)
                            clear()
                            GameText(u"\u001b[32mJosh looks down with a depressed look on his face and leaves the room\u001b[0m")
                            GameText(u"\u001b[32mYou now have Josh's job\u001b[0m")
                            phase2()
                        if winner == "challenger":
                            time.sleep(1)
                            clear()
                            GameText(u"\u001b[32mJosh jumps and punches the air\u001b[0m")
                            GameText(u"\u001b[32mYou are sad but you expected this outcome\u001b[0m")
                            GameText(u"\u001b[32mYou walk home and go to bed\u001b[0m")
                            time.sleep(1)
                            phase1()


# Second part of the game
def phase2():
    clear()
    global lphaseCount
    lphaseCount = 2
    save()
    GameText(u"\u001b[32mYour spirits are high and you are happy\u001b[0m")
    GameText(u"\u001b[32mYour boss leads you to the printer maintenance door and says 'I will leave you here. The guys inside will tell you what you need to do.'\u001b[0m")
    ans = ''
    while ans != "open" or ans != "limber up":
        GameText(u"\u001b[32mYou have a choice to (limber up) before opening the door or you can just (open) the door\u001b[0m")
        ans = input("")
        ans = ans.lower()
        if ans == "limber up":
            clear()
            GameText(u"\u001b[32mYou enter the room and walk towards the desk where the head of maintenance sits. Everyone is staring at you the 'new guy'.\u001b[0m")
            GameText(u"\u001b[32mThe your boss says \u001b[0m")
        elif ans == "open":
            clear()
            if int(lhealth) < 70:
                GameText(u"\u001b[32mYou decided to wear thongs to work today and there was a lip on the door frame that you stub your toe on.\u001b[0m")
                healthUpdate(-50)
                
        GameText(u"\u001b[32mYou enter the room and walk towards the desk where the head of maintenance sits. Everyone is staring at you the 'new guy'.\u001b[0m")
        GameText(u"\u001b[32mWhen you get to the desk he says\u001b[0m")
        GameText(u"\u001b[32m'My name is James, here's the deal I already don't like you because you replaced Josh now he has to work as a janitor and his pay was halved'\u001b[0m")
        GameText(u"\u001b[32mYou find his tone rude and unfair\u001b[0m")

        
        ans = ""
        while ans != "say" or ans != "leave it":
            GameText(u"\u001b[32mDo you (say) something or (leave it) alone.\u001b[0m")
            ans = input("")
            ans = ans.lower()
            if ans == "say":
                clear()
                GameText(u"\u001b[32mJames stands up and says 'OH YEAH'\u001b[0m")
                while ans != "y" or ans != "n":
                    GameText(u"\u001b[32m'WANA GO MATE'(Y/N)\u001b[0m")
                    ans = input("")
                    ans = ans.lower()
                    if ans == "y":
                        clear()
                        GameText(u"\u001b[32mYou respond with 'HEll YES'\u001b[0m")
                        GameText(u"\u001b[32mJames then winds up and punches you square in the face and you fall to the ground and pass out.\u001b[0m")
                        healthUpdate(-70)
                        GameText(u"\u001b[32mWhen you are passed out on the ground, your boss decides to demote you back to janitor.\u001b[0m")
                        time.sleep(2)
                        GameText(u"\u001b[32mYou trudge home and go to bed.\u001b[0m")
                        time.sleep(2)
                        phase1()
                    elif ans == "n":
                        clear()
                        GameText(u"\u001b[32mYou say 'I don't want any trouble sorry.'\u001b[0m")
                        GameText(u"\u001b[32mYou still seem to have provoked him\u001b[0m")
                        GameText(u"\u001b[32mJames then winds up and punches you square in the face and you fall to the ground and pass out.\u001b[0m")
                        healthUpdate(-70)
                        GameText(u"\u001b[32mWhen you are passed out on the ground your boss deides to demote you back to janitor.\u001b[0m")
                        time.sleep(2)
                        GameText(u"\u001b[32mYou trudge home and go to bed.\u001b[0m")
                        time.sleep(2)
                        phase1()
            elif ans == "leave it":
                clear()
                GameText(u"\u001b[32mJames then says 'follow me' and you walk over to a printer. James says that this is one of their most used matchines and runs you through some troubleshooting routines and how to use it.\u001b[0m")
                GameText(u"\u001b[32mThis guy continues to be condesending so you decide to do something but this time you go over his head.\u001b[0m")
                GameText(u"\u001b[32mYou are going to confront the CEO of Xerox John Visentin.\u001b[0m")
                

                while ans != "call" or ans != "walk":
                    GameText(u"\u001b[32mYou have a choice to (walk) to his office or to (call) John Visentin.\u001b[0m")
                    ans = input("")
                    ans = ans.lower()
                    if ans == "call":
                        clear()
                        GameText(u"\u001b[32mYou don't have his phone number...you're not that important.\u001b[0m")
                    elif ans == "walk":
                        clear()
                        GameText(u"\u001b[32mYou leave the room and realise that Xerox is like a huge, white grid with no signs and you have no idea how to get to the CEO's office.\u001b[0m")
                        while ans != "call" or ans != "walk":
                            GameText(u"\u001b[32mWould You like to go (forward) (left) or (right)\u001b[0m")
                            save()
                            ans = input("")
                            ans = ans.lower()                
                            if ans == "right":
                                clear()
                                GameText(u"\u001b[32mWould You like to go (forward) (left) or (right)\u001b[0m")
                                ans = input("")
                                ans = ans.lower()
                                if ans == "left":
                                    clear()
                                    GameText(u"\u001b[32mWould You like to go (forward) (left) or (right)\u001b[0m")
                                    ans = input("")
                                    ans = ans.lower()
                                    if ans == "forward":
                                        clear()
                                        # battle scene start and final boss battle music start
                                        pygame.mixer.music.stop()
                                        musicBossBattle.play()
                                        GameText(u"\u001b[32mYou finally make it to the CEO's office and you fling the door open saying 'John I have had it with with head of printer maintenance and would like to be moved to a knew branch of Xerox'\u001b[0m")
                                        GameText(u"\u001b[32mJohn Visentin swivels around in his executives chair and says 'You know what, why don't you copier battle me if you think you are so great!'\u001b[0m")
                                        GameText(u"\u001b[32mYou can here gasps coming from the hallway and people running into the room.'\u001b[0m")
                                        GameText(u"\u001b[32mYou start to shake. You have never been under more pressure in your life\u001b[0m")
                                        GameText(u"\u001b[32mYou respond with 'So John what are the stakes?'\u001b[0m")
                                        GameText(u"\u001b[32mJohn says 'If you win, you take my job. If I win, you are fired on the spot'\u001b[0m")
                                        GameText(u"\u001b[32mYou then say 'OK DEAL'\u001b[0m")
                                        time.sleep(2)
                                        clear()
                                        # Final printer battle start
                                        Printerbattle(40, "John Visetin", 2)

                                        if winner == "you":
                                            GameText(u"\u001b[32mJohn falls down to his knees and you see a tear roll down his cheek\u001b[0m")
                                            GameText(u"\u001b[32mYou call the guards into the room and say 'Take him away we have no room for losers here at Xerox'\u001b[0m")
                                            GameText(u"\u001b[32m...\u001b[0m")
                                            GameText(u"\u001b[32mThe End\u001b[0m")
                                            GameText(u"\u001b[32mThis game was made by Finn Jones\u001b[0m")
                                            GameText(u"\u001b[32mThanks For Playing\u001b[0m")
                                            f = open(FlexyPath + '/data.txt','w')
                                            f.write("0 100")
                                            f.close()
                                            exit()
                                        elif winner == "challenger":
                                            GameText(u"\u001b[32mJohn Visetin starts to walk towards you and says 'GAME OVER'\u001b[0m")
                                            GameText(u"\u001b[32mHe then says 'Guards escort this man out of the building please'\u001b[0m")
                                            GameText(u"\u001b[32mThe guards grab your arms and you slowly start to get dragged out of the building\u001b[0m")
                                            GameOver()
                                            clear()
                                    else:
                                        clear()
                                        GameText(u"\u001b[32mYou walk into a wall and lose 10HP\u001b[0m")
                                        healthUpdate(-10)
                                        
                                else:
                                    clear()
                                    GameText(u"\u001b[32mYou walk into a wall and lose 10HP\u001b[0m")
                                    healthUpdate(-10)
                                    
                            else:
                                clear()
                                GameText(u"\u001b[32mYou walk into a wall and lose 10HP\u001b[0m")
                                healthUpdate(-10)
                                
                                    



# Find out what section you are up to and start from there.
if lphaseCount == 0 or lphaseCount == "0":
    H2P()
    shop()
    phase1()
elif lphaseCount == 1 or lphaseCount == "1":
    shop()
    phase1()
elif lphaseCount == 2 or lphaseCount == "2":
    # shop()
    phase2()
import time, sys, pygame, random, os
from pygame import mixer

# Variables
phaseCount = 0
health = 100
careerP = 1

FlexyPath = os.path.dirname(os.path.abspath(__file__))

f=open(FlexyPath + "/data.txt", "r")
contents = f.read()
f.close()
print(contents)
contents = contents.split()
print(contents)
if contents != []:
    phaseCount = contents[0]
    health = contents[1]
else:
    f = open(FlexyPath + '/data.txt','w')
    f.write("0 100")

powerUP = 0

f = open(FlexyPath + '/data.txt','w')
f.write(str(phaseCount)+ " " + str(health))

# contents = f.read()
# print(contents)

FlexyPath = os.path.dirname(os.path.abspath(__file__))
# Music/Sound Effects

mixer.init()


alarm = pygame.mixer.Sound(FlexyPath+ "/Alarm.wav")
music = pygame.mixer.music.load(FlexyPath + "/ThemeSong.wav")

musicBattle = pygame.mixer.Sound(FlexyPath + "/Battle.wav")
musicBossBattle = pygame.mixer.Sound(FlexyPath + "/FinalBossFight.wav")

# musicBossBattle.play(-1)

pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

def GameText(text):
    for letter in (text):
        rand = random.uniform(0.001, 0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(rand)
    print("")

#Functions
def GameOver():
    for letter in (u"\u001b[31mGame Over\u001b[0m"):
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

def YouDied():
    for letter in (u"\u001b[31mYou Died\u001b[0m"):
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

def loading():
    print ("Loading...")
    for i in range(0, 100):
        time.sleep(0.05)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()

    
def healthUpdate(damage):
    global health
    health = health + damage
    GameText(u"\u001b[32mYour health is now "+  str(health)+ " HP\u001b[0m")
    if health <= 0:
        YouDied()
        exit()

def CareerUpdate(career):
    global careerP
    careerP = careerP + career
    if careerP == 0:
        GameOver()
        exit()





def clear():
    time.sleep(0.5)
    os.system('clear')


def shop():
    buy = ''
    loopS = 1
    global powerUP
    powerUP = 0
    while loopS == 1:
        GameText(u"\u001b[35mShop\u001b[0m")
        GameText(u"\u001b[33m1. Rewind 50HP\u001b[0m")
        GameText(u"\u001b[24m2. Wrench 50HP\u001b[0m")
        GameText(u"\u001b[36;1m3. Skip phase 1 99HP\u001b[0;0m")
        GameText(u"\u001b[35m1, 2, 3 or exit:")
        buy = input("\u001b[0m")

        if buy == "1":
            GameText(u"\u001b[35mYou Now Have Rewind\u001b[0m")
            GameText(u"\u001b[35mDescription: At the end of a scene you can choose if you want to restart the phase or not.\u001b[0m")
            healthUpdate(-50)
            powerUP = 1
            time.sleep(2)
            loopS = 2
        elif buy == "2":
            GameText(u"\u001b[35mYou Now Have Wrench\u001b[0m")
            GameText(u"\u001b[35mDescription: In a copier battle if you use it you will get one extra copy giving you the advantage also any tiebreaker will go your way.\u001b[0m")
            healthUpdate(-50)
            powerUP = 2
            time.sleep(2)
            loopS = 2
        elif buy == "3":
            GameText(u"\u001b[35mSkip phase 1\u001b[0m")
            GameText(u"\u001b[35mDescription: This will allow you to skip over the first part of the game if you are finding it too hard.\u001b[0m")
            healthUpdate(-99)
            powerUP = 3
            time.sleep(2)
            loopS = 2
        elif buy == "exit":
            loopS = 2

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
    print(ls)

def Printerbattle(copyTime, ChallengerName, ChallengerSpeed):

    copyCount = 0
    loopa = 1
    start = time.time()
    chalengerPBattle(ChallengerSpeed, copyTime)

    if powerUP == 1:
        GameText(u"\u001b[32mWould You like to use Your Wrench Y/N\u001b[0m")
        ans = input("")
        ans = ans.lower()
        if ans == "y":
            copyCount = copyCount + 1

    while loopa == 1:
        
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


    print(time.time() - start)
    lenLS = 0
    lenLS = len(ls)

    if len(ls) == copyCount:
        if ans == "y":
            copyCount = copyCount + 1
        else:
            ran = random.randint(2, 5)
            print(ran)
            if ran == 3:
                lenLS = lenLS - 1
            elif ran == 4:
                lenLS += 1

    
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






# def powerups():
#     if buy == "1":
#         asdf


def H2P():
    GameText(u"\u001b[32mThis is\u001b[0m")
    GameText(u"\u001b[32mLife of Dave from Xerox\u001b[0m")
    GameText(u"\u001b[32mYou Start with 100HP and 10 Life Points\u001b[0m")
    GameText(u"\u001b[32mTo check these stats just type stats\u001b[0m")
    GameText(u"\u001b[32mThis game is about a guy who is down on his luck and is trying to get through life\u001b[0m")
    GameText(u"\u001b[32mThe aim of the game is to make your way from Janitor to Ceo at Xerox by accumulating career points without letting your HP get to 0\u001b[0m")
    GameText(u"\u001b[32mPress Enter To Start\u001b[0m")
    input("")
    phase1()
    

def phase1():
    alarm.play()
    GameText(u"\u001b[32mYou wake up to the sound you have grown to hate\u001b[0m")
    GameText(u"\u001b[32mThe alarm clock\u001b[0m")
    clear()
    phaseCount = 1
    GameText(u"\u001b[32mDo you (Punch) the alarm clock or do you (Wake) up:\u001b[0m")
    ans = input()
    ans = ans.lower()
    clear()
    if ans == "punch":
        GameText(u"\u001b[32mYou get electrocuted\u001b[0m")
        healthUpdate(-50)
        clear()
        GameText(u"\u001b[32mYou say 'Screw This!' and you go back to bed\u001b[0m")
        GameText(u"\u001b[32mYou wake up to the sound of your phone ringing\u001b[0m")
        GameText(u"\u001b[32mYou pick up the phone it's your boss it's your fourth time you have forgotten to come into work your boss says...\u001b[0m")
        GameText(u"\u001b[32mDAVE YOU ARE SUCH AN IDIOT DON'T COME INTO XEROX EVER AGAIN\u001b[0m")
        GameText(u"\u001b[32mThen suddenly you feel a strong pain coming from your chest the electricity has caused your heart beat to become irregular.\u001b[0m")
        GameText(u"\u001b[32mYour bosses sudden yelling has caused you to go into cardiac arrest\u001b[0m")
        GameText(u"\u001b[32mThen suddenly your heart stops.\u001b[0m")
        print("")
        if powerUP == 1:
            powerUP = 0
            GameText(u"\u001b[32mWould You like to use Rewind Y/N\u001b[0m")
            ans = input("")
            if ans == "y":
                GameText(u"\u001b[32mRewinding Please Wait\u001b[0m")
                
                loading()
                clear()
                phase1()
        YouDied()
    elif ans == "wake":
        rand = random.randrange(5, 9)
        GameText(u"\u001b[32mYou wake up and check the time your watch reads "+ str(rand) +":00\u001b[0m")
        if rand > 7:
            GameText(u"\u001b[32mYou are running late should you eat (Breakfast) or (Leave) without\u001b[0m")
            ans = input("")
            ans = ans.lower()
            if ans == "breakfast":
                GameText(u"\u001b[32mYou eat breakfast and gain 20 health but you are now running 20 minutes late\u001b[0m")
                healthUpdate(20)
                GameText(u"\u001b[32mWhen you get to work you look at the time you are 40 minutes late\u001b[0m")
                GameText(u"\u001b[32mYour boss walks up to you and says 'I have never seen a more idiotic indifferent worker in my life you are FIRED'\u001b[0m")
                CareerUpdate(-1)
            elif ans == "leave":
                GameText(u"\u001b[32mYou skip breakfast and go straight to work you just make it on time.\u001b[0m")
                GameText(u"\u001b[32mYou grab your mop and start cleaning\u001b[0m")
                GameText(u"\u001b[32mYou finish your work at 5:00 and you go home and flop onto your bed.\u001b[0m")
                phase1()
        else:
            GameText(u"\u001b[32mYou are on schedule should you eat (Breakfast) or (Leave) without\u001b[0m")
            ans = input("")
            ans = ans.lower()
            if ans == "breakfast":
                GameText(u"\u001b[32mYou eat breakfast and gain 20 health and you get to work on time\u001b[0m")
                healthUpdate(20)
                
                GameText(u"\u001b[32mYou grab your mop and start cleaning\u001b[0m")
                GameText(u"\u001b[32mYou finish your work at 5:30 and you go home and flop onto your bed.\u001b[0m")
                phase1()
            elif ans == "leave":
                GameText(u"\u001b[32mYou skip breakfast and go straight to work you are early by 10 minutes this makes a good impression on your boss and you he says\u001b[0m")
                GameText(u"\u001b[32mI like to see a dedicated worker, have you ever done printer maintenance before?\u001b[0m")
                GameText(u"\u001b[32mYou respond with 'I am fairly handy and printers can't be too hard'\u001b[0m")
                GameText(u"\u001b[32mOk then it's settled you will challenge josh in an hour for the job of printer maintenance with a copier battle!\u001b[0m")
                time.sleep(2)
                GameText(u"\u001b[32mAn hour passes.\u001b[0m")
                GameText(u"\u001b[32mYou are extremely nervous as you approach the photo copier\u001b[0m")
                GameText(u"\u001b[32mYour boss says 'You will need as many copies as possible by typing the word (copy) and pressing enter in 20 seconds\u001b[0m")
                time.sleep(2)
                clear()
                GameText(u"\u001b[32mThe Game will start in 3 seconds\u001b[0m")
                clear()
                GameText(u"\u001b[32mThe Game will start in 2 seconds\u001b[0m")
                clear()
                GameText(u"\u001b[32mThe Game will start in 1 seconds\u001b[0m")
                clear()
                Printerbattle(20, "Josh", 2)
                if winner == "you":
                    GameText(u"\u001b[32mJosh looks down with a depressed look on his face and leaves the room\u001b[0m")
                    GameText(u"\u001b[32mYou gain a career point you now have "+  str(careerP) + " points\u001b[0m")
                    phase2()
                if winner == "challenger":
                    GameText(u"\u001b[32mJosh jumps and punches the air\u001b[0m")
                    GameText(u"\u001b[32mYou walk home and go to bed.\u001b[0m")
                    time.sleep()
                    phase1()


def phase2():
    phaseCount = 2
    GameText(u"\u001b[32mYour spirits are high and you are happy\u001b[0m")
    GameText(u"\u001b[32mYour boss leads you to the printer maintenance door and says 'I will leave you here the guys inside will tell you what you need to do.'\u001b[0m")
    GameText(u"\u001b[32mYou have a choice to (limber up) before opening the door or you can just (open) the door\u001b[0m")
    ans = input("")
    ans = ans.lower()
    if ans == "limber up":
        GameText(u"\u001b[32mYou enter the room and you walk towards the desk where the head of maintenance sits as you walk everyone is stareing at at you the new guy.\u001b[0m")
        GameText(u"\u001b[32mThe your boss says \u001b[0m")
    elif ans == "open":
        if health < 70:
            GameText(u"\u001b[32mYou decided to wear thongs to work today and there was a lip on the door frame that you stub your toe on.\u001b[0m")
            healthUpdate(-50)
        GameText(u"\u001b[32mYou enter the room and you walk towards the desk where the head of printer maintenance sits as you walk everyone is stareing at you the new guy.\u001b[0m")
        GameText(u"\u001b[32mWhen you get to the desk he says\u001b[0m")
        GameText(u"\u001b[32m'My name is James, heres the deal I already don't like you because you replaced Josh now he has to work as a jaitor and his pay was halved'\u001b[0m")
        GameText(u"\u001b[32mYou find his tone rude and unfair\u001b[0m")
        GameText(u"\u001b[32mDo you (say) something or (leave it) alone.\u001b[0m")
        ans = input("")
        ans = ans.lower()
        if ans == "say":
            GameText(u"\u001b[32mJames stands up and says 'OH YEAH'\u001b[0m")
            GameText(u"\u001b[32m'WANA GO MATE'(Y/N)\u001b[0m")
            ans = input("")
            ans = ans.lower()
            if ans == "y":
                GameText(u"\u001b[32mYou respond with 'HEll YES'\u001b[0m")
                GameText(u"\u001b[32mJames then winds up and punches you in the face and you fall to the ground and pass out.\u001b[0m")
                healthUpdate(-70)
                GameText(u"\u001b[32mWhen your are passed out on the ground your boss deides to demote you back to janitor.\u001b[0m")
                time.sleep(2)
                GameText(u"\u001b[32mYour trudge home and go to bed.\u001b[0m")
                time.sleep(2)
                phase1()
            elif ans == "n":
                GameText(u"\u001b[32mYou say 'I don't want any trouble sorry.'\u001b[0m")
        elif ans == "leave it":
            GameText(u"\u001b[32mJames then says follow me you walk over to a printer. James says that this is one of their most used matchines and runs you through some troubleshooting routines and how to use it.\u001b[0m")
            GameText(u"\u001b[32mThis guy continues to be condesending so you decide to do something but this time you go over his head.\u001b[0m")
            GameText(u"\u001b[32mYou go to the CEO of Xerox John Visentin.\u001b[0m")
            GameText(u"\u001b[32mYou have a choice to (walk) to his office or to (call) John Visentin.\u001b[0m")
            ans = input("")
            ans = ans.lower()
            if ans == "call":
                GameText(u"\u001b[32mYou don't have his phone number you're that important....\u001b[0m")
            elif ans == "walk":
                GameText(u"\u001b[32mYou leave the room and realise that Xerox is a huge company with a huge building and there are no signs the entire building is like a grid.\u001b[0m")
                GameText(u"\u001b[32mWould You like to go (forward) (left) or (right)\u001b[0m")
                ans = input("")
                ans = ans.lower()                
                if ans == "right":
                    GameText(u"\u001b[32mWould You like to go (forward) (left) or (right)\u001b[0m")
                    ans = input("")
                    ans = ans.lower()
                    if ans == "left":
                        GameText(u"\u001b[32mWould You like to go (forward) (left) or (right)\u001b[0m")
                        ans = input("")
                        ans = ans.lower()
                        if ans == "forward":
                            pygame.mixer.music.stop()
                            musicBossBattle.play()
                            GameText(u"\u001b[32mYou finally make it to the CEO's office you fling the door open say 'John I have had it with with head of printer matenance and would like to be moved to a knew branch of Xerox'\u001b[0m")
                            GameText(u"\u001b[32mJohn Visentin swivels around in his executives chair and says 'You know what why don't copier battle me if you think you are so great!'\u001b[0m")
                            GameText(u"\u001b[32mYou can here gasps coming from the hallway and people running into the room.'\u001b[0m")
                            GameText(u"\u001b[32mYou start to shake you have never been under more pressure in your life\u001b[0m")
                            GameText(u"\u001b[32mYou respond with 'So John what are the stakes'\u001b[0m")
                            GameText(u"\u001b[32mJohn says with 'If you win you take my job if I win you are fired on the spot'\u001b[0m")
                            GameText(u"\u001b[32mYou then say 'OK DEAL'\u001b[0m")
                            time.sleep(2)
                            clear()
                            GameText(u"\u001b[32mThe Game will start in 3 seconds\u001b[0m")
                            clear()
                            GameText(u"\u001b[32mThe Game will start in 2 seconds\u001b[0m")
                            clear()
                            GameText(u"\u001b[32mThe Game will start in 1 seconds\u001b[0m")
                            clear()

                        else:
                            GameText(u"\u001b[32mYou walk into a wall and loose 1HP\u001b[0m")
                            healthUpdate(-1)
                    else:
                        GameText(u"\u001b[32mYou walk into a wall and loose 1HP\u001b[0m")
                        healthUpdate(-1)
                else:
                    GameText(u"\u001b[32mYou walk into a wall and loose 1HP\u001b[0m")
                    healthUpdate(-1)
                


# rand = random.randrange(6, 8,)
# # print(rand)
# # shop()
# # phase1()
# time.sleep(2)
# pygame.mixer.music.stop()
# musicBattle.play(-1)
# Printerbattle(10, "asd", 3)
# # H2P()



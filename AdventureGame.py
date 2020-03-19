import time, sys, pygame, random
from pygame import mixer


# Variables
health = 100
careerP = 1

 
# Music/Sound Effects
mixer.init()

alarm = pygame.mixer.Sound("/Users/finn.jones/Documents/AdventureGame/The-Life-of-Dave-From-Xerox/Alarm.wav")
music = pygame.mixer.music.load("/Users/finn.jones/Documents/AdventureGame/The-Life-of-Dave-From-Xerox/ThemeSong.wav")

pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)


#Functions


def loading():
    print ("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    
def healthUpdate(damage):
    global health
    health = health + damage

def CareerUpdate(career):
    global careerP
    careerP = careerP + career



def YouDied():
    for letter in (u"\u001b[31mYou Died\u001b[0m"):
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

def GameText(text):
    for letter in (text):
        rand = random.uniform(0.001, 0.2)
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(rand)
    print("")

def H2P():
    GameText(u"\u001b[32mThis is\u001b[0m")
    GameText(u"\u001b[32mLife of Dave from Xerox\u001b[0m")
    GameText(u"\u001b[32mYou Start with 100HP and 10 Life Points\u001b[0m")
    GameText(u"\u001b[32mTo check these stats just type stats\u001b[0m")
    GameText(u"\u001b[32mThis game is about a guy who is down on his luck and is trying to get through life\u001b[0m")
    GameText(u"\u001b[32mThe aim of the game is to make your way from Janitor to Ceo at Xerox by acumulating career points without letting your HP get to 0\u001b[0m")
    GameText(u"\u001b[32mPress Enter To Start\u001b[0m")
    input("")
    phaze1()
    

def phaze1():
    alarm.play()
    GameText(u"\u001b[32mYou wake up to the sound you have grown to hate\u001b[0m")
    GameText(u"\u001b[32mThe alarm clock\u001b[0m")
    
    GameText(u"\u001b[32mDo you (Punch) the alarm clock or do you (Wake) up:\u001b[0m")
    ans = input()
    ans = ans.lower()

    if ans == "punch":
        GameText(u"\u001b[32mYou get electricuted\u001b[0m")
        healthUpdate(-50)
        GameText(u"\u001b[32mYour health is now "+  str(health)+ " HP\u001b[0m")
    elif ans == "wake":
        rand = random.randint(8, 6)
        GameText(u"\u001b[32mYou wake up and check the time"+ str(rand) +"\u001b[0m")
        if rand > 7:
            GameText(u"\u001b[32mYou are running late should you eat (Breakfast) or (Leave) without\u001b[0m")
            ans = input("")
            ans = ans.lower()
            if ans == "breakfast":
                GameText(u"\u001b[32mYou eat breakfast and gain 20 health but you are now running 20 minutes late\u001b[0m")
                healthUpdate(20)
            elif ans == "leave":
                GameText(u"\u001b[32mYou skip breakfast and go straight to work you just make it on time.\u001b[0m")
        else:
            if ans == "breakfast":
                GameText(u"\u001b[32mYou eat breakfast and gain 20 health and you get to work on time\u001b[0m")
                GameText(u"\u001b[32mYour health is now "+  str(health)+ " HP\u001b[0m")
            elif ans == "leave":
                GameText(u"\u001b[32mYou skip breakfast and go straight to work you are early by 10 minutes this makes a good impression on your boss and you he says\u001b[0m")
                GameText(u"\u001b[32mI like to see a deticated worker I am going to make you head of janitor management\u001b[0m")
                CareerUpdate(1)
                GameText(u"\u001b[32mYou gain a career point you now have "+  str(careerP) + " points\u001b[0m")







H2P()


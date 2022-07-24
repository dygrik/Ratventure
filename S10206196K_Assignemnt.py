#Dylan Sim Jing Ren P05 S10206196K
#Program: Ratventure
#Last Update: 16/8/2020
from random import randint

# +------------------------+
# | Text for various menus |
# +------------------------+

main_text = ["New Game",\
             "Resume Game",\
             "View Leaderboard",\
             "Exit Game"]

town_text = ["View Character",\
             "View Map",\
             "Move",\
             "Rest",\
             "Save Game",\
             "Exit Game"]

open_text = ["View Character",\
             "View Map",\
             "Move",\
             "Sense Orb",\
             "Exit Game"]

fight_text = ["Attack",\
              "Run"]

#List of sounds that will display when attacked
sounds = ['Oomf', 'Aaah', 'Ouchie Wowchie', 'Oh Nyo', 'Ooop', 'Argh', 'Youch', 'Aiee']

#Hero's stats
stats = {'Name':'The Hero', 'Damage':'2 - 4', 'Defence':'1', 'HP':'20'}
#Normal Rat's stats
rat = {'Name':'Rat', 'Damage':'1 - 3', 'Defence':'1', 'HP':'10'}
#Rat King's stats
ratking = {'Name':'Rat King', 'Damage':'6 - 10', 'Defence':'5', 'HP':'25'}
#Important variables used during the duration of the code
variables = {'orbPresent':False, 'ratAlive':True, 'day':1, 'position':[0, 0], 'orb':[], 'ratBuffed':False, 'kingBuffed':False}
#world_map is initiated to enable appending of stored map, when resuming game
world_map = []

print("Welcome to Ratventure!")
print("----------------------")

# Code your main program here

#Displays the main menu and routes the user to their respective functions
def mainmenu():
    count = 0
    for i in range(1, 5):
        print("{}) {}".format(i, main_text[count]))
        count += 1
    while True:
        try:
            print()
            menuchoice = int(input("Enter your choice: "))
            print()
        except:
            print()
            print('Invalid input. Try again')
            print()
            continue
        
        if menuchoice == 1:
            newgame()
        elif menuchoice == 2:
            resumegame()
        elif menuchoice == 3:
            viewleaderboard()
        elif menuchoice == 4:
            exit_game()
        else:
            print('Invalid number. Input choice from 1 to 4.')    #Displays error messgae if input choice is not from 1 to 4
            continue
      

#Sets up a new game
def newgame():
    global world_map
    world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]    
    world_map[0][0] = 'H/T'
    stats['Name'] = input("Enter your name, Hero: ")    #Used for later use in leaderboard
    print()
    #Randomising of the towns and storing their positions in the list towns
    towns = [[0,0]]
    while len(towns) < 5:
        row = randint(0,7)
        column = randint(0, 7)
        test = [row, column]
        if test in towns or test == [7,7]:
            continue
        else:
            for i in towns:
                steps = abs(i[0] - row) + abs(i[1] - column)
                if steps <= 3:
                    valid = False
                    break
                else:
                    valid = True
            if valid == True:
                towns.append(test)
    #Randomising of the Orb of Power and storing its position in the 'variables' dictonary with a key of 'orb'
    while True:
        orbrow = randint(0, 7)
        orbcolumn = randint(0, 7)
        orbtest = [orbrow, orbcolumn]
        if (orbrow <= 3 and orbcolumn <=3) or (orbtest in towns) or orbtest == [7, 7]:
            continue
        else:
            variables['orb'] = orbtest
            break
    #Integrates the randomised town into 'world_map' by replacing the spaces with 'T'
    for i in towns:
        if i == [0, 0]:
            continue
        else:
            world_map[i[0]][i[1]] = 'T'
    story()
    
def story():          
    input("Press enter to start!")
    print()
    choice = input("Press 1 to skip the story or enter to continue!")
    if choice == '1':
        print()
        print("Specialty")
        print("1  Knight")
        print("2  Armoured Corp")
        print("3  Assassins")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                print()
            except:
                print("That is not a valid choice...")
                print()
                continue
            
            #Lets user alter stats by choosing a class
            if choice == 1:
                print("You have been knighted!")
                print()
                break
            elif choice == 2:
                stats['Defence'] = '3'
                stats['Damage'] = '1 - 3'
                print("You receive your armour and joing the Armoured Corp!")
                print()
                break
            elif choice == 3:
                stats['Defence'] = '0'
                stats['Damage'] = '3 - 5'
                print("You are handed your pitch black Assassin uniform and a sharp dagger!")
                print()
                break
            else:
                print()
                print("That is not a valid choice...")
                print()
                break
        townmenu()
    else:
        input("Press enter to progress the story!")
        input("A long time ago, or rather 20 years ago, a boy was born")
        input("He was an orphan and lived a hard life")
        input("That was, until one day")
        input("A man walked into the orphanage")
        input("He was a tall, handsome man, with jewelery on his body worth more than an average person would earn in a lifetime")
        input("With clothes befitting the richest, and an aura that matched it")
        input("All of the workers at the orphanage looked on in shock as the King walked towards the boy")
        input("And held out his hand, offering it to the boy with a kind smile")
        input("\'Come with me\' The man said, \'And never suffer poverty again\'")
        input("The boy took his hand")
        input("And just like that, the boy's life changed forever")
        input("That boy is you, {}".format(stats['Name']))
        print()
        input("Fast forward 10 years...")
        print()
        input("You are now a clever, dashing boy at the age of 14")
        input("The king, your adopted father, has decided to raise you as a warrior")
        input("As such, he has decided to increase your strength beyond the human limit by financing experiments to make a Super-Soldier Serum")
        input("You have been the subject of these experiments for almost two years, enduring hours of mind-bending pain each day")
        input("Finally, the serum has been perfected and you already have the strength of a full grown man")
        input("As you have reached a mature age, you will now have to pick which specialty you want to specialise in")
        input("As you are the prince, The King has arranged for a master in each specialty to display what they have to offer in the royal court")
        input("First up, you watch as the leader of the Knights, Sir Douglas McArthur, gallops in on his horse")
        input("Well roundedness is what the Knights prioritised, from strength to formidabality")
        print()
        input("Next up, the Armoured Corp leader, Sir Ivan Quasimodo, barely clipping through the door with his large stature")
        input("The Armoured Corp are equipped with the strongest armour made by the kingdom's best blacksmiths")
        input("They prioritise defence more than anything")
        print()
        input("Last but not least, it's the Assassins turn")
        input("Murmurs erupt as the Assassin leader is nowhere to be seen")
        input("A shout is heard bouncing around the room")
        input("Everyone turns to see the Assassin leader standing atop the throne and the King on the floor in shock")
        input("The Assassins take pride in killing their enemies swiftly, not bothered by their relatively weak bodies")
        print()
        print("Specialty")
        print("1  Knight")
        print("2  Armoured Corp")
        print("3  Assassins")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                print()
            except:
                print("That is not a valid choice...")
                print()
                continue
            
            #Lets user alter stats by choosing a class
            if choice == 1:
                print("You have been knighted!")
                print()
                break
            elif choice == 2:
                stats['Defence'] = '3'
                stats['Damage'] = '1 - 3'
                print("You receive your armour and joing the Armoured Corp!")
                print()
                break
            elif choice == 3:
                stats['Defence'] = '0'
                stats['Damage'] = '3 - 5'
                print("You are handed your pitch black Assassin uniform and a sharp dagger!")
                print()
                break
            else:
                priny()
                print("That is not a valid choice...")
                print()
                break
        input("You follow your new comrades to train for the next 5 years...")
        print()
        input("You wake up in the middle of the night, hearing a scream")
        input("You rush to the sound, to the sight of rats eating the corpse of one of your comrades")
        input("You stumble back in shock as the rats scatter, leaving only broken bones")
        input("You rush back to the kingdom, desperate to tell the King, only to see guards on high alert")
        input("You question them on what is happening and they confirm your worst dreams")
        print()
        input("Villages all over the country had been ravaged and destroyed by hoards of kiler rats")
        input("Your people are falling by the thousands")
        input("You head to the kingdom where your father is ready for you")
        input("\'Your time has come son...\' The king said grimly \'It is time for you to defend your people and save us all\'")
        input("You waste no time and travel to the nearest town, finding a house to rent")
        input("As you prepare to rest and sharpen your weapon, you look out the window and see a horde of rats attacking a group of gypsies next to the town")
        input("Their screams echo through the night and through your heart")
        input("You look away, praying for their souls and vowing revenge against anyone who has hurt your people") 
        input("The day has finally come for you to prove your worth")
        input("Will you take up the gauntlet or fall like your fellow countrymen?")        
        townmenu()

#Displays the town menu and routes the user to their respective functions
def townmenu():
    while True:
        print('Day {}: You are in a peaceful town.'.format(variables['day']))
        count = 0
        for i in range(1,7):
            print('{}) {}'.format(i, town_text[count]))
            count += 1        
        try:
            print()
            townchoice = int(input("Enter your choice: "))
            print()
        except:
            print()
            print('Invalid input. Try again')
            print()
            continue
        
        if townchoice == 1:
            viewcharacter()
        elif townchoice == 2:
            viewmap()
        elif townchoice == 3:
            move()
        elif townchoice == 4:
            stats['HP'] = '20'
            print("You are sufficiently rested and fully healed.")
            print()
            variables['day'] += 1
            continue
        elif townchoice == 5:
            savegame()
        elif townchoice == 6:
            exit_game()
        else:
            print('Invalid number. Input choice from 1 to 6.')
            print()
            continue

#Displays the character stats as well as the presence of the Orb of Power, once the user has obtained it
def viewcharacter():
    for i in stats:
        print("{:>7}: {}".format(i, stats[i]))
    if variables['orbPresent'] == True:
        print("You are holding the legendary Orb of Power.")
    print()

#Displays the map
def viewmap():
    count = 0
    for i in range(1, 9):
        print("+---+---+---+---+---+---+---+---+")
        print("|", end = '')
        for j in world_map[count]:
            print("{:^3}".format(j), end = '')
            print("|", end = '')
        count += 1
        print()      
    print("+---+---+---+---+---+---+---+---+")
    print()

#Displays a message to indicate a successful exit and exits thereafter    
def exit_game():
    print("We await your return, Brave Hero!")
    print("*mutter* get a load of this coward *mutter*")
    exit()

#Changes the number in the position key in the 'variables' dictionary and routes it to the mover() function where it changes the map
def move():
    variables['day'] += 1
    viewmap()
    print("W = Move Up; A = Move Left; S = Move Down; D = Move Right")
    while True:
        try:
            movechoice = input("Your move: ")
            movechoice = movechoice.capitalize()
        except:
            print()
            print('Invalid input. Try again')
            print()
            continue
        
        if movechoice == 'W' and variables['position'][0] != 0:
            variables['position'][0] -= 1
            mover()
            break
        elif movechoice == 'A' and variables['position'][1] != 0:
            variables['position'][1] -= 1
            mover()
            break
        elif movechoice == 'S' and variables['position'][0] != 7:
            variables['position'][0] += 1
            mover()
            break
        elif movechoice == 'D' and variables['position'][1] != 7:
            variables['position'][1] += 1
            mover()
            break
        else:
            print()
            print('Invalid direction. Input choice of W, A, S or D.')
            print()

#Changes the position of the Hero after moving and adds accounts for the space left after moving
def mover():
    global world_map
    print()

    for i in world_map:
        for j in i:
            count = i.index(j)
            count1 = world_map.index(i)            
            if j == 'H':
                world_map[count1][count] = ' '
            elif j == 'H/T':
                world_map[count1][count] = 'T'
            elif j == 'H/K':
                world_map[count1][count] = 'K'
            else:
                continue
        
    if world_map[variables['position'][0]][variables['position'][1]] == 'T':
        world_map[variables['position'][0]][variables['position'][1]] = 'H/T'
        townmenu()
    elif world_map[variables['position'][0]][variables['position'][1]] == 'K':
        world_map[variables['position'][0]][variables['position'][1]] = 'H/K'
        kingmenu()
    else:
        world_map[variables['position'][0]][variables['position'][1]] = 'H'
        combatmenu()

#Displays encounter of Normal Rat and combat menu, and routes the user to it's respective functions
def combatmenu():
    variables['ratAlive'] = True    #Makes the rat 'alive' again, to prevent user from using certain options in outmenu(), after he has defeated a single rat and moved on
    if variables['ratBuffed'] == False:    #Checks to see if rat has been buffed in this encounter
        chance = variables['day'] % 6     #Increases the rat's attack every 6 days
        if chance == 0:
            dmglist = rat['Damage'].split(' - ')
            for i in range(2):
                dmglist[i] = str(int(dmglist[i]) + 1)
            rat['Damage'] = dmglist[0] + ' - ' + dmglist[1]
            print("The rats have grown ever stronger and can now break you just by looking at you! Their damage has increased by 1!")
            variables['ratBuffed'] == True
    print('Day {}: You are out in the open. Be careful...'.format(variables['day']))
    print("Encounter! - Rat")    

    while True:

        print("""\
        
       __             _,-"~^"-.
     _// )      _,-"~` +       `.
   ." ( /`"-,-"`          ##     ;
  / Q       +     #               ;
 /       #   ,          +  ,-"   + ;
(,__.--.      \      #    /   #    ;
 //'   /`-.\   | #        |   ##   `._________
   _.-'_/`  )  )--...,,,___\     \-----------,)
 ((("~` _.-'.-'           __`-.   )         //
       ((("`             (((---~"`         //
                                          ((________________
                                          `-----------------)      
                            """)        
        for i in rat:
            print("{:>7}: {}".format(i, rat[i]))        
        print()
        count = 0
    
        for i in range(1,3):
            print('{}) {}'.format(i, fight_text[count]))
            count += 1        
        try:
            print()
            fightchoice = int(input("Enter your choice: "))
            print()
        except:
            print()
            print('Invalid input. Try again')
            print()
            continue
        
        if fightchoice == 1:
            attack()
        elif fightchoice == 2:
            print("You run and hide...")
            outmenu()
        else:
            print('Invalid number. Input choice from 1 to 2.')
            continue

#Calculates and distribute the appropriate damage to the two parties 
def attack():
    herolist = stats['Damage'].split(' - ')
    ratlist = rat['Damage'].split(' - ')
    herodmg = randint(int(herolist[0]), int(herolist[1])) - int(rat['Defence'])
    ratdmg = randint(int(ratlist[0]), int(ratlist[1])) - int(stats['Defence'])
    #Ensures that damage done does not go below 0, which will instead heal the opponent
    if herodmg < 0:
        herodmg = 0
    if ratdmg < 0:
        ratdmg = 0
    rat['HP'] = str(int(rat['HP']) - herodmg)
    print("You deal {} damage to the Rat!".format(herodmg))
    #Helps in ensuring that the rat is unable to hit the user after the rat has died
    if int(rat['HP']) > 0:
        print("{}! The Rat hit you for {} damage!".format(sounds[randint(0, 7)], ratdmg))
        herohealth = int(stats['HP']) - ratdmg
        stats['HP'] = str(herohealth)
        print("You have {} HP left.".format(herohealth))
        print()
        if int(stats['HP']) <= 0:
            print("{:=^51}".format("You Died"))    #Displays death message and tips to confirm that the game is over, before exiting
            print("{:=^51}".format("Game Over"))
            print()
            print("{:=^51}".format("Tip! Try to avoid damage to not die!"))
            print("{:=^51}".format("Tip! Try to keep your health above 0!"))
            print("{:=^51}".format("Tip! Try to kill your opponent before he kills you!"))
            print("{:=^51}".format("Tip! Enemies die if they're killed!"))
            print("{:=^51}".format("Tip! To win the game, try to not die!"))
            exit()
        combatmenu()
    else:
        print("The Rat is dead! You are victorious! Huzzah!")
        print()
        rat['HP'] = '10'
        variables['ratAlive'] = False   #Asserts that the rat is dead
        variables['ratBuffed'] = False    #Resets the variable for next encounter
        print("You've heard that consuming rat flesh has the chance of increasing your damage! You decide to take the risk...")
        print("This seems reminiscent of how a certain pandemic began..")
        print()
        luck = randint(1, 10)
        if luck == 1 or luck == 2 or luck == 3:    #Provides a 30% chance for an increase of 1 damage every time a rat is killed
            dmglist = stats['Damage'].split(' - ')
            for i in range(2):
                dmglist[i] = str(int(dmglist[i]) + 1)
            stats['Damage'] = dmglist[0] + ' - ' + dmglist[1]
            stats['Defence'] = str(int(stats['Defence']) + 1)
            print("You feel strength rushing through your body, something you have never felt before! The feeling soon fades and the normality of life returns...")
            print("Your damage has increased by 1!")
            print("Your defence has increased by 1!")
            print()
        else:
            print("You feel a rumbling in your belly and rush to respond to the call of nature...")
            print()
        
        outmenu()
        
#Displays the outdoors menu and routes the user to their respective functions after checking that the Rat is dead
def outmenu():
    while True:
        print('Day {}: You are out in the open. Be careful...'.format(variables['day']))
        count = 0
        for i in range(1,6):
            print("{}) {}".format(i, open_text[count]))
            count += 1
        try:
            print()
            openchoice = int(input("Enter your choice: "))
            print()
        except:
            print()
            print('Invalid input. Try again')
            print()
            continue
        
        if openchoice == 1:
            if variables['ratAlive'] == False:
                viewcharacter()
            else:
                combatmenu()
        elif openchoice == 2:
            if variables['ratAlive'] == False:
                viewmap()
            else:
                combatmenu()                 
        elif openchoice == 3:
            move()
        elif openchoice == 4:
            if variables['ratAlive'] == False:
                senseorb()
            else:
                combatmenu()            
        elif openchoice == 5:
            exit_game()
        else:
            print('Invalid number. Input choice from 1 to 5.')
            print()
            continue

#Checks the different sense orb situations and prints the respective messages
def senseorb():
    variables['day'] += 1
    if variables['orb'] == variables['position'] and variables['orbPresent'] == False:    #Situation where user is on the space where the orb is and has not picked it up yet
        print("You found the legendary Orb of Power!")    #Tells user that the orb has been picked up and that the stats have been increased
        print("Your attack increases by 5! You are now capable of lifting a twig!")
        print("Your defence increases by 5! You can now stub your toes without bawling your eyes out!")
        print()
        #Addition of damage and defence
        dmglist = stats['Damage'].split(' - ')
        for i in range(2):
            dmglist[i] = str(int(dmglist[i]) + 5)
        stats['Damage'] = dmglist[0] + ' - ' + dmglist[1]
        stats['Defence'] = str(int(stats['Defence']) + 5)
        variables['orbPresent'] = True
        outmenu()
    elif variables['orb'] == variables['position'] and variables['orbPresent'] == True:    #Situation where user is on the space where the orb is and has already been picked up
        print("You remember that you already have the orb...")
        print()
        outmenu()
    else:    #Situation where user is not on the space where the orb is
        xaxis = variables['orb'][1] - variables['position'][1]
        yaxis = variables['orb'][0] - variables['position'][0]
        #Displays the respective messages for the directions
        if xaxis > 0 and yaxis == 0:
            print("You sense that the Orb of Power is to the East. Go have a feast!")
        elif xaxis < 0 and yaxis == 0:
            print("You sense that the Orb of Power is to the West. You are the best!")
        elif xaxis == 0 and yaxis > 0:
            print("You sense that the Orb of Power is to the South. Put some food in your mouth!")
        elif xaxis == 0 and yaxis < 0:
            print("You sense that the Orb of Power is to the North. Go catch a moth!")
        elif xaxis > 0 and yaxis > 0:
            print("You sense that the Orb of Power is to the South-East. You are a beast!")
        elif xaxis < 0 and yaxis > 0:
            print("You sense that the Orb of Power is to the South-West. You should really get some rest!")
        elif xaxis < 0 and yaxis < 0:
            print("You sense that the Orb of Power is to the North-West. You should take an intelligence test!")
        elif xaxis  > 0 and yaxis < 0:
            print("You sense that the Orb of Power is to the North-East. Your fame has now increased!")
        print()
        outmenu()

#Displays encounter of Rat King and combat menu, and routes the user to it's respective functions
def kingmenu():
    print('Day {}: You see the Rat King!'.format(variables['day']))
    print("Encounter! - Rat King")    
    
    if variables['kingBuffed'] == False:    #Checks to see if Rat King has been buffed in this encounter
        times = variables['day'] // 10    #Increases the Rat King's damage by 1 every 10 days
        dmglist = ratking['Damage'].split(' - ')
        for i in range(2):
            dmglist[i] = str(int(dmglist[i]) + times)
        ratking['Damage'] = dmglist[0] + ' - ' + dmglist[1]
        print("You stumble as you behold the Rat King's might! He has grown ever stronger...")
        print("The Rat King's damage has been increased by {}!".format(times))  
        variables['kingBuffed'] = True

    
    

    while True:

        print('''

        ,  .            
       c(\/|           
       /  o `-.       
      |    --'       
    _-_    (_       /
   /`` `---' \     /
/  `---. \ \-'\__./
\  ( -< -'-'|\_.-/'
 |  `-.`. ,`(
 |   /`'----'\\
 \\\_/ | | | | \\ 
  `-~~\~~|~/~~'
       \ |/
        \|\_,
      ,_/  '
       `
       
       ''')   
        for i in ratking:
            print("{:>7}: {}".format(i, ratking[i]))        
        print()
        count = 0
    
        for i in range(1,3):
            print('{}) {}'.format(i, fight_text[count]))
            count += 1
        try:
            print()
            fightchoice = int(input("Enter your choice: "))
            print()
        except:
            print()
            print('Invalid input. Try again')
            print()
            continue
        
        while True:
            if fightchoice == 1:
                kingattack()
            elif fightchoice == 2:
                print("You run and hide from the Rat King...")
                outmenu()
            else:
                print('Invalid number. Input choice from 1 to 2.')
                break

#Calculates and distribute the appropriate damage to the two parties 
def kingattack():
    #Checks for the presence of the Orb of Power and informs the user if their attack did not go through
    if variables['orbPresent'] == False:
        print("You do not have the legendary Orb of Power - the Rat King is immune to your pathetic attacks!")
        print("You stumble as your blade hits the Rat King's skin and barely leaves a scratch")
        print("You lie in the dust, realising just how weak you are")
        print("If only you had the intellectual capability to strengthen yourself before coming here")
        print("Now, your only choice is to stand and die a pathetic death or plead for mercy and run away")
        herodmg = 0
    else:
        herolist = stats['Damage'].split(' - ')
        herodmg = randint(int(herolist[0]), int(herolist[1])) - int(ratking['Defence'])
        
    kinglist = ratking['Damage'].split(' - ')    
    kingdmg = randint(int(kinglist[0]), int(kinglist[1])) - int(stats['Defence'])
    #Ensures that damage done does not go below 0, which will instead heal the opponent
    if herodmg < 0:
        herodmg = 0
    if kingdmg < 0:
        kingdmg = 0
    ratking['HP'] = str(int(ratking['HP']) - herodmg)
    print("You deal {} damage to the Rat King!".format(herodmg))
    #Helps in ensuring that the rat is unable to hit the user after the rat has died
    if int(ratking['HP']) > 0:
        print("{}! The Rat King hit you for {} damage!".format(sounds[randint(0, 7)], kingdmg))
        herohealth = int(stats['HP']) - kingdmg
        stats['HP'] = str(herohealth)
        print("You have {} HP left.".format(herohealth))
        print()
        if int(stats['HP']) <= 0:
            input("Press enter to continue!")
            input("As you lay on the ground, near death, the Rat King walks slowly to you")
            input("He falls down onto his knees, weapon dropped at his side")
            input("\'I didn't mean to do this, it didnt have to be this way...my son\' The Rat King cries out")
            input("A single tear falls down his face")
            input("He buries your body somberly and walks away")
            input("His sword left as a headstone...")
            print()
            print("{:=^51}".format("You Died"))    #Displays death message and tips to confirm that the game is over, before exiting
            print("{:=^51}".format("Game Over"))
            print()
            print("{:=^51}".format("Tip! Try to avoid damage to not die!"))
            print("{:=^51}".format("Tip! Try to keep your health above 0!"))
            print("{:=^51}".format("Tip! Try to kill your opponent before he kills you!"))
            print("{:=^51}".format("Tip! Enemies die if they're killed!"))
            print("{:=^51}".format("Tip! To win the game, try to not die!"))
            exit()
        kingmenu()
    else:
        input("Press enter to continue!")
        input("You walk over to the Rat King's body, ready to finish him off")
        input("As you draw near, he holds out something to you")
        input("It's a pendant with a picture of younger you and a man inside")
        input("You seen to be about a year old and the man is carrying you")
        print()
        input("You stand there, confused as to how the Rat King has this")
        input("\'It's been too long...my son\' The Rat King says as tears come rolling out of his eyes")
        input("Your head whips to look at him, confused as to how he could be your father")
        print()
        input("\'I used to be the king's most trusted advisor, and he needed test subjects for the first batch of experiments for the serum\' He explained")
        input("\'As the doses I received were the first batch, there were horrible side effects, which led to me becoming this\' He said as the waterworks increased")
        input("\'I thought that they would try to fix me, but the King wanted me to be thrown out instantly and have you put into an orphanage\'")
        input("\'His plan all along was to have you experimented on and thrown out if the experiment had become a failure\'")
        input("\'He never looked at you as his son, only a tool to experiment with\'")
        input("\'I'm glad to see you turned out fine and have become a handsome young man\'")
        input("\'It's a shame that we couldn't spend much time together, but I hope you'll forever remember me\'")
        input("\'This was all I ever wanted, this was my final wish, the only reason I attacked the kingdom, was to see you again\'")
        input("\'Now I can die happy\'")
        input("\'Live happily, my son\'")
        print()
        input("You watch as his eyelids close, a sweet smile on his face")
        input("You wipe your eyes and stand up, carrying his body and burying him")
        input("You leave your sword as a headstont to remember him by")
        input("As you kneel beside his grave, you swear vengence upon the King and swear to kill him in the name of your father")
        input("With that, you picked up your father's sword and began your new journey")
        input("To correct all the wrongs that have been done to your father")
        input("To kill the King")
        print()
        print("The Rat King is dead! You are victorious in your initial quest")    #Displays victory message before going through the process of checking for eligibility on leaderboard in wingame()
        print("Congratulations, you have defeated the Rat King, but would you do it again?")
        print("The world is saved! You win but at what cost")
        print("Now, you have a new purpose in life")
        print()
        print("You took {} days to beat the game! That is very adequate!".format(variables['day']))
        wingame()

#Saves the game
def savegame():
    
    file = open("data.txt", 'w+')

    for i in stats:
        file.write(i)
        file.write(': ')
        file.write(stats[i])
        file.write('\n')
        
    for i in rat:
        file.write(i)
        file.write(': ')
        file.write(rat[i])
        file.write('\n')
    
    for i in ratking:
        file.write(i)
        file.write(': ')
        file.write(ratking[i])
        file.write('\n') 
        
    for i in variables:
        file.write(i)
        file.write(': ')
        file.write(str(variables[i]))
        file.write('\n')   
    
    for line in world_map:
        for i in line:
            if i == 'H/T':
                file.write('0')
            else:
                file.write(i)
    print('Game Saved')    #Displays successful save message
    file.close()
    print()
    townmenu()

#Resumes game
def resumegame():
    
    try:
        data = open("data.txt", 'r')
    
    except:
        print("Error loading file")
        print()
        return
        
    for i in range(0, len(stats)):
        line = data.readline()
        line = line.strip('\n')
        line = line.split(': ')
        stats[line[0]] = line[1]
        
    for i in range(0, len(rat)):
        line = data.readline()
        line = line.strip('\n')
        line = line.split(': ')
        rat[line[0]] = line[1]  
        
    for i in range(0, len(ratking)):
        line = data.readline()
        line = line.strip('\n')
        line = line.split(': ')
        ratking[line[0]] = line[1]

    for i in range(0, len(variables)):
        line = data.readline()
        line = line.strip('\n')
        line = line.split(': ')
        if line[1] == 'False':    #Ensures that the variable saves as a boolean and not a string
            variables[line[0]] = False
        elif line[1] == 'True':    #Ensures that the variable saves as a boolean and not a string
            variables[line[0]] = True
        elif line[0] == 'day':    #Changes the string back to an integer
            variables[line[0]] = int(line[1])
        elif line[1].find('[') != -1:    #Changes the list from a string back into a list
            subline = line[1].strip('[, ]')
            subline = subline.split(',')
            variables[line[0]] = [int(subline[0]), int(subline[1])]
        
    line = data.readline()
    temp = []
    for i in line:    #Converts the saved map into the format of a real map
        if i == '0':
            temp.append('H/T')
        else:
            temp.append(i)
        if len(temp) == 8:
            world_map.append(temp)
            temp = []
    data.close()
    townmenu()
    
#Displays leaderboard
def viewleaderboard():
    print("{:=^51}".format(""))
    print("{:=^51}".format("   Hall of Fame   "))
    print("{:=^51}".format(""))
    print()
    print("{:<6}{:<20}{:<4}".format('Rank', 'Name', 'Days'))
    try:
        leaderboard = open("leaderboard.txt", 'r')
        count = 1
        for i in leaderboard:
            count += 1
        leaderboard.close()
        leaderboard = open("leaderboard.txt", 'r')
        for i in range(1, count):
            line = leaderboard.readline()
            line = line.strip("\n")
            line = line.split(": ")
            print("{:<6}{:<20}{:<4}".format(i, line[0], line[1]))
        print()
        leaderboard.close()
    except FileNotFoundError:
        print("File not found.")
        print()
    mainmenu()
  
#Checks for eligibility for leaderboard
def wingame():
    try:
        leaderboard = open("leaderboard.txt", 'r')
    except:
        leaderboard = open("leaderboard.txt", 'w+')
    days = []
    names = []
    combine = {}
    for line in leaderboard:
        line = line.strip("\n")
        line = line.split(": ")
        names.append(line[0])
        days.append(int(line[1]))
    leaderboard.close()
    
    for i in range(len(names)):
        combine[names[i]] = int(days[i])
    combine[stats['Name']] = variables['day']
    
    #Lambda is a function without a name.
    sortedcombine = sorted(combine.items(), key = lambda x: x[1])    
    #key allows me to perform custom sort operations which I used to sort the combine 
    #based on the value of the key of each element in the list
    
    leaderboard = open("leaderboard.txt", "w")
    for i in range(len(sortedcombine)):
        leaderboard.write(sortedcombine[i][0] + ': ' + str(sortedcombine[i][1]))
        leaderboard.write('\n')
        if i == 4:    #Ensures that only the top 5 scores are recorded
            break
        else:
            continue
    leaderboard.close()
    exit()
    
    
#Executes the entire code
mainmenu()
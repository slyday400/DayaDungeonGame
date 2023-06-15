weapon = False
def start():
  directions = ["left", "right", "forward"]
  print("Type how you make your way through the dungeon.\nYou come across three passage ways. Which way will you go?")
  print("left, right, forward")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/forward")
    userInput = input()
    if userInput == "left":
      ratScene()
    elif userInput == "right":
      hauntedRoom()
    elif userInput == "forward":
      warningScene()
    else: 
      print("Please enter a valid option.")
def ratScene():
  directions = ["go down", "go back"]
  print("You make your way through the dark passage. \nYou suddenly hear the sounds of squeaking coming from a stone staircase leading down deeper. \nDo you venture downward or turn back?")
  print("go down, go back")
  userInput = ""
  while userInput not in directions:
    print("Options: go down/go back")
    userInput = input()
    if userInput == "go down":
      print("After a few steps, a swarm of rats scamper past your feet. \nThey seem to be running in fright. But from what? \nYou steel your nerves and continue to delve deeper into the dungeon.")
      catacombs()
    elif userInput == "go back":
      hallway()
    else:
      print("Please enter a valid option.")

def warningScene():
  actions = ["search skeleton","go back"]
  print("You come across an skeleton slouched near a blood-stained wall.\n \"TURN BACK NOW\" written across stone. \nA warning from a previous advenuturer. What will you do?")
  print("search skeleton, go back")
  userInput = ""
  while userInput not in actions:
    print("Options: search skeleton/go back")
    userInput = input()
    if userInput == "search skeleton":
      print("You search the skeleton and find a tattered journal. Most of the pages are unreadable, but something catches your eye.\n\"They Call Me The King. I Have The Eyes, Hiss, And Fangs Of A Snake, But Have No Scales Or Venom.\" \nMight need to remember this later.")
      hallway()
    elif userInput == "go back":
      hallway()
    else:
      print("Please enter a valid option.")


def hauntedRoom():
  actions = ["search", "leave"]
  global weapon
  print("You enter a decrypted room. Cobwebs and dust covering all visible surfaces. \nWonder what you will find here?")
  print("search or leave?")
  userInput = ""
  while userInput not in actions:
    print("Options: search/leave")
    userInput = input()
    if userInput == "search":
      print("You shuffle around the room and find a dagger with the engraving of a holy symbol. You head back.")
      weapon = True
      hallway()
    elif userInput == "leave":
      hallway()
    else:
      print("Please enter a valid option.")

def catacombs():
  actions = ["fight", "sneak", "search"]
  print("The staircase leads you down into the catacombs. You hear rattling of bones and shrieking moans. \nThe undead are near.What will you do?")
  userInput = ""
  while userInput not in actions:
    print("Options: fight/sneak/search")
    userInput = input()
    if userInput == "fight":
      print("You decided to fight whatever comes your way. \nUnfortunatly, what came was a horde of hungry zombies. \nYou fall prey to being this horde's lastest meal.")
      gameOver()
    elif userInput == "sneak":
      print("You play it safe by sneaking around the catacombs. \nYou manage to avoid a horde of zombies.")
      trapRoom()
    elif userInput == "search":
      print("You're curious of potenial loot in some expensive looking coffins. \nBut you didn't think there was something occupying the coffins. You disturbed a vampire from its slumber. \nHe drains you of every drop of blood.")
      gameOver()
    else:
      print("Please enter a valid option for the adventure game.")

def trapRoom():
  answers = ["snake", "lion", "cat"]
  print("This room contains animal-shaped statues. In the center podium lays a gold crown. \nInscribed on the podium are the words: \"Crown the King\" \nThree statues stand out to be the answer.")
  print("snake, lion or cat?")
  userInput = ""
  while userInput not in answers:
    print("Options: snake,lion,cat")
    userInput = input()
    if userInput == "snake":
      print("You place the crown on the snake statue. It comes to live, hisses, and wraps its coils around you. \nYou succumbed to the snake's squeeze.")
      gameOver()
    elif userInput == "lion":
      print("You place the crown on the lion statue. It comes to live, roars, and pounces on you.\nYou are clawed and mauled to pieces.")
      gameOver()
    elif userInput == "cat":
      print("You place the crown on the cat statue. It comes to live and purrs. \nA hidden wall opens for you to venture further.")
      treasureRoom()
    else:
      print("Please enter a valid option.")

def hallway():
  directions = ["left", "right", "forward"]
  print("A hallway with three directions to choose from.")
  print("left, right, forward")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/forward")
    userInput = input()
    if userInput == "left":
      ratScene()
    elif userInput == "right":
      hauntedRoom()
    elif userInput == "forward":
      warningScene()
    else:
      print("Please enter a valid option.")

def treasureRoom():
  actions = ["search"]
  print("You have made it to the treasure room. Heaps of gold and gems scattered around the floor. \nBut before you can celebrate, you hear chanting in the next chamber. \nBetter grab what you can.")
  userInput = ""
  while userInput not in actions:
    print("Options: search")
    userInput = input()
    if userInput == "search":
      print("You begin to fill your pockets with as much as you can carry. Just when you were ready to leave, the lich appears. \n\"YOU SHALL PAY FOR YOUR THIEVRY WITH YOUR SOUL!\"")
      finalFight()
    else:
      print("Please enter a valid option.")

def finalFight():
  actions = ["fight","flee"]
  global weapon
  print("Do you fight or flee?")
  userInput = ""
  while userInput not in actions:
    print("Options: fight/flee")
    userInput = input()
    if userInput == "fight":
      if weapon:
        print("Your engraved dagger glows holy light in the presence of the lich. \nWith one swift stab, the lich is defeated.")
        print("Congrats! YOU WON!")
        quit()
      else:
        print("The lich shoots out a powerful spell. You are disintregrated to dust.")
      gameOver()
    elif userInput == "flee":
      print("You try to run, but your heavy pockets made you a slower target. \nThe lich shoots out a spell hitting you in the back. You are disintregrated to dust.")
      gameOver()
    else:
      print("Please enter a valid option.")

def gameOver():
  choices = ["yes","no"]
  print("GAME OVER! \nTry Again?")
  userInput = ""
  while userInput not in choices:
    print("[yes]<-->[no]")
    userInput = input()
    if userInput == "yes":
      start()
    elif userInput == "no":
      quit()
    else:
      print("Please enter a valid option.")
  
if __name__ == "__main__":
  while True:
    print("Welcome To Daya's Dungeon!")
    print("You came to this dungeon on the quest for riches beyond your imagination.")
    print("But beware brave adventurer. For this dungeon holds many a foe and beset with dangerous traps.")
    print("Can you reach the end of this dungeon?")
    print("What is your name: ")
    name = input()
    print("Good luck, " +name+ ". You'll need it.")
    start()
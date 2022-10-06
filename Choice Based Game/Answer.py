

import random

def gameLoop(story,question,options1,options2,insults):
    while True:
        print(story)
        while True:
            choice = input(question)
            if (choice in options1):
                story = " option 1"
                break
            elif choice in options2:
                story = "option 2"
                break

            else:
                print(random.choice(insults))








gameLoop("starting","give me an input",[1,"one","yes"],[2,"two","no"],["you suck","nope not gonna work","really???"])
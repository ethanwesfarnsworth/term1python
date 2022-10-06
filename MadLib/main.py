# Ethan Farnsworth
# 09.20.22
# Madlib


# imports


# globals()
PSYCHO = """I used to be a (renegade)
I used to (fool) around
But I couldn't take the (punishment)
And had to settle down
Now I'm playing it real straight
And yes, I cut my (hair)
You might think I'm (crazy)
But I don't even (care)
'Cause I can (tell) what's going on
It's (hip) to be (square)
It's (hip) to be (square)
I like my (bands) in (business suits)
I (watch) them on TV
I'm (working out) most every day
And watchin' what I eat
They (tell) me that it's good for me
But I don't even (care)
I know that it's (crazy)
I know that it's nowhere
But there is no denying that
It's (hip) to be (square)
It's (hip) to be (square)
It's (hip) to be (square)
So (hip) to be (square)
It's not too hard to figure out
You (see) it every day
And those that were the farthest out
Have gone the other way
You see them on the (freeway)
It don't look like a lot of fun
But don't you try to (fight) it
An idea whose time has come
Don't (tell) me that I'm (crazy)
Don't (tell) me I'm nowhere
Take it from me
It's (hip) to be (square)
It's (hip) to be (square)
It's (hip) to be (square)
So (hip) to be (square)
(Tell) 'em, boys
So (hip) to be (square)"""


# functions



# main

def main():

    # Welcomes the Player to the Game
    print("Welcome To The American Psycho MadLib!\n")

    # Prompts the players to insert words to replace words from the song and defines them as a variable
    renegade = input("Give Me A Noun: ")
    fool = input("Give Me An Verb: ")
    punishment = input("Give Me A Noun: ")
    hair = input("Give Me A Noun: ")
    crazy = input("Give Me an Adjective: ")
    tell =  input("Give Me A Verb: ")
    hip = input("Give Me An Adjective: ")
    square = input("Give Me A Shape: ")
    bands =  input("Give Me A Plural Noun: ")
    business_suits =  input("Give Me A Plural Noun: ")
    watch = input("Give Me A Verb: ")
    working_out = input("Give Me A Verb: ")
    care = input("Give Me A Verb: ")
    see = input("Give Me A Verb: ")
    freeway = input("Give Me A Noun: ")
    fight = input("Give Me A Verb: ")



    # Inserts the user defined variables into the lyrics
    text1 = """I used to be a ("""+renegade+""")
I used to ("""+fool+""") around
But I couldn't take the ("""+punishment+""")
And had to settle down
Now I'm playing it real straight
And yes, I cut my ("""+hair+""")
You might think I'm ("""+crazy+""")
But I don't even ("""+care+""")
'Cause I can ("""+tell+""") what's going on
It's ("""+hip+""") to be ("""+square+""")
It's ("""+hip+""") to be ("""+square+""")
I like my ("""+bands+""") in ("""+business_suits+""")
I ("""+watch+""") them on TV
I'm ("""+working_out+""") most every day
And watchin' what I eat
They ("""+tell+""") me that it's good for me
But I don't even ("""+care+""")
I know that it's ("""+crazy+""")
I know that it's nowhere
But there is no denying that
It's ("""+hip+""") to be ("""+square+""")
It's ("""+hip+""") to be ("""+square+""")
It's ("""+hip+""") to be ("""+square+""")
So ("""+hip+""") to be ("""+square+""")
It's not too hard to figure out
You ("""+see+""") it every day
And those that were the farthest out
Have gone the other way
You see them on the ("""+freeway+""")
It don't look like a lot of fun
But don't you try to ("""+fight+""") it
An idea whose time has come
Don't ("""+tell+""") me that I'm ("""+crazy+""")
Don't ("""+tell+""") me I'm nowhere
Take it from me
It's ("""+hip+""") to be ("""+square+""")
It's ("""+hip+""") to be ("""+square+""")
It's ("""+hip+""") to be ("""+square+""")
So ("""+hip+""") to be ("""+square+""")
("""+tell+""") 'em, boys
So ("""+hip+""") to be ("""+square+""")"""

    # Prints the final version of the mad lib
    print(text1)
main()

input()
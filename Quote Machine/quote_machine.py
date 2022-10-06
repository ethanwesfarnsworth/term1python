# Ethan Farnsworth
# 9.12.2022
## Quote Machine

# imports
import random
import requests
from bs4 import BeautifulSoup

# global Variables

welcomes =["Good Morning","Howdy","Buenos Dias","Guten Morgan","Peace up","Nice Morning",
           "Scrungled Morning", "Uncringe Morning", "Super Morning", "Great morning",
           "Happy Morning", "Stenchless Morning", "Liberty Morning",
           "Glory to Big Papa and all he sees!", "May money man green you up!",
           "Papalingless morning to you!", "Zerked up morning!"]


quote_1 = " \"It\'s fine to celebrate success but it is more important to heed the lessons of failure. \" "
quote_1_name = "bill gates"
quote_2 = " \"You can't have everything you want, but you can have the things that really matter to you. \" "
quote_2_name = "marissa mayer"
quote_3 = " \"the biggest risk is not taking any risk... In a world that's changing \nreally quickly, the only strategy... \" "
quote_3_name = "Mark Zuckerberg"
quote_4 = " \"Perhaps we make too much of what is wrong and too little of what is right. The trouble with gloom... \" "
quote_4_name = "Queen Elizabeth"


quotes =[quote_1,quote_2,quote_3,quote_4]

names =[quote_1_name,quote_2_name,quote_3_name,quote_4_name]

url = "http://www.quotationspage.com/random.php"

# functions
def quote_card(quote,name):
    size = len(quote)+5 # get the size of the quote and add 5 to it
    welcome = random.choice(welcomes)
    print()
    print()
    print()
    print()
    print()
    print()
    print("\t\t\t\t"+"="*size)
    print("\t\t\t\t|"+"="*(size -2)+"|")
    print("\t\t\t\t|"+welcome+" "*(size-len(welcome)-2)+"|")
    print("\t\t\t\t|"+quote+"="*(size-len(quote)-2)+"|")
    print("\t\t\t\t|"+name+" "*(size-len(name)-2)+"|")
    print("\t\t\t\t|"+" "*(size -2)+"|")
    print("\t\t\t\t|"+" "*(size -2)+"|")
    print("\t\t\t\t|"+" "*(size -2)+"|")
    print("\t\t\t\t"+"="*size)

def scraper(url):
    # Connects to the given website and tells us if it connects or not
    response = requests.get(url)
    if response.ok:
        print("Connected to "+url)
        soup = BeautifulSoup(response.text,"lxml")


        
        # <p class="quote"> this is the tag for the quote
        # getting the quote from the soup by searching for its tags and class name
        quote = str(soup.find("dt",{"class":"quote"}))
        # clean up the quote by replacing any uneeded parts of the String with "" (nothing)
        quote = quote.replace("<dt class=\"quote\>","")
        quote = quote.replace("</a> </dt>","")


        # loop through whats left of the string and collect the parts we need
        createString = False # create a bool we can toggel when we need to start creating the string
        x="" # create a place holder variable to create a new string in using cancatination
        for i in quote: # cycle through each char in the string
            if i == ">": #if the char is > we need to start collecting the next characters
                createString = True # toggle the bool to start collecting
            if createString: # if our bool is true
                x += i # start adding each char to string
        quote = x # set the string we built to quote variable

        # finish removing the un needed data
        quote = quote.replace(">","")
        quote = quote.title()


    # <span class="author" this is tag for the author
        name = str(soup.find("dd",{"class":"author"}))
        name = name.replace("<div class=\"icons\">","")
        name = name.replace("<dd class=\"author\">","")
        num = len(name)

        start = False
        end = False
        x = ""
        for i in range(len(name)):
            if name[i*-1] =="(":
                start = True
            if start and end == False:
                x+=name[i*-1]
                if name[i*-1] == "\"":
                    end = True
        name = x
        name = name[6:len(name)-2:1]
        name = name[::-1]
        if name == "":
            name = "Author Unknown"
    return quote,name

# main
def main():
    # build program
    quote, name = scraper(url)
    quote_card(quote,name)
    

# start the program
main()
input()



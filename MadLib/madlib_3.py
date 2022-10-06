# Ethan Farnsworth
# 09.22.22
# MadLib

# imports



# globals

ORIGINAL = """Oh, yeah
Alright
Somebody's Heine'
Is crowdin' my icebox
Somebody's cold one
Is givin' me chills
Guess I'll just close my eyes
Oh, yeah
Alright
Feels good
Inside
Flip on the telly
Wrestle with Jimmy
Something is bubbling
Behind my back
The bottle is ready to blow
Say it ain't so
Your drug is a heartbreaker
Say it ain't so
My love is a life taker
I can't confront you
I never could do
That which might hurt you
To try and be cool
When I say
This way is a waterslide away from me
That takes her further every day
So be cool
Say it ain't so
Your drug is a heartbreaker
Say it ain't so
My love is a life taker
Dear daddy, I write you
In spite of years of silence
You've cleaned up, found Jesus
Things are good, or so I hear
This bottle of Steven's awakens ancient feelings
Like father, stepfather
The son is drowning in the flood
Yeah, yeah, yeah, yeah, yeah
Say it ain't so
Your drug is a heartbreaker
Say it ain't so
My love is a life taker"""




# main


def main():
    text3 = ORIGINAL

    words =["Heine'","icebox","chills","eyes","Inside","telly","Wrestle","heartbreaker","waterslide","drowning"]
    i = 0
    for word in words:
        text3 = text3.replace(word,"({"+str(i)+"})")
        i+=1

    vars = []
    for i in range(len(words)):
        x = input("Give me a word to Replace"+words[1])
        vars.append(x)

        text3 = str.format(text3,vars[0],vars[1],vars[2],vars[3],vars[4],vars[5],vars[6],vars[7],vars[8],vars[9])

        print(text3)
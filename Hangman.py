from os import system, name

def clrscr():
    if name=='nt':
        system('cls')
    else:
        system('clear')
    return
def draw(errors):
    match errors:
        case 0:
            print("""






                  
""")
        case 1:
            print("""





._____        
""")
        case 2:
            print("""
.
|
|
| 
|
|_____              
""")
        case 3:
            print("""
.____
|
|
| 
|
|_____              
""")
        case 4:
            print("""
.____
|   |
|
| 
|
|_____                 
""")
        case 5:
            print("""
.____
|   |
|   o
| 
|
|_____              
""")
        case 6:
            print("""
.____
|   |
|   o
|   | 
|
|_____            
""")
        case 7:
            print("""
.____
|   |
|   o
|  /| 
|
|_____            
""")
        case 8:
            print("""
.____
|   |
|   o
|  /|\ 
|
|_____              
""")
        case 9:
            print("""
.____
|   |
|   o
|  /|\ 
|  /
|_____
                  
""")
        case _:
            print("""
.____
|   |
|   o
|  /|\ 
|  / \\
|_____ 
You lost!        
""")
    return
def randomWord():
    from requests import get
    from random import choice
    x=get('https://randomtextgenerator.com/')
    lines=x.text.replace('<','>').split('>')
    words=[]
    found=False
    for line in lines:
        if found:
            if line.__contains__('RandomTextGenerator.com') and len(words)>0:
                while 1:
                    word=choice(words).strip()
                    if len(word)>2:
                        return word.lower()
            if line is not 'br':
                words.extend(line.replace('.','').split(' '))
        elif line.__contains__('div id="randomtext_box"'):
            found=True
    return ''
def display(progress,mistakes):
    clrscr()
    mistakeNum=len(mistakes)
    draw(mistakeNum)
    if mistakeNum>0:
        print('Mistakes: ',''.join(map(lambda x:x+' ',mistakes)))
    print(''.join(map(lambda x:x+' ',progress)),'\n')
    return
def getGuess(progress,mistakes):
    while 1:
        guess=input('Guess a letter: ')
        guess=guess.strip().lower()
        if guess=='quit': return guess
        elif len(guess) == 1 and guess not in progress+mistakes:
            if 123>ord(guess)>96:
                return guess
    #in case of incorrect input:
        display(progress,mistakes)
        print('\nEnter 1 new alphabet only!\nEnter \'quit\' to give up\n')

def main():
    mistakes=[]
    progress=[]
    word=randomWord()
    for each in enumerate(word):
        progress.append('_')
    guess=''
    while not guess=='quit':
        display(progress,mistakes)
        print(word)
        if progress.count('_')==0:
            print("You won!")
            break
        if len(mistakes)>9:
            break
        guess=getGuess(progress,mistakes)
        if word.__contains__(guess):
            ind=0
            for letter in enumerate(word):
                if letter[1]==guess:
                    progress[ind]=guess
                ind+=1
        else:
            mistakes.append(guess)
    print('\nThe word was: ',word,'\n')
    return

if __name__=="__main__":
    clrscr()
    print('Loading...\n')
    while 1:
        main()
        if not input('Wanna try again? y/n: ')=='y':break
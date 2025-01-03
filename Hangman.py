
def randomWord():
    import requests, random
    x=requests.get('https://randomtextgenerator.com/')
    lines=x.text.replace('<','>').split('>')
    words=[]
    found=False
    for line in lines:
        if found:
            if line.__contains__('RandomTextGenerator.com') and len(words)>0:
                while 1:
                    word=random.choice(words).strip()
                    if len(word)>2:
                        return word.lower()
            if line is not 'br':
                words.extend(line.replace('.','').split(' '))
        elif line.__contains__('div id="randomtext_box"'):
            found=True
    return ''

def main():
    mistakes=[]
    progress=[]
    

if __name__=="__main__":
    import os
    os.system('cls')
    main()
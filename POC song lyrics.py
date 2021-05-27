
import pygame
l={}
lyrics={}
with open('Singer_name.txt','r',encoding='utf-8') as s:
    for i in s:
        temp = i[:-1].split(",")
        l[temp[0]] = temp[1]
with open('Song_lyrics.txt','r',encoding='utf-8') as a:
    for i in a:
        temp = i[:-1].split(",")
        lyrics[temp[0]] = temp[1]

pygame.mixer.init()
def play(songname):
    songname=songname.split(" ")
    pygame.mixer.music.load(f"music/{songname[0][2:]}.mp3")
    pygame.mixer.music.play(loops=0)
name=input("Enter your name : ")
print()
print(f'Welcome {name} Please select your song... ')
print()
for j in l.keys():
    print(j,'\n')
'''def lyrics_gen():
    global lyrics
    global l'''
 

while True:
    n=[]
    q=input("Enter '*' to continue or q to quit : ").lower().strip()
    if q=='*':
        pygame.mixer.music.stop()
        select=int(input("Please enter song Number : "))
        for g in l.keys():
            n.append(g)
           #print(n)
        print(f"\n{'-'*10}{n[select-1]}{'-'*10}\n")
        x=lyrics.get(f'{select}')
        print(x)
        play(n[select-1])

    elif q=='q':
        pygame.mixer.music.stop()
        break
    else:
        print('incorrect input')
 

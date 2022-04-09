#Let's Shuffle ccc08j2

import sys
from typing import List

def shuffle(playlist: List[str], button: str)-> List[str]:
    
    if button == '1':
        temp = playlist.pop(0)
        playlist.append(temp)
        return playlist

    if button == '2':
        temp = playlist.pop(-1)
        playlist.insert(0,temp) 
        return playlist

    if button == '3':
        temp = playlist[0]
        playlist[0] = playlist[1]
        playlist[1] = temp
        return playlist

    if button == '4':
        return playlist  

play_List = ["A", "B", "C", "D", "E"]

while True:
    b = input("")
    n = int(input(""))
    
    if b == '4' and n == 1:
        print(" ".join(play_List))
        break
    else:
        for _ in range(n):
            play_List = shuffle(play_List,b)    


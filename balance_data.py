import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('training2_data.npy')

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
forwards = []
forward_rights=[]
forward_lefts=[]
reverse=[]
reverse_right=[]
reverse_left=[]
nokey=[]
shuffle(train_data)
print(len(train_data))

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [0,0,0,0,0,0,1,0,0]:
        lefts.append([img,choice])
    elif choice == [1,0,0,0,0,0,0,0,0]:
        forward_rights.append([img,choice])
    elif choice == [0,0,0,0,1,0,0,0,0]:
        forwards.append([img,choice])
    elif choice == [0,1,0,0,0,0,0,0,0]:
        forward_lefts.append([img,choice])
    elif choice == [0,0,1,0,0,0,0,0,0]:
        reverse_right.append([img,choice])
    elif choice==[0,0,0,1,0,0,0,0,0]:
        reverse_left.append([img,choice])
    elif choice == [0,0,0,0,0,1,0,0,0]:
        reverse.append([img,choice])
    elif choice == [0,0,0,0,0,0,0,1,0]:
        rights.append([img,choice])
    elif choice == [0,0,0,0,0,0,0,0,1]:
        nokey.append([img,choice])
    else:
        print('no matches')


forwards = forwards[:len(lefts)][:len(rights)][:len(forward_rights)][:len(reverse_right)][:len(reverse)][:len(reverse_left)][:len(forward_lefts)][:len(nokey)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]
forward_rights = forward_rights[:len(forwards)]
forward_lefts=forward_lefts[:len(forwards)]
reverse=reverse[:len(forwards)]
reverse_right=reverse_right[:len(forwards)]
reverse_left=reverse_left[:len(forwards)]
nokey=nokey[:len(forwards)]


final_data = forwards + lefts + rights + reverse + forward_rights + forward_lefts + reverse_right + reverse_left + nokey
shuffle(final_data)

print(len(final_data))

np.save('train_final2.npy', final_data)





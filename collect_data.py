import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os







def keys_to_output(keys):

    
    output = [0,0,0,0,0,0,0,0,0]

    if 'W' in keys and 'A' in keys:
        output[5] = 1
    elif 'W' in keys and 'D' in keys:
        output[6] = 1
    elif 'S' in keys and 'A' in keys:
        output[7] = 1
    elif 'S' in keys and 'D' in keys:
        output[8] = 1
    elif 'W' in keys:
        output[0] = 1
    elif 'S' in keys:
        output[1] = 1
    elif 'A' in keys:
        output[3] = 1
    elif 'D' in keys:
        output[4] = 1
    else:
        output[8] = 1
    return output
file_name = 'training1_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    print('STARTING!!!')
    while(True):
        
        if not paused:
            screen = grab_screen(region=(0,40,800,600))
            last_time = time.time()
            screen = cv2.resize(screen, (480,480))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen,output])
            last_time = time.time()


            if len(training_data) % 100 == 0:
                print(len(training_data))
                np.save(file_name,training_data)
                   
                    

                    
        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)


main()

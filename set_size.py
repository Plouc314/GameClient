# set the size of the game window according to the screen resolution

done = False

while not done:
    resolution = input('Enter resolution (ex: 1920x1080): ')
    resolution = resolution.split('x')
    try:
        x = int(resolution[0])
        y = int(resolution[1])
        done = True
    except:
        print('Incorrect values.')

ratio_x = x/3000
ratio_y = y/1600

ratio =  min(ratio_x, ratio_y)*.8

import platform

os = platform.system()
if os == "Windows":
    font_factor = 1.3
elif os == "Darwin":
    font_factor = 1

try:
    with open("GameClient/parameters.txt","w") as file:
	file.write(str(ratio)+"\n")
	file.write(str(font_factor))
except:
    print("Can't open GameClient/parameters.txt file")
	

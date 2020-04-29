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

ratio =  min(ratio_x, ratio_y)*.9

try:    
    with open('GameClient/screen_factor.txt', 'w') as file:
        file.write(str(ratio))
except:
    print("Can't open 'GameClient/screen_factor.txt' file")

from interface import Interface, TextBox, Button, InputText, Cadre, C, Font, Dimension, set_screen
import pygame
import requests

pygame.init()

E = lambda x: int(x*Dimension.f) 
dim = Dimension((E(3000),E(1600)))
Font.init(dim.f)

inter = Interface()

DIM_SCREEN = (E(800), E(400))
screen = pygame.display.set_mode(DIM_SCREEN)
screen.fill(C.WHITE)
pygame.display.set_caption('Update')

set_screen(screen)

DIM_TC = (E(400), E(60))

text_conn = TextBox(DIM_TC, C.WHITE, (E(200),E(100)), 'Connecting...', font=Font.f30)

text_fail_conn = TextBox(DIM_TC, C.WHITE, (E(200),E(100)), 'Connection failed', font=Font.f30)

text_search = TextBox(DIM_TC, C.WHITE, (E(200),E(100)), 'Looking for update...', font=Font.f30)

text_finish = TextBox(DIM_TC, C.WHITE, (E(200),E(100)), 'Game up to date.', font=Font.f30)

text_update = TextBox(DIM_TC, C.WHITE, (E(200),E(100)), 'Installing updates...', font=Font.f30)

state = 'inconn'

#get the current game version
with open('version.txt') as file:
    current_version = file.read()

delay = 0

def run_update():
    contents = {}
    contents['interface'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/interface.py')
    contents['main'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/main.py')
    contents['base'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/base.py')
    contents['client'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/client.py')
    contents['friends'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/client.py')
    contents['chat'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/chat.py')
    contents['helper'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/helper.py')
    contents['menu'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/menu.py')
    contents['teams'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/teams.py')
    contents['game/game_menu'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/game/game_menu.py')
    contents['game/main'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/game/main.py')
    contents['game/helper'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/game/helper.py')
    contents['game/platform'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/game/platform.py')
    contents['game/player'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/game/player.py')
    contents['game/score'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/game/score.py')
    contents['game/weapons'] = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/game/weapons.py')
    
    for path, content in contents.items():
        with open(path+'.py', 'w') as file:
            file.write(content.text)

while inter.running:
    pressed, events = inter.run()
    if state == 'inconn':
        text_conn.display()
        try:
            from client import Client
            state = 'conn'
            text_search.display()
        except:
            state = 'fail'
    elif state == 'fail':
        text_fail_conn.display()
    elif state == 'conn':
        text_update.display()
        client = Client()
        version = client.get_version()
        print('SERVER:',version, 'LOCAL:',current_version)
        if version == current_version:
            state = 'ok'
            delay = 0
        else:
            # need to update the game
            text_update.display()
            state = 'updating'
    elif state == 'ok':
        delay += 1
        if delay == 15:
            inter.running = False
        text_finish.display()
    elif state == 'updating':
        text_update.display()
        run_update()
        # set new version
        with open('version.txt','w') as file:
            file.write(version)
        inter.running = False
        



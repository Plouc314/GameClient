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

def get_imgs_index(infos):
    for i, info in enumerate(infos):
        if info == 'imgs':
            return i

def get_infos():
    infos = requests.get('https://raw.githubusercontent.com/Plouc314/SocketGame/master/info.txt').text
    infos = infos.split('\n')
    server_version = infos[0]
    img_index = get_imgs_index(infos)
    file_names = infos[1:img_index]
    img_names = infos[img_index+1:]
    return server_version, file_names, img_names

def run_update(file_names, img_names):
    # update python files
    contents = {}
    for fname in file_names:
        fname = fname.strip()
        text = requests.get(f'https://raw.githubusercontent.com/Plouc314/SocketGame/master/{fname}.py').text
        contents[fname] = text

    for path, content in contents.items():
        with open(path+'.py', 'w') as file:
            file.write(content)
    
    # update imgs
    for img_path in img_names:
        response = requests.get(f'https://raw.githubusercontent.com/Plouc314/SocketGame/master/{img_path}')
        if response.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(response.content)

inter.run()
text_conn.display()
while inter.running:
    pressed, events = inter.run()
    if state == 'inconn':
        text_conn.display()
        try:
            server_version, file_names, img_names = get_infos()
            state = 'conn'
        except:
            state = 'fail'
    elif state == 'fail':
        text_fail_conn.display()
    elif state == 'conn':
        text_update.display()
        if server_version == current_version:
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
        run_update(file_names, img_names)
        # set new version
        with open('version.txt','w') as file:
            file.write(server_version)
        inter.running = False
        



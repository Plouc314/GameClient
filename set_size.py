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
    
    with open('interface.py') as file:
        content = file.read()
    content = content.replace('##RATIO##',str(ratio))
    print(content)
    
    with open('interfarce.py', 'w') as file:
        file.write(content)
except:
    print("Can't open interfarce.py file")
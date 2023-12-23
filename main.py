try:
    from ursina import *
except ImportError:
    #installs ursina if it isn't installed
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'ursina'])
    from ursina import *
import random
import os
import random
import time
import threading

app = Ursina()

# Create a window

def randomize():
    #picks a random picture from the assets/towers/earlygame folder and sets it as the texture for the slot1 entity
    slot1.alpha = 1
    for i in range(random.randint(1, 50)):
        slot1.texture = random.choice(os.listdir('assets\\towers\\earlygame\\'))
        time.sleep(0.01)
    slot2.alpha = 1
    for i in range(random.randint(1, 50)):
        slot2.texture = random.choice(os.listdir('assets\\towers\\midgame'))
        time.sleep(0.01)
    slot3.alpha = 1
    for i in range(random.randint(1, 50)):
        slot3.texture = random.choice(os.listdir('assets\\towers\\midgame'))
        time.sleep(0.01)
    slot4.alpha = 1
    for i in range(random.randint(1, 50)):
        slot4.texture = random.choice(os.listdir('assets\\towers\\lategame'))
        time.sleep(0.01)
    slot5.alpha = 1
    for i in range(random.randint(1, 50)):
        slot5.texture = random.choice(os.listdir('assets\\towers\\support'))
        time.sleep(0.01)

def randomizeFullRandom():
    slot1.alpha = 1
    for i in range(random.randint(1, 50)):
        slot1.texture = random.choice(os.listdir('assets/towers/fullyrandom'))
        time.sleep(0.01)
    slot2.alpha = 1
    for i in range(random.randint(1, 50)):
        slot2.texture = random.choice(os.listdir('assets/towers/fullyrandom'))
        time.sleep(0.01)
    slot3.alpha = 1
    for i in range(random.randint(1, 50)):
        slot3.texture = random.choice(os.listdir('assets/towers/fullyrandom'))
        time.sleep(0.01)
    slot4.alpha = 1
    for i in range(random.randint(1, 50)):
        slot4.texture = random.choice(os.listdir('assets/towers/fullyrandom'))
        time.sleep(0.01)
    slot5.alpha = 1
    for i in range(random.randint(1, 50)):
        slot5.texture = random.choice(os.listdir('assets/towers/fullyrandom'))
        time.sleep(0.01)

def randomizeFullyRandomThreadStarter():
    threading.Thread(target=randomizeFullRandom).start()



def randomizeThreadStarter():
    threading.Thread(target=randomize).start()

    
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = False
#window.entity_counter.enabled = False
#window.collider_counter.enabled = False
window.color = color.rgb(255, 255, 255)
window.size = (800, 600)
window.title = 'Tower Battles tower randomizer'
window.cog_button.visible = False

mainScreen = Entity(model='quad', texture='assets\\menus\\mainRandomizerScreen', scale=(16, 12), z=1)


randomizeButton = Button(model="quad", scale=(0.31, 0.125), position=(0.03, -0.19), z=2, alpha=0)
randomizeButton.on_click = randomizeThreadStarter

settingsButton = Button(model="quad", scale=(0.31, 0.11), position=(0.03, -0.375), z=2, alpha=0)

slot1 = Entity(model='quad', scale=(2.555, 2.555), position=(-4.23, 2.12), z=-2, alpha=0)
slot2 = Entity(model='quad', scale=(2.555, 2.555), position=(0.19, 2.12), z=-2, alpha=0)
slot3 = Entity(model='quad', scale=(2.555, 2.555), position=(4.6, 2.12), z=-2, alpha=0)
slot4 = Entity(model='quad', scale=(2.555, 2.555), position=(-4.23, -1.88), z=-2, alpha=0)
slot5 = Entity(model='quad', scale=(2.555, 2.555), position=(4.6, -1.88), z=-2, alpha=0)

app.run()




input()
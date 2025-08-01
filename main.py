import time
import threading 
from pynput.mouse import Controller,Button
from pynput.keyboard import Listener, KeyCode


TOGGLE_KEY= KeyCode(char='t')

clicking=False
mouse=Controller()

def click():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)

def toggel_event(key):
    if key == TOGGLE_KEY:
        global clicking
        print("Toggle!" +str(clicking))
        clicking= not clicking
    elif key ==KeyCode(char='o'):
        print("Quiting")
        quit()

click_thread= threading.Thread(target=click)
click_thread.start()

with Listener(on_press=toggel_event) as listener:
    listener.join()
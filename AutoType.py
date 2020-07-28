import os
import sys
from pynput.keyboard import Key, Controller
from time import sleep
sleep(15)
typing_string = "This is the typing string"
send_amount = 5
keyboard = Controller()
for i in range(send_amount):
    sleep(0.1)
    auto_fraction = " "+str(i+1)+"/"+str(send_amount)
    keyboard.type(typing_string+auto_fraction)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(0.1)


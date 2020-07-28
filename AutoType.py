from pynput.keyboard import Key, Controller
from time import sleep
delay_before_type = 15 # This is the delay before auto-typing in seconds
sleep(delay_before_type)
typing_string = "This is the typing string" # This is the string which will be repeatedly typed
send_amount = 5 # This is the number of times it will be typed
keyboard = Controller()
for i in range(send_amount):
    sleep(0.1)
    auto_fraction = " "+str(i+1)+"/"+str(send_amount)
    keyboard.type(typing_string+auto_fraction)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(0.1)


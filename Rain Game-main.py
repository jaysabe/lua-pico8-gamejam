# Imports go at the top
from microbit import *
import random as r
import radio
import music
radio.config(group=42)
import sys as s

radio.on()
player = 2
rainx = r.randint(0,4)
rainy = -1
score = 0
inc_sec = 0
var = 0

# Code in a 'while True:' loop repeats forever
while True:
    inc_sec += 1
    inc_sec /= 10
    if button_a.was_pressed() and player > 0:
        display.set_pixel(player,4,0)
        player -= 1
    if button_b.was_pressed() and player < 4:
        display.set_pixel(player,4,0)
        player += 1
    display.set_pixel(player,4,9)

    # rain movement
    rainy += 1 
    if rainy < 5:
        display.set_pixel(rainx,rainy,9)
    if rainy > 0 and rainy < 6:
        display.set_pixel(rainx,rainy-1,0)
    if rainy == 4 and rainx == player:
        score += 1
    if rainy > 4:
        rainx = r.randint(0,4)
        rainy = -1

    if score > 4:
        # music.play(music.FUNERAL)
        display.scroll("You survived " + str(inc_sec))
        s.exit()
    sleep(100)
    
    
    
    if button_a.was_pressed() and button_b.was_pressed():
        radio.send('rain game fr')
        display.show('message sent.')
    
    rec_mess = radio.receive()
    if rec_mess:
        display.scroll(rec_mess)
    # Same:
        # cout << "This person is " << age << "years old." endl;
        # print(f"This person is {21} years old.")



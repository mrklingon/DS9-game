from adafruit_circuitplayground import cp
import time
import random
from bach import *

#Define colors
pink = (12,10,12)
gold = (50, 40, 5)
blue = (0,0,8)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)
white = (20,20,20)

color = [red,orange,gold,green,blue,white,pink]

def cycle(x):
    for i in range(x*10):
        cp.pixels[i%10] = random.choice(color)
        time.sleep(.1)

def blinknum(num,color):
    if num != 0:
        for i in range(num):
            cp.pixels.fill(color)
            time.sleep(.25)
            cp.pixels.fill(blank)
            time.sleep(.10)
    else:
        for i in range(10):
            cp.pixels[i] = color
            cp.pixels.show()
            time.sleep(.14)

        cp.pixels.fill(blank)


blinknum(1,red)
docage()
blinknum(2,green)
blinknum(3,blue)
cycle(1)

wrmhole = [5,6,7,8,9,0,1,2,3,4]
statcolor = blue

def showPos(station):
    cp.pixels.fill(blank)
    cp.pixels[station] = statcolor
    cp.pixels[wrmhole[station]] = (random.randrange(100),random.randrange(100),random.randrange(100))

while True:
    launch = False
    probe = green
    score = 0
    station = 0
    probes = 10

    while probes > 0:
        showPos(station)
        sdelta = random.randrange(3)-1
        station = station + sdelta
        if station > 9: station = 0
        if station < 0: station = 9

        if launch and steps >0:
            steps = steps - 1
            ppos = ppos + pdelta
            if ppos > 9: ppos = 0
            if ppos < 0: ppos = 9
            cp.pixels[ppos]=probe
            if ppos == wrmhole[station]:
                if not cp.switch: 
                    cycle(1)
                    playstring("cdefgabk",.1)
                else:
                    cycle(2)
                    
                score = score + 1
            if steps <= 0 : 
                launch = False
                probes = probes - 1
                

        if cp.button_a and launch == False:
            if not cp.switch: playnote("c",.1)
            launch = True
            steps = 4
            pdelta = 1
            ppos = station
            
        
        if cp.button_b and launch == False:
            if not cp.switch: playnote("c",.1)
            launch = True
            steps = 4
            pdelta = -1
            ppos = station
        
        time.sleep(.3)
    #game over, show score
    cp.pixels.fill(blank)
    for i in range(score):
        cp.pixels[i] = gold
    pause = True
    while pause:
        if cp.button_a or cp.button_b:
            pause = False

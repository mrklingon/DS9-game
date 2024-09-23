from adafruit_circuitplayground import cp
import time
import random

allnotes = [130.8128, 138.5913, 146.8324, 155.5635, 164.8138, 174.6141, 184.9972, 195.9977, 207.6523, 220, 233.0819, 246.9417, 261.6256, 277.1826, 293.6648, 311.127, 329.6276, 349.2282, 369.9944, 391.9954, 415.3047, 440, 466.1638, 493.8833, 523.2511]
notes = [ 261.6256, 277.1826, 293.6648, 311.127, 329.6276, 349.2282, 369.9944, 391.9954, 415.3047, 440, 466.1638, 493.8833, 523.2511]

Knote = "cCdDefFgGaAbk"



def playall():
    for i in range(len(notes)):
        cp.play_tone(notes[i],.25)

def swtune(x):
    for i in range(x):
        playstring("cgxfedk",.5)
        playstring("g",1)
        time.sleep(1)

def sttune(x):
    for i in range(x):
        playstring("cgAagdk",.5)
        time.sleep(1)

def playnote(note,dur):
    try:
        cp.play_tone(notes[Knote.index(note)],dur)
    except:
        time.sleep(dur)

def playstring(tune,time):
    for i in range(len(tune)):
        playnote(tune[i],time)

def compthink(cycles):
    for i in range (10*cycles):
        freq = random.randrange(200,1200)
        dur = random.uniform(.02,.125)
        cp.play_tone(freq,dur)

def docage():
    for i in range(random.randrange(12)):
        cp.play_tone(allnotes[random.randrange(len(allnotes))],1/(1+random.randrange(4)))
        # Write your code here :-)

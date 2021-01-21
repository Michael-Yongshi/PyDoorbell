# -*- coding: utf-8 -*-
# Input-output and time function for delay, audio library and system commands
from time import sleep
from os import system
import logging

# for handling the GPIO connections
from gpiozero import LED, Button
from signal import pause

# for sounds
from playsound import playsound

# set GPIO connection used for the button (with hold time) and led
button = Button(18, hold_time=2.5)
led = LED(4)

# set sound
sound = "/home/pi/mixkit doorbell sounds/mixkit-home-standard-ding-dong-109.wav"

def doorbell():

    # set the functions to be run by the button
    button.when_pressed = button_pressed
    button.when_held = button_held
    button.when_released = button_released
    
    # Listen for events of the button
    print(f"listening for visitors")
    pause()

def button_pressed():
    print("Button was pressed")

    # turn on led to signal the visitor
    led.on()

    # play music
    playsound(sound)

    # a break to prevent impatient visitors pressing to quickly
    # (playsound blocks the thread, so if a long sound / song adjust the break time accordingly!)
    sleep(10.0)

    # turn off led to signal the visitor ringing has ended
    led.off()

def button_held():
    print("Button was held")

def button_released():
    print("Button was released")

if __name__ == "__main__":
    
    try:
        doorbell()
    finally:
        print(f"doorbell error!")
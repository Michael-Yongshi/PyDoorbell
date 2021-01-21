# set up logging
import logging
logging.basicConfig(level=logging.DEBUG)

# system methods
import os.path
from time import sleep
from signal import pause

# for handling the GPIO connections
from gpiozero import LED, Button

# for sounds
from playsound import playsound


# set GPIO connection variables used for the button (with hold time) and led
button = Button(18, hold_time=2.5)
led = LED(4)

# set sound variable
sound = '~/sounds/disturbence.wav'

def doorbell():

    # set the functions to be run by the button
    button.when_pressed = button_pressed
    button.when_held = button_held
    button.when_released = button_released
    
    # Listen for events of the button
    logging.info('Listening for visitors')
    pause()

def button_pressed():
    logging.debug('Button was pressed')

    # turn on led to signal the visitor
    led.on()

    # play music
    play_sound()

    # a break to prevent impatient visitors pressing to quickly
    # (playsound blocks the thread, so if a long sound / song adjust the break time accordingly!)
    sleep(10.0)

    # turn off led to signal the visitor ringing has ended
    led.off()

def button_held():
    logging.debug('Button was held')

def button_released():
    logging.debug('Button was released')

def play_sound():

    # try to play the sound
    try:
        playsound(sound)
        logging.info(f"Sound was played")

    # trow an error if file cant be played
    except IOError:
        if os.path.isfile(sound) == True:
            logging.error(f"Sound file not accessible: {sound}")
        else:
            logging.error(f"Sound file is missing: {sound}")
        
if __name__ == "__main__":
    
    try:
        play_sound()
        doorbell()
    finally:
        logging.critical('Doorbell encountered a critical error!')
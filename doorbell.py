# set up logging
import logging
logging.basicConfig(level=logging.DEBUG)

# system methods
import os.path
import requests
from time import sleep
from signal import pause

# for handling the GPIO connections
from gpiozero import LED, Button

# for sounds
import simpleaudio

# set GPIO connection variables used for the button (with hold time) and led
button = Button(4, hold_time=2.5)
led = LED(18)

# set sound variable
sound = simpleaudio.WaveObject.from_wave_file('/home/pi/sounds/mixkit-home-standard-ding-dong-109.wav')

def doorbell():

    # set the functions to be run by the button
    button.when_pressed = button_pressed
    button.when_held = button_held
    button.when_released = button_released
    
    logging.debug('Doorbell program is initiated')
    pause()

def button_pressed():
    logging.debug('Button was pressed')

    # emit the event to Home Assistant
    emit_event()

    # turn on led to signal the visitor
    led_on()

    # play sound
    play_sound()

    # a break to prevent impatient visitors pressing to quickly
    delay = 10
    logging.debug(f'Going to sleep for {delay} seconds')
    sleep(delay)

    # turn off led to signal the visitor ringing has ended
    led_off()

def button_held():
    logging.debug('Button was held')

def button_released():

    # Signal that program is continuing to listen to events
    logging.info('Listening for visitors')

def led_on():

    led.on()
    logging.debug('Led is turned on')

def led_off():

    led.off()
    logging.debug('Led is turned off')

def play_sound():

    # try to play the sound
    try:
        logging.info(f'Sound is playing')
        play_obj = sound.play()
        play_obj.wait_done()
        logging.info(f"Sound was played")

    # trow an error if file cant be played
    except:
        logging.error(f"Sound couldn't be played")

        # Check if sound file exists
        if os.path.isfile(sound) == True:
            logging.error(f"Sound file not accessible: {sound}")
        else:
            logging.error(f"Sound file is missing: {sound}")

def emit_event():

    try:
        # default address for the rest api in default settings
        url = "http://homeassistant:8123/api/events/DOORBELL_PRESSED"

        # send the authorization token (long lived tokens in settings) and denote that we are sending data in the form of a json string
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkYWZjMWZhOTdiNzQ0N2MzYTdkMGM0NTZiOGI5MGY3NiIsImlhdCI6MTYxMjAxMTk3MiwiZXhwIjoxOTI3MzcxOTcyfQ.yKc0kqTgX5FCVbnP85pCw9bsWD-bKYkxBlXnUzNfxt8"
        headers = {
            "Authorization": f"Bearer {token}",
            "content-type": "application/json",
        }

        # send out the actual request to the api
        response = requests.post(url=url, headers=headers)

        logging.debug('Send event to home assistant')
        logging.debug(f"response: {response.text}")
        
    except:
        logging.debug('Couldnt send event to home assistant')

if __name__ == "__main__":

    doorbell()
    # try:
    #     doorbell()
    # finally:
    #     logging.critical('Doorbell encountered a critical error!')
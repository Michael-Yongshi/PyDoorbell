import simpleaudio

# set sound variable
sound = simpleaudio.WaveObject.from_wave_file('/home/pi/sounds/disturbence.wav')

play_obj = sound.play()
play_obj.wait_done()
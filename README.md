# PyDoorbell

## How to
### install a raspbian pi
install pip
```
sudo apt install python3-pip
```

### dependencies
install requirements
```
pip3 install playsound && pip3 install gpiozero && pip3 install rpi.gpio
```

or run the requirements file
```
pip3 install -r requirements.txt
```

NOTE:
On ubuntu there is a missing dependency for simpleaudio
```
sudo pip3 install -y python3-dev libasound2-dev
```

### copy repo
copy files from other pc (or install git and clone the repo)
```
scp pc:~/Doorbell/* ~/
```

### systemd script
on the pi, mv the service file to systemd
```
sudo mv ~/doorbell.service /etc/systemd/system/
```

enable the script
```
sudo systemctl enable doorbell.service
sudo systemctl start doorbell.service
```

## Optional functions
### add sounds
Move Wav3 or mp3 sounds to the 'sounds' folder

change the sound variable accordingly in doorbell.py
```
# set sound variable
sound = "/home/pi/sounds/soundfile.wav"
```

## Tested
Only test on 
Hardware: Raspberry Pi 2b
OS:Raspbian Buster 

## Licence
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
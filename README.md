# PyDoorbell

## How to
### install a raspbian pi
install pip
```
sudo apt install python3-pip
```

NOTE:
if using raspbian OS, there are missing python sound bindings
install gst sound bindings to enable playsound
```
sudo apt install python3-gst-1.0
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

### copy repo
copy files from other pc (or install git and clone the repo)
```
scp pc:~/Doorbell/* ~/
```

### systemd script
on the pi, mv the service to systemd
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

## Licence

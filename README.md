# PyDoorbell

## install a raspbian pi
install pip
```
sudo apt install python3-pip
```

## dependencies
install requirements
```
pip3 install playsound && pip3 install gpiozero && pip3 install rpi.gpio
```

or run the requirements file
```
pip3 install -r requirements.txt
```

## copy repo
copy files from other pc (or install git and clone the repo)
```
scp pc:~/Doorbell/* ~/
```

## systemd script
on the pi, mv the service to systemd
```
sudo mv ~/doorbell.service /etc/systemd/system/
```

enable the script
```
sudo systemctl enable doorbell.service
sudo systemctl start doorbell.service
```

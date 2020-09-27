# pi

## Hardware

+ Raspberry Pi Zero W
+ Waveshare Eink Shield 2.13 inch

## Github

Allow pushing to github

(add ssh-keygen -t rsa -b 4096 -C "your_email@example.com")
Add ./ssh/id_rsa.pub to Github known keys

## Scripts

Allow accessing scripts across system

Add folders to .bashrc

```
export PATH=$PATH:~/pi/display
export PATH=$PATH:~/pi
```

## Launch on boot

```
sudo crontab -e
```

Add…
```
@reboot /usr/bin/python /home/pi/pi/display/display $(/home/pi/pi/timestamp)

# Every minute
* * * * * /usr/bin/python /home/pi/pi/display/display $(/home/pi/pi/timestamp)
```

## E-Ink

Update absolute path to font

## Test

Display output of script

```
display $(ipaddress)
```

## Log Crontab
```
grep CRON /var/log/syslog
tail -f grep CRON /var/log/syslog
```

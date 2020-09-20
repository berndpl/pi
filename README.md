# pi

## Github

Allow pushing to github

(add ssh-keygen -t rsa -b 4096 -C "your_email@example.com")
Add ./ssh/id_rsa.pub to Github known keys

## Scripts

Allow accessing scripts across system

Add folders to .bashrc

```export PATH=$PATH:~/pi/display
export PATH=$PATH:~/pi
```

## Launch on boot

Add to /etc/rc.local

```
@reboot ~/pi/display/display $(timestamp)
@reboot ~/pi/display/display $(ipaddress)
```

## E-Ink

Update absolute path to font

## Test

Display output of script

```
display $(ipaddress)
```


----

#PI

Reboot
# 1ghzclock
Python clock script made for Raspberry Pi devices with waveshare 2.13inch V4 screen.

![1](https://i.ibb.co/fMgD6zD/image.png)

## How to use?

You have to clone the repository while in your Raspberry Pi:
```bash
git clone https://github.com/iodomi/1ghzclock
```
And you can run the script with:

Screen:
```bash
screen -S clock python 1ghzclock/main.py
```

Tmux:
```bash
tmux new -s clock python 1ghzclock/main.py
```

## Will there be support for diffrent screens?
Actually no, it's pretty easy to literally fork the project and add files for your own waveshare screen or any screen really.
*And i'm lazy ;w;*

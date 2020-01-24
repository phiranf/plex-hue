# Plex — Philips Hue Bridge

Simple python script to brighten or dim you Philips Hue Lights when you start or stop media on your PlexMediaServer.  
Requires a valid [Plex Pass](https://www.plex.tv/plex-pass/) subscription and [webhooks](https://support.plex.tv/articles/115002267687-webhooks/) enabled.

For now it just takes the current colors and dims or brigthen it. You can set a custom color in the [hsl color format](https://www.w3schools.com/colors/colors_hsl.asp).

## Installation

### Plex

Go to your Plex settings -> Webhooks and add a new webhook. Set the IP address of whatever device you plan to run the script on and use port 8090 and end it with `/postjson`. If the scripts runs on the same device as the PlexMediaServer just use localhost

**Example**  
http://localhost:8090/postjson

### Script

Find your Philips Hue Bridge IP address and insert it in `b = Bridge('IP_ADRESS')`. Then set the ID of the lightgroup you want to interact with.  
When you start the script it'll tell you which lights and lightgroups it found.

Run the script with python:  

```bash
python main.py
```

To run in the background use something like [nohup](https://linux.die.net/man/1/nohup):  

```bash
nohup python main.py &
```

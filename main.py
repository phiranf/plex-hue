import json

from phue import Bridge
from flask import Flask
from flask import request

b = Bridge('192.168.178.65')
app = Flask(__name__)

lightGroup = 1
transitionTime = transitiontime=20

def setupHueBridge():
    try:
        b.connect()
    except:
        print ("Could not connect to Hue Bridge")

    print "\nConnection to Hue Bridge successful\n"
    print "-------------------------"
    print "-------------------------\n"
    print "Following lights found:"
    for l in b.lights:
        print(l.name)
    print "-------------------------\n"

    print "Following groups were found:"
    for g in b.groups:
        print(g.name)
    print "-------------------------\n"

    print json.dumps(b.get_group(1), indent=4)

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    try:
        webhook = json.loads(request.form['payload'])
    except:
        print ("No payload found")

    handleIncomingPayload(webhook)

    return 'JSON posted', 200

def handleIncomingPayload(data):
    event = data['event']
    user = data['Account']['id']
    mediaType = data['Metadata']['type']
    image = data['Metadata']['thumb']

    print "\n\n------\nEvent: {} \nUser: {} \nMedia type: {} \nImage: {}\n------".format(event, user, mediaType, image)

    if event == 'media.play':
        hueMediaStart()
    elif event == 'media.pause':
        hueMediaPause()
    elif event == 'media.resume':
        hueMediaResume()
    elif event == 'media.stop':
        hueMediaStop()

def hueMediaPause():
    print "Media was paused."
    b.set_light( [1,2], 'bri', 254, transitionTime)
    b.set_light( 3, 'bri', 165, transitionTime)

    if b.get_group(lightGroup, 'on') == False:
        b.set_group(lightGroup, 'on', True)

def hueMediaStart():
    print "Media was started."
    b.set_light( [1,2], 'bri', 63, transitionTime)
    b.set_light( 3, 'bri', 50, transitionTime)

    if b.get_group(lightGroup, 'on') == False:
        b.set_group(lightGroup, 'on', True)


def hueMediaResume():
    hueMediaStart() # For now just handle it the same way as if the media was started

def hueMediaStop():
    hueMediaPause() # For now just handle it the same way as if the media was paused

setupHueBridge()
app.run(host='0.0.0.0', port= 8090)

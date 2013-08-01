from flask import Flask
import time
from libs.launcher import Thunder

app = Flask(__name__)

missile_launcher = Thunder()
try:
    missile_launcher.connect()
except ValueError:
    print "no connected"

@app.route('/launcher/left')
def left_move():
    missile_launcher.send_actions('left')
    return 'moved_left'

@app.route('/launcher/right')
def right_move():
    missile_launcher.send_actions('right')
    return 'moved_right'

@app.route('/launcher/up')
def up_move():
    missile_launcher.send_actions('up')
    return 'moved_up'

@app.route('/launcher/down')
def down_move():
    missile_launcher.send_actions('down')
    return 'moved_down'

@app.route('/launcher/fire')
def fire_action():
    missile_launcher.fire()
    return 'fire'

@app.route('/led/on')
def led_on():
    missile_launcher.led('on')
    return 'led on'

@app.route('/led/off')
def led_off():
    missile_launcher.led('off')
    return 'led off'

if __name__ == '__main__':
    app.run(host= '0.0.0.0')

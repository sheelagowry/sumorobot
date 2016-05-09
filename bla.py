import os
from time import sleep
from threading import Thread
from flask import Flask, render_template, Response
import json

class MotorThread(Thread):
    # This class generates PWM signal necessary for servo motors

    def __init__(self, pin=192):
        Thread.__init__(self)
        self.path = "/sys/class/gpio/gpio%d" % pin
        if not os.path.exists(self.path):
            with open("/sys/class/gpio/export", "w") as fh:
                fh.write(str(pin))
        with open(os.path.join(self.path, "direction"), "w") as fh:
            fh.write("out")
        self.speed = 0
        self.daemon = True
            
    def run(self):
        with open(os.path.join(self.path, "value"), "w") as fh:
          while True:
            if self.speed:
                fh.write("1")
                fh.flush()
                sleep(0.001 if self.speed > 0 else 0.002)
                fh.write("0")
                fh.flush()
                sleep(0.019 if self.speed > 0 else 0.018)
            else:
                sleep(0.020)

left = MotorThread(132)    # CSID0
r2 = MotorThread(133)   # CSID1
            
left.start()
r2.start()

app = Flask(__name__ )

@app.route("/style.css")
def css():
    return app.send_static_file('style.css')
@app.route("/javas.js")
def java():
    return app.send_static_file('javas.js')
@app.route("/")
def robot():
    return app.send_static_file('web.html')

@app.route("/left")
def command():
    left.speed = 1
    r2.speed = 1
    return "ok"
@app.route("/stop")
def stop():
    left.speed = 0
    r2.speed = 0
    return "ok"

@app.route("/go")
def go():
    left.speed = 1
    r2.speed = -1
    return "ok"

@app.route("/right")
def right():
    left.speed = -1
    r2.speed = -1
    return "ok"
@app.route("/back")
def back():
    left.speed = -1
    r2.speed = 1
    return "ok"
    




if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True, threaded = True)
        
        


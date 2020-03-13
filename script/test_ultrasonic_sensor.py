import time
from matrix_lite import gpio
# from RPI.GPIO as GPIO

class UltraSonicSensor:
    def __init__(self, trig, echo):
        self.TRIG = trig
        self.ECHO = echo
        gpio.setFunction(self.TRIG, 'DIGITAL')
        gpio.setFunction(self.ECHO, 'DIGITAL')
        gpio.setMode(self.TRIG, 'output')
        gpio.setMode(self.ECHO, 'input')
        print('GPIO set is OK: Trig os: ', self.TRIG, ' Echo is:', self.ECHO)
        time.sleep(0.3)
    
    def reading_sonic(self):
        gpio.setDigital(self.TRIG, 'ON')
        # GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        gpio.setDigital(self.TRIG, 'OFF')
        # GPIO.output(self.TRIG, False)
        print(gpio.getDigital(self.ECHO))

        while gpio.getDigital(self.ECHO) == 0:
            signaloff = time.time()
        
        while gpio.getDigital(self.ECHO) == 1:
            signalon = time.time()
        
        timepassed = signalon - signaloff
        distance = timepassed * 17000
        # GPIO.cleanup()
        print('distance is: ', distance)
        return distance


if __name__ == '__main__':
    UltraSonicSensor(15, 2).reading_sonic()

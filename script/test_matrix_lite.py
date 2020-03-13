from matrix_lite import led
from time import sleep
from math import pi, sin

everloop = ['black'] * led.length

ledAdjust = 0.0
if len(everloop) == 35:
    ledAdjust = 0.51 # MATRIX Creator
else:
    ledAdjust = 1.01 # MATRIX Voice

frequency = 0.375
counter = 0.0
tick = len(everloop) - 1

while True:
    # Create rainbow
    for i in range(len(everloop)):
        r = round(max(0, (sin(frequency*counter+(pi/180*240))*155+100)/10))
        g = round(max(0, (sin(frequency*counter+(pi/180*120))*155+100)/10))
        b = round(max(0, (sin(frequency*counter)*155+100)/10))

        counter += ledAdjust

        everloop[i] = {'r':r, 'g':g, 'b':b}

    # Slowly show rainbow
    if tick != 0:
        for i in reversed(range(tick)):
            everloop[i] = {}
        tick -= 1

    led.set(everloop)

    sleep(.035)

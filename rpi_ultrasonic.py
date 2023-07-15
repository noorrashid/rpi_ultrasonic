from gpiozero import DistanceSensor
from gpiozero import LED
from time import sleep

ultrasonic= DistanceSensor (echo=17, trigger=4)
red= LED(15)
while True:
    print(ultrasonic.distance)
    if ultrasonic.distance *100 <=10:
        red.on()
    else:
        if ultrasonic.distance *100 > 10:
            red.off()
    #sleep(1)
        

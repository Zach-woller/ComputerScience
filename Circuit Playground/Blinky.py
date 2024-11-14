import time


from adafruit_circuitplayground import cp


while True:
    time.sleep(0.367)
    cp.pixels.fill((0,8,0))
    time.sleep(.5)
    cp.pixels.fill((0))
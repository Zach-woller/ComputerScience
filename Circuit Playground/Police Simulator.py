import time


from adafruit_circuitplayground import cp


while True:
    cp.play_tone(500, .5)
    cp.pixels.fill((24,155,204))
    time.sleep(.5)
    cp.play_tone(900, .5)
    cp.pixels.fill((234,33,58))
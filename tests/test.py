import sys
sys.path.append("..")
import leglight
import time

theLights = leglight.discover(2)
print(theLights)
theLights[0].on()
time.sleep(1)
theLights[0].off()
time.sleep(1)

theLights[0].on()
theLights[0].brightness(5)
t = 3000
while t <= 7000:
    theLights[0].color(t)
    time.sleep(1)
    t += 500
time.sleep(1)

l = 1
while l <= 100:
    theLights[0].brightness(l)
    time.sleep(.1)
    l += 5

theLights[0].brightness(5)
theLights[0].color(4000)
theLights[0].off()

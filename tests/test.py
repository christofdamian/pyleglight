import sys

sys.path.append("..")
import leglight
import time
import logging

logging.basicConfig(level=logging.DEBUG)

# Find all lights on the network and print em out:
theLights = leglight.discover(2)
for aLight in theLights:
    print(aLight)
    print(
        "Light Status: On - {} // Brightness - {} // Temp - {}".format(
            aLight.isOn, aLight.isBrightness, aLight.isTemperature
        )
    )

# Lets pick one to turn on and off, basic stuff.
theLights[0].on()
time.sleep(1)
theLights[0].off()
time.sleep(1)

# Now we'll do a color temp test.
theLights[0].on()
theLights[0].brightness(5)
t = 3000
while t <= 7000:
    theLights[0].color(t)
    time.sleep(1)
    t += 500
time.sleep(1)

# Finally a brightness test
l = 1
while l <= 100:
    theLights[0].brightness(l)
    time.sleep(0.1)
    l += 5

# Reset the light to something sane and turn it off
theLights[0].brightness(5)
theLights[0].color(4000)
theLights[0].off()

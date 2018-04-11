# https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat

import time
import envirophat
from envirophat import analog, leds
analog.read(2)

out = open('enviro.log', 'w')
out.write('reading\n')

try:
  while True:
      leds.on()
      analogRead = analog.read(2)
      out.write('%f\n' % (analogRead))
      time.sleep(1)

except KeyboardInterrupt:
    leds.off()
    out.close()

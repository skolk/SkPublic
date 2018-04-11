#Day4
pressure sensor with datadog setup

hardware:
raspberry Pi Zero W (wifi!)
An analog to digital converter
A pressure sensor

set up the raspberry pi

write some code!
update the libraries

pip install datadog
pip install (whatever library you need for your ADC)
I usd a pidibah and got the library from xyz

raspbaerry pies don't have an analog port, only digital I/O's
this means you need to turn a analog signal (from the pressure sensor)
into a digital one (which must be transfered using I2C or SPI communication)

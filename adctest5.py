#!/usr/bin/python
# you have to include the spidev module
import spidev

# put these functions and variables  at the
# top of your python project or in another
# file and import it
A0 = 0
A1 = 1
A2 = 2
A3 = 3
A4 = 4
A5 = 5
A6 = 6
A7 = 7

def adcInit():
    connection = spidev.SpiDev()
    connection.open(0, 0)
    connection.max_speed_hz = 1350000
    connection.mode = 0b00
    return connection

def adcRead(connection, channel):
    assert 0 <= channel <= 7, 'ADC number has to be 0-7'
    ret = connection.xfer2([0x01, (8 + channel) << 4, 0x00 ])
    tmp = (ret[1] & 0x03) << 9
    tmp |= (ret[2] & 0xFF)
    return tmp
#-------------------------------------------------------

# only call adcInit() once in you project close to
# the top before calling adcRead()
adc = adcInit()
line1 = 0
line2 = 0
line3 = 0
line4 = 0
line5 = 0
line6 = 0
looptrue = True


while True:
    # the first argument to adcRead() is the reurn from adcInit()
    # the second argument is the analog pin to read A0-A7

    data = adcRead(adc, A0)
    data1 = adcRead(adc, A1)
    data2 = adcRead(adc, A2)

    data3 = adcRead(adc, A3)
    data4 = adcRead(adc, A4)
    data5 = adcRead(adc, A5)    
    if data >300:
    	print(data)
	print("lane1")
	lane1 = 1

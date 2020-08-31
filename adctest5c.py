#!/usr/bin/python
# you have to include the spidev module
import spidev
import time

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

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
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
start_time = time.time()
last_triger_time1 =start_time
last_triger_time2 =start_time
last_triger_time3 =start_time
last_triger_time4 =start_time
last_triger_time5 =start_time

while looptrue:
    # the first argument to adcRead() is the reurn from adcInit()
    # the second argument is the analog pin to read A0-A7
    data = adcRead(adc, A0)
    data1 = adcRead(adc, A1)
    data2 = adcRead(adc, A2)

    data3 = adcRead(adc, A3)
    data4 = adcRead(adc, A4)
    data5 = adcRead(adc, A5)
    if line1 == 0:
        if data >300:
            end_time = time.time()
            print(data)
            print("line1")
            line1 = 1
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
    if line2 == 0:
        if data1 >300:
            end_time = time.time()
            print(data1)
            print("line2")
            line2 = 1
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
    if line3 == 0:
        if data2 > 300:
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_lapsed_bitween_las_trigger = end_time -last_triger_time3
            last_triger_time3 = end_time
            time_convert(time_lapsed_bitween_las_trigger)
            if time_lapsed_bitween_las_trigger < 0.005:
                line3 = 1
                print(data2)
                print("line3")
                time_convert(time_lapsed)
    if line4 == 0:
        if data3 > 300:
            end_time = time.time()
            print(data3)
            print("line4")
            line4 = 1
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
    if line5 == 0:
        if data4 > 300:
            end_time = time.time()
            print(data4)
            print("line5")
            line5 = 1
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
    if line6 == 0:
        if data5 > 300:
            end_time = time.time()
            print(data5)
            print("line6")
            line6 = 1
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)

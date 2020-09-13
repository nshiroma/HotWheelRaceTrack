#!/usr/bin/python
# you have to include the spidev module
import spidev
import time

# put these functions and variables  at the
# top of your python project or in another
# file and import it
A={}
A[0]=0
A[1]=1
A[2]=2
A[3]=3
A[4]=4
A[5]=5
A[6]=6
A[7]=7

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
# initiazie the dictionaries
adc = adcInit()
line ={}
last_triger_time={}
data ={}
start_time = time.time()
input("Press Enter to start")
for x in range(1,7):
    print(x)
    line[x] = 0
    last_triger_time[x] = start_time
looptrue = True
while looptrue:
    # the first argument to adcRead() is the reurn from adcInit()
    # the second argument is the analog pin to read A0-A7
    for x in range(1, 7):
        data[x] = adcRead(adc, A[x-1])
    for y in range(1,7):
        if line[y] == 0:
            if data[y] > 300:
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_lapsed_bitween_las_trigger = end_time - last_triger_time[y]
                #            print(time_lapsed_bitween_las_trigger)
                last_triger_time[y] = end_time
                #            time_convert(time_lapsed_bitween_las_trigger)
                if time_lapsed_bitween_las_trigger < 0.005:
                    line[y] = 1
                    print(data[y])
                    #               print(time_lapsed_bitween_las_trigger)
                    linename ="LineNumber{}"
                    print(linename.format(y))
                    time_convert(time_lapsed)
#
    race_time=time.time()
    race_time_lasped = race_time-start_time
    if race_time_lasped > 30:
        looptrue = False
        print("Race time out")
# end of race if all six car reached goal line

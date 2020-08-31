# HotWheelRaceTrack
python project for IOT study
by using the IOT ( Raspberry PI ) and IR distance sensor 
20200830 - first race.
first race which confirm the functinality of sensors.
one of sensor line 3 (A2) is over senstive had tendencey so need to change or cange the code to 
compensate for the over senstive of line 3. 

for first race we used 4 lanes.
with same HW cars which is BMW2002. 
different color but same chassis and same casting. 



here is the result.
pi@HotWheels6Lanes:~ $ ./adctest5b.py
512
line3
692
line6
708
line1
676
line2
566
line5


order of crossing the finish lines are 
line 6 -> 1 > 2 > 5
( line 3 over sentive sensor ) 
confirmed with the slow motion.  


# HotWheelRaceTrack
python project for IOT study
by using the IOT ( Raspberry PI ) and IR distance sensor 
<br>
<h3>20200830 - first race.</h3>
<br>
first race which confirm the functinality of sensors.
one of sensor line 3 (A2) is over senstive had tendencey so need to change or cange the code to 
compensate for the over senstive of line 3. 

for first race we used 4 lanes.
with same HW cars which is BMW2002. 
different color but same chassis and same casting. 



here is the result.
pi@HotWheels6Lanes:~ $ ./adctest5b.py
<br>
512
<br>
line3
<br>
692
<br>
line6
<br>
708
<br>
line1
<br>
676
<br>
line2
<br>
566
<br>
line5

<br>
order of crossing the finish lines are 
<br>
line 6 -> 1 > 2 > 5
( line 3 over sentive sensor ) 
confirmed with the slow motion.  


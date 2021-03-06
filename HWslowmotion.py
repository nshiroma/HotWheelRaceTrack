#!/usr/bin/python
# Slow Motion
# For this to work you need to have MP4Box installed
# You can do this by using:
# sudo apt-get install gpac

import picamera
import subprocess # To be able to use MP4Box from within this script
import time

######################################
# Config data
######################################20200914
m_FPS = 180
m_resolutionX = 960/3
m_resolutionY = 540/3

######################################

# Init camera
camera = picamera.PiCamera()
camera.resolution = (m_resolutionX, m_resolutionY)
camera.framerate = m_FPS
camera.start_preview(fullscreen=False, window=(35, 40, 306, 228))

time.sleep(2) # Wait for camera to settle

# wait for the user input to start recording
raw_input("Press <ENTER> to start recording")

# This is the tricky part
camera.start_recording("tmp.h264") # record to temporary file
time.sleep(5) # pauses the program for 5 seconds.... the camera will record 5 second of video
camera.stop_recording() # stop the recording

# The recorded file is recorded with high fps speed. Now we need to change its properties
# so when playing it back it is played at a lower fps rate, so we get the slow motion effect.
# We will use tha MP4Box program to process our video
# The output will be at 15 fps for a more dramatic effect.

print "Processing video file. Please wait"
r = subprocess.call('rm video.mp4', shell=True) # delete any previous video of the same name
r = subprocess.call('MP4Box -fps 15 -add tmp.h264 video.mp4', shell=True) # process video and create new file
r = subprocess.call('rm tmp.h264', shell=True) # delete temporary file
print "Done!"
print "To play back your new video use\nomxplayer video.mp4"

camera.stop_preview()

import sys
import multiprocessing
import threading
import time
sys.path.insert(0, 'C:/Users/ishit/Desktop/DSS Server/Models/Smoking_Detector_Hand_Gesture_Full')
sys.path.insert(0,'C:/Users/ishit/Desktop/DSS Server/Screen Capture')
sys.path.insert(0,'C:/Users/ishit/Desktop/DSS Server/GPS')
sys.path.insert(0,'C:/Users/ishit/Desktop/DSS Server/Server')
from RunModel_Pic_Stream import startModel2
from ScreenGrab import startCapture_NEW
from Extract_GPS import GPS_TEST
from sendserver import sendimg

[tmp, gps] = GPS_TEST('C:/Users/ishit/Desktop/DSS Server/Capture/','M06D01h18m35s21')
sendimg('C:/Users/ishit/Desktop/DSS Server/Capture/',tmp,gps[0],gps[1])





# adding Folder_2 to the system path


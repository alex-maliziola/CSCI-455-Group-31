from maestro import Controller
import tkinter as tk
import time

#controls - 0(motor controll) , 1(motor control left right), 2(waist)
#3(headtilt up down), 4(hesd left rigth) 5(rigth shoulder) 6(right bicep)
#7(right elbow) 8(right upper forearm) 9(right wrist) 10(rigth gripper close) 11(left shoulder)
#12(left bicep) 13(left elbow) 14(left forearm) 15(left wrist) 16(left gripper)

class Tango:
    def __init__(self,face):
        self.head_loc = 5900
        self.tango = Controller()
        self.face = face

    def stabalize(self):
        self.tango.setTarget(2, 5900)
        self.tango.setTarget(3, 5900)
        self.tango.setTarget(4, 5900)
        self.tango.setTarget(5, 3000)
        self.tango.setTarget(6, 5900)
        self.tango.setTarget(7, 5900)
        self.tango.setTarget(8, 5900)
        self.tango.setTarget(9, 5900)
        self.tango.setTarget(10, 5900)
        self.tango.setTarget(11, 5900)
        self.tango.setTarget(12, 5900)
        self.tango.setTarget(13, 5900)
        self.tango.setTarget(14, 5900)
        self.tango.setTarget(15, 5900)
        self.tango.setTarget(16, 5900)

    def project_1(self):
        self.tango.setTarget(2, 5000)
        time.sleep(1)
        self.tango.setTarget(3, 5000)
        time.sleep(1)
        self.tango.setTarget(4, 5000)
        time.sleep(1)
        self.tango.setTarget(5, 5000)
        time.sleep(1)
        self.tango.setTarget(6, 5000)
        time.sleep(1)
        self.tango.setTarget(7, 5000)
        time.sleep(1)
        self.tango.setTarget(8, 5000)
        time.sleep(1)
        self.tango.setTarget(9, 5000)
        time.sleep(1)
        self.tango.setTarget(10, 5000)
        time.sleep(1)
        self.tango.setTarget(11, 5000)
        time.sleep(1)
        self.tango.setTarget(12, 5000)
        time.sleep(1)
        self.tango.setTarget(13, 5000)
        time.sleep(1)
        self.tango.setTarget(14, 5000)
        time.sleep(1)
        self.tango.setTarget(15, 5000)
        time.sleep(1)
        self.tango.setTarget(16, 100)


    def head_turn_right(self,event):
        self.face.toggle_sweating()
        self.head_loc = self.head_loc +10
        print(self.head_loc)
        self.tango.setTarget(4, self.head_loc)
        self.face.toggle_sweating()


    def head_turn_left(self,event):
        self.head_loc = self.head_loc - 10
        self.tango.setTarget(4, self.head_loc)

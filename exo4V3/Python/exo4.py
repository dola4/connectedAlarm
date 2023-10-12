from gpiozero import LED, Button
import time
#from time import sleep
from main import main 
import pyodbc
from datetime import datetime
import mysql.connector
import requests

class Alarm:
    
    def __init__(self):
        self.zone1 = Button(27)
        self.zone2 = Button(6)
        self.zone3 = Button(13)
        self.start = Button(19)
        self.ledA = LED(17)
        self.ledB = LED(5)
        self.ledC = LED(25)
        self.ledD = LED(16) 
        self.ledE = LED(20)
        self.ledF = LED(22)
        self.ledG = LED(26)
        self.point = LED(21)
        
    
    def allOff(self):
        self.ledA.on()
        self.ledB.on()
        self.ledC.on()
        self.ledD.on()
        self.ledE.on()
        self.ledF.on()
        self.ledG.on()
        self.point.on()
    
    def num0(self):
        self.ledA.off()
        self.ledB.off()
        self.ledC.off()
        self.ledD.off()
        self.ledE.off()
        self.ledF.off()
        self.ledG.on()
        self.point.on()
        
    def num1(self):
        self.ledA.on()
        self.ledB.off()
        self.ledC.off()
        self.ledD.on()
        self.ledE.on()
        self.ledF.on()
        self.ledG.on()
        self.point.on()
        
    def num2(self):
        self.ledA.on 
        self.ledB.off()
        self.ledC.on()
        self.ledD.off()
        self.ledE.off()
        self.ledF.on()
        self.ledG.off()
        self.point.on()
    
    def num3(self):
        self.ledA.off()
        self.ledB.off()
        self.ledC.off()
        self.ledD.off()
        self.ledE.on()
        self.ledF.on()
        self.ledG.off()
        self.point.on()
    
    def num4(self):
        self.ledA.on()
        self.ledB.off()
        self.ledC.off()
        self.ledD.on()
        self.ledE.on()
        self.ledF.off()
        self.ledG.off()
        self.point.on()
        
    def num5(self):
        self.ledA.off()
        self.ledB.on()
        self.ledC.off()
        self.ledD.off()
        self.ledE.on()
        self.ledF.off()
        self.ledG.off()
        self.point.on()
        
    def num6(self):
        self.ledA.off()
        self.ledB.on()
        self.ledC.off()
        self.ledD.off()
        self.ledE.off()
        self.ledF.off()
        self.ledG.off()
        self.point.on()
        
    def num7(self):
        self.ledA.off()
        self.ledB.off()
        self.ledC.off()
        self.ledD.on()
        self.ledE.on()
        self.ledF.on()
        self.ledG.on()
        self.point.on()
        
    def num8(self):
        self.ledA.off()
        self.ledB.off()
        self.ledC.off()
        self.ledD.off()
        self.ledE.off()
        self.ledF.off()
        self.ledG.off()
        self.point.on()
        
    def num9(self):
        self.ledA.on()
        self.ledB.off()
        self.ledC.off()
        self.ledD.off()
        self.ledE.on()
        self.ledF.off()
        self.ledG.off()
        self.point.on()
        
    def armed(self):
        self.ledA.on()
        self.ledB.off()
        self.ledC.off()
        self.ledD.on()
        self.ledE.off()
        self.ledF.off()
        self.ledG.off()
        self.point.on()    
        
    def compte(self):
        self.num1()
        time.sleep(1)
        self.num2()
        time.sleep(1)
        self.num3()
        time.sleep(1)
        self.armed()
        
    def decompte(self):
        self.num3()
        time.sleep(1)
        self.num2()
        time.sleep(1)
        self.num1()
        time.sleep(1)
        self.num0()
    
    def sendData(self, moment, zone, status):
        url = "http://169.254.22.229:44939/Home/UpdateAlarm"
        data = {
            "id": 1,
            "status": status,
            "zone": zone,
            "moment": moment                       
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            print("Les données ont été insérées avec succès.")
        else:
            print(f"Error: {response.status_code}")

    def catchData(self):
        url = "http://169.254.22.229:44939/Home/SendData"
        params = {
            "id": 1
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data
        
    
    def checkState(self, zone, state):
        def reset_state():
                nonlocal state
                state = 0
        
        if state == 0:
            self.start.when_pressed = lambda: (self.decompte(), self.sendData(datetime.now(), None, 1))
            state = 1
            self.point.off()
            self.sendData(datetime.now(), None, state)

        elif state == 1 and zone == "zone1":
            self.num1()
        elif state == 1 and zone == "zone2":
            self.num2()
        elif state == 1 and zone == "zone3":
            self.num3()

        else:
            self.zone1.when_pressed = lambda: (self.num1(), self.sendData(datetime.now(), 'zone1', 1))
            self.zone2.when_pressed = lambda: (self.num2(), self.sendData(datetime.now(), 'zone2', 1))
            self.zone3.when_pressed = lambda: (self.num3(), self.sendData(datetime.now(), 'zone3', 1))
            self.start.when_pressed = lambda: (self.compte(), self.point.on(), self.sendData(datetime.now(), None, 0), reset_state())


def start():
    alarm = Alarm()
    data = alarm.catchData()
    zone = data['zone']
    status = data['status']
    alarm.checkState(zone, status)
    
if __name__ == '__main__':
    start()
        
        
from gpiozero import LED, Button
import time
from datetime import datetime
import requests

class Alarm:
    
    def __init__(self):
        self.zone1 = Button(27)
        self.zone2 = Button(6)
        self.zone3 = Button(13)
        self.start = Button(19)
        self.leds = [LED(x) for x in [17, 5, 25, 16, 20, 22, 26]]
        self.point = LED(21)

    def allOff(self):
        for led in self.leds:
            led.on()
        self.point.on()

    def display_num(self, num):
        nums = [
            '0111111', '0000110', '1011011', '1001111',
            '1100110', '1101101', '1111101', '0100111',
            '1111111', '1101111', '1100110'
        ]
        if 0 <= num <= 9:
            code = nums[num]
        else:  # Display armed
            code = nums[10]
        for i, led in enumerate(self.leds):
            if code[i] == '0':
                led.off()
            else:
                led.on()
        self.point.on()

    def compte(self):
        for i in range(1, 4):
            self.display_num(i)
            time.sleep(1)
        self.display_num(-1)  # Display armed
        
    def decompte(self):
        for i in range(3, 0, -1):
            self.display_num(i)
            time.sleep(1)
        self.display_num(0)

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

    if not state:
        self.start.when_pressed = lambda: (self.decompte(), self.sendData(datetime.now(), None, 1))
        state = 1
        self.point.off()
        self.sendData(datetime.now(), None, state)
    elif zone in ['zone1', 'zone2', 'zone3']:
        self.display_num(int(zone[-1]))
    else:
        for i, btn in enumerate([self.zone1, self.zone2, self.zone3], 1):
            btn.when_pressed = lambda i=i: (self.display_num(i), self.sendData(datetime.now(), f'zone{i}', 1))
            
        self.start.when_pressed = lambda: (self.compte(), reset_state(), self.point.on(), self.sendData(datetime.now(), None, 0))



def start():
    alarm = Alarm()
    data = alarm.catchData()
    zone = data['zone']
    status = data['status']
    alarm.checkState(zone, status)
    
if __name__ == '__main__':
    start()
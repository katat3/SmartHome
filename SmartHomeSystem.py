from Appliances import Light, AirConditioner, Curtain, CleaningRobot
from datetime import datetime, timedelta

class SmartHomeSystem:
    def __init__(self):
        self.name = 'SmartHomeSystem'
        self.devices = []

    def add_device(self, device):
            self.devices.append(device)

    def check_robot_schedule(self):
        if datetime.now().hour == 14:
            for device in self.devices:
                if isinstance(device, CleaningRobot):
                    if not device.turned_on:
                        device.turn_on()
                        device.start_cleaning()

        elif datetime.now().hour == 16:
            for device in self.devices:
                if isinstance(device, CleaningRobot) and device.turned_on:
                    device.return_to_base()

    #Home mode
    def home_mode(self):
        current_hour = datetime.now().hour
        night_time = current_hour >= 18 or current_hour < 7
        print("HOME MODE activated")

        for device in self.devices:
            if isinstance(device, AirConditioner):
                if device.location == 'Living Room':
                    device.turn_on()

            if isinstance(device, Curtain):
                if night_time:
                    device.closed()
                else:
                    device.open()

            if isinstance(device, Light):
                if night_time and device.location == 'Living Room':
                    device.turn_on()
                else:
                    device.turn_off()

    #pre sleep mode
    def pre_sleep_mode(self):
        print("PRE SLEEP MODE activated")
        for device in self.devices:
            if isinstance(device, Light):
                if device.location == 'Bedroom' and device.light_type == 'Lamp':
                    device.turn_on()
                    device.set_mode(30, "Warm Yellow")
                else:
                    device.turn_off()
                if isinstance(device, AirConditioner):
                    if device.location == 'Bedroom':
                        device.turn_on()
                    else:
                        device.turn_off()
                if isinstance(device, Curtain):
                    device.closed()

    #gaming mode
    def gaming_mode(self):
        print("GAME MODE activated")
        for device in self.devices:
            if isinstance(device, Light):
                if device.location == 'Study':
                    device.turn_on()
                else:
                    device.turn_off()

            if isinstance(device, AirConditioner):
                if device.location == 'Study':
                    device.turn_on()
                else:
                    device.turn_off()

            if isinstance(device, Curtain):
                device.closed()

    #sleep mode
    def sleep_mode(self):
        print("SLEEP MODE activated")
        for device in self.devices:
            device.turn_off()
            if isinstance(device, Curtain):
                device.closed()







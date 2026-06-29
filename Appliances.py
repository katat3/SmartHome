from Device import Device

class Light(Device):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.brightness = 100
        self.color_mode = "Warm White"

    def set_mode(self, brightness, color_mode):
        if self.turned_on:
            self.brightness = brightness
            self.color_mode = color_mode
            print(f'{self.name} is set to {self.brightness}% brightness and {self.color_mode} ')
        else:
            print(f'{self.name} cannot set because {self.name} is currently OFF.')

    def get_state(self):
        state =  super().get_state()
        return f'{state} | Brightness: {self.brightness} | Color: {self.color_mode} '



class AirConditioner(Device):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.temperature = 24

    def set_temperature(self, temperature):
        if self.turned_on:
            self.temperature = temperature
            print(f'{self.name} is set to {self.temperature} degrees C')
        else:
            print(f'{self.name} cannot set because {self.name} is currently OFF.')

class Curtain(Device):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.opening_percentage = 0

    def open(self):
        if self.turned_on:
            self.opening_percentage = 100
            print(f'{self.name} is now OPEN')
        else:
            print(f'{self.name} cannot open because {self.name} is already OPEN.')

    def closed(self):
        if self.turned_on:
            self.opening_percentage = 0
            print(f'{self.name} is now CLOSED')
        else:
            print(f'{self.name} cannot close because {self.name} is already CLOSED.')


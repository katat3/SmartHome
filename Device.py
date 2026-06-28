class Device:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'({self.name}) is already turned on.')
        else:
            self.turned_on = True
            print(f'({self.name}) is now turned on.')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'({self.name}) is now turned off.')
        else:
            print(f'({self.name}) is already turned on.')

    def get_state(self) -> str:
        state = "ON" if self.turned_on else "OFF"
        return f"{self.name} in {self.location} | statues: {state}"
from Appliances import Light, CleaningRobot, Curtain, AirConditioner
from Device import Device
from SmartHomeSystem import SmartHomeSystem

def main():
    my_home = SmartHomeSystem()

    living_room_lamp = Light("Living Room Lamp", "Living Room", "Lamp")
    living_room_ceiling_light = Light("Living Room Ceiling Light", "Living Room", "Ceiling Light")
    study_lamp = Light("Study Lamp", "Study", "Lamp")
    study_ceiling_light = Light("Study Ceiling Light", "Study", "Ceiling Light")
    bedroom_lamp = Light("Bedroom Lamp", "Bedroom", "Lamp")
    bedroom_ceiling_light = Light("Bedroom Ceiling Light", "Bedroom", "Ceiling Light")

    main_ac = AirConditioner("Main AC", "Living Room")
    study_ac = AirConditioner("Study AC", "Study")
    bedroom_ac = AirConditioner("Bedroom AC", "Bedroom")

    living_room_curtain = Curtain("Living Room Curtain", "Curtain")
    study_curtain = Curtain("Study Curtain", "Curtain")
    bedroom_curtain = Curtain("Bedroom Curtain", "Curtain")

    cleaning_robot = CleaningRobot("Cleaning Robot", "Living Room")

    my_home.add_device(living_room_lamp)
    my_home.add_device(living_room_ceiling_light)
    my_home.add_device(study_lamp)
    my_home.add_device(study_ceiling_light)
    my_home.add_device(bedroom_lamp)
    my_home.add_device(bedroom_ceiling_light)
    my_home.add_device(main_ac)
    my_home.add_device(study_ac)
    my_home.add_device(bedroom_ac)
    my_home.add_device(living_room_curtain)
    my_home.add_device(study_curtain)
    my_home.add_device(bedroom_curtain)
    my_home.add_device(cleaning_robot)

    print("Welcome to the Smart Home System")
    command = {
        "1": my_home.home_mode(),
        "2": my_home.gaming_mode(),
        "3": my_home.pre_sleep_mode() ,
        "4": my_home.sleep_mode() }

    while True:
        print("\nAvailable Mode:")
        print("1. Home Mode | 2. Gaming Mode | 3. Pre-Sleep Mode | 4. Sleep Mode | S. Current System State | E. Exit ")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "e":
            print("The system is shutting down. Goodbye!")
            break

        if choice == "s":
            for device in my_home.devices:
                print(device.get_state())

        if choice in command:
            command[choice]()
        else:
            print("Sorry, I did not understand. Please try again.")


if __name__ == "__main__":
    main()
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

    my_home.home_mode()
    my_home.gaming_mode()
    my_home.pre_sleep_mode()
    my_home.sleep_mode()
    my_home.check_robot_schedule()

    print("Current System State")
    for device in my_home.devices:
        print(device.get_state())

if __name__ == "__main__":
    main()
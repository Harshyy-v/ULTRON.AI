import psutil
from func.Speak import speak


def get_battery_percentage():
    battery = psutil.sensors_battery()
    if battery is not None:
        return battery.percent
    else:
        return None


def Batterymain():
    battery_percentage = get_battery_percentage()
    if battery_percentage is not None:
        print(f"Battery Percentage: {battery_percentage}%")
        speak(f"Battery Percentage is {battery_percentage}%")
    else:
        print("Could not retrieve battery information.")


if __name__ == "__main__":
    main()

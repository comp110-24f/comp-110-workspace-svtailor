"""practice with elif statements"""


def get_weather_report() -> str:
    """display weather instructions"""
    weather: str = input("What is the weather?")
    if (weather == "rainy") or (weather == "cold"):
        # check for equality, takes whats on either side of the or as bools
        print("Bring a jacket!")

    elif weather == "hot":
        print("Keep cool out there!")

    else:
        print("I don't recognize this weather")

    return weather


get_weather_report()

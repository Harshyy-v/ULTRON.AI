import datetime
from func.Speak import speak


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        print("ULTRON : Good Morning,sir ")
        speak("Good Morning,sir")

    elif 12 < hour <= 18:
        print("ULTRON : Good Afternoon ,sir ")
        speak("Good Afternoon ,sir")


    else:
        print("ULTRON : Good Evening,sir")
        speak("Good Evening,sir")

    print("ULTRON : Please tell me, How can I help you ?")
    speak("Please tell me, How can I help you ?")

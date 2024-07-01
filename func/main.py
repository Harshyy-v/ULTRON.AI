from Speak import speak, micexecution
from commands import searchpls
from commands.greetme import greetMe
from commands.whatsapp import ask_user_and_send_message
from commands.time import fetch_time
from commands.mausam import scrape_weather
from commands.temperature import taapmaan
from commands.alarmapp import main
import commands.searchpls
from commands.appopener import openapp, closeapp
from commands.systemInfo import print_system_info
from commands.selfie import take_selfie
from commands.screenShot import take_screenshot
from commands.samachaar import Samachaarmain
from commands.planTrip import Tripmain
from commands.notepad import write_to_notepad
from commands.net_ki_raftaar import raftaar
from commands.movies import Moviesmain
from commands.kasrat import ExerciseMain
from commands.jokes import JokeMain
from commands.intro import introduce_ultron
from commands.gaanaChalade import gaane
from commands.controlvolume import volumeMain
from commands.brightness import BrightnessMain
from commands.battery import Batterymain


# from Chat import Chat

if __name__ == '__main__':

    greetMe()

    while True:
        query = micexecution()
        text = query.lower()

        if "hello".lower() in text:
            print(f"ULTRON : Hello sir, how are you ?")
            speak("Hello sir, how are you ?")
        if "i am fine".lower() in text:
            print(f"ULTRON : That's great, sir")
            speak("That's great, sir")
        if "how are you".lower() in text or "What is the solution".lower() in text:
            print(f"ULTRON : Perfect, sir ")
            speak("Perfect, sir")
        if "thank you".lower() in text or "thank".lower() in text:
            print(f"ULTRON : You are welcome, sir")
            speak("You are welcome, sir")

        if ("tell me time".lower() in text or "what is the time".lower() in text or "tell me the time".lower() in text
                or "time".lower() in text):
            fetch_time()

        if ("stop".lower() in text.lower() or "no thanks".lower() in text.lower() or "nothing".lower() in text.lower()
                or "can go".lower() in text):
            print("Execution stopped...")
            speak("Execution stopped..")
            exit()

        if "google".lower() in text:
            searchpls.searchGoogle()
        if "youtube".lower() in text:
            searchpls.searchYoutube()
        if "wikipedia".lower() in text:
            searchpls.searchWikipedia()

        if "temperature".lower() in text:
            taapmaan()
        if "weather".lower() in text:
            scrape_weather()

        if "close".lower() in text or "close the".lower() in text or "close app".lower() in text:
            closeapp()
        if ("open".lower() in text or "drive".lower() in text or "open the".lower() in text or "run app".lower() in text
                or "open app".lower() in text):
            openapp()

        if "alarm".lower() in text or "alaram".lower() in text:
            main()

        if "send message".lower() in text or "whatsapp".lower() in text or "message".lower() in text:
            ask_user_and_send_message()

        if "system".lower() in text or "device".lower() in text:
            print_system_info()

        if "selfie".lower() in text:
            take_selfie()

        if "screenshot".lower() in text:
            take_screenshot()

        if "news".lower() in text or "headlines".lower() in text:
            Samachaarmain()

        if "trip".lower() in text or "journey".lower() in text:
            print("Sure Sir . PLease fill-up these questions :-")
            speak("Sure Sir . PLease fill-up these questions .")
            Tripmain()

        if "note".lower() in text or "write".lower() in text:
            print("Sure Sir . Opening Notepad. ")
            speak("Sure Sir . Opening Notepad. ")
            write_to_notepad()

        if "speed".lower() in text:
            raftaar()

        if "movie".lower() in text or "film".lower() in text:
            Moviesmain()

        if "exercise".lower() in text or "work out".lower() in text or "workout".lower() in text:
            ExerciseMain()

        if "joke".lower() in text:
            JokeMain()

        if "who are you".lower() in text or "yourself".lower() in text or "introduction".lower() in text:
            introduce_ultron()

        if "songs".lower() in text or "song".lower() in text:
            gaane()

        if "volume".lower() in text or "sound".lower() in text:
            volumeMain()

        if "brightness".lower() in text:
            BrightnessMain()

        if "battery".lower() in text:
            Batterymain()

        # getchat  = Chat(text)
        #
        # if getchat!= None:
        #     print(f"ULTRON :{getchat[0]}")
        #     speak(getchat[0])
        # else:
        #     print(f"ULTRON :{getchat[0]}")
        #     speak(getchat[0])

from func.Speak import speak


def introduce_ultron():
    introduction = """
    Hello, I am Ultron, your virtual assistant.
    I can help you with various tasks like taking notes, setting reminders, and much more.
    Just tell me what you need, and I will do my best to assist you.
    By the way, Hershi is my creator. I was designed and developed to make your life easier.
    """
    print(introduction)
    speak(introduction)



import pyttsx3
engine=pyttsx3.init()
rate=engine.getProperty('rate')
volume=engine.getProperty('volume')
engine.setProperty('rate',200)
engine.setProperty('volume',0.9)
engine.say("hello there my name is emaad")
engine.runAndWait()

# import pyjokes
# print(pyjokes.get_joke())


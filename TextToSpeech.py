#import pyttsx
import pyttsx

#initiate the tts engine
ttsEngine =  pyttsx.init()

#put words to speak by the tts engine
ttsEngine.say("Hello World")

ttsEngine.runAndWait()
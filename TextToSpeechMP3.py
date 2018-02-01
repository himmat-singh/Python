from gtts import gTTS

import os

tts = gTTS(text="Hello, world", lang="en")

tts.save("Hello.mp3")

os.system("mpg321 Hello.mp3")
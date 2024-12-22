from gtts import gTTS
import os

text = "Привет! Проверка звука."
tts = gTTS(text, lang="ru")
tts.save("output.mp3")
os.system("start output.mp3")  # Воспроизводит звук на Windows

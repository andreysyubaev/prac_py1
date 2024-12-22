import os
import random
import speech_recognition as sr
from gtts import gTTS

def speak(text, language="ru"):
    """Функция синтеза речи с использованием gTTS."""
    tts = gTTS(text=text, lang=language)
    tts.save("response.mp3")
    os.system("start response.mp3")

def listen_online(recognizer, mic, lang="ru-RU"):
    """Распознавание речи онлайн."""
    with mic as source:
        print("Слушаю (online)...")
        audio = recognizer.listen(source)
    try:
        print("Распознаю...")
        return recognizer.recognize_google(audio, language=lang)
    except sr.UnknownValueError:
        return "Не удалось распознать речь"
    except sr.RequestError:
        return "Ошибка сервиса Google Speech Recognition"

def coin_toss():
    """Подбрасываем монетку."""
    result = random.choice(["Орёл", "Решка"])
    return result

def main():
    """Главная функция ассистента."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Выберите режим: online или offline")
    mode = input("Введите режим (online/offline): ").strip().lower()

    if mode not in ["online", "offline"]:
        print("Неверный режим. Завершение программы.")
        return

    language = "ru-RU"  # По умолчанию русский язык
    while True:
        if mode == "online":
            command = listen_online(recognizer, mic, language)
        else:
            print("Offline режим пока не реализован.")
            break

        if "привет" in command.lower():
            speak("Привет! Чем могу помочь?")
        elif "пока" in command.lower():
            speak("До свидания!")
            break
        elif "подбрось монетку" in command.lower():
            result = coin_toss()
            speak(f"Результат: {result}")
        elif "сменить язык" in command.lower():
            speak("На какой язык вы хотите переключиться? Например, русский или английский.")
            new_lang = input("Введите новый язык (ru/en): ").strip().lower()
            if new_lang == "ru":
                language = "ru-RU"
                speak("Язык изменён на русский.")
            elif new_lang == "en":
                language = "en-US"
                speak("Language changed to English.")
            else:
                speak("Язык не распознан.")
        else:
            speak("Извините, я не понял вашу команду.")

if __name__ == "__main__":
    main()

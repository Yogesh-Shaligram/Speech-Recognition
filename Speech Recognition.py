import speech_recognition as sr
import random

print("Speech Recognition Game based on Addition")

x = 10
count = 0
flag = 0
r = sr.Recognizer()

with sr.Microphone() as source:
    while (1):
        try:
            a = int(random.random() * x)
            b = int(random.random() * x)
            print(a, "+", b)
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if (int(text) == a + b):
                count += 1
            print("I heard this", int(text), "Correct answer is =", a + b)
            print("Your score is =", count)
            if (count % 5 == 0):
                x *= 10
        except:
            print("Could not detect! Correct answer is =", a + b)
            print("Your score is ", count)
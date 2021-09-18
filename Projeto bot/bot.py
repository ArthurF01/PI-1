from chatterbot import trainers
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS

bot = ("ChatBot")

def ouvi_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Microfone...")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt-br')
        print('humano: ' + frase)
    except sr.UnknownValueError:
        print('bot: Erro')
    return frase

def cria_audio(audio):
    tts= gTTS(audio, lang="pt-br")
    tts.save('bot.mp3')
    playsound('bot.mp3')

tag = ['teste', 
			'isso e um teste',]

trainer = ListTrainer(bot)
trainer.train(tag)


while True:
    quest = ouvi_microfone()
    resposta = bot.get_response(quest)
    cria_audio(resposta)
    print('bot: ', resposta)

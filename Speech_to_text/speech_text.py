# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:22:19 2019

@author: Rudrajit
"""
import speech_recognition as sr
#audio_file=("sample.wav")#use audio file as source
#print(audio_file)
r=sr.Recognizer()#initialize recognizer

with sr.Microphone() as source:
    #audio=r.record(source)#reads the audio file
        print("Listening...")
        #r.pause_threshold=1 # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)

try:
    print("Audio file says:",r.recognize_google(audio))#converts and prints text
except UnknownValueError:
    print("Couldn't understand audio")
except sr.RequestError:
    print("Couldn't get results from google")
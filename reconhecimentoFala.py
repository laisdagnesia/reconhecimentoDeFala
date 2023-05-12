import speech_recognition as sr  

# get audio from the microphone                                                                       
rec = sr.Recognizer()                                                                                   
#print(sr.Microphone().list_microphone_names())

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print('Estou ouvindo, pode falar! ')
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language='pt-BR')
    print('Você falou: ' + texto)
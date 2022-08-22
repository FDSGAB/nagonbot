import pyttsx3

def voice_start ():
    #Comandos de texto para voz　(Aqui precisa achar Japones na maquina de destiono, so funciona nessa assim)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[2].id)
    engine.setProperty("rate", 135)

    #Mensagem para avisar que o programa está rodando
    engine.say("わ、起きちゃった")
    print("\nナゴン:\nわ、起きちゃった")
    engine.runAndWait()

    return engine

def voice_answer (res,engine):
    engine.say(res)
    print("\nナゴン:\n" + res)
    engine.runAndWait()
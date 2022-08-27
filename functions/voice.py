import pyttsx3

class voice:
    #Comandos de texto para voz　(Aqui precisa achar Japones na maquina de destiono, so funciona nessa assim)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[2].id)
    engine.setProperty("rate", 135)

    def __init__(self,engine):
        #Mensagem para avisar que o programa está rodando
        engine = self.engine
        engine.say("わ、起きちゃった")
        print("\nナゴン:\nわ、起きちゃった")
        engine.runAndWait()

    def __repr__():
        pass
        

    def voice_answer (self,res):
        engine = self.engine
        engine.say(res)
        print("\nナゴン:\n" + res)
        engine.runAndWait()
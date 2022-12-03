import pyttsx3

class Voice():
   
    #Comandos de texto para voz　(Aqui precisa achar Japones na maquina de destiono, so funciona nessa assim)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[2].id)
    engine.setProperty("rate", 135)

    def __init__(self):
        #Mensagem para avisar que o programa está rodando
        self.engine.say("わ、起きちゃった")
        print("\nナゴン:\nわ、起きちゃった")
        self.engine.runAndWait()


    def __repr__(self):
        return "TTS class that is configurated to use " + self.voices[2].id + " japanese voice as the default voice."
        

    #Funcao de resposta do bot
    def voice_answer (self,res):
        self.engine.say(res)
        print("\nナゴン:\n" + res)
        self.engine.runAndWait()
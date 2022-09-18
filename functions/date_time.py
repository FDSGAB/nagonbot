from datetime import datetime

#Funções relacionadas a datas e tempo (retiradas do sistema)
def get_time (n:str) -> str:
    #Caso para devolver o horário
    if n == "時間":
        str = "今は" + datetime.now().strftime("%H:%M") + "です。"
    #Caso para devolver a data
    if n == "日付": 
        str = "今日は" + datetime.now().strftime("%Y-%m-%d") + "です。"
    #Caso para devolver o nome do dia da semana
    if n == "曜日":
        if int(datetime.now().strftime("%w")) == 0:
            str = "今日は日曜日です。"
        if int(datetime.now().strftime("%w")) == 1:
            str = "今日は月曜日です。"
        if int(datetime.now().strftime("%w")) == 2:
            str = "今日は火曜日です。"
        if int(datetime.now().strftime("%w")) == 3:
            str = "今日は水曜日です。"
        if int(datetime.now().strftime("%w")) == 4:
            str = "今日は木曜日です。"
        if int(datetime.now().strftime("%w")) == 5:
            str = "今日は金曜日です。"
        if int(datetime.now().strftime("%w")) == 6:
            str = "今日は土曜日です。"
    return str

def age () -> str:
    return str((int(datetime.now().strftime("%Y"))-996)) + "歳です"
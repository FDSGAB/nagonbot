from bs4 import BeautifulSoup
import requests

#Acessando os dados da estação de São Caetano do Sul
#Cabeçalho para burlar a restrição de acesso do SAISP
headers= {'user-agent': 
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
          'referer': 'https://www.saisp.br/geral/processo.jsp?USERID=Publico&PRODUTO=50',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'}

#Acessando a página do SAISP para obter os dados
url = 'https://www.saisp.br/geral/processo.jsp?PRODUTO=50&USERID=Publico&&WHICHCHANNEL=143&WHICHCODE=100'

#GET request para obter o conteúdo de HTML primário utilizando o cabeçalho
html_conteudo = requests.get(url, headers=headers).text

#Dividindo o conteúdo do HTML
soup = BeautifulSoup(html_conteudo, "html.parser")

#Acessando somente as linhas dos horários
linhas=soup.find("table").find("tbody", {'id':'tbTelemBody'}).findAll("tr", {'onmouseout':"javascript:this.setAttribute('bgColor','#ffffff');"})

print("Estação Prosperidade em São Caetano do Sul: ")
for linha in linhas:
    #Acessa o horário
    hora=linha.td.text
    #Acessa o valor do pluviômetro da estação no horário
    valorPLU=float(linha.td.next_sibling.text.replace("\n",""))
    #Acessa a tendência do pluviômetro
    tendenciaPLU=linha.td.next_sibling.img['alt']
    #Acessa o valor do fluviômetro da estação no horário
    valorFLU=float(linha.td.next_sibling.next_sibling.text.replace('\n',""))
    #Acessa a tendência do nível fluvial
    tendenciaFLU=linha.td.next_sibling.next_sibling.img['alt']
    print([hora,valorPLU,tendenciaPLU,valorFLU,tendenciaFLU])
    
#Quebra-linha   
print("")  
 
#Agora para a estação de Mauá
url = 'https://www.saisp.br/geral/processo.jsp?PRODUTO=50&USERID=Publico&&WHICHCHANNEL=1000490&WHICHCODE=100'

html_conteudo = requests.get(url, headers=headers).text

soup = BeautifulSoup(html_conteudo, "html.parser")

linhas=soup.find("table").find("tbody", {'id':'tbTelemBody'}).findAll("tr", {'onmouseout':"javascript:this.setAttribute('bgColor','#ffffff');"})

print("Estação da nascente em Mauá: ")
for linha in linhas:
    hora=linha.td.text
    valorPLU=float(linha.td.next_sibling.text.replace("\n",""))
    tendenciaPLU=linha.td.next_sibling.img['alt']
    valorFLU=float(linha.td.next_sibling.next_sibling.text.replace('\n',""))
    tendenciaFLU=linha.td.next_sibling.next_sibling.img['alt']
    
    print([hora,valorPLU,tendenciaPLU,valorFLU,tendenciaFLU])
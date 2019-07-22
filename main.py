import requests

dado = None

try:
    dado = requests.get("https://api.thingspeak.com/channels/814858/feeds.json?results=2")
    dado = dado.json()
    
    print(dado["feeds"][0]['created_at']) # recebendo valor de data ... será tratado posteriormente
    print(dado["feeds"][0]['field1']) # valor de corrente de ventiladoresclclear
    print(dado["feeds"][0]['field2']) # valor de corrente de iluminção
    
    for a in dado["feeds"][0]['created_at']: # for como teste para separação de ano, mes, dia e hh:mm:ss
        print(a)
 
except:
    print(dado.status_code)

''' 
    criar função para request 
    criar função para separar datas
    criar função para escrever no excel
'''
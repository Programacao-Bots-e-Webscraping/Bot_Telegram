import requests

def enviar_mensagem(mensagem):
    
    chat_id = '-1002112763550'
    token = '6956796797:AAG7dXDItCrva1SUjiMxzaTVolaJPcjx9B4'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensagem}'
    response = requests.post(url)

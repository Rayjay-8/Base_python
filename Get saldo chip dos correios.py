import requests,json,time

#url2 = "https://apps.correios.com.br/correioscelular/v1/clientes/plataforma/A/versao/1.1.1"
#                                                                                           /NumeroCorreto
url = "https://apps.correios.com.br/correioscelular/v1/saldos/44920005176"
auth = "Basic MTU4OTE6YXBwMjAxOA=="
UserAgente = "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532MT Build/MMB29T)"
host = "apps.correios.com.br"
connec = "Keep-Alive"
accept = "gzip"
x1 = {'Authorization':auth,'User-Agent':UserAgente, 'Host':host,'Connection':connec,'Accept-Encoding': accept}

def login(URL,xx):
    rec= requests.get(URL,headers=xx)
    print(rec.text)
    input()

login(url,x1)

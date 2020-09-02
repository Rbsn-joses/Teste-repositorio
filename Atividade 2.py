#Instalar biliboteca de requisição
#pip install requests
import requests
endereco = "http://www.google.com/"
r = requests.get(endereco)
requisicao = r.status_code
print("Número de requisição " +str(requisicao))

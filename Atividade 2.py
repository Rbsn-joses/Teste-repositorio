import requests
endereco =  "http://www.google.com/"
r = request.get(endereco)
r.status.code
print(r.status.code)

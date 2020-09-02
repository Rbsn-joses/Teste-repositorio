
#baixar biblioteca requests
# pip install requests
contador = 0
numero = 100
 while(contador < 100):
    primo = False
    for numero2 in range(2,numero):
        if(numero % numero2 == 0):
            primo = True
            break
    if(not primo):
      contador += 1
      print(numero)
    numero += 1

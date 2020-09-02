
FROM python
LABEL version="1.0.0" description="Programa para calculo de números primos" ma>
RUN pip install flask
EXPOSE 80
COPY primos.py /primos.py
CMD ["python", "primos.py"]
#sudo docker build -t robson/primos .
#sudo docker run robson/primos 
#Após os passos o programa é inicializado perfeitamente

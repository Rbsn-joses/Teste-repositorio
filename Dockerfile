
FROM python
LABEL version="1.0.0" description="Programa para calculo de números primos" 
RUN pip install flask
EXPOSE 80
COPY Atividade1.py /Atividade1.py
CMD ["python", "Atividade1.py"]


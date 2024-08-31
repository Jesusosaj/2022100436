#Usa la imagen base oficial de python
FROM python:3.9-slim

WORKDIR /app

#Copia los archivos de requerimientos
COPY requirements.txt requirements.txt

#Instala las dependencias
RUN pip install -r requirements.txt

#Copia el resto de los archivos de la aplicacion
COPY . .

#Expone el puerto donde la aplicacion correra
EXPOSE 5000

#Define el comando por defecto para correo la aplicacion
CMD ["python","app.py"]
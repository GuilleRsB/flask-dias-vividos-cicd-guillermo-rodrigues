# Utiliza una imagen base ligera de Python 3.9
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias e instala
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto de los archivos del proyecto
COPY . .

# Expone el puerto 5000 para la aplicación
EXPOSE 5000

# Ejecuta la aplicación usando gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

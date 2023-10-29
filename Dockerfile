FROM python:3.11-slim

WORKDIR /app

# install requirements
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y tesseract-ocr    

COPY . .

ENV TZ="Asia/Colombo"

EXPOSE 8000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000" ]
FROM python:3.9-slim
#IMPORTING THE BASE IMAGE

WORKDIR /app
#WORKING DIRECTORY FOR THE APPLICATION

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

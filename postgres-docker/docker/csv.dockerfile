FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/generate_csv.py ./  

CMD ["python", "generate_csv.py"]  

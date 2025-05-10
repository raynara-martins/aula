FROM python
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/generate_and_read_csv.py ./

CMD ["python", "generate_and_read_csv.py"]

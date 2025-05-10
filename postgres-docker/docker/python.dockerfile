FROM python
WORKDIR /usr/src/app
COPY  requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/read_database.py ./

CMD ["python", "./read_database.py"]
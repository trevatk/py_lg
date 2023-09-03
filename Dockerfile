FROM python:3.11-alpine

ENV PYTHONPATH=/usr/src/app/src

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9091

CMD [ "python", "./src/main.py" ]
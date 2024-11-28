

FROM python:3.12-slim

COPY . /app

RUN pip3 install flask Cx_Oracle

#config.sh 실행
RUN chmod +x /app/config.sh

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
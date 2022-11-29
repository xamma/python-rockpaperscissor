FROM ubuntu:focal

RUN apt update && apt install -y \
python3

RUN mkdir /app

ADD game_class.py /app/game_class.py
ADD main.py /app/main.py

CMD ["/app/main.py"]
ENTRYPOINT ["python3"]
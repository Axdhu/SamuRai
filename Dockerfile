FROM python:3.9
ENV PYTHONUNBUFFERED=1


#clonning repo 
RUN git clone https://github.com/Axdhu/SamuRai.git /root/userbot

#working directory 
RUN mkdir /root/userbot/bin/
WORKDIR /root/samurai


ENV PATH="/home/samurai/bin:$PATH"

RUN bash startup.sh

CMD ["python3","-m","samurai"]

FROM python:3.9
ENV PYTHONUNBUFFERED=1

FROM axdhu/samurai:slim-buster


#clonning repo 
RUN git clone https://github.com/Axdhu/SamuRai.git /root/userbot
#working directory 
WORKDIR /root/samurai

# Install requirements
RUN pip3 install --no-cache-dir requirements.txt

ENV PATH="/home/samurai/bin:$PATH"

RUN bash startup.sh

CMD ["python3","-m","samurai"]

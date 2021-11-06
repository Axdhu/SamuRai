FROM python:3.9
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN 
RUN git clone -b sql-extended https://github.com/Axdhu/SamuRait /root/userbot
RUN bash startup.sh
CMD ["python3","-m","samurai"]

FROM python:3.9
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN 
RUN git clone  https://github.com/Axdhu/SamuRait 
RUN bash startup.sh
CMD ["python3","-m","samurai"]

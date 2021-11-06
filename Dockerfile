FROM python:3.9
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN bash startup.sh
CMD ["python3","-m","samurai"]

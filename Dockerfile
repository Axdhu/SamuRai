FROM python:3.9
ENV PYTHONUNBUFFERED=1


#clonning repo 
RUN git clone https://github.com/Axdhu/SamuRai.git /root/samurai

#working directory 
RUN mkdir /root/samurai/bin/
WORKDIR /root/samurai


ENV PATH="/home/samurai/bin:$PATH"


CMD ["python3","-m","samurai"]

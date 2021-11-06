FROM python:3.9
ENV PYTHONUNBUFFERED=1


#clonning repo 
RUN git clone https://github.com/Axdhu/SamuRai.git /root/userbot

# Install requirements
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt


#working directory 
WORKDIR /root/samurai



ENV PATH="/home/samurai/bin:$PATH"

RUN bash startup.sh

CMD ["python3","-m","samurai"]

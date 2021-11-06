FROM python:3.9
ENV PYTHONUNBUFFERED=1


#clonning repo 
RUN git clone https://github.com/Axdhu/SamuRai.git /root/userbot
#working directory 
WORKDIR /root/samurai

# Install requirements
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PATH="/home/samurai/bin:$PATH"

RUN bash startup.sh

CMD ["python3","-m","samurai"]

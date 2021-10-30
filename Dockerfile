FROM Axdhu/userbot_docker:latest

ENV PATH="/usr/src/app/bin:$PATH"
WORKDIR /usr/src/app

RUN git clone https://github.com/Axdhu/SamuRai.git -b master ./

#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* ./client_secrets.json* ./secret.json* ./

#
# Finalisation
#
CMD ["bash","init/start.sh"]

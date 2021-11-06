FROM python:3.9
ENV PYTHONUNBUFFERED=1

#clonning repo 
RUN git clone https://github.com/Axdhu/SamuRai.git /root/samurai

#working directory 
RUN mkdir /root/samurai/bin/
WORKDIR /root/samurai

RUN pip3 install aiohttp
RUN pip3 install async_generator
RUN pip3 install bs4
RUN pip3 install cowpy
RUN pip3 install cffi
RUN pip3 install covid
RUN pip3 install cryptg
RUN pip3 install deezloader
RUN pip3 install dnspython
RUN pip3 install emoji
RUN pip3 install gitpython
RUN pip3 install google-api-python-client
RUN pip3 install google-auth-httplib2
RUN pip3 install google-auth-oauthlib
RUN pip3 install google_images_download
RUN pip3 install google_trans_new
RUN pip3 install gTTS
RUN pip3 install gTTS-token
RUN pip3 install hachoir
RUN pip3 install heroku3
RUN pip3 install html_telegraph_poster
RUN pip3 install httplib2
RUN pip3 install humanize
RUN pip3 install jikanpy
RUN pip3 install lxml
RUN pip3 install lyricsgenius
RUN pip3 install oauth2client
RUN pip3 install pendulum
RUN pip3 install Pillow
RUN pip3 install psutil
RUN pip3 install psycopg2
RUN pip3 install psycopg2-binary
RUN pip3 install pybase64
RUN pip3 install pyfiglet
RUN pip3 install pylast
RUN pip3 install pySmartDL
RUN pip3 install python-barcode
RUN pip3 install python-dotenv
RUN pip3 install youtube-dl
RUN pip3 install pytz
RUN pip3 install qrcode
RUN pip3 install redis
RUN pip3 install requests
RUN pip3 install search-engine-parser
RUN pip3 install speedtest-cli
RUN pip3 install sqlalchemy 
RUN pip3 install telethon-tgcrypto
RUN pip3 install telethon
RUN pip3 install telethon-session-sqlalchemy 
RUN pip3 install telegraph
RUN pip3 install urbandict
RUN pip3 install wikipedia
RUN pip3 install PyGithub
RUN pip3 install python-dateutil
RUN pip3 install vcsi
RUN pip3 install youtube_search               

ENV PATH="/home/samurai/bin:$PATH"


CMD ["python3","-m","samurai"]

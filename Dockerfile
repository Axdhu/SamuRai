# using Alpine Edge
FROM Axdhu/userbutt:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/Axdhu/SamuRai /root/samurai
RUN mkdir /root/samurai/bin/
WORKDIR /root/samurai/

# Make open port TCP
EXPOSE 80 

CMD ["python3","-m","samurai"]

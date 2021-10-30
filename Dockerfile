#Copyright (C) 2021 Axdhu/SamuRai
#This file is a part of < https://github.com/Axdhu/SamuRai >
#PLease read the GNU Affero General Public License < https://github.com/Axdhu/SamuRai/blob/main/LICENSE >
# All rights reserved.

FROM python:3.9
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN bash startup.sh
ENTRYPOINT ["python3", "-m", "main_startup"]

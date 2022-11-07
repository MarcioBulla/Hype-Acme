FROM python:3.10

WORKDIR /usr/src/app



ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv /opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --no-cache-dir gdown

RUN mkdir -p -v data
RUN gdown 1tQsYSIN2YXrMACxRjIDCnDTV10K4NKJ_ -O data/
RUN gdown 1AJmk-B-Ok1kvSZGnXa1HlJjX5nojkQOe -O data/
RUN curl "https://servicodados.ibge.gov.br/api/v3/agregados/1420/periodos/201201%7C201202%7C201203%7C201204%7C201205%7C201206%7C201207%7C201208%7C201209%7C201210%7C201211%7C201212%7C201301%7C201302%7C201303%7C201304%7C201305%7C201306%7C201307%7C201308%7C201309%7C201310%7C201311%7C201312%7C201401%7C201402%7C201403%7C201404%7C201405%7C201406%7C201407%7C201408%7C201409%7C201410%7C201411%7C201412%7C201501%7C201502%7C201503%7C201504%7C201505%7C201506%7C201507%7C201508%7C201509%7C201510%7C201511%7C201512%7C201601%7C201602%7C201603%7C201604%7C201605%7C201606%7C201607%7C201608%7C201609%7C201610%7C201611%7C201612%7C201701%7C201702%7C201703%7C201704%7C201705%7C201706%7C201707%7C201708%7C201709%7C201710%7C201711%7C201712%7C201801%7C201802%7C201803%7C201804%7C201805%7C201806%7C201807%7C201808%7C201809%7C201810%7C201811%7C201812%7C201901%7C201902%7C201903%7C201904%7C201905%7C201906%7C201907%7C201908%7C201909%7C201910%7C201911%7C201912/variaveis/306?localidades=N1%5Ball%5D&classificacao=315%5B7169%5D" -o data/ipca.json



COPY requirements.txt .
COPY import_data.py .

RUN pip install --no-cache-dir -r requirements.txt
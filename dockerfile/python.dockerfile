FROM python:3.10

WORKDIR /usr/src/app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv /opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
COPY import_data.py .

RUN pip install --no-cache-dir -r requirements.txt

# CMD [ "python","-u", "import_data.py" ]

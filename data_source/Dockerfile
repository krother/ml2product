
FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY rest_api.py /app/
COPY data_ex.csv /app/
COPY data_reader.bin /app/

CMD ["uvicorn", "--host", "0.0.0.0", "rest_api:app"]

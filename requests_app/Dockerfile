FROM python:3.9-slim
WORKDIR /requests_app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "request_script.py"]
